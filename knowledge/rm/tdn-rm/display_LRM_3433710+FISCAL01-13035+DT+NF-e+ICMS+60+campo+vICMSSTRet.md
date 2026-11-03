---
content_hash: cacd9df3318d57a838935b23e0a9afe9a5275de119975f32fdd2bfcf81759054
fetched_at: '2026-06-29T00:10:43.862202+00:00'
page_id: '551420565'
product: rm
source: tdn-rm
title: 3433710 FISCAL01-13035 DT NF-e ICMS 60 campo vICMSSTRet
type: documentation
url: https://tdn.totvs.com/display/LRM/3433710+FISCAL01-13035+DT+NF-e+ICMS+60+campo+vICMSSTRet
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Emissão de NF-e |
| Ticket: | 3433710 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13035 |

## **02. SITUAÇÃO/REQUISITO**

Passar a considerar para o campo vICMSSTRet sempre o valor de ICMSST - ICMS visto que o valor de ICMS no movimento estará preenchido com base na última compra

## **03. SOLUÇÃO**

Foi modificado o preenchimento da tag vICMSSTRet para o ICMS 60 de forma o cálculo passou a ser ICMSST - ICMS desde que o parâmetro, da regra de ICMS, "ICMS S.T. NÃO considera ICMS Próprio " esteja desmarcado e o valor não seja negativo.

Exemplo de Cálculo:

**CFOP das operações**

|  |  |  |
| --- | --- | --- |
| **CFOP** | 1.102.02 | 5.102.05 |
| **CST** | 90 | 60 |
| **Alíq. ICMS** | 18% | 20% |
| **Alíq. ICMSST** | 18% | 20% |
| **Margem de lucro ICMSST** | 50% | 50% |

Como era, Como ficou - Normal, Como ficou - Simples Nacional1,2,3yes1

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Movimento** | 1.2.02 (última compra) | 2.2.02 (**NÃO** Calcula com base na última entrada) | 2.2.02 (Calcula com base na última entrada) |
| **Número Movimento** | 000028 | 000000030 | 000000031 |
| **Valor unitário** | 100,00 | 130,00 | 130,00 |
| **Quantidade** | 1000 | 10 | 10 |
| **Total dos Itens** | 100.000,00 | 1.300,00 | 1.300,00 |
| **BC ICMS** | 100.000,00 | 1.300,00 | 1.300,00 |
| **Alíquota ICMS** | 18% | 20% | 20% |
| **Valor ICMS** | 18.000,00 | 260,00 | 260,00 |
| **BC ICMS ST** | 150.000,00 | 2.080,00 | 1.500,00 |
| **Alíquota ICMS ST** | 18% | 20% |  |
| **Valor ICMS ST** | 27.000,00 | 416,00 | 270,00 |
| **Xml NF-e** | **Grupo gerado:** ICMS90  **CST:** 90  **vBC:** 100.000,00  **pICMS:** 18,00  **vICMS:** 18.000,00  **vBCST:** 150.000,00  **pICMSST:** 18,00  **vICMSST:** 9.000,00 | **Grupo gerado:** ICMS60  **CST:** 60  **vBCSTRet:** 2.080,00  **pST:** 20,00  **vICMSSubstituto:** 260,00  **vICMSSTRet:** 416,00  **vBCEfet:** 1.300,00  **pICMSEfet:** 12,00  **vICMSEfet:** 156,00 | **Grupo gerado:** ICMS60  **CST:** 60  **vBCSTRet:** 1.500,00  **pST:** 0,00  **vICMSSubstituto:** 260,00  **vICMSSTRet:** 270,00  **vBCEfet:** 1.300,00  **pICMSEfet:** 12,00  **vICMSEfet:** 156,00 |

no2

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Movimento** | 1.2.02 (última compra) | 2.2.02 (**NÃO** Calcula com base na última entrada) | 2.2.02 (Calcula com base na última entrada) |
| **Número Movimento** | 000028 | 000000034 | 000000033 |
| **Valor unitário** | 100,00 | 130,00 | 130,00 |
| **Quantidade** | 1000 | 10 | 10 |
| **Total dos Itens** | 100.000,00 | 1.300,00 | 1.300,00 |
| **BC ICMS** | 100.000,00 | 1.300,00 | 1.300,00 |
| **Alíquota ICMS** | 18% | 20% |  |
| **Valor ICMS** | 18.000,00 | 260,00 | 180,00 |
| **BC ICMS ST** | 150.000,00 | 2.080,00 | 1.500,00 |
| **Alíquota ICMS ST** | 18% | 20% |  |
| **Valor ICMS ST** | 27.000,00 | 416,00 | 270,00 |
| **Xml NF-e** | **Grupo gerado:** ICMS90  **CST:** 90  **vBC:** 100.000,00  **pICMS:** 18,00  **vICMS:** 18.000,00  **vBCST:** 150.000,00  **pICMSST:** 18,00  **vICMSST:** 9.000,00 | **Grupo gerado:** ICMS60  **CST:** 60  **vBCSTRet:** 2.080,00  **pST:** 20,00  **vICMSSubstituto:** 260,00  **vICMSSTRet:** 156,00  **vBCEfet:** 1.300,00  **pICMSEfet:** 12,00  **vICMSEfet:** 156,00 | **Grupo gerado:** ICMS60  **CST:** 60  **vBCSTRet:** 1.500,00  **pST:** 0,00  **vICMSSubstituto:** 180,00  **vICMSSTRet:** 90,00  **vBCEfet:** 1.300,00  **pICMSEfet:** 12,00  **vICMSEfet:** 156,00 |

no3

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Movimento** | 1.2.02 (última compra) | 2.2.02 (**NÃO** Calcula com base na última entrada) | 2.2.02 (Calcula com base na última entrada) |
| **Número Movimento** | 000028 | 000000039 | 000000038 |
| **Valor unitário** | 100,00 | 130,00 | 130,00 |
| **Quantidade** | 1000 | 10 | 10 |
| **Total dos Itens** | 100.000,00 | 1.300,00 | 1.300,00 |
| **BC ICMS** | 100.000,00 | 1.300,00 | 1.300,00 |
| **Alíquota ICMS** | 18% | 20% |  |
| **Valor ICMS** | 18.000,00 | 260,00 | 180,00 |
| **BC ICMS ST** | 150.000,00 | 2.080,00 | 1.500,00 |
| **Alíquota ICMS ST** | 18% | 20% |  |
| **Valor ICMS ST** | 27.000,00 | 416,00 | 270,00 |
| **Xml NF-e** | **Grupo gerado:** ICMS90  **CST:** 90  **vBC:** 100.000,00  **pICMS:** 18,00  **vICMS:** 18.000,00  **vBCST:** 150.000,00  **pICMSST:** 18,00  **vICMSST:** 9.000,00 | **Grupo gerado:** ICMS60  **CSOSN:** 500  **vBCSTRet:** 2.080,00  **pST:** 20,00  **vICMSSubstituto:** 260,00  **vICMSSTRet:** 156,00 | **Grupo gerado:** ICMS60  **CSOSN:** 500  **vBCSTRet:** 1.500,00  **pST:** 0,00  **vICMSSubstituto:** 180,00  **vICMSSTRet:** 90,00 |

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
