---
content_hash: a6035cc77d642c713473149139dd20f7c497a8a6b6294ec692f7cdd1c8ad2647
fetched_at: '2026-06-29T00:10:27.797812+00:00'
page_id: '516647160'
product: rm
source: tdn-rm
title: FISCAL01-10964  DT - NF-e - Calcular o Valor do Crédito no ICMS-ST para empresa
  Optante pelo Simples Nacional (NF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516647160
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10964 |

**02. SITUAÇÃO/REQUISITO**

Na geração da NF-e as tags <pCredSN> e <vCredICMSSN> devem ser preenchidas considerando o Tributo com o Tipo "**ICMS Crédito SN**".

Se não houver este tributo informado no movimento, considerar o comportamento atual, pegando do ICMS.

Tratar os CSOSN 101, 201 e 900.

**03. SOLUÇÃO**

Ajuste para geração das tags <pCredSN> e <vCredICMSSN> considerando o novo tributo com o tipo "ICMS Crédito SN". Se não houver este tributo informado no movimento, considerar o comportamento atual, pegando do ICMS.

CSOSN 101, 201 e 900.

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
