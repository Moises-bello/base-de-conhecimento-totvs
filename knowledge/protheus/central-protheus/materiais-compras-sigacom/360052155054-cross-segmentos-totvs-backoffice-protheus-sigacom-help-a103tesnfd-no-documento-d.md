---
article_id: 360052155054
category: Materiais - Compras (SIGACOM)
content_hash: 01505a722415b5595ade37b7692663675eb512cb39aedc17b5d046c1f7f89ab8
fetched_at: '2026-06-28T22:41:18.842611+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A103TESNFD no
  Documento de Entrada
type: support-article
updated_at: '2025-12-16T13:11:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052155054-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A103TESNFD-no-Documento-de-Entrada
---

**Dúvida**

O que fazer quando ocorrer o Help A103TESNFD em notas de Devolução no módulo de Compras?  
  
**Ambiente**

Protheus  – Compras – A partir da versão 12

**Causa:**O erro ocorre, quando o campo Poder de Terc. **(F4\_PODER3)** da TES de Saída está incompatível com o campo Poder de Terc. **(F4\_PODER3)**de TES de Entrada utilizado no Documento de Devolução. E também quando o tipo da nota de entrada que está sendo usado é o tipo D ( usado pelo padrão somente para entradas que não movimentam o controle de poder de terceiros ). Quando há uma entrada de produtos recebidos de clientes e que movimentam o controle de poder de terceiros, o tipo da nota a ser utilizado é o B.

**Solução**

* ### **Exemplo A**

1. Se na TES de Saída o campo Poder Terc. **(F4\_PODER3)** estiver preenchido como **Remessa** conforme exemplo abaixo, o correto é que a TES de Entrada esteja configurado como Poder Terc. **(F4\_PODER3)** como **Devolução.**

* TES de Saída campo Poder Terc. **(F4\_PODER3)** = **Remessa**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085073673)

* TES de Entrada Campo Poder Terc **(F4\_PODER3)** = **Devolução**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085074153)

No exemplo acima se o campo Poder Terc **(F4\_PODER3)** estivesse com conteúdo **Normal** na nota de Devolução lançada no Documento de Entrada o Help seria apresentado, pois se foi utilizado um controle de Poder de terceiro na NF de Saída, na NF de Entrada referente a NF de Saída deverá ser configurado para ter o controle de Poder de Terceiro também, para que dessa forma não seja apresentado o Help.

* ### **Exemplo B**

2. Se na TES de Saída o campo Poder Terc. **(F4\_PODER3)** estiver preenchido como **Normal** conforme exemplo abaixo, o correto é que na TES de Entrada esteja configurado como Poder Terc. **(F4\_PODER3)** como **Normal.**

* TES de Saída Campo Poder Terc. **(F4\_PODER3)** = **Normal**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085074793)

* TES de Entrada Campo Poder Terc **(F4\_PODER3)** = **Normal**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085079693)

Se no Exemplo acima na TES de Entrada o campo Poder Terc. **(F4\_PODER3)**estivesse preenchido como **Remessa** ou **Devolução** o Help seria apresentado, pois, ficaria incompatível com o campo Poder Terc. **(F4\_PODER3)** da NF de Saída.

Saiba mais em :

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
