---
article_id: 360039084454
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: c922bedc7ee5fc7233a99122a8c1ac3d720e2ade354255e7f667aa34d04c8411
fetched_at: '2026-06-28T22:39:36.978389+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: MP - FIS - Como configurar Pis/Cofins/Csll para Auto Peças?
type: support-article
updated_at: '2021-09-27T13:49:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039084454-MP-FIS-Como-configurar-Pis-Cofins-Csll-para-Auto-Pe%C3%A7as
---

**Dúvida**Como configurar Pis/Cofins/Csll para Auto Peças?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

**Apuração**

**TES**

PIS/COFINS (F4\_PISCOF) = Ambos

Cred. PIS/COF = Debita

Tp Regime (F4\_TPREG) = Não cumulativo

Para o valor do IPI não compor a base de calculo do IR, do PIS ou da COFINS , para operações de saída ou complemento de IPI.

IPI na BC (F4\_IPIPC) = 2

Para o valor do IPI compor a base de calculo do IR, do PIS ou da COFINS , para operações de saída ou complemento de IPI.

IPI na BC (F4\_IPIPC) = Branco ou 1

**PARÂMETROS**

MV\_TXPIS = 1.65

MV\_TXCOFIN = 7.6

Retenção  
Para a retenção de 0,10% e 0,50%, configure a natureza e outros cadastros:

**NATUREZA**

Calcula PIS (ED\_CALCPIS) = Sim

Percentual de PIS (ED\_PERCPIS) = 0,10

Calcula COFINS (ED\_CALCCOF) = Sim

Percentual de COFINS (ED\_PERCCOF) = 0,50

**PRODUTO**

Retem PIS (B1\_PIS) = Sim

Retem COFINS (B1\_COFINS) = Sim

Ret.Operacao (B1\_RETOPER) - Indica se o produto faz parte dos Anexos I e II da Lei 10.485 de 03/07/2002 e deverá ter os valores do PIS e da Cofins retidos em cada operação (de acordo com a lei 11.196 de 21/11/2005), não sendo aplicado valor mínimo de retenção.

**CLIENTE**

Recolhe COFINS (A1\_RECCOF) = Sim

Recolhe PIS (A1\_RECPIS) = Sim
