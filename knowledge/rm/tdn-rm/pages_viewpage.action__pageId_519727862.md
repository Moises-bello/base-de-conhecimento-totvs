---
content_hash: 4508dfde793abfa64ed97a9b91143a553dfaac00c0f931b94f44e28d27130ca9
fetched_at: '2026-06-29T00:10:30.371010+00:00'
page_id: '519727862'
product: rm
source: tdn-rm
title: DT Pagamento de título com boleto - eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519727862
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Pagamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-23](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-23) |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de se pagar por boleto.

Para isso, o boleto "Não registrado" tem que ser registrado e o IPTE resultante ser mostrado para o usuário com a opção de cópia da linha digitável para a área de transferência.

## **03. SOLUÇÃO**

Implementação do pagamento por boleto com registro online do mesmo caso não tenha sido registrado.

Caso o título já tenha sido registrado, será mostrado o IPTE do boleto.

Opção de cópia do IPTE para a área de transferência a fim de possibilitar o usuário colar o mesmo em seu app do banco.

O título só aparecerá na aba "Pagos" do app eduConnect quando o pagamento do boleto for confirmado pela instituição financeira.

Mais detalhes, consulte o documento de referência: [10.4 - Pagamento com boleto](https://tdn.totvs.com/display/LRM/10.4+-+Pagamento+com+boleto)

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
