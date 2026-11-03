---
article_id: 360018332772
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 370747ee382276fce0bcfaa68a86949fa910edac3c5ea5aa83c66451d37fe7ed
fetched_at: '2026-06-28T22:38:28.730669+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Calculo
  da Média de Atraso (A1_METR)
type: support-article
updated_at: '2022-09-20T15:02:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018332772-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Calculo-da-M%C3%A9dia-de-Atraso-A1-METR
---

**Dúvida**

Qual a formula utilizada para gravação do campo **Media Atraso (A1\_METR)?**  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) – A partir da versão 11.80.  
  
  
**Solução**

A média de atraso é calculada pela seguinte fórmula:

SA1 -> A1\_METR = (A1\_METR\*(A1\_NROPAG-1) + (E1\_BAIXA - E1\_VENCREA)) / A1\_NROPAG

Onde:

A1\_METR = Média de atraso em dias (MA)  
A1\_NROPAG = Número de pagamentos (NP)  
E1\_BAIXA = Data da Baixa (DB)  
E1\_VENCREA = Vencto real do titulo (DV)

**MA = [(MA \* (NP-1) + (DB - DV))] / NP**

Supondo que o primeiro titulo atrasou 5 dias e este foi o primeiro titulo do cliente, neste caso a média de atraso anterior é zero.

MA = (0 \* (1 - 1) + (5)) / 1

MA = 5 (o cliente paga, em média, com 5 dias de atraso)

Supondo que um segundo titulo atrasou 3 dias

MA = (5 \* (2 - 1) + (3)) / 2

MA = 4 (o cliente paga, em média, com 4 dias de atraso)

Supondo que um terceiro titulo não teve atraso, sendo quitado no dia do vencimento

MA = (4 \* (3 - 1) + (0)) / 3

MA = 2,67 (o cliente paga, em média, com 2,67 dias de atraso)

Supondo que um quarto titulo titulo não teve atraso, sendo quitado 10 dias antes do vencimento  
MA = [(2.67 \* (4 - 1) + (-10))] / 4

MA = -0,50 (o cliente paga em média com meio dia de adiantamento)
