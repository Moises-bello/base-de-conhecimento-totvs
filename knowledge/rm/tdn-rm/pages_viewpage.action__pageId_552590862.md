---
content_hash: f2eb58d3345d7b34d5bd8d6a68011e41ded2bcc78db54cff00d50258b8dd18d2
fetched_at: '2026-06-29T00:10:44.463896+00:00'
page_id: '552590862'
product: rm
source: tdn-rm
title: DEDUCONNECT-783 DT Pagamento com cartão de crédito - Adyen (Android)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552590862
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Pagamento Carteira Digital |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-783](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-783) |

## **02. SITUAÇÃO/REQUISITO**

Implementação do pagamento com cartão de crédito utilizando o Gateway de pagamentos Adyen (Para Android)

Utilização do SDK Android e funções de criptografia a fim de enviar os dados criptografados do cartão de crédito.

Implementação do pagamento para cartões da carteira digital e cartões não cadastrados na carteira.

## **03. SOLUÇÃO**

Criação dos projetos para geração das DLLs de binding na solution de Bindings (Android) do eduCONNECT  
Inclusão de DLLs no Diretório Bindings/Bin  
Reestruturação de classes/objetos para trabalhar com os dois Gateways (Adyen / Cybersource)  
Implementação do pagamento com cartão de crédito utilizando o Gateway Adyen  
Utilização do SDK Android da Adyen para criptografia dos dados do cartão  
Ajuste na data de expiração para que não considere o mês/ano incorretamente

Mais detalhes, consulte os documentos de referência: 

[11.2 - Listagem da Carteira Digital](https://tdn.totvs.com/display/LRM/11.2+-+Listagem+da+Carteira+Digital)

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
