---
content_hash: 6485e77cad14c12244dbef81fc752e2f738cf2bef50b37687f9368fdd9fa6871
fetched_at: '2026-06-29T00:09:12.948077+00:00'
page_id: '419529700'
product: rm
source: tdn-rm
title: 3968366 FISCAL01-6627 DT - SEFII E120
type: documentation
url: https://tdn.totvs.com/display/LRM/3968366+FISCAL01-6627+DT+-+SEFII+E120
version: 1
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Estadual SEF - Pernambuco |

**02. SITUAÇÃO/REQUISITO**

Ao realizar a geração da SEF II para Pernambuco, os lançamentos com o código do modelo do documento 63 que se refere a Bilhete de Passagem Eletrônico não está gerando o registro E120.

**03. SOLUÇÃO**

Implementação no registro E120:

* Carregar chave de acesso do movimento para modelo de documento (63)BP-e
* Não será gerado o campo (04)COD\_PART para modelo de documento (63)BP-e
* Será gerado também documentos modelo (67) CT-e OS

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
