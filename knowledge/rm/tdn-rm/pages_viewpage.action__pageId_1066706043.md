---
content_hash: eeb04a5841419f5a7054da315da5766d660da6529430b576080420729bec299b
fetched_at: '2026-06-29T00:05:53.127393+00:00'
page_id: '1066706043'
product: rm
source: tdn-rm
title: Criando atividades customizadas na Fórmula visual (WFCore)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1066706043
version: 17
---

## 1. Visão Geral: O Novo Paradigma da Fórmula Visual

Para suportar as novas inovações da TOTVS e preparar o ERP RM para a nuvem e interfaces web, o motor da Fórmula Visual foi completamente reescrito. Substituímos a dependência do antigo *Windows Workflow Foundation* pelo nosso próprio motor de alta performance: o **WFCore**.

**O que muda para você, desenvolvedor?**   
No modelo antigo, você criava uma única classe (herdando de **`RMSActivity`**) que misturava propriedades de tela, atributos do *Designer* e o código de execução. Agora, a arquitetura exige a separação clara em quatro camadas:

| Camada | Projeto | Responsabilidade |
| --- | --- | --- |
| **Visual (Design)** | RM.Custom.WFCore.Design | A classe visual que desenha o componente na tela do RM e que aparece na [Toolbox](https://tdn.totvs.com/x/UQSLCQ). Herda de RMSActivity. |
| **Metadados (Common)** | RM.Custom.WFCore.Common | Uma classe simples, que define apenas *o que* a atividade é e os dados que ela recebe. Ela é pura, serializável em JSON e não executa regras de negócio. |
| **Conversor (Converter)** | RM.Custom.WFCore.Converter | Traduz a atividade visual (Design) para a de metadados (Common) antes da execução. |
| **Execução (Runtime)** | RM.Custom.WFCore.Runtime | Contém a lógica de execução que define *como* a atividade roda. Ela é injetada nativamente pelo motor de Injeção de Dependência (DI) e processa os metadados de forma assíncrona. |

---

## 2. Estrutura de Projetos

Sugestão para organizanização dos projetos, seguindo a convenção de nomenclatura **`RM*.WFCore.*`**:

📁 Solution  
├── 📂 **RM.Custom.WFCore.Design**      → Referencia: RM.Lib.Workflow, System.Workflow.ComponentModel  
├── 📂 **RM.Custom.WFCore.Common**     → Referencia: RM.WFCore.Common  
├── 📂 **RM.Custom.WFCore.Converter**  → Referencia: RM.WFCore.Converter, Design, Common  
└── 📂 **RM.Custom.WFCore.Runtime**    → Referencia: RM.WFCore.Runtime, RM.WFCore.Common, Common

---

## 3. Passo a Passo: Construindo a Nova Atividade

Abaixo, demonstramos como criar uma atividade completa utilizando um exemplo real: **HoraCertaActivity**, que captura a hora atual do sistema.

### Passo 1: A Casca Visual (Design-Time)

Esta é a classe que aparecerá na **Toolbox** do sistema. Ela deve herdar de `RMSActivity` e registrar suas propriedades como `DependencyProperty` (padrão WF 3.5).

c#RDark1RMSActivitytrue

### Passo 2: Criando a Classe de Metadados (Common)

Esta classe é a representação em dados da sua atividade. Ela deve ser o mais limpa possível.

* **Herança:** Deve herdar de `RM.WFCore.Common.Activity` (ou `CompositeActivity` / `DynamicActivity`).
* **Propriedades:** Não utilize atributos diretamente. Utilize os métodos `GetProperty<T>` e `SetProperty` para que o motor consiga serializar o estado da atividade corretamente via JSON.

c#RDark1Activitytrue GetProperty(nameof(Hora));
set => SetProperty(nameof(Hora), value);
}
}
}]]>

### Passo 3: O Conversor (A Ponte)

Transforma a classe visual (Design) na classe de metadados (Common) antes da execução. Herda de `ActivityConverter<TDesign, TCommon>` e sobrescreve o método `Convert`.

c#RDark1Convertertrue
{
protected override void Convert(
Design.HoraCertaActivity activity,
Common.HoraCertaActivity coreActivity)
{
// Tenta mapear como expressão primeiro; se não for expressão, copia o valor literal
if (!coreActivity.SetExpressionProperty(nameof(coreActivity.Hora), activity, "HoraProperty"))
coreActivity.Hora = activity.Hora;
}
}
}]]>Nota

*Certifique-se de referenciar `RM.WFCore.Converter.dll` e implementar a interface base exigida pelo nosso motor*

### Passo 4: Criando a Classe de Runtime (O Motor de Execução)

Aqui é onde a mágica acontece. O método `OnExecute` é acionado pelo pipeline de compilação do RM.

* **Herança:** Crie uma interface vazia herdando de `IActivityRuntime<T>` e implemente a classe base `ActivityRuntime<T>`.
* **Assincronismo:** A execução agora é assíncrona (`Task<bool>`). Retorne `true` para continuar o fluxo, ou `false` para interromper.
* **Serviços do RM:** Acesso a contexto, banco de dados e DataServers agora é feito de forma segura utilizando o `IBrokerService`, que é injetado via construtor.

c#RDark1Runtimetrue
{
public HoraCertaActivityRuntime(IActivityLogger logger) : base(logger)
{
}
protected override Task OnExecute(
IActivityContext context,
HoraCertaActivity activity,
CancellationToken cancellationToken,
ITraceLogger traceLogger)
{
// Define a propriedade "Hora" com a hora atual do sistema
activity.Hora = DateTime.Now.ToString("HH:mm:ss");
return Task.FromResult(true);
}
}
}]]>

### Exemplo Avançado: Usando IBrokerService e DataServer

Para cenários mais complexos que exigem acesso a banco de dados ou DataServers do RM:

c#RDark
{
private readonly IBrokerService \_brokerService;
public ManipulaProdutoActivityRuntime(
IActivityLogger logger,
IBrokerService brokerService) : base(logger)
{
\_brokerService = brokerService;
}
protected override async Task OnExecute(
IActivityContext context,
ManipulaProdutoActivity activity,
CancellationToken cancellationToken,
ITraceLogger traceLogger)
{
traceLogger?.WriteTrace(EventName.BeforeExecute, activity);
var rmsContext = \_brokerService.GetContext();
using var dataServer = (IRMSDataServer)\_brokerService
.CreateServer("RMSPRJ3249920Server");
string filter = string.IsNullOrEmpty(activity.FiltroProduto)
? "Codigo like '%000%'"
: activity.FiltroProduto;
DataSet dsView = dataServer.ReadView(rmsContext, new object[] { filter }, null);
if (dsView.Tables[0].Rows.Count > 0)
{
Logger.Information(
$"Encontrados {dsView.Tables[0].Rows.Count} registros.");
}
traceLogger?.WriteTrace(EventName.AfterExecute, activity);
return true;
}
}
}]]>

---

## 4. Tratamento de Exceções e Tracing

* **Falhas:** Se sua regra de negócio falhar, utilize o lançamento de exceções padrão do C# (`throw new Exception(...)`). O motor WFCore detectará o erro e o redirecionará para as `FaultActivities` (atividades de Catch/Tratamento de Erros) caso o usuário tenha configurado isso no fluxo.
* **Logs:** Diferencie `IActivityLogger` (usado para logs técnicos e diagnóstico em arquivos) de `ITraceLogger` (usado para registrar as etapas visíveis no log operacional da Fórmula Visual).

---

## 5. Deploy e Compilação

Para que sua atividade customizada seja carregada pelo motor **WFCore**, você deve seguir rigorosamente os padrões de nomenclatura e localização. O RM utiliza um rastreamento automático (*Scan*) durante a inicialização do serviço.

c#RDark

1. **Nomenclatura da DLL:** O motor de busca do RM filtra apenas arquivos que seguem o padrão de nomenclatura de infraestrutura do WFCore.
   1. Padrão: `RM*.WFCore.Runtime*.dll`
   2. Exemplo : `RM.NomeDoModulo.WFCore.Runtime.MinhaAtividade.dll`
   3. Se o nome da DLL não começar com `RM` e não contiver `.WFCore.Runtime`, ela será ignorada pelo carregador automático e sua fórmula falhará ao tentar localizar o executor.
2. **Contrato de Interface:** Para que o motor de Injeção de Dependência (DI) registre sua atividade corretamente, você **deve** definir a interface específica (`IActivityRuntime`) para o seu Runtime.
3. **Target Framework:** Compile sua biblioteca mirando `.NET 4.8` ou `.NET Standard 2.0` (conforme exigência técnica atual da TOTVS).
4. **Referências:** Referencie as DLLs base do WFCore localizadas na pasta `RM.Net` (ex: `RM.WFCore.Common.dll`, `RM.WFCore.Runtime.dll`).
5. **Compilação:** Compile o projeto em modo Release
6. **Deploy:** A DLL deve ser copiada para o diretório de binários do RM (geralmente a pasta **`RM.Net`**), especificamente no **mesmo diretório** onde se encontra a DLL `RM.WFCore.Runtime.dll`.

   1. O sistema não realiza buscas em subpastas ou caminhos externos.

---

## 6. Migrando Atividades WFCore

Se você já possui atividades customizadas de Fórmula Visual no RM, você tem a **camada Design** — a classe que herda de `RMSActivity` e aparece na Toolbox. Essa classe **continua funcionando** e **não precisa ser alterada**.

O que você precisa criar são as **3 camadas restantes** exigidas pelo novo motor WFCore: [Metadados (Common)](https://tdn.totvs.com/pages/viewpage.action?pageId=1066706043#CriandoatividadescustomizadasnaF%C3%B3rmulavisual(WFCore)-Passo2:CriandoaClassedeMetadados(Common)), [Conversor (Converter)](https://tdn.totvs.com/pages/viewpage.action?pageId=1066706043#CriandoatividadescustomizadasnaF%C3%B3rmulavisual(WFCore)-Passo3:OConversor(APonte)) e [Execução (Runtime)](https://tdn.totvs.com/pages/viewpage.action?pageId=1066706043#CriandoatividadescustomizadasnaF%C3%B3rmulavisual(WFCore)-Passo4:CriandoaClassedeRuntime(OMotordeExecu%C3%A7%C3%A3o))

---

## 7. Projeto de exemplo

---

Aviso Legal

*A TOTVS não se responsabiliza por lógicas de negócio aplicadas em atividades customizadas. A retirada da DLL customizada do diretório fará com que o motor ignore a etapa durante a execução da fórmula).*
