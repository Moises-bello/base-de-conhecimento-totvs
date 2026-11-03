---
content_hash: db6441b6d6e629af416247c531869321eea11b0b36c7bf249c5d8ba35b3e8121
fetched_at: '2026-06-29T00:10:52.308337+00:00'
page_id: '571795989'
product: rm
source: tdn-rm
title: Estrutura tabelas de Transações com Cartão de Crédito/Débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571795989
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Financeira |
| Função: | Histórico de Transações |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Restruturação das tabelas de integração com pagamento com cartão de crédito/débito para atender futuramente o pagamento de mais de um boleto/lançamento e com mais de um cartão na mesma transação.

## **03. SOLUÇÃO**

A partir da versão 12.1.29 foi feita uma reestruturação da tabela FINTEGRACAOCARTAO, para atender futuramente o pagamento de mais de um boleto e com mais de um cartão na mesma transação.

O campo IDENTIFICADORORIGEM da tabela FINTEGRACAOCARTAO foi removido, ele era apenas uma concatenação do CODCOLIGADA | IDBOLETO, os mesmos ainda continuam na tabela FINTEGRACAOCARTAO.

Alguns campos da tabela FINTEGRACAOCARTAO foram removidos e passaram para a tabela FINTEGRACAOTRANSACAO, são os seguintes:

IDMODELO  
CODAFILIACAO  
IDRECORRENCIA  
CANALPAGAMENTO

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Use esse box para destacar informações relevantes e/ou de destaque.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Coloque links com páginas de assuntos relacionados.

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
