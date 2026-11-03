---
article_id: 4410106880791
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: f909d34293e0b96a04ba52efd9ee549080e73360ce0e1a3bb8a67a0bf9d42450
fetched_at: '2026-06-28T22:39:36.914155+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como identificar
  a gravação do PIS/COFINS Apuração e o PIS/COFINS Retenção no Banco de Dados?
type: support-article
updated_at: '2023-02-24T00:08:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410106880791-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-identificar-a-grava%C3%A7%C3%A3o-do-PIS-COFINS-Apura%C3%A7%C3%A3o-e-o-PIS-COFINS-Reten%C3%A7%C3%A3o-no-Banco-de-Dados
---

**Dúvida**

Como identificar a gravação do PIS/COFINS Apuração e o PIS/COFINS Retenção no Banco de Dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

Como a quantidade de questões relacionadas à este assunto é relevante, estamos disponibilizando abaixo uma tutorial demonstrando

a diferença de gravação em banco de dados quando é calculado o PIS/COFINS Retenção ou Apuração.

* Em operações onde é calculado o **PIS/COFINS Retenção**, são gravados os campos abaixo:

- **PIS Retenção:**

D1\_BASEPIS | D1\_VALPIS

D2\_BASEPIS | D2\_VALPIS

F1\_BASEPIS | F1\_VALPIS

F2\_BASEPIS | F2\_VALPIS

FT\_BRETPIS | FT\_VRETPIS

- **COFINS Retenção:**

D1\_BASECOF | D1\_VALCOF

D2\_BASECOF | D2\_VALCOF

F1\_BASECOF | F1\_VALCOF

F2\_BASECOF | F2\_VALCOF

FT\_BRETCOF | FT\_VRETCOF

* Em operações onde é calculado o **PIS/COFINS Apuração**, são gravados os campos abaixo:

- **PIS Apuração:**

D1\_BASIMP6| D1\_VALIMP6

D2\_BASIMP6 | D2\_VALIMP6

F1\_BASIMP6 | F1\_VALIMP6

F2\_BASIMP6 | F2\_VALIMP6

FT\_BASEPIS | FT\_VALPIS -> Utilizado como base para o SPED

- **COFINS Apuração:**

D1\_BASIMP5 | D1\_VALIMP5

D2\_BASIMP5 | D2\_VALIMP5

F1\_BASIMP5 | F1\_VALIMP5

F2\_BASIMP5 | F2\_VALIMP5

FT\_BASECOF | FT\_VALCOF -> Utilizado como base para o SPED

**Assuntos relacionados:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como identificar em quais campos foram gravados o PIS/COFINS apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026245534-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-identificar-em-quais-campos-foram-gravados-o-PIS-COFINS-apura%C3%A7%C3%A3o-?source=search)

[MP - FIS - Qual a Configuração Necessária Para Gerar Nota Fiscal Com Cálculo de PIS E COFINS Via Apuração?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038813773-MP-FIS-Qual-a-Configura%C3%A7%C3%A3o-Necess%C3%A1ria-Para-Gerar-Nota-Fiscal-Com-C%C3%A1lculo-de-PIS-E-COFINS-Via-Apura%C3%A7%C3%A3o-?source=search)
