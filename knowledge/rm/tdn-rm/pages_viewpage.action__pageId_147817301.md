---
content_hash: bc63fe29a2794c3578e5599b37f33a840058ba64e5ed453134771d47524257fc
fetched_at: '2026-06-29T00:05:55.937369+00:00'
page_id: '147817301'
product: rm
source: tdn-rm
title: Como se processa Pagamento e Desconto de Adiantamento de salário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=147817301
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Como se processa Pagamento e Desconto de Adiantamento de salário?** |
| Solução | Primeiramente cria-se o evento de Desconto (Código de Cálculo 19) e Provento (Código de Cálculo 34).  Evento CC 19 -> <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AdiantamentoQuinzenalDesconto.aspx>  Evento CC 34 -> <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.PagamentoAdiantamentoProvento.aspx>  O lançamento dos eventos deverá ser executado através do menu "Lançamentos automáticos | Grupos de eventos", sendo que o evento de CC 19 deverá ser lançado após o lançamento do CC 34 em um Grupo de evento separado |
