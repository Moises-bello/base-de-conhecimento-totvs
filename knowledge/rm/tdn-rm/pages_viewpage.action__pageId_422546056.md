---
content_hash: 393602d335e13f00a308e9e45d63aae097086d84c483a3f39aa57d0eda9f3bfc
fetched_at: '2026-06-29T00:09:23.146213+00:00'
page_id: '422546056'
product: rm
source: tdn-rm
title: SEF II (Origem dos Dados)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546056
version: 4
---

A rotina é gerada exclusivamente com dados retirados do produto TOTVS Gestão Fiscal[,](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) com exceção dos dados de Inventário de Estoque. Estas informações deverão ser gravadas de forma manual, importação por texto ou escrituradas do [TOTVS Gestão de Estoque,Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835)[.  
 Alguns registros da rotina solicitam informações dos](http://tdn.totvs.com/pages/viewpage.action?pageId=423937954) [tributos](http://tdn.totvs.com/display/LRM/Tributos) [(ICMS, IPI e ISSQN) por item movimentado. Portanto estes deverão estar parametrizados nos Itens do](http://tdn.totvs.com/pages/viewpage.action?pageId=422546150) [Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=431680255)[.  
 As informações referentes ao Inventário do Estoque são retiradas do](http://tdn.totvs.com/pages/viewpage.action?pageId=422546150) [TOTVS Gestão de Estoque,Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835)[. Para a correta geração destas informações todos os processos de](http://tdn.totvs.com/pages/viewpage.action?pageId=423937954)[geração de saldo de inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423937977) [deverão ter sido disparados antes da geração da rotina.  
 É importante lembrar que os lotes de Lançamento Fiscal deverão ter sido liberados e os](http://tdn.totvs.com/pages/viewpage.action?pageId=423937977) [períodos de apuração](http://tdn.totvs.com/pages/viewpage.action?pageId=422545773) [dos tributos  antes da geração da rotina.](http://tdn.totvs.com/pages/viewpage.action?pageId=431677780)
