---
content_hash: abb3738cce32b80883b9556070ccf60885bad8fcbf9ada6c81140cbe573369c4
fetched_at: '2026-06-29T00:10:46.193099+00:00'
page_id: '554635014'
product: rm
source: tdn-rm
title: 8939649 FISCAL01-13315 DT - Apuração da CPRB - Cálculo de outras atividades
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=554635014
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Apuração de CPRB |
| Ticket: | 8939649 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13315 |

## **02. SITUAÇÃO/REQUISITO**

A Filial Matriz ficou com as atividades paradas durante 3 meses e por isso seu faturamento foi zero, porém outras filiais tiveram o faturamento normal. Diante deste cenário é não possível encerrar o período de apuração da CPRB com o valor de faturamento zerado.

## **03. SOLUÇÃO**

Foi modificado o processo de encerramento do período de CPRB da filial matriz para permitir o encerramento com o valor de faturamento zerado. Também foi alterado o cálculo dos valores de receita de outras atividades (99990025) para ser gerado por filial tanto pelo regime de caixa quando pelo regime de competência.

**Tal alteração será refletida nos Eventos da EFD Reinf R2060 e na geração do bloco P da EFD Contribuições. Em ambos os casos será gerado um registro de outras atividades para cada filial.IMPORTANTE!**

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
