---
article_id: 235302007
category: Materiais - Compras (SIGACOM)
content_hash: c7fbfaf6aa086afd9eae9e9c74b7ec6be810549751196447f67480b3a85be05f
fetched_at: '2026-06-28T22:41:22.120922+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ponto de Entrada MT120RCC
  - Permite manipular o aCols da rateio de centro ao iniciar a tela de rateio (pedido
  de compra)
type: support-article
updated_at: '2022-05-18T21:09:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ponto-de-Entrada-MT120RCC-Permite-manipular-o-aCols-da-rateio-de-centro-ao-iniciar-a-tela-de-rateio-pedido-de-compra
---

**Dúvida**

Ponto de Entrada MT120RCC - Permite manipular o aCols da rateio de centro ao iniciar a tela de rateio (pedido de compra)

**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

No Pedido de Compra (MATA120), esta localizado na função a120RatCC, antes de iniciar a tela do rateio.

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function MT120RCC()

Local aHeaderCH := PARAMIXB[1]  
Local aColsCH := PARAMIXB[2]

//Validações do usuario

Return aColsCH

***Saiba Mais :***

[MT120RCC - Ponto que permite manipular o aCols do Rateio](https://tdn.totvs.com/display/PROT/MT120RCC+-+Ponto+que+permite+manipular+o+aCols+do+Rateio)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
