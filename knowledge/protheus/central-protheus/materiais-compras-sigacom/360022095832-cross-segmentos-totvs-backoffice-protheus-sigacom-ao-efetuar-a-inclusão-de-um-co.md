---
article_id: 360022095832
category: Materiais - Compras (SIGACOM)
content_hash: 1bac09abf8858c0c3880156bb79eaa938982333bc8368ff8c311770101ee7414
fetched_at: '2026-06-28T22:41:14.135286+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao efetuar a inclusão
  de um conhecimento de frete, via rotina automática, o sistema apresenta o error
  log : type mismatch on ascan on RATPED2NF(MATA103X.PRX) 19/12/2018 15:35:03 line
  : 12535'
type: support-article
updated_at: '2022-05-16T21:14:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022095832-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-efetuar-a-inclus%C3%A3o-de-um-conhecimento-de-frete-via-rotina-autom%C3%A1tica-o-sistema-apresenta-o-error-log-type-mismatch-on-ascan-on-RATPED2NF-MATA103X-PRX-19-12-2018-15-35-03-line-12535
---

**Ocorrência**  
Ao efetuar a inclusão de uma nota de **conhecimento de frete** através de **rotina automática** o sistema apresenta o error.log:

**type mismatch on ascan on RATPED2NF(MATA103X.PRX)** 19/12/2018 15:35:03 line : 12535  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17  
  
**Causa**

Este incidente ocorre pois se faz necessário passar corretamente os campos do array de **centro de custo aRateioCC.**  
  
**Solução**

Para corrigir o incidente verificar se todos os campos do array de centro de custo estão sendo passados, sendo os listados abaixo, sendo necessário poderá verificar o execauto da rotina automática do **MATA116** afim de verificar se o array do centro de custo esta sendo chamado corretamente :

nPosRatCC  := Ascan(aAux[nX],{|x| AllTrim(x[1]) == "**DE\_CC**" })  
nPosRatPer := Ascan(aAux[nX],{|x| AllTrim(x[1]) == "**DE\_PERC**"})  
nPosRatCLVL := Ascan(aAux[nX],{|x| AllTrim(x[1]) == "**DE\_CLVL**"})  
nPosRatItCta := Ascan(aAux[nX],{|x| AllTrim(x[1]) == "**DE\_ITEMCTA**"})  
nPosRatConta := Ascan(aAux[nX],{|x| AllTrim(x[1]) == "**DE\_CONTA**"})

Exemplo da Rotina automática do MATA116:

[MATA116 - Programa de digitação de Nota Fiscal de conhecimento de Frete](http://tdn.totvs.com/pages/releaseview.action?pageId=6085187)

***OBSERVAÇÃO :***

Para maiores dúvidas e/ou informações sobre rotina automática, solicitar o apoio à equipe de suporte do ADVPL.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
