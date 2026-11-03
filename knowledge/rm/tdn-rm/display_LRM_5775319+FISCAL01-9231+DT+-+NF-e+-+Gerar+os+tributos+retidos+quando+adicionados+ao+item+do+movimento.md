---
content_hash: 0d6ddf99aec4b77e7d5df66a3004684eb5ff431b9875e8c359834a58ed9170e8
fetched_at: '2026-06-29T00:10:25.026844+00:00'
page_id: '501126179'
product: rm
source: tdn-rm
title: 5775319 FISCAL01-9231 DT - NF-e - Gerar os tributos retidos quando adicionados
  ao item do movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/5775319+FISCAL01-9231+DT+-+NF-e+-+Gerar+os+tributos+retidos+quando+adicionados+ao+item+do+movimento
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | NF-e Estadual |
| Ticket: | 5775319 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9231 |

**02. SITUAÇÃO/REQUISITO**

Cliente solicita que ao realizar o envio da NF-e (Serviço) para Brasília, os tributos IRRF e CSLLRF adicionados ao item do movimento, possam ser considerados ao gerar o XML da NF-e.

**03. SOLUÇÃO**

Foi modificado o processo de envio de NF-e para que seja considerado os tributos retidos do item de movimento.

vRetPIS = PISRF  
vRetCOFINS = COFINSRF  
vRetCSLL = CSLLRF  
vIRRF = IRRFPJ, IRRF  
vBCIRRF = IRRFPJ,IRRF  
vBCRetPrev = INSS ou FUNRURAL  
vRetPrev = INSS ou FUNRURAL

ISSQNtot.vOutro = COSIRF, CONTRIBSOCIALRF

Validações:

Para a regra o sistema irá considerar os tributos retidos preenchidos no item, na ausência destes tibutos no item , o sistema irá verificar os tributos retidos do movimento. 

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
