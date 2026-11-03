---
article_id: 360045775574
category: Escrita Fiscal - Impostos - IR
content_hash: da2ab2bef542fdbc8a8aa208aa14fac125bcb0d13c609b6c77939818470127d8
fetched_at: '2026-06-28T22:39:31.919965+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais campos são
  gravados na retenção de IRRF em uma nota de saída?
type: support-article
updated_at: '2021-06-17T13:19:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045775574-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-campos-s%C3%A3o-gravados-na-reten%C3%A7%C3%A3o-de-IRRF-em-uma-nota-de-sa%C3%ADda
---

**Dúvida**Quando efetuar saída e tiver IR retido, onde são gravadas as informações de IR?  
  
**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Saída de nota fiscal com retenção de IR, as informações são gravadas nas seguintes tabelas:

**Tabela SE1**

E1\_BASEIRF, E1\_IRRF, E1\_VRETIRF

**Tabela SF2**

F2\_BASEIRR, F2\_VALIRRF

**Tabela SD2**

D2\_BASEIRR, D2\_ALQIRRF D2\_VALIRRF

**Tabela SFT**

FT\_VALIRR, FT\_ALIQIRR, FT\_VALIRR

Configuração para tratamento da Retenção IR:  https://tdn.totvs.com/pages/releaseview.action?pageId=47908805
