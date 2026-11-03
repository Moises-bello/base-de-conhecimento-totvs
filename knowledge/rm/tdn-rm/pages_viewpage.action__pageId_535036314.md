---
content_hash: 5038ffad1b9beb9a9019068c440ac3e675fafb26b5f54fd8053de6ff2aa44813
fetched_at: '2026-06-29T00:10:37.079944+00:00'
page_id: '535036314'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-5285 DT Tipo contábil específico por bolsas de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535036314
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Bolsa de crédito |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

O cliente tem a necessidade de que o tipo contábil dos lançamentos de determinadas bolsas de crédito seja diferente do tipo contábil do lançamento financeiro do aluno, por exemplo, o lançamento do aluno é contabilizado na inclusão, porém o lançamento de bolsa de crédito deve ser contabilizado na baixa.

## **03. SOLUÇÃO**

Foi realizado uma evolução no cadastro de bolsa para que seja possível definir qual o tipo contábil do lançamento de outro sacado.

Quando o campo “Tipo de sacado” for igual a “Outro sacado” será habilitado o campo “Tipo contábil do lançamento do outro sacado” que permite definir qual é o tipo contábil do lançamento da bolsa de crédito que será gerado juntamente com o lançamento do aluno.

## **04. DEMAIS INFORMAÇÕES**

É importante destacarmos a regra de preenchimento do tipo contábil do lançamento da bolsa de crédito, pois existem outras parametrizações que serão levadas em consideração.

O TOTVS Educacional permite que seja definido nos parâmetros um tipo contábil para bolsa de crédito, ou seja, caso este parâmetro esteja preenchido todos os lançamentos de bolsas de créditos gerados irão considerar a parametrização.

Se no cadastro da bolsa de crédito o campo “Tipo contábil do lançamento do outro sacado” estiver preenchido o lançamento será gerado considerando o tipo contábil definido no cadastro.

Caso o campo no “Tipo contábil do lançamento do outro sacado” não esteja preenchido, será considerado o tipo contábil definido no parâmetro citado anteriormente.

Se o tipo contábil não estiver informado no cadastro da bolsa e o parâmetro não estiver preenchido, será considerado o tipo contábil do lançamento financeiro do aluno.

Este recurso está disponível a partir da versão 12.1.25, porem para habilitar o recurso em versões inferior 12.1.28 será necessário executar o  CN.2020.02\_03.

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
