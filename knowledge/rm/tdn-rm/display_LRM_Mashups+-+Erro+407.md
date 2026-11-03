---
content_hash: ee908a20639fd0515bd4a3402f2aa5d5bc098242bfe7f558be113f9b214c3f19
fetched_at: '2026-06-29T00:05:54.074167+00:00'
page_id: '107382172'
product: rm
source: tdn-rm
title: Mashups - Erro 407
type: documentation
url: https://tdn.totvs.com/display/LRM/Mashups+-+Erro+407
version: 7
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer a solução para o Erro 407 - Proxy Authenication Required.

# Solução:

---

       É preciso preencher os dados de Proxy nos parâmetros Globais, clicando em: ***SERVIÇOS GLOBAIS > AMBIENTE > PARÂMETROS > PARAMETROS  GLOBAIS > ABA GOOGLE OU PROXY***

       Além disso, deverá ser criado uma regra no proxy que libere os seguintes links:

**[http://share.totvs.com.br/RMSMarketPlaceWS/RMSMarketPlaceWS.asmx](http://share.totvs.com.br/RMSMarketPlaceWS/RMSMarketPlaceWS.asmx "http://share.totvs.com.br/RMSMarketPlaceWS/RMSMarketPlaceWS.asmx")****[http://feeds.feedburner.com/TotvsConnect](http://feeds.feedburner.com/TotvsConnect "http://feeds.feedburner.com/TotvsConnect").****[http://mashups.totvs.com.br](http://mashups.totvs.com.br/)**

       Outros endereços que também poderão ser configurados p/ esta regra no proxy:

- totvs.com.br  
 - wikihelp.totvs.com.br  
 - share.totvs.com.br  
 - translate.google.com  
 - widgets.twimg.com  
 - google.com  
 - 189.89.45.16   
 - 189.89.45.13  
- mashups.totvs.com.br

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX

false

**Processo:** Erro 407 - Proxy Authentication Required

falsefalse

**Status:** Finalizado

false

**Data:** 04/08/2016

false

**Autores:**
