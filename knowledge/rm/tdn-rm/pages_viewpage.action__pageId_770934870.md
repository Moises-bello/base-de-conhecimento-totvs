---
content_hash: 42d3d3397c67bdfee851b7d20005352f3718927960f61dbe550b3907a5d4179c
fetched_at: '2026-06-29T00:11:35.985148+00:00'
page_id: '770934870'
product: rm
source: tdn-rm
title: TCGI - Automação de Testes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770934870
version: 38
---

Este guia visa demonstrar alguns processos e padrões da automação de testes do TCGI no TestFlow.

11AUSUÁRIOSambarsolidUsuários

O TCGI possui três usuários, **TCGI Core,** **TCGI Real Estate e TCGI IntegraSync:**

TCGI Core:

* [squadtin@gmail.com](mailto:squadtin@gmail.com)
* Responsáveis: Adriano Astoni ([aferreira@totvs.com.br](mailto:aferreira@totvs.com.br)) e Alexandre de Jesus ([alexandre.lopes@totvs.com.br](mailto:alexandre.lopes@totvs.com.br))

TCGI Real Estate:

* [TribeCP.Squad.TINRev@totvs.com.br](mailto:TribeCP.Squad.TINRev@totvs.com.br)
* Responsáveis: Ricardo Louback ([ricardo.alvarenga@totvs.com.br](mailto:ricardo.alvarenga@totvs.com.br))

TCGI IntegraSync:

* [tribecp.squad.tcgiintsync@totvs.com.br](mailto:tribecp.squad.tcgiintsync@totvs.com.br)
* Responsáveis: Bruna Caroline ([bruna](mailto:bruna.caroline@totvs.com.br)[.caroline@totvs.com.br](mailto:ricardo.alvarenga@totvs.com.br)) e Jorge Pereira ([jorge.pereira@totvs.com.br](mailto:jorge.pereira@totvs.com.br))
1BAGENDAMENTOSsolidAgendamentos

### Do usuário **Squad TCGI Jornada e Locação**

#### PVI: Postman: PVI\_Tests (Mercado e Atual)

---

Estes agendamentos são importantes pois passam nos processos básicos / críticos do Portal de Imóveis. Esses projetos não rodam na IC. **Disparam todos os dias às 17:05** na VM BH-ENG-AUTTIN02.

Todos os projetos com versão maior ou igual a **12.1.2506** rodam na BH-ENG-AUTTINPR, visto a necessidade do **PHP8**

É importante **conferi-los diariamente** acessando o log do agendamento de todas as versões como mostra a imagem abaixo:

É enviado e-mail para a equipe caso exista algum projeto com falhas.

#### Atualizador de Ambientes TOTVS Restore (Mercado e Atual)

---

O agendamento Atualizador de Ambientes TOTVS Restore **roda todos os dias às 16:30** e irá atualizar os três servidores (BH-ENG-AUTTIN01, BH-ENG-AUTTIN02, BH-ENG-AUTTINPR) com as últimas versões do mercado e Atual.

Para que a atualização ocorra - os três servidores devem ter o Restore iniciado e o Agent em execução.

Importante: O agendamento **Atualizador de Ambientes TOTVS Restore AUTTINPR** (Versão Atual) além de atualizar o servidor BH-ENG-AUTTINPR **às 16:30,** também irá realizar a atualização de scripts na versão atual de todos os bancos de dados das equipes.

As bases Oracle não estão incluidas nesse agendamento visto o problema da issue → <https://jiraproducao.totvs.com.br/browse/DENGAUT01-7521> que ainda se encontra com a equipe do TestFlow.

É importante verificar diariamente esse agendamento, através do seu log específico se não está ocorrendo erros na atualização dos bancos de dados.

Neste agendamento são atualizados os bancos nos diretórios abaixo:

* \\bh-aut-bdcp\BasesAutomacao\v1200\{Versao}\Imb-Imobiliario\SQL\Aluguel
* \\bh-aut-bdcp\BasesAutomacao\v1200\{Versao}\Imb-Imobiliario\SQL\Refatoração
* \\bh-aut-bdcp\BasesAutomacao\v1200\{Versao}\PVI\SQL

No caso do Portal de Imóveis, apenas a base RM é convertida.

O processo de atualização realiza um backup no mesmo diretório. É importante limpar estes backups caso estejam ocupando muito espaço.

Exemplo:

Os arquivos sublinhados na imagem são os arquivos de backup realizados pelo agendamento e são seguros para exclusão. Normalmente deixamos apenas os dois últimos backups realizados por segurança / precaução.

Atente-se a data no nome do arquivo e faça a deleção do mais antigo para o mais novo.

#### Requer Execução e Erro/Alerta (Mercado e Atual)

---

Este agendamento irá ser disparado **todos os dias, às 19:10** e tem por objetivo executar todos os projetos que possuem em seu status "Erro/Alerta" ou "Requer Execução".  
Existe um agendamento para cada versão de mercado e também para a versão atual.

#### Exclusão de Bases dos Servidores

---

O próprio nome já diz. Este agendamento possui uma consulta SQL que é disparada no servidor BH-AUTBDCP e deleta todos os bancos temporários do servidor. **Este agendamento é executado diariamente, a cada 30 minutos.**

1HAUTOMAÇÃO ORACLEBases Oracle

A automação Oracle roda normalmente na IC.

O servidor onde estão as bases Oracle da equipe Real Estate, Core e Integra Sync é o **BH-AUT-ORACLE.SP01.LOCAL**

**Bases Oracle Real Estate:**

* **REALESTATEV1212410**
* **REALESTATEV1212502**
* **REALESTATEV1212506**
* **REALESTATEV1212510**

**Bases Oracle Core:**

* **TCGIV1212410**
* **TCGIV1212502**
* **TCGIV1212506**
* **TCGIV1212510**

**Bases Oracle Integra Sync:**

* **ORAPIMIGRADOV1212506**
* **ORAPIMIGRADOV1212510**

1CCOBERTURA DE CÓDIGOCobertura de Código

Todos os projetos devem ter sua cobertura de código coletada. É importante que, ao criar um projeto e versioná-lo para a versão Atual, o mesmo deve ter o seu código coletado pela engenharia. Lembre-se de disparar a coleta através do menu lateral Cobertura de Código no TestFlow.

1DANÁLISE DE PROJETOS COM FALHASAnálise de Projetos com Falhas

Exemplo de um Projeto com erros na CT:

Ao verificar o log clicando em Erro/Alerta percebo que algumas atividades estão com erro.

Isso deve-se ao fato de que alguma atividade do tipo webservice não executou de forma correta.

Temos que nos atentar que, mesmo o Test Flow mostrando que o WS executou com sucesso, não quer dizer que o resultado do processo tenha sido o esperado.

Então não é só por que a atividade está com sucesso que ela executou corretamente.

Neste caso tenho uma atividade de geração de lançamentos com falhas. Veja que o Test Flow não mostra o erro no print acima, mas somente quando clicamos no "olhinho". Dessa forma temos que investigar sempre nestes cenários onde a consulta SQL está com erro se algum WS executou de forma errada.

Vemos aqui que a atividade Gerar lançamentos do Fechamento executou com um resultado não esperado.

Para entender melhor esse log normalmente substituímos a atividade que fecha o projeto por uma atividade **C# "Faz Nada"**. Dessa forma o projeto irá executar no ambiente e irá parar sem deletar o banco. E então podemos acessá-lo e verificar os logs de execução:

Substituindo e salvando, iremos executar novamente o projeto em uma VM.

Dentro do RM, posso ir em *Ambiente / Gerenciamento de Jobs* e encontrar o processo que ocasionou o erro, filtrando pela data de hoje.

Ao clicar no processo de gerar lançamentos podemos entender melhor o log e verificar se é um bug ou se o projeto precisa ser alterado, facilitando a análise do erro.

# **OUTROS PROBLEMAS COMUNS / SOLUÇÕES**

# **Queda do agent dos servidores:**

Solução: Reiniciar o agent e avaliar o estado das execuções. O agent.exe deve obrigatoriamente ser executado como administrador

É importante verificar também se o TOTVS.Restore está em execução nas três VM's

# **Espaço do servidor BH-AUT-BDCP:**

Solução: Contactar um usuário administrador para efetuar a limpeza. Os admins desse servidor são:

Com o agendamento de limpeza de bancos normalmente estes problemas não ocorrem mais. Porém, pode acontecer da instância do SQLServer estar parada. Dessa forma é preciso logar no servidor e iniciá-la manualmente.

# **Erros do script na versão atual por falta de campos:**

Este erro é bastante comum e é mitigado com o agendamento atualizador de bases. Porém ainda há momentos em que o código que necessita do script já está no restore porém o script ainda não. Nestes casos, devemos aguardar e não executar de forma manual os scripts de banco.

Solução: Atualizar a base de automação, utilizando o último RM.Atualizador para popular a base com os novos scripts.

O Script abaixo desbloqueia um banco que esteja com erros para fins de teste na versão 1212510.

sql

# **Erros Winforms de timeout ou clique:**

Solução: A grande maioria dos erros em scripts Winforms ocorrem de forma intermitente, a solução nestes casos é a reexecução do script com problema.

Aguardar a execução do script Winforms via agendamento. Caso o erro persista após nova reexecução devemos verificar.

1ETREINAMENTOS E LINKSTreinamentos e Links

Abaixo alguns links para treinamentos e apostilas e o help do Test Flow

**Help**

* [http://](http://tdn.totvs.com/display/EN/Help+TestFlow+2.0)[tdn.totvs.com/display/EN/Help+TestFlow+2.0](http://tdn.totvs.com/display/EN/Help+TestFlow+2.0)

**Novidades**

* [http://](http://tdn.totvs.com/display/EN/Novidades+do+TestFlow+2.0)[tdn.totvs.com/display/EN/Novidades+do+TestFlow+2.0](http://tdn.totvs.com/display/EN/Novidades+do+TestFlow+2.0)

**Boas Práticas**

* [http://](http://tdn.totvs.com/pages/viewpage.action?pageId=286208460)[tdn.totvs.com/pages/viewpage.action?pageId=286208460](http://tdn.totvs.com/pages/viewpage.action?pageId=286208460)

**Capacitações**

* [http://](http://tdn.totvs.com/pages/viewpage.action?pageId=286028481)[tdn.totvs.com/pages/viewpage.action?pageId=286028481](http://tdn.totvs.com/pages/viewpage.action?pageId=286028481)

**Criação de projetos Web Services e API's**

* <https://drive.google.com/open?id=13favAVmvUWJ2y6vpdSoAhF3la7VnPBXG&usp=drive_fs>

**Status dos servidores: (Os links abaixo só funcionam com um usuário logado)**

* <http://bh-testflow/testflow/servers/BH-ENG-AUTTIN01/status>
* <http://bh-testflow/testflow/servers/BH-ENG-AUTTIN02/status>
* <http://bh-testflow/testflow/servers/BH-ENG-AUTTINPR/status>

**Repositório TestFlow (Agent e pasta TestFlow)**

* \\bhengfiles\rmflex$\Outros\Ferramentas\TestFlow2.0

**Caminho dos arquivos .json que executam nas automações do Postman:**

* \\bh-autbdcp\BasesAutomacao\v1200\{{versao}}\Imb-Imobiliario\restFul
* \\bh-autbdcp\BasesAutomacao\v1200\{{versao}}\PVI\restFul

**Bases TestFlow**

* \\bh-autbdcp\BasesAutomacao\v1200
* \\bh-autbdcp\BasesAutomacao\ORA ***(BAT PARA SERVIDOR ORACLE)***

**Servidor oficial da automação Construção e Projetos**

* Servidor: BH-AUT-BDCP
* Usuário: rm/rm

**Servidores de Execução TCGI (VM’S)**

* BH-ENG-AUTTIN01
* BH-ENG-AUTTIN02
* BH-ENG-AUTTINPR

**Os usuários listados abaixo são administradores dos servidores. Caso necessite acesso, favor contatá-los.**

* Adriano Astoni Ferreira ([aferreira@totvs.com.br](mailto:aferreira@totvs.com.br)),
* Ricardo Alvarenga Louback ([ricardo.alvarenga@totvs.com.br](mailto:ricardo.alvarenga@totvs.com.br)),
* Alexandre De Jesus Oliveira Lopes ([alexandre.lopes@totvs.com.br](mailto:alexandre.lopes@totvs.com.br)),
* Jorge De Assis Pereira Junior ([jorge.pereira@totvs.com.br](mailto:jorge.pereira@totvs.com.br)).
* Bruna Caroline ([bruna.caroline@totvs.com.br](mailto:bruna.caroline@totvs.com.br))

Portal de Cobertura de Código:

* <http://bh-eng-cover.sp01.local/Home/Index>

Dashboard da IC e CT

* <http://engenhariabh/ic/versions/latest>

Apostilas



1FDICAS WINFORMS

Ajustando Scripts Winforms

---

O jeito mais simples de ajustar os scripts Winforms é reexecutando os mesmos com um tempo mais elevado entre as ações e entre as janelas.

Por padrão temos um tempo entre janelas de 300 segundos e entre ações de 5 segundos.

Em alguns momentos talvez possa ser necessário ajustar esse tempo, principalmente na cobertura de código, onde os scripts executam num ambiente mais carregado e lento.

Para alterar o tempo de um script winforms basta acessá-lo via edição dentro do projeto:

Os parâmetros a seguir devem ser ajustados:

Usar sempre um **tempo do tipo Fixo**.

O mesmo padrão deverá ser usado na aba "Aguardar Janelas".

Editando ações winforms

---

As vezes quando temos mudança de posições do menu de processos os scripts podem quebrar. Quando um novo processo surge e altera a posição dos menus antigos. Nestes casos, podemos alterar diretamente na ação que clica no menu seguindo os passos abaixo:

Clicar na ação que clica no processo e que está com erro:

Veja que sua posição está definida como **btnProcess\_10**

Porem nesse exemplo esse processo no RM já está definido como **btnProcess\_11,** por isso o erro.

Podemos editar diretamente essa ação clicando com o mouse em "WinformControlBase" e dando um Tab.

Após o ajuste, basta clicar em salvar na ação:

1GSELENIUM

TEMPLATE CODIGO SELENIUM

---

c# resourceExchange, CancellationToken cancellationToken)
{
  // Cria uma instancia da classe de ScriptWebBase...
  var scriptWebBase = new SeleniumWebDriver();
  try
  {
Browser browser;
string url;
// Executa o código antes do Teste
scriptWebBase.BeforeTest(out browser, out url);
var jsonResource = resourceExchange.LastOrDefault(r => r is IJsonResource);
var PostmanParams = ((IJsonResource)jsonResource).GetResource();
            string chromeDriverPath = PostmanParams.chromeDriverPath;
            
            // Defina o serviço do ChromeDriver com o caminho personalizado
            ChromeDriverService service = ChromeDriverService.CreateDefaultService(chromeDriverPath);
        
            // Cria o Driver para o Chrome
            ChromeOptions options = new ChromeOptions();
            options.AddArgument("--disable-extensions");
            options.AddArgument("start-maximized"); // Opcional: maximizar a janela ao iniciar
            options.AddArgument("--disable-gpu");
options.AddArgument("--disable-software-rasterizer");
options.AddArgument("--disable-accelerated-video");
options.AddArgument("--disable-accelerated-2d-canvas");
options.AddArgument("--disable-accelerated-compositing");
options.AddArgument("--disable-accelerated-layers");
options.AddArgument("--disable-accelerated-fixed-root-background");
options.AddArgument("--disable-accelerated-mjpeg-decode");
options.AddArgument("--disable-accelerated-video-decode");
            
            // Crie o driver do Chrome usando o serviço e as opções configuradas
            ChromeDriver driver = new ChromeDriver(service, options);
            
// Executa o código de teste
scriptWebBase.Test(driver, resourceExchange);
return new TestResult(TestStatusEnum.Success, this.Id, this.GetType().Name, "Script Web executado com sucesso.");
  }
  catch (Exception exception)
  {
return new TestResult(TestStatusEnum.Failed, this.Id, this.GetType().Name, exception.Message);
  }
  finally
  {
scriptWebBase.AfterTest(scriptWebBase.Driver);
  }
}
public class PostmanParams
{
  public string chromeDriverPath { get; set; }
}
  }
  public class SeleniumWebDriver : ScriptWebBase
  {
/// 
/// Método executado antes do teste
/// 
/// Tipo de Browser a ser usado
/// Url
public override void BeforeTest(out Browser browser, out string url)
{
  browser = Browser.Chrome;
  url = "http://localhost:8000/";
}
/// 
/// Método de teste, todo o script de teste deve ser colocado dentro deste método
/// 
/// Driver
public override void Test(IWebDriver driver, IEnumerable resourceExchange)
{
    INSIRA SEU CÓDIGO AQUI
}
/// 
/// Método executado depois da execução do teste
/// 
/// Driver
public override void AfterTest(IWebDriver driver)
{
  base.Quit();
}
  }
 }]]>
