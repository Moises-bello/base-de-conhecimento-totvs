---
article_id: 360026251034
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: ee538031f67300253ef189de860e58ff6c99c412a59448bde215ed4d821aa460
fetched_at: '2026-06-28T22:39:36.921323+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como identificar
  em quais campos foram gravados o PIS/COFINS/CSLL retenção?
type: support-article
updated_at: '2021-06-22T12:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026251034-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-identificar-em-quais-campos-foram-gravados-o-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o
---

**Dúvida**

Como identificar em quais campos foram gravados o PIS/COFINS/CSLL Retenção?  
  
**Ambiente**

Protheus – Compras/Faturamento – A partir da versão 11.80.  
  
**Solução**

- Em operações onde é calculado o **PIS/COFINS/CSLL Retenção**, são gravados os campos abaixo:

**- PIS Retenção:**

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

- **CSLL Retenção:**

D1\_BASECSL | D1\_VALCSL

D2\_BASECSL | D2\_VALCSL

F1\_BASECSL | F1\_VALCSL

F2\_BASECSL | F2\_VALCSL

FT\_BRETCSL | FT\_VRETCSL

OBS: Referente às alíquotas, seguem os mesmos formatos acima onde temos "ALIQPIS, ALÍQCOF" e "ALIQCSL".
