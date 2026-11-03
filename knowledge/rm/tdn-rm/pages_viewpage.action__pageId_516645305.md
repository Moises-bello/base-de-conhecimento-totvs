---
content_hash: 7f33ba5271c3cc3e4b3ffa2d4e78f1c98cc4ffd7454df88ce85c48a842ea418a
fetched_at: '2026-06-29T00:10:27.791136+00:00'
page_id: '516645305'
product: rm
source: tdn-rm
title: FISCAL01-10961 DT - Serviço de Tribu - Calcular o Valor do Crédito no ICMS-ST
  para empresa Optante pelo Simples Nacional (SERVIÇO DE SELEÇÃO DE ALÍQUOTA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516645305
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Serviço de Tributação |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10961 |

**02. SITUAÇÃO/REQUISITO**

A forma de determinação da alíquota do Simples Nacional foi alterada pelo Fisco, porém, o serviço de determinação da Alíquota para o TOTVS Gestão de Estoque não foi evoluído.

**03. SOLUÇÃO**

Evoluído o Serviço de Tributação para buscar a Alíquota dos tributos no cadastro de Simples Nacional.

Caso a movimentação seja posterior a 2017, será buscada a alíquota efetiva do período anterior no cadastro de Período de Apuração e, sobre esta, aplicado o percentual de partilha do tributo em questão no cadastro de Alíquotas Simples. Caso a movimentação seja anterior a 2018, a alíquota será buscada como já é atualmente, vindo diretamente do cadastro de Simples Nacional.

Em ambos os casos, a Alíquota no Simples Nacional só é carregada se o tributo estiver no Item do Movimento.

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
