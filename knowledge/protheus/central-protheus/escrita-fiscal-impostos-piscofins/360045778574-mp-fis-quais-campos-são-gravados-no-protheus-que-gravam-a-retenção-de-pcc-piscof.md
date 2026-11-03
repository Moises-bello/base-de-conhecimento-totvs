---
article_id: 360045778574
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: ca6de7ae81e994a779a73285101eff0891b541e51c8af6ec73ac739f518ec552
fetched_at: '2026-06-28T22:39:36.992956+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: MP - FIS - Quais campos são gravados no Protheus que gravam a retenção de PCC
  "PIS/COFINS/CSLL em uma nota de Entrada ?
type: support-article
updated_at: '2021-04-28T20:03:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045778574-MP-FIS-Quais-campos-s%C3%A3o-gravados-no-Protheus-que-gravam-a-reten%C3%A7%C3%A3o-de-PCC-PIS-COFINS-CSLL-em-uma-nota-de-Entrada
---

**Dúvida**Quando efetuar entrada e tiver IR retido, onde são gravadas as informações de PCC "PIS/COFINS/CSLL"  
   
 **Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
   
 **Solução**

Quando efetuar entrada e tiver PCC "PIS/COFINS/CSLL" retido, as informações são gravadas nos seguintes campos:

**Tabela SE2**

E2\_BASEPIS, E2\_PIS  
E2\_BASECOF, E2\_COFINS  
E2\_BASECSL, E2\_CSLL

**Tabela SF1**

F1\_BASPIS, F1\_VALPIS  
F1\_BASCOFI, F1\_VALCOF  
F1\_BASCSLL, F1\_VALCSLL

**Tabela SD1**

D1\_BASEPIS, D1\_ALQPIS, D1\_VALPIS  
D1\_BASECOF, D1\_ALQCOF, D1\_VALCOF  
D1\_BASECSL, D1\_ALQCSL, D1\_VALCSL

**Tabela SFT**

FT\_BRETPIS, FT\_ARETPIS, FT\_VRETPIS  
FT\_BRETCOF, FT\_ARETCOF, FT\_VRETCOF  
FT\_BRETCSL, FT\_ARETCSL, FT\_VRETCSL

Configuração para tratamento da Retenção PCC "PIS/COFINS/CSLL": <https://tdn.totvs.com/pages/releaseview.action?pageId=6076816>
