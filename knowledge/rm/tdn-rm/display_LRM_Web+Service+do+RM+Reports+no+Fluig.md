---
content_hash: edc900283efca1cef39fabdbe6efa13c0fbd88b3e960af9ae30fd5290aa8a8f8
fetched_at: '2026-06-29T00:08:49.378904+00:00'
page_id: '330140381'
product: rm
source: tdn-rm
title: Web Service do RM Reports no Fluig
type: documentation
url: https://tdn.totvs.com/display/LRM/Web+Service+do+RM+Reports+no+Fluig
version: 37
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Exemplo de utilização do Web Service do RM Reports no Fluig. Este documento tem o intuito de auxiliar na criação de uma integração simples entre o Fluig e o Web Service do RM Reports ()

# Cadastro do Web Service do RM Reports no Fluig:

---

O Web Service do RM Reports deve ser cadastrado no Fluig para que possa ser acessado na integração. Segue link da documentação para disponibilizar o serviço no Fluig:

# Criação do DataSet com o conteúdo do relatório gerado:

---

Para que os dados de um relatório sejam retornados, deve-se criar um DataSet no Fluig que consumirá o Web Service do RM Reports, solicitará a geração do relatório desejado e retornará o conteúdo do relatório gerado. O arquivo WsFuigDataSet.js é um exemplo da criação de um DataSet com informações para a geração de um relatório de boleto. Segue link da documentação do Fluig para o desenvolvimento de DataSets: [Desenvolvimento de Datasets](http://tdn.totvs.com/display/public/fluig/Desenvolvimento+de+Datasets)

Segue link da documentação da integração do Fluig com aplicativos externos que auxilia no entendimento de como recuperar as informações do Web Service: [Integração com Aplicativos Externos](http://tdn.totvs.com/pages/releaseview.action?pageId=73082260)

jsExemplo - WsFuigDataSet.jstrue SERVICE\_STUB: " + SERVICE\_STUB);
const SERVICE\_HELPER = SERVICE\_STUB.getBean();
// Cria o obejto da classe principal do Servico
const wsReport = SERVICE\_HELPER.instantiate('com.totvs.WsReport');
log.info("wsProjetos-> wsReport: " + wsReport);
// Obtem o objeto do WS
var iWsReport = wsReport.getRMIwsReport();
log.info("wsProjetos-> iWsReport: " + iWsReport);
// Usuário e senha para autenticação no RM
var rm\_user = 'XXXXX';
var rm\_pass = '\*\*\*\*\*';
var authIwsDataServer = SERVICE\_STUB.getBasicAuthenticatedClient(iWsReport, 'com.totvs.IwsReport', rm\_user, rm\_pass);
log.info("wsProjetos-> authIwsDataServer: " + authIwsDataServer);
var NomeRelatorio = 'Relatorio.pdf';
var IdBoleto = '1';
// recupera o ID do boleto de acordo com parâmetro passado na constraint
if (constraints.length > 0) {
IdBoleto = String(new java.lang.String(constraints[0].getInitialValue()));
}
// XML de parâmetros recuperado pelo Web Service do RM Reports
var parametros = "" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"" +
"CODCOLIGADA" +
"1" +
"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" +
"" +
"" +
"" +
"IDBOL" +
"" + IdBoleto + "" +
"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" +
"" +
""
// dados de cadastro relatório
var CodigoColigadaRel = 1;
  var IdRelatorio = 29;
var Contexto = "codcoligada=1;codsistema=G";
// solicita a geração do realtório e armazena o identificador único
var guid = authIwsDataServer.generateReport(CodigoColigadaRel, IdRelatorio, '', parametros, NomeRelatorio, Contexto);
// recupera o tamanho do relatório gerado
var size = authIwsDataServer.getGeneratedReportSize(guid);
var offset = 0;
var rptstr = "";
var pack = 65000;
// monta o arquivo com o relatório gerado
while (offset < size) {
var temp = pack;
if ((offset + temp) > size)
temp = size - offset;
rptstr += authIwsDataServer.getFileChunk(guid, offset, temp);
offset = offset + pack;
}
result = rptstr;
log.info("Resultado do Servico: " + result);
//O TBC retorna os valores da chave caso o registro tenha sido salvo,
//caso contrário, a exceção ocorrida é enviada pelo mesmo retorno, porém
//formatada entre linhas '==='
if ((result != null) && (result.indexOf("===") != -1)) {
log.info("Erro no serviço.");
var msgErro = result.substring(0, result.indexOf("==="));
log.info(msgErro);
throw msgErro;
}
var dataset = DatasetBuilder.newDataset();
dataset.addColumn("RELATORIO");
dataset.addRow(new Array(result));
log.info("RELATORIO: " + result);
return dataset;
} catch (e) {
return getDatasetError(e);
};
}
function getDatasetError(exception) {
var dtsError = DatasetBuilder.newDataset();
dtsError.addColumn("ERROR");
dtsError.addRow(["Ocorreu um erro na execução do DataSet. Mensagem: " + exception]);
return dtsError;
};]]>

# Exibição do relatório gerado nas páginas do Fluig:

---

Depois de disponibilizar o serviço e criar o DataSet do relatório, é necessário recuperar os dados DataSet e exibir o relatório. A página em que a integração for disparada deve possuir um link com a chamada para as funções JavaScript que solicitam a geração dos relatórios, no caso deste exemplo, inserimos um link simples na página.

xmlExemploGerar Boleto]]>

O evento de click deste link executa as funções JavaScript abaixo que solicitarão a geração do relatório. O arquivo WsFluigReports.js deve ser referenciado na página do Fluig com o link para geração.

jsExemplo - WsFluigReports.js true
