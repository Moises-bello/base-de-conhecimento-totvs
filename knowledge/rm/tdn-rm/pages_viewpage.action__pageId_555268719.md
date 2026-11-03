---
content_hash: 953d1ca29e0bd691e1d0c8bd18006ae6b30c4aa90a38c91919c4343ed3eaeb2a
fetched_at: '2026-06-29T00:10:46.635461+00:00'
page_id: '555268719'
product: rm
source: tdn-rm
title: 9113262 FISCAL01-13374 DT - NFS-e - Nova Friburgo/RJ - E43 - INSCRIÇÃO MUNICIPAL
  DO PRESTADOR DO SERVIÇO NÃO ENCONTRADA NA BASE DE DADOS DO MUNICÍPIO.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555268719
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e - Municipal |
| Ticket: | 9113262 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13374 |

## **02. SITUAÇÃO/REQUISITO**

Ao consultar uma NFS-e que foi enviada para a Prefeitura de Nova Friburgo/RJ a seguinte rejeição abaixo está sendo apresentada.

*"E43 - INSCRIÇÃO MUNICIPAL DO PRESTADOR DO SERVIÇO NÃO ENCONTRADA NA BASE DE DADOS DO MUNICÍPIO."*

A Inscrição Municipal utiliza hífen em seu cadastro na Prefeitura.

## **03. SOLUÇÃO**

Foi realizado um ajuste no envio da NFS-e para o município de Nova Friburgo/RJ a fim de não retirar a máscara(hífen) da Inscrição Municipal.

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
