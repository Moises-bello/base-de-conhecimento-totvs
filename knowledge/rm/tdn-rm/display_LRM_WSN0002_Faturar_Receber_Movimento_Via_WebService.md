---
content_hash: c91526daa03400d32037457c1069f31c164f611d99a2be93669ab9023c2e6394
fetched_at: '2026-06-29T00:08:46.262333+00:00'
page_id: '315908015'
product: rm
source: tdn-rm
title: WSN0002_Faturar_Receber_Movimento_Via_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/WSN0002_Faturar_Receber_Movimento_Via_WebService
version: 3
---

# Faturamento/Recebimento de Movimento via WebService

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compra e Faturamento |
| **Versões:** | A partir da 11.8x |
| **Ocorrência:** | Faturamento/Recebimento de Movimento via WebService |
| **Ambiente:** | Faturamento/Recebimento de Movimento |
| **Passo a passo:** | Este documento tem por finalidade ensinar como realizar o Faturamento/Recebimento de movimento via WebService. Será utilizado o aplicativo SoapUI para consumo do WebService do RM.   Passo a PassoIdentificar o WSDLConfiguração do WS (Webservice) RM Executar o documento: <http://tdn.totvs.com/x/HoFXBQ>  Obs.: Acessando a página do Webservice RM (Orientado no link acima), clicar no link “wsProcess/MEX?wsdl” e copiar o endereço da página que será aberta.  Este será utilizado na criação do projeto no SoapUI.(Exemplo: <http://localhost:8051/wsProcess/MEX?wsdl>)   Criando Projeto no SoapUICriação do Projeto no SoapUI Acessar o aplicativo SoapUi (Disponível na web gratuitamente <http://www.soapui.org/>)  Solicitar um novo Projeto e informar:   * + Nome do Projeto   + O link WSDL copiado anteriormente na configuração do WS RM     Será criado um projeto com as opções e métodos do print abaixo   Faturar/Receber MovimentoRestrições do processo  * Apenas movimentos configurados para faturamento/recebimento **automático** podem ser utilizados * Apenas os campos apresentados no SCHEMA podem ser informados para o consumo    XML do processo   xmlConfluenceXML do Processotruetrue  1 T 1.1.71 1.1.11 mestre  22  9993 0 2017-11-21   2   1 1 9993 1 1,0000  true ]]>    Parâmetros para o consumo do WSDefinição do Processo Procedimentos para executar o processo de faturamento via WS.    1- Crie uma request para configurar os dados do consumo no método "ExecuteWithParams" (É possível renomeá-la na janela de propriedades - Campo NAME)  Este Método pede dois parâmetros:  Parâmetro 1 = ProcessServerName (Nome do processo a ser consumido)  Parâmetro 2 = strXmlParams (XML com os dados a serem consumidos)  2 - Informar no primeiro parâmetro o valor ***MovFaturamentoProc***  3 - Informar no parâmetro do XML o valor do XML com a marcação obrigatório ***<![CDATA[****–informara aqui o XML--****]]>***  4 - Clicar no ícone ***Submeter*** (play verde) para consumir o serviço    A tela configurada fica como na imagem abaixo:   Importante  * É necessário informar o usuário e senha para conexão do WS no menu de propriedades. Campos "Username" e "Password" respectivamente * O conteúdo do XML deve ser inserido dentro do conjunto de caracteres "<![CDATA[ ]]>", entre a ultima abertura de colchete e o primeiro fechamento dele ex.: ***<![CDATA[*** <MovFaturamentoProcParams>  ...  </MovFaturamentoProcParams> **]]>** * O movimento deve estar configurado para realizar o faturamento parcial automático * Para gerar JOB no RM, deverá adicionar o seguinte grupo no XML:   <context>  <codusuario>mestre</codusuario>  <codcoligada>1</codcoligada>  <codsistema>T</codsistema>  </context> * Para realizar o faturamento parcial, deverá marcar o parâmetro "Marcar os itens que farão parte do movimento gerado" na etapa Compra/Venda - Outros Dados do movimento de origem conforme print abaixo: |
| **Observações:** | Para mais informações:       [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
