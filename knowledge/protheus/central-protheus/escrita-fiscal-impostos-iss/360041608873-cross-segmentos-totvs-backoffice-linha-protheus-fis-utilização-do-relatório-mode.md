---
article_id: 360041608873
category: Escrita Fiscal - Impostos - ISS
content_hash: a366ce4cd16a5656b0a3fe5e0425181dba938046a78877d1e4a6467c8253e979
fetched_at: '2026-06-28T22:39:35.264756+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Utilização do Relatório
  modelo 56 ISS (MATR912) pela data de entrada ou emissão
type: support-article
updated_at: '2021-09-30T21:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041608873-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Utiliza%C3%A7%C3%A3o-do-Relat%C3%B3rio-modelo-56-ISS-MATR912-pela-data-de-entrada-ou-emiss%C3%A3o
---

**Dúvida:**

Com utilizar o relatório do ISS pela data de entrada ou data de emissão?

**Ambiente:**

Protheus – Livros Fiscais – A partir da versão 12.1.17.  
  
**Solução:**

GERAÇÃO DE NOTAS NO MATR912(56) PELA ENTRADA OU EMISSÃO:  
  
**DATA DE EMISSÃO:**  
MV\_EMIENT = .F.  
MV\_VSEMENT = .F.  
  
**DATA DE ENTRADA:**  
MV\_EMIENT = .T.  
MV\_VSEMENT = .T.
