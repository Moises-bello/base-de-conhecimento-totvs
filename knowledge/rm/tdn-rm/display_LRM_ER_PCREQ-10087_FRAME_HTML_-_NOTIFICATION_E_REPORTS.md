---
content_hash: 8b174f7c555d8a3d95ccfad9a09fa493b5e9c39c1bd1bf2210eff0fe62069eb3
fetched_at: '2026-06-29T00:08:06.916939+00:00'
page_id: '236595735'
product: rm
source: tdn-rm
title: ER_PCREQ-10087_FRAME_HTML_-_NOTIFICATION_E_REPORTS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10087_FRAME_HTML_-_NOTIFICATION_E_REPORTS
version: 135
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** |  | **Framework** |  |
| **Segmento Executor** |  | | |
| **Projeto1** |  | PCREQ-10031 |  |
| **Requisito1** |  | * [R\_FRW\_FRW002](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_FRW_FRW002 "R_FRW_FRW002") |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

      Criar um mecanismo para possibilitar que processos e relatórios possam ter sua execução agendada via protocolo http, adaptar a classe RMSProcess pra que seja possível enviar notificações ao Fluig e fazer a integração do novo Reports com o GED.

      Com essa mudança, teremos os seguintes benefícios:

* Será possível agendar a execução de processos em apps criados com o THF (TOTVS HTML Framework).
* A execução de relatórios também será disponibilizada via THF.
* Qualquer aplicativo que suporte comunicação via HTTP e que construa mensagens no padrão definido pelo THF poderá agendar a execução de processo e relatórios do CorporeRM.
* Os relatórios produzidos pelo novo gerador poderão ser exportados diretamente para o GED.
* Poderá ser enviado notificações para o Fluig quando da execução de qualquer processo no CorporeRM.

Definição da Regra de Negócio

* ****Execução de processos****

 *Para agendar a execução de algum processo, será necessário criar um controller WebAPI para disponibilizar um meio de acessar a funcionalidade via web. Esse controller deverá ser criado por cada segmento e deve ser um sub-tipo do controller RMSFrameHtmlController que está definido no assembly RM.WebAPI.dll. Como os parâmetros necessários para a execução do processo devem ser providos pelo controller, este deve receber no corpo da requisição um objeto do tipo **RMSJobExecutorInfo<T>**, onde T é algum sub-tipo de **RMSJobParameter**, e este deve conter propriedades que serão fonte de dados para os parâmetros do processo. O tipo RMSJobExecutorInfo<T> contém todas as propriedades comuns à todos os processos do CorporeRM bem como as informações utilizadas para o agendamento da execução.*

***Para agendar a execução do processo, deve-se utilizar uma instância de **RMSJobSchedulerBase<T>** onde T também é do tipo RMSJobParameter. Essa classe é responsável por fazer a carga dos parâmetros do processo e, logo após, realizar a leitura dos parâmetros comuns do processo na classe RMSJobexecutorInfo<T> e associá-los aos parâmetros de execução do processo. Esta classe também define o método virtual DoReadParamsProc que deve ser sobrescrito caso haja necessidade de passar parâmetros específicos do processo e/ou alterar parâmetros comuns. Para fazer o agendamento do processo deve ser realizada uma chamada ao método SubmitJob da classe que retornará um objeto do ripo **RMSJobInfo** que conterá as informações do job criado.***

 **Abaixo encontra-se o modelo de um controller que agenda a execução de um processo que espera dois valores inteiros para sua execução:**

c#1Backend - Sampletruetrue Execute([FromBody]RMSJobExecutionInfo p)
{
try
{
// cria uma instância do scheduller que agendará a execução do processo 
// e submete os parâmetros de execução do mesmo...
RMSJobInfo result = new SampleScheduller().SubmitJob(p, this.Context);
 
// monta a mensagem de retorno padrão do THF...
return new RMSFrameHtmlResponse
{
Data = result,
Length = 1
};
}
catch (Exception ex)
{
// fazer o tratamento da exeção...
throw ex;
}
}
}
 
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
/\*\* DEFINIÇÃO DO SCHEDULLER \*\*/
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
public class SampleScheduller : RMSJobSchedulerBase
{
// deve-se passar para a classe base os dados do processo que 
// será agendado: Nome da Action, Código do sistema, Nome do 
// Processo e Nome do Server.
public SampleScheduller() : base("NomeActionProcesso", 
"CodigoSistema", "NomeProcesso", "NomeServerProcesso")
{ 
// construtor padrão...
}
// método sobrescrito para que os dois parâmetros específicos do processo
// possam ser carregados...
protected override void DoLoadParamsProc(SampleParameters paramsSample,
RMSParamsProc paramsProc)
{
// faz o cast dos parâmetros do processo para o tipo específico do processo
SampleParamsProc p = (SampleParamsProc) paramsProc;
 
// inicializa o valor dos parâmetros específicos do processo com o valor 
// que veio na requisição HTTP...
p.Parametro1 = paramsSample.P1;
p.Parametro2 = paramsSample.P2;
}
}
 
 
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
/\*\* DEFINIÇÃO DA CLASSE DE PARÂMETROS \*\*/
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
public class RptReportJobParameter : RMSJobParameter
{
//Parâmetro #1 do processo
[JsonProperty(PropertyName = "p1", Required = Required.Always)]
public int P1 { get; set; }
 
//Parâmetro #2 do processo
[JsonProperty(PropertyName = "p2", Required = Required.Always)]
public int P2 { get; set; }
}]]>js1FrontEnd - Sampletruetrue
var scheduleParams = {
"notify": true,
"notifyEmail": false,
"schedule": {
"type": "TODAY",
"time":"10:00",
"date": "01/01/2016",
},
"parameters": {
"p1": 98,
"p2": 1,
"codUsuario": "mestre"
}
};
 
// faz a requisição post...
$http.post('/api/sales/executeprocess', scheduleParams, [])
.then(successCallback, errorCallback);
}]]>

* ****Gerenciador de Jobs (Web)****

*Existe também uma página HTML desenvolvida com o THF em que são exibidos todos os processos os processos (jobs) executados. Nesta página o usuário poderá visualizar e remover processos da fila de execução do RM. Não é possível fazer qualquer tipo de edição ou incluir processos na fila através dessa página.*

* ****Executar um relatório****

*****Como a execução de relatórios é feita por um processo, foi criado um controller especial para execução de relatórios no assemply RM.Rpt.webAPI.dll. Esse controller funciona da mesma forma que os demais específicos para agendamento de processos. Entretanto, não é necessário que seja feito um controller e um scheduller para cada relatório, pois o modo de execução e a estrutura de parâmetros é o mesmo para todos os relatórios. Então basta que seja feita uma requisição POST para o endereço /rm/api/report/execute passando no corpo da requisição um objeto json do tipo RMSJobExecutionInfo<RptReportJobParameter>.************Nesse objeto serão informados a coligada, o id, os filtros e parâmetros  do relatório, bem como os demais valores referentes ao agendamento da execução do relatório. Os parâmetros referentes ao relatórios são definidos pela classe **RptReportJobParameter**.*******

************Nesse mesmo controller também está disponível um método para recuperar as informações de metadados dos relatórios. Dentre as informações retornadas destacam as seguintes: Nome de todas as bandas do relatório, lista de todos os parâmetros, indentificador de filtro principal, nome de todas as tabelas e campos disponíveis, etc. O objeto retornado é definido pela classe **RptReportInfo**.************

*********Abaixo encontra-se o código javascript para a execução de um relatório fictício que possui um parâmetro e é passado um filtro para a banda principal e outro para buscar as informações de metadados desse mesmo relatório..*********

js1FrontEnd - Execute Reporttruetruejs1FrontEnd - Report Infotruetrue

## Schema dos objetos

textRMSJobInfotruetextRMSJobExecutionInfo<RptReportJobParameter>truetextRMSJobScheduleInfotruetextRptReportJobParametertruetextRMSJobRepeatWeektruetextRMSJobRepeatMonthtruetextRptReportParametertruetextRptReportParametertruetextRptReportInfotruetextRptParameterReportPartruetextRptParameterProviderPartruetextRptFilterReportPartruetextRptFilterFormulaPartruetextRptMemberInfotruetextRptFilterByTablePartrue

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
