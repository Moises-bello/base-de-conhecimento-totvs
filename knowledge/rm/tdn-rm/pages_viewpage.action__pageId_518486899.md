---
content_hash: a918860b163612072cb74934dc8e92ee154f56acca2e7cf1fee422caf4a81fa7
fetched_at: '2026-06-29T00:10:30.053497+00:00'
page_id: '518486899'
product: rm
source: tdn-rm
title: FISCAL01-10900 DT - NF-e - Melhoria na geração da tag cBenef (Atual)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518486899
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| Ticket: | 6851705 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10900 |

## **02. SITUAÇÃO/REQUISITO**

Na geração da tag cBenef, o sistema deve buscar o Código de Ajuste associado ao Item do Movimento, considerando a UF da Filial emitente e o CST do CFOP.

Exemplo

Considerando:

* Que o Código de Ajuste RJ801001 é aplicável aos CST's 30 e 40 e
* Que o Produto 01.01 possui o Código de Ajuste RJ801001 associado, então:

1. Na Filial do Rio de Janeiro, ao movimentar o Produto 01.01 com um CFOP que possui CST 30 ou 40, a tag cBenef deve ser preenchida com o "RJ801001".  
Se for qualquer outro CST, a tag não deve ser gerada.

2. Se a movimentação desse produto foi na Filial de Minas Gerais, como não há nenhum Código de Ajuste que seja de MG associado ao Produto, a tag também não deve ser gerada.

## **03. SOLUÇÃO**

Implementado para que ao gerar da tag cBenef, o sistema verifique o cadastro de   considerando a UF da Filial emitente e o CST do CFOP.

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
