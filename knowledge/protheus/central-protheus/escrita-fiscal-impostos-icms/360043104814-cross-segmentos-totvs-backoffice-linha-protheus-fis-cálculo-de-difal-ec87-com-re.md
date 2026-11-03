---
article_id: 360043104814
category: Escrita Fiscal - Impostos - ICMS
content_hash: ec77d906a9d659030d55c629c68d29534d0636108698dd70ceb3514c9d54cfc5
fetched_at: '2026-06-28T22:39:24.103180+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Cálculo de Difal
  ec/87 com reduções diferentes pela exceção fiscal
type: support-article
updated_at: '2021-07-28T02:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043104814-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Difal-ec-87-com-redu%C3%A7%C3%B5es-diferentes-pela-exce%C3%A7%C3%A3o-fiscal
---

**Dúvida**Cálculo de Difal ec/87 com reduções diferentes pela exceção fiscal  
  
**Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
  
**Solução**

- Parâmetro SX6:

* MV\_BICMCMP = .F.

- Cadastro de Cliente:

* (A1\_INSCR - Inscrição Estadual) em branco.
* (A1\_TIPO - Tipo) preenchido com Consumidor Final.

- Cadastro de TES:

* (F4\_ICM - Calcula ICMS) = Sim
* (F4\_LFICM - L.Fisc.ICM) Diferente de Não
* (F4\_COMPL - Calc.Dif.Icm) = Sim
* (F4\_CONSUMO - Mat.Consumo) = Sim
* (F4\_DIFAL - Calc. Difal) = Sim

Exceção fiscal

% red icms = 26,57

% red base difal = 48,24

Cadastro de clientes

![](https://ci6.googleusercontent.com/proxy/1bMP3EZU3km8kMADr0gUxxVBxgg4Mw5fbhwh9ZZmTNaUndB034L8vLoveJX2q2M3lx3ieJsUDO_nWB4hL12Rrm4Ma223W-eg5MH7CqDnHKhSGEwVWitoL3XoCFlSp-LEP-D9piPo5hyd8tXjHcXo7blpaUg_lLKq_Yo=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/91OhtnUTJN9u5bc7GdkPLtlIC/?name=inline1858313552.png)

cadastro de produtos

![](https://ci6.googleusercontent.com/proxy/tjieB5BJPd8S-FhMCY_bJ2Lcp1D3r8BoWZgo51tsvGrwB5R48s8eJ4sjYth1HsVK0Lx2WEQ11ty147-DHl2jHvYr71Gl3pPzBOPebSNLExZSqai9zQR7QY3EoqrdF_tc3HNuSSOjkNYjzF1BBT8X7uuEewmFOaENiy0b=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/gcB8wQ35au2C3giuiQ0gWVYx8/?name=inline-1298872938.png)

Exceção fiscal

![](https://ci6.googleusercontent.com/proxy/7fKexYbQ75ORgwuDoC_f13NfysWjTowjG0Xz9r4YdZEfKpo_RCgare5UyvRg_M5YiFIP5bs2AYVxRpNfbSUdqC7MZ0IcnfiY5fpZe50XbQaGZ6b5l43JvqTLwXRAtEzQdw07IYWNH8jZhDGvc0hziLD5cOWg-Msw7w=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/Zh4x2muLClyRoq7dz3T2dhWov/?name=inline533787575.png)

![](https://ci6.googleusercontent.com/proxy/15u9ck8ko39AzNZ0Xii4QnQDobJdNElLIi9tcC28es158FiIxttHlywQxRpt0QAILBJ6V5i1tV1hSWhUXyXB8CBXy_n_yXZoQkuW4e4NWmujX-8WISj7xQ0YDY0-KEPHhFV1_LjvXV5l9l9vnHrBRHiUB4m__8i8O67L=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/xypWPl7skUZ5COG14ReRExNaX/?name=inline-1048391182.png)

![](https://ci5.googleusercontent.com/proxy/KSPQKDXHGfabN4aBankvVn7TmSoNMDwJQGh-u-A5HAxenkxvkv9UEb6iN1B-pkFXBkXU6VrSq02YKNhzlHhYlJnDcH8wh9eThLACHzmQKk_Dc4o-Gq9fl-DISBTC89gxIVZp-1SzXvMoA1yV-QfBpOsClwcdkSOxn7w=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/vtQb6o2ihBpp80T1USABcmoDE/?name=inline1689212427.png)

TES

![](https://ci5.googleusercontent.com/proxy/czNQlxQit47CHCMVamWaztNO9hJDgUdgRGOJ9WTCDCaHITnIElXXKWajZm8xSDFfhi_PMRNgriszmaflz697o10ij3ksk3CcME6h9U6t3j-mhql4xXAPwPYPRXPXabDxNAubT5Wdmxm_DqRTlpdX04EUWMYEfmE4FDE=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/GuLDOeJARxE3GkyYD4wYyKO5y/?name=inline1911655996.png)

![](https://ci4.googleusercontent.com/proxy/v1u0K9g9J6CAZg0Igvogg_W9xJaNXBF2zcA1Qes64bPdmWj7pGFUhuTBNVVA-0PfvMRhFAYrsiMruoXACYaksNY37DNKo-L6PyV1hgVk6yGMMg9g-J52kh5he16BvYCFUrr18163gZj9_-QlmuGGrwAduPr7_pWzIrY=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/Mji1QbVKOG2KHMAPTLGCdnzRo/?name=inline1994798755.png)

Teste efetivado nota fiscal de saídas

![](https://ci6.googleusercontent.com/proxy/l_QcvF14XBGdpWkxh_S0m_CCkBe8PUNOfrOho363El2yN0L1BRVEWCOc10b82sGgI4FKIlr58SaKLAHsEoKNXlgO1ATacu7JslBmyvVii3KVUCBATm_Bk1d5PlmPvFp93RPQL5a_Pg83b82FJcHfrlinFmDtRdbo6cVt=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/xoErz3K1baEsProzCj3YxIukn/?name=inline-1084261026.png)

<https://tdn.totvs.com/display/public/PROT/TVIBXE_DT_REDUCAO_BASE_DE_CALCULO_ICMS_COMPLEMENTAR_DIFAL_SAIDA>
