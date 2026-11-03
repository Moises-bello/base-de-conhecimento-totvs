---
article_id: 360045779754
category: Escrita Fiscal - Impostos - IR
content_hash: 206191a57463753c604bac90c4f9e1176d446e21b4281bdefd19a1ecadfc479b
fetched_at: '2026-06-28T22:39:31.922960+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais campos são
  gravados na retenção do IRRF em uma nota de entrada?
type: support-article
updated_at: '2021-06-17T13:08:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045779754-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-campos-s%C3%A3o-gravados-na-reten%C3%A7%C3%A3o-do-IRRF-em-uma-nota-de-entrada
---

**Dúvida**Quando efetuar entrada de uma nota com retenção de IR retido, onde são gravadas as informações?  
  
**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Entrada de nota fiscal com retenção de IR, as informações são gravadas nas seguintes tabelas:

**Tabela SE2**

E2\_BASEIRF, E2\_IRRF, E2\_VRETIRF

**Tabela SF1**

F1\_BASEIRR, F1\_VALIRRF

**Tabela SD1**

D1\_BASEIRR, D1\_ALQIRRF D1\_VALIRRF

**Tabela SFT**

FT\_VALIRR, FT\_ALIQIRR, FT\_VALIRR

Configuração para tratamento da Retenção IR:  https://tdn.totvs.com/pages/releaseview.action?pageId=47908805
