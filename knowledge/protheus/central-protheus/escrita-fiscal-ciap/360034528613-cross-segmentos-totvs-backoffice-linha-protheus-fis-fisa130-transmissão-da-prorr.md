---
article_id: 360034528613
category: Escrita Fiscal - CIAP
content_hash: 19d351983a03ac8f4dd91bf1bfc69812a18acf44f0c6c27bc91397144f71fc02
fetched_at: '2026-06-28T22:39:33.974246+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- FISA130 - Transmissão
  da prorrogação da suspensão do ICMS, conforme NT 2015 01
type: support-article
updated_at: '2021-07-28T17:20:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034528613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA130-Transmiss%C3%A3o-da-prorroga%C3%A7%C3%A3o-da-suspens%C3%A3o-do-ICMS-conforme-NT-2015-01
---

**Dúvida**Como gerar registro na tela da rotina de FISA130, para transmissão do evento de prorrogação.

**Ambiente**A partir da versão 11.80  
  
**Solução**

1 - Utilizar um TES com campo Poder Terc. (F4\_PODER3) =R-Remessa, para alimentar a Tabela SB6.  
2- Emitir uma nota de saída modelo 55(SPED).  
3- Transmitir/autorizar a Nota.  
4- Acessar a rotina FISA130, para transmissão do evento de Prorrogação.
