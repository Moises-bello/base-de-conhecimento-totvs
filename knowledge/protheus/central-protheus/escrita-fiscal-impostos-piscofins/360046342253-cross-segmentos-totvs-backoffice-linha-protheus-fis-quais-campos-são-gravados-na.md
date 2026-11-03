---
article_id: 360046342253
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: a9971bfd11cfba28f5d616e8d7576579c2608e804f9e6f3a1b4d270d684690eb
fetched_at: '2026-06-28T22:39:36.767552+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais campos são
  gravados na retenção de PCC “PIS/COFINS/CSLL” em uma nota de saída?
type: support-article
updated_at: '2021-06-17T13:51:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046342253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-campos-s%C3%A3o-gravados-na-reten%C3%A7%C3%A3o-de-PCC-PIS-COFINS-CSLL-em-uma-nota-de-sa%C3%ADda
---

**Dúvida**Quando efetuar SAÍDA de nota fiscal e tiver retenção de PCC “PIS/COFINS/CSLL, onde são gravadas as informações de PCC “PIS/COFINS/CSLL” ?

**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Saída de nota fiscal com retenção de PCC, as informações são gravadas nas seguintes tabelas:

**Tabela SE1**

E1\_BASEPIS, E1\_PIS, E1\_VRETPIS

E1\_BASECOF, E1\_COFINS, E1\_VRETCOF

E1\_BASECSL, E1\_CSLL, E1\_VRETCSL

**Tabela SF2**

F2\_BASPIS, F2\_VALPIS  
F2\_BASCOFI, F2\_VALCOFI  
F2\_BASCSLL, F2\_VALCSLL

**Tabela SD2**

D2\_BASEPIS, D2\_ALQPIS, D2\_VALPIS

D2\_BASECOF, D2\_ALQCOF, D2\_VALCOF

D2\_BASECSL, D2\_ALQCSL, D2\_VALCSL

**Tabela SFT**

FT\_BRETPIS, FT\_ARETPIS, FT\_VRETPIS

FT\_BRETCOF, FT\_ARETCOF, FT\_VRETCOF

FT\_BRETCSL, FT\_ARETCSL, FT\_VRETCSL

Configuração para tratamento da Retenção PCC “PIS/COFINS/CSLL:  https://tdn.totvs.com/pages/releaseview.action?pageId=6076816
