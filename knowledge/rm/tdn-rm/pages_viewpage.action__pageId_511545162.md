---
content_hash: 1c56cf1b4c2746d8cdc0aed96d0b69ad19bec6fdf16476c8c9ab1e46a7bb96cd
fetched_at: '2026-06-29T00:10:26.084034+00:00'
page_id: '511545162'
product: rm
source: tdn-rm
title: FISCAL01-10236 Serviço para geração de Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=511545162
version: 9
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Eventos Periódicos - EFD Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10236, FISCAL01-10238, FISCAL01-10372, FISCAL01-10373 e FISCAL01-10374 |

**02. SITUAÇÃO/REQUISITO**

Geração dos Eventos Periódicos:

Evento R-2010, R-2020, R-2030, R-2040 e R-2050.

**03. SOLUÇÃO**

Criado Serviço API para a Geração dos Eventos Periódicos:

Especificação:

**Obs.:** O Evento R-2030 não esta sendo gerado pois o Serviço do Totvs Gestão de Estoque e Faturamento não esta retornando Movimentos de Entrada,

Serviço será ajustado posteriormente.

**03. DEMAIS INFORMAÇÕES**

Url's para acesso ao serviço de Geração de Eventos Periódicos:

HEAD <http://localhost:8051/api/fiscal/v1/reinfserver/gerarevento/1|1>

GET <http://localhost:8051/api/fiscal/v1/eventoreinf/origens/1|1>

GET <http://localhost:8051/api/fiscal/v1/eventoreinf/eventosfilhos/1|1>

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
