---
content_hash: 228b26c3e7e5e0ed504d520f164548dc8a708840f4d803f06c82f7ae4e655c54
fetched_at: '2026-06-29T00:10:44.472103+00:00'
page_id: '552593253'
product: rm
source: tdn-rm
title: DEDUCONNECT-785 DT Inclusão de cartão na carteira - Adyen
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552593253
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Carteira Digital |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-785](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-785) |

## **02. SITUAÇÃO/REQUISITO**

Implementação da inclusão de cartão de crédito na carteira do aluno utilizando Adyen.

## **03. SOLUÇÃO**

Tratamento da inclusão de cartão para funcionar tanto para Cybersource quanto para Adyen  
Preparação da classe base de Gateway para funcionar para inclusão de cartões para futuros Gateways  
Ajuste da mensagem que estava mostrando o resource quando a chave pública não havia sido informada.

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
