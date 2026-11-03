---
content_hash: b2fb1f22576b62a27ab2259d0e9b104d05e8ea95f109f65f618db0ddaba6aff7
fetched_at: '2026-06-29T00:10:32.459183+00:00'
page_id: '525821742'
product: rm
source: tdn-rm
title: DT Adesão ao Pagamento recorrente - eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525821742
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Pagamento automático |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-212](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-212) |

## **02. SITUAÇÃO/REQUISITO**

Necessidade do usuário informar que os títulos de um determinado contrato serão pagos automaticamente na data de vencimento.

## **03. SOLUÇÃO**

* Criação do parâmetro para "Habilitar pagamento automático" nos parâmetros do eduConnect (Essa opção somente estará visível se a base do cliente estiver parametrizada para utilização do eduCONNECT Pay).
* Criação do campo para "Habilitar pagamento automático" na tela de exibição de cartões a serem utilizados para pagamento (carteira digital).
* Criação do campo para "Habilitar pagamento automático" na tela de dados do endereço do cartão (Somente estará disponível para **pagamento** tendo em vista que essa mesma tela é utilizada para inclusão de cartão).
* Campo de habilitação de pagamento automático será desmarcado (se o mesmo tiver sido marcado anteriormente) ao pagar com outro cartão (fora da carteira digital) pois esse campo dependerá do campo de salvamento do cartão na carteira estar marcado.

Mais detalhes, consulte o documento de referência: [10.5 - Adesão ao pagamento automático](https://tdn.totvs.com/pages/viewpage.action?pageId=525821739)

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
