---
content_hash: 8f7c1f1f13e9529ba29b878cf6df873da0ddafde2a09bef61d1fee7486af33ba
fetched_at: '2026-06-29T00:09:12.945154+00:00'
page_id: '419528770'
product: rm
source: tdn-rm
title: 3456399 FISCAL01-6569 DT NF-e 4.0 - Geração das tags vBCRetPrev e vRetPrev
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419528770
version: 3
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e 4.0 |

**02. SITUAÇÃO/REQUISITO**

Ao realizar o envio da nota fiscal no layout 4.0 com os tributos FunRural, GILRAT e SENAR nos tributos do Movimento, os 3 tributos são do tipo FunRural,   
no xml não esta sendo gerado as tags "vBCRetPrev" e "vRetPrev".

**03. SOLUÇÃO**

Ajuste no Processo de Envio da NF-e para que quando o Tributo for do tipo FunRural as tags "vBCRetPrev" e "vRetPrev" sejam geradas corretamente.
