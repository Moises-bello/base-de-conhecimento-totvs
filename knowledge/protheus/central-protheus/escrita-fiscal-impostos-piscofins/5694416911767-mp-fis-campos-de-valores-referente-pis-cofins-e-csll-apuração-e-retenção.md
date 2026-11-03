---
article_id: 5694416911767
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: f9ff3d053ca8812b77aa61f825c276c31d87613576bef788bdcafa9cfed7e963
fetched_at: '2026-06-28T22:39:36.974785+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: MP - FIS - Campos de Valores Referente Pis, Cofins e CSLL - Apuração e Retenção. 
type: support-article
updated_at: '2024-10-08T21:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5694416911767-MP-FIS-Campos-de-Valores-Referente-Pis-Cofins-e-CSLL-Apura%C3%A7%C3%A3o-e-Reten%C3%A7%C3%A3o
---

**Dúvida**  
Campos de Valores Referente Pis, Cofins e CSLL - Apuração e Retenção.   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

PIS e COFINS apuração são gravados nos campos:  
  
**PIS/COFINS Apuração**  
**Saída**  
F2\_BASIMP5, F2\_BASIMP6, F2\_VALIMP5, F2\_VALIMP6,   
D2\_BASIMP5,D2\_ALQIMP5, D2\_VALIMP5, D2\_BASIMP6,D2\_ALQIMP6, D2\_VALIMP6  
FT\_BASEPIS, FT\_ALIQPIS, FT\_VALPIS, FT\_BASECOF, FT\_ALIQCOF, FT\_VALCOF  
  
  
**Entrada**  
F1\_BASIMP5, F1\_BASIMP6, F1\_VALIMP5, F1\_VALIMP6  
D1\_BASIMP5,D1\_ALQIMP5, D1\_VALIMP5, D1\_BASIMP6,D1\_ALQIMP6, D1\_VALIMP6  
FT\_BASEPIS, FT\_ALIQPIS, FT\_VALPIS, FT\_BASECOF, FT\_ALIQCOF, FT\_VALCOF  
  
**Importante:**  
IMP5 refere-se ao COFINS  
IMP6 refere-se a o PIS  
  
**Para Retenção são gravados:**  
  
**Saída**  
D2\_BASEPIS, D2\_ALQPIS, D2\_VALPIS  
D2\_BASECOF, D2\_ALQCOF, D2\_VALCOF  
D2\_BASECSL, D2\_ALQCSL, D2\_VALCSL  
FT\_BRETPIS, FT\_ARETPIS, FT\_VRETPIS  
FT\_BRETCOF, FT\_ARETCOF, FT\_VRETCOF  
FT\_BRETCSL, FT\_ARETCSL, FT\_VRETCSL  
  
**Entrada:**  
D1\_BASEPIS, D1\_ALQPIS, D1\_VALPIS  
D1\_BASECOF, D1\_ALQCOF, D1\_VALCOF  
D1\_BASECSL, D1\_ALQCSL, D1\_VALCSL  
FT\_BRETPIS, FT\_ARETPIS, FT\_VRETPIS  
FT\_BRETCOF, FT\_ARETCOF, FT\_VRETCOF  
FT\_BRETCSL, FT\_ARETCSL, FT\_VRETCSL
