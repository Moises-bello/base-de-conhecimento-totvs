---
article_id: 360027336312
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 933605f6f18a4e7ae92704e0765059c3577dbf4559e5e807d649ca77be0d9dac
fetched_at: '2026-06-28T22:39:36.946703+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - ICMS ST agregado
  indevidamente após o tratamento de deduzir o ICMS próprio na base do PIS e COFINS.
type: support-article
updated_at: '2021-06-22T13:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027336312-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-ICMS-ST-agregado-indevidamente-ap%C3%B3s-o-tratamento-de-deduzir-o-ICMS-pr%C3%B3prio-na-base-do-PIS-e-COFINS
---

**Dúvida**

Cliente deduziu o ICMS próprio e na sua base de cálculo está agregando o ICMS ST na base do PIS e COFINS, como resolver?

**Ambiente**

Protheus - MATA103 - A partir da versão 11.30.  
  
**Solução**

Cliente fez a tratativa de dedução do ICMS próprio conforme destaca o artigo abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020917572-MP-FIS-Valor-de-ICMS-na-Base-de-C%C3%A1lculo-do-PIS-COFINS?source=search>

Contudo, cliente possui memória de cálculo o ICMS ST. O problema inicia na base de cálculo, pois como foi feito a tratativa em deduzir o ICMS próprio, o sistema começa **a agregar** na base do PIS e COFINS o ICMS ST. Para resolver essa questão é necessário deixar os parâmetros abaixo nesta opção:

**MV\_DBSTPIS = 6**

**MV\_DBSTCOF = 6**
