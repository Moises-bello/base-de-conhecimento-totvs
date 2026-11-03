---
article_id: 4417340891031
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cc42b7e4e923a775dd93ff5cba9eb87de7255d077ccdf26913b94a8fc3b95536
fetched_at: '2026-06-28T22:38:30.056088+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Títulos a pagar
  de IRRF via Faturamento
type: support-article
updated_at: '2021-12-28T18:17:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417340891031-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-T%C3%ADtulos-a-pagar-de-IRRF-via-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais os parâmetros e campos para gerar Títulos a pagar de IRRF (Imposto de Renda) no modulo Faturamento do Protheus   
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões  
  
**Solução**  
  
Abaixo os campos e parâmetros para gerar Títulos de Imposto de Renda a pagar no modulo Faturamento. Qualquer dúvida adicional, favor entrar em contato com suporte TOTVS Fiscal

**NATUREZA**

Calcula IRRF = SIM

Percentual de cálculo de IRRF = 1,5

Recolhe IRRF = 3 – Cad Cliente

**CLIENTE**

Recolhe IRRF (A1\_RECIRRF) = NÃO

Modo Abatimento do Imposto (A1\_ABATIMP) = Calculado pelo sistema

**PRODUTOS**

Impos Renda (B1\_IRRF) = Sim

**Parâmetros:**

|  |  |
| --- | --- |
| ***Parametro*** | ***Conteudo*** |
| **MV\_MP447** | F |
| **MV\_VENCIRF** | E |
| **MV\_VCTIRPF** | V |
| **MV\_ACMIRPF** | 2 |
| **MV\_ACMIRPJ** | 1 |
| **MV\_VC11196** | 2 |
| **MV\_PRZIRRF** | 1 |
| **MV\_IRMP232** | 2 |
| **MV\_ALIQIRF** | 1.5 |
| **MV\_IMPADT** | S |
| **MV\_NATNDF** | "NDF" |
| **MV\_VLRETIR** | 10.00 |
| **MV\_RATIRRF** | F |
| **MV\_IRF** | "IRF" |
| **MV\_IRPJ** |  |
| **MV\_RNDIRF** | .F. |
| **MV\_AGLIMPJ** | 3 |
| **MV\_ACMIRCR** | 1 |
| **MV\_ACMIRRF** | 1 |
