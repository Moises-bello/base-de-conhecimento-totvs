---
content_hash: 1ac008d9777533211fafb67825bf6672f3903bebba2949d17e0a2e64881a76e4
fetched_at: '2026-06-29T00:10:22.592512+00:00'
page_id: '497483526'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1346 DT Formatação de valores numéricos financeiro - Relatórios
  Fast Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497483526
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | TOTVS Fast Analytics |
| Função: | Relatórios |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1346 |

## **02. SITUAÇÃO/REQUISITO**

Havia a necessidade de se criar uma regra para concatenação e formatação dos números financeiros exibidos nos relatórios do Fast Analytics.

## **03. SOLUÇÃO**

A seguinte regra foi criada, para ser utilizada nos gráficos financeiros:  
  
[=Null][color=3a3a3a]R$ 0;  
[=0][color=3a3a3a]R$ 0;  
[>=1000000000][color=3a3a3a]R$ #...,# B;  
[>=1000000][color=3a3a3a]R$ #..,# M;  
[>=10000][color=3a3a3a]R$ #. K;  
[>=1000][color=3a3a3a]R$ #.,# K;  
[>0][color=3a3a3a]R$ #.##0;  
[<=-1000000000][color=E2421D]-R$ #...,# B;  
[<=-1000000][color=E2421D]-R$ #..,# M;  
[<=-10000][color=E2421D]-R$ #. K;  
[<=-1000][color=E2421D]-R$ #.,# K;  
[<0][color=E2421D]-R$ #.##0

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
