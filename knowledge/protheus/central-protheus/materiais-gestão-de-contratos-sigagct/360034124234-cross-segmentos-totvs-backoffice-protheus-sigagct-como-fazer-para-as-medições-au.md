---
article_id: 360034124234
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: da000a583ab5114d43936f46375bace42cb2c2748d349aad6e90deae6e7ba169
fetched_at: '2026-06-28T22:37:21.499329+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como fazer para as
  Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição (CNTA121)
  ?  - MV_CT26021
type: support-article
updated_at: '2022-12-02T11:20:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034124234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-fazer-para-as-Medi%C3%A7%C3%B5es-Autom%C3%A1ticas-CNTA260-serem-geradas-pela-Rotina-Nova-Medi%C3%A7%C3%A3o-CNTA121-MV-CT26021
---

**Ocorrência**Como fazer para as Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição  ?(CNTA121)

**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Causa**

Quando o sistema executa a rotina de Geração de ***Medições Automáticas (CNTA260)*** gerava as medições através da rotina antiga de ***Medições (CNTA120)***, e hoje com sua descontinuação, elas devem ser geradas pela rotina ***Nova Medição(CNTA121).***

**Solução**

Para que o sistema gere as medições automáticas na rotina ***CNTA260*** através da rotina de Nova Medição é necessária a criação do parâmetro ***MV\_CT26021*** conforme abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044162154/mceclip3.png)

**Importante**

O parâmetro MV\_CT26021 será disponibilizado de forma padrão no próximo release 12.1.33

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
