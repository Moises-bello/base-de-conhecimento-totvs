---
content_hash: 775565e893b392a0ef6a56ef9cbdfa74c61c3e86b8e94c1c684e9ed4a8331b36
fetched_at: '2026-06-29T00:11:39.119391+00:00'
page_id: '787871470'
product: rm
source: tdn-rm
title: 2.4.1 Códigos C#
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787871470
version: 38
---

## O que é?

Uma **Atividade C#** na ferramenta TOTVS Automação de testes é um bloco de automação personalizado, desenvolvido em **C#**, que permite a execução de tarefas específicas dentro do ambiente de testes.

Embora a plataforma ofereça atividades pré-definidas para automação de processos, uma **Atividade C#** possibilita a criação de soluções personalizadas quando as opções padrão não são suficientes para atender a determinadas necessidades.

## Para que serve?

A **Atividade C#** na ferramenta serve para permitir a personalização e automação de processos específicos que não são atendidos pelas atividades padrão do sistema.

Tarefas que esta atividade possibilita:

* **Automatizar Tarefas Personalizadas**: Criar soluções sob medida para necessidades específicas.
* **Integrar Sistemas Externos**: Conectar-se a APIs, bancos de dados e outros serviços externos.
* **Personalizar Fluxos de Teste**: Adaptar testes a cenários mais complexos e personalizados.

## Ferramentas recomendadas

* [Utilizando o Visual Studio para auxiliar a criação de Atividades C#](https://tdn.totvs.com.br/pages/viewpage.action?pageId=787872660)
* [Testes automatizados com Selenium](https://tdn.totvs.com.br/display/LRM/Testes+automatizados+com+Selenium)

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Código**→ **Códigos C#.**

 2. Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Carregar Template 

É necessário escolher um template antes de iniciar. Existem dois tipos: **Padrão** e **Selenium WebDriver**. Esses templates já contêm a estrutura necessária para a ferramenta de Automação de Testes, facilitando a criação e organização do seu código.

* **Template Selenium**: Este template oferece uma estrutura padrão para a criação de programas que utilizam o **Selenium WebDriver**. Ele é projetado para facilitar a automação de interações com navegadores web, fornecendo o ambiente básico necessário para iniciar rapidamente o desenvolvimento de testes automatizados com o Selenium.
* **Template Padrão**: Este template fornece uma estrutura básica para a criação de programas em **C#**. Ele inclui os componentes essenciais para desenvolver atividades genéricas dentro da ferramenta, permitindo a personalização e expansão de funcionalidades conforme necessário.
Assemblies

Você pode desenvolver seu código fora do método `Execute`, mas para que a sua Atividade C# funcione corretamente, o método `Execute` deve sempre ser chamado. O mesmo se aplica às referências externas: os assemblies devem ser adicionados à sua Atividade C# através do botão **Assemblies (+)**, especificando o caminho e o nome completo do assemblie.

Observação 

Se você optar por usar **Assemblies externos** no seu código, os projetos que utilizarem essa Atividade C# deverão ser sempre executados no mesmo servidor, pois dependem da presença desses Assemblies. Por isso, é importante avaliar cuidadosamente a necessidade de utilizar esse recurso.

Recursos

A função **Recursos** em uma **Atividade de C#** na ferramenta de Automação de testes gerencia os objetos e serviços que a atividade pode **necessitar** (consumir) ou **oferecer** (disponibilizar) para outras atividades no fluxo de testes. Esses recursos facilitam a integração e reutilização de componentes, garantindo que dados e ferramentas possam ser compartilhados de forma eficiente entre diferentes atividades.

#### 1. Necessita (Recursos Consumidos)

* **Recursos consumidos** são aqueles que a atividade precisa para ser executada corretamente. Esses recursos podem ser fornecidos por outras atividades ou configurados no início do fluxo de teste.

  Exemplos de recursos que uma Atividade de C# pode consumir:

  + **Conexões de banco de dados**: Para realizar consultas ou operações de leitura/escrita.
  + **Instâncias de WebDriver**: Para automação de interações com navegadores usando Selenium.
  + **Parâmetros de execução**: Como credenciais de usuário, URLs, ou dados de entrada que a atividade precisará processar.

  **Exemplo:**

  `var dbConnection = context.Resources.OfType<IRdbConnectionResource>().First().Value;`

#### 2. Oferece (Recursos Disponibilizados)

* **Recursos oferecidos** são aqueles que a atividade gera ou disponibiliza para que outras atividades utilizem posteriormente no fluxo de teste. Eles podem incluir objetos instanciados durante a execução da atividade ou dados processados que serão necessários em atividades subsequentes.

  Exemplos de recursos que uma Atividade de C# pode oferecer:

  + **WebDriver**: Configurado e pronto para ser reutilizado em outras atividades que necessitem de automação web.
  + **Resultados de processamento**: Informações geradas pela atividade, como status de testes ou dados extraídos de uma página web.

  **Exemplo:**

  `context.Resources.Add(_seleniumManager, "Selenium Manager");`

#### 3. Recursos de Atividade no TOTVS Automação de Testes

* As **Atividades C#** naferramenta de automação podem consumir e oferecer recursos, garantindo que o fluxo de teste seja eficiente e organizado. Isso permite que uma atividade forneça dados ou instâncias de objetos para outra, mantendo a continuidade e a reutilização dos mesmos.

  **Exemplo de uso em contexto**:

  1. Uma atividade cria uma instância de **WebDriver** e adiciona ao contexto.
  2. Atividades subsequentes reutilizam o **WebDriver** sem a necessidade de nova instanciação, otimizando o processo.
Criando Código C#Guia Prático de Desenvolvimento em C#

1. Utilizar um Parâmetro de Execução

Para obter o valor de um parâmetro passado na execução da atividade:

c#("name");]]>

2. Utilizar um Recurso

Para acessar um recurso previamente adicionado, como uma conexão de base de dados:

c#().First().Value;]]>

3. Adicionar Resultado de Teste

Registre os resultados do teste de acordo com o status da execução:

* **Sucesso:**

c#

* **Ignorado**

c#

* **Erro**

c#

4. Adicionar Status de Execução

Monitore o status da execução do teste, informando o progresso ou alertas:

* **Teste Concluído:**

c#

* **Teste Falhado:**

c#

* **Adicionar Etapa:**

c#

* **Adicionar Alerta:**

c#

5. Adicionar um Recurso

Adicione novos recursos à atividade, como uma conexão ou outro objeto necessário:

c#(T resource [, string alias]);]]>

Use o **Visual Studio** para facilitar a criação de suas **Atividades C#**, aproveitando seus recursos avançados de desenvolvimento. Para mais detalhes, clique [aqui](https://tdn.totvs.com.br/pages/viewpage.action?pageId=787872660).

Compilador Rápido C#

Para auxiliar na construção do código da sua Atividade C# é possível **compilar seu código** em tempo de projeto não necessitando executar para que seja compilado e mostrado algum possível erro. Para compilar o seu código, clique no botão **Verificar Compilação**, selecione

A fim de compilar o seu código, clique no botão **Verificar Compilação**, selecione o **servidor** desejado e, em seguida, clique em **Compilar**, localizado no lado direito da janela de edição.

**Log de Erro**

**Log de Sucesso**

Para utilizar deve haver um Agent do TOTVS Automação de Testes Disponível e operante.

Exemplo prático

Uma equipe de desenvolvimento realiza testes constantes em um ambiente de pré-produção. Para cada rodada de testes, eles restauram várias bases de dados para garantir que os dados estejam no estado inicial. No entanto, após cada rodada, as bases restauradas acumulam-se no servidor, ocupando espaço desnecessário e podendo afetar o desempenho.

**OBS:** Os desenvolvedores optaram por **não realizar a limpeza automática** da ferramenta de automação de testes, e por esse motivo, as bases não são apagadas.

Para resolver esse problema e evitar que o servidor fique sobrecarregado, o analista de TI decide automatizar a remoção das bases restauradas ao final de cada ciclo de testes. Para isso, ele cria uma **Atividade C#** na ferramenta, que verifica e remove automaticamente as bases de dados restauradas.

*Código utilizado para criar uma Atividade C# que automatiza a remoção de bases de dados restauradas:*

c#
/// Apaga todas as bases dos recursos de IRdbRestoredDatabaseResource
///
/// Observações:
/// - Nenhum parâmetro é necessário
/// - Se nenhuma base for encontrada, um alerta será emitido.
/// - Se o apagar de alguma base falhar, a atividade falha.
///
[ActivityResourceDependency(typeof(IRdbRestoredDatabaseResource), "Recurso de uma base restaurada", required: true)]
public class ApagarBasesRestauradas : ICSharpCodeAction
{
#region Messages
public const string DATABASE\_DROPED = "A base {0} foi apagada com sucesso";
public const string NO\_RESOURCE\_FOUND = "Nenhum recurso de base restaurada encontrado.";
public const string SGBD\_FAULT = "O SGBD falhou em apagar a base {0}. \n - Mensagem: {1} \n - Código: {2} \n - Mais detalhes: {3}";
public const string FAULT = "A base {0} não pode ser apagada. \n Erro: {1}";
public const string DONE = "Todas as bases encontradas foram apagadas com sucesso.";
#endregion Messages
public void Execute(IActivityContext context)
{
// Recursos que serão apagados
var toDelete = context.Resources.SelectResourceOfType();
// Alerta caso nenhum recurso seja encontrado
if (!toDelete.Any())
{
context.Status.AddAlert(1, NO\_RESOURCE\_FOUND);
context.Status.SetCompleted();
return;
}
// Apagamos cada um dos items
var currentStep = 0;
foreach (var item in toDelete)
{
currentStep++;
try
{
item.Drop();
var message = string.Format(DATABASE\_DROPED, item.Name);
context.Status.AddStage(currentStep, message);
}
//Caso o usuário cancele a execução
catch (OperationCanceledException)
{
context.Status.SetFailed("Execução cancelada pelo usuário");
}
// Tratamento de erros da engine
catch (RdbException ex)
{
var message = string.Format(FAULT, item.Name, ex.Message);
context.Status.SetFailed(message);
}
// Tratamento de erros SQL SERVER
catch(SqlException ex)
{
var message = string.Format(SGBD\_FAULT, item.Name, ex.Message, ex.Number, "https://bit.ly/2Z3u7cj");
context.Status.SetFailed(message);
}
// Tratamento de erros ORACLE
catch(OracleException ex)
{
var message = string.Format(SGBD\_FAULT, item.Name, ex.Message, ex.Number, "https://bit.ly/2MZOMvr");
context.Status.SetFailed(message);
}
}
// Não não houve falhas, logamos como foi concluído com sucesso.
if (!context.Status.IsFailed)
{
context.Status.SetCompleted(DONE);
}
}
}
}
]]>

*A seguir, apresentamos um exemplo de um projeto de teste com a atividade de Limpeza do Ambiente:*

---

# Saiba mais

Atividades C# podem ser programadas para rodar em horários específicos inserindo a atividade na  ferramenta de  [Agendamentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=746516153#Comocadastrar-2066477995).

Aconselha-se que possuam nomes e descrições que deixem clara sua função e aplicação.

Para a criação de programas automatizados Web, Sugerimos o uso do Browser PhantomJs, uma vez que é um browser que não exibe tela, executa muito mais rápido e foi criado principalmente como o intuito de facilitar automação de testes.

# FAQ

**P: Como o TOTVS Automação de Testes lida com parâmetros de entrada nas Atividades C#?**

R: AFerramenta de Automação de Testes permite passar parâmetros de entrada para as **Atividades C#**. Esses parâmetros podem ser configurados diretamente na interface de execução e acessados no código utilizando o método **context.Parameters.Get<T>()**. Isso facilita a personalização dos testes sem a necessidade de alterar o código-fonte.

**P: Posso reutilizar uma Atividade C# em diferentes projetos?**

R: Sim, uma vez criada, a Atividade C# pode ser reutilizada em diferentes projetos dentro do TOTVS Automação de Testes. Isso economiza tempo e esforço, permitindo que o mesmo código seja aplicado em múltiplos cenários de teste

**P: Qual a vantagem de versionar uma Atividade C#?**

R**:** Versionar uma Atividade C# permite que você acompanhe as mudanças e revisões feitas ao longo do tempo. Isso é particularmente útil para manter o controle de diferentes versões do código, garantindo que atualizações e melhorias sejam rastreáveis e que versões anteriores possam ser restauradas se necessário.
