---
content_hash: bd1f4a94d1f370b1af36b36d554988f9c4703e82dc1f9cdc4d4c6a88a0dcbb4a
fetched_at: '2026-06-29T00:10:30.008438+00:00'
page_id: '518478976'
product: rm
source: tdn-rm
title: FISCAL01-10896 DT - NF-e - Melhoria na geração da tag cBenef (12.1.24, 12.1.25
  e 12.1.26)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518478976
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| Ticket: | 6851705 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10896 |

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

Foi realizado a implementação no envio da Nota Fiscal Eletrônica - Estadual para que na geração da tag cBenef no xml , o sistema busque  o Código de Ajuste associado ao Item do Movimento que está presente no cadastro do produto | Anexos |  [Benefícios Fiscais](https://tdn.totvs.com/pages/viewpage.action?pageId=516644471) considerando a UF da Filial emitente e o CST do CFOP vinculado ao movimento.

A regra para geração da tag cBenef no xml , irá verificar se o cadastro de Benefícios Fiscais foi criada e alimentada , caso não exista nenhum registro criado neste cadastro , o sistema vai verificar o comportamento anterior conforme documentação [DT Alterar forma de geração da tag cBenef na NF-e](https://tdn.totvs.com.br/pages/releaseview.action?pageId=510496178).

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
