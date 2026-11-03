---
article_id: 1500010468942
category: Financeiro - Baixas a Receber
content_hash: ebfa0276c1d0b5c2f0945a42b9b8fd708678c98954d651eb202f252df4a09da5
fetched_at: '2026-06-28T22:37:43.729105+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Qual o funcionamento
  do campo E1_VALLIQ  - Vlr.Liq Baix
type: support-article
updated_at: '2025-07-30T17:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010468942-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Qual-o-funcionamento-do-campo-E1-VALLIQ-Vlr-Liq-Baix
---

**Dúvida**Qual o funcionamento do campo **E1\_VALLIQ** (Vlr.Liq Baix)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O campo **E1\_VALLIQ** registra apenas o valor da movimentação individual, **sem realizar acúmulo de valores**.

**Exemplo**

Independentemente do tipo de baixa realizada, ao efetuar o cancelamento, o valor final registrado será **zero**. Isso ocorre porque o cancelamento reflete a movimentação inversa do valor baixado. Por exemplo, se a baixa foi de R$ 50.000,00, o cancelamento gerará um valor de **-R$ 50.000,00**, resultando em um saldo líquido de **R$ 0,00**.

Observe o seguinte comportamento na liquidação parcial:

* Na **1ª baixa parcial** de R$ 50.000,00, o campo **E1\_VALLIQ** registra R$ 50.000,00.
* Na **2ª baixa parcial** de R$ 10.000,00, o campo **E1\_VALLIQ** registra **apenas R$ 10.000,00**, e **não acumula** com a primeira baixa, ou seja, **não totaliza R$ 60.000,00**.

**Importante**O controle de saldo pode ser realizado por meio da **consulta de posição do título**.

**Saiba Mais**

[Gravação\_do\_campo\_E1\_VALLIQ](https://tdn.totvs.com/pages/releaseview.action?pageId=286004910)
