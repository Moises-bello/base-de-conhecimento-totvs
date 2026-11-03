---
content_hash: 749ace149cdd8fcd93e67882d7445bc520e3211df745722d25722e7f18b2511a
fetched_at: '2026-06-29T00:10:43.682162+00:00'
page_id: '550325753'
product: rm
source: tdn-rm
title: DT Permitir informar o número máximo de parcelas por serviço - eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550325753
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Carteira Digital Cadastro de serviços |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-794](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-794) |

## **02. SITUAÇÃO/REQUISITO**

Incluir a opção de informar o número máximo de parcelas para pagamento por cartão no cadastro de serviços e mostrar esse número máximo de parcelas na carteira digital do usuário.

## **03. SOLUÇÃO**

Leitura do número máximo de parcelas para pagamento da API de valores do boleto selecionado (paymentSummary) a qual buscará esse número máximo do cadastro de serviços.   
Caso não tenha informado o número máximo de parcelas no serviço, será buscado o número máximo de parcelas parametrizado no financeiro em:  
  Parâmetros do financeiro -> Contas a Receber -> Baixas -> Cartão de Crédito/Débito

O valor default para o número máximo de parcelas é 1 caso não tenha sido parametrizado esse valor em lugar nenhum.

Mais detalhes, consulte os documentos de referência: 

[11.2 - Listagem da Carteira Digital](https://tdn.totvs.com/display/LRM/11.2+-+Listagem+da+Carteira+Digital)

[Cadastro de Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=425458880)

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
