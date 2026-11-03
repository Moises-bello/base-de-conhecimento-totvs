---
article_id: 1500012694482
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 6c8dc1c9435351f868128ecc2ad3547c0440177dd740c10fd19f929cf9ccc556
fetched_at: '2026-06-28T22:39:20.523234+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Template DCL - ICMS-ST
  não é calculado para determinados CST's
type: support-article
updated_at: '2021-07-13T17:56:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012694482-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Template-DCL-ICMS-ST-n%C3%A3o-%C3%A9-calculado-para-determinados-CST-s
---

**Ocorrência**Ao utilizar o template DCL com necessidade de para realizar cálculo do ICMS-ST, sistema só está considerando cálculo para operações com alguns CST's.  
**Ambiente**  
Microsiga Protheus– Livros Fiscais – A partir da versão 11.80  
  
**Causa**

Este incidente ocorre por conta do parâmetro MV\_ICMSST estar configurado apenas para determinados CST.

**Solução**  
Ajustar o parâmetro MV\_ICMSST e inserir os CST's que necessitem calcular ICMS ST.  
Lembrando que esse parâmetro é de exclusivo uso para clientes que tem o Template DCL em seu ambiente.

EX: MV\_ICMSST = 10/70/90
