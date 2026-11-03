---
article_id: 37354001232535
category: Escrita Fiscal - Error.log
content_hash: 4cba32aa39fd7dabca7bfdcc89bf0ed3501f8cec622f0dbb0c06e19d3baa4d6c
fetched_at: '2026-06-28T22:39:32.759319+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como corrigir o
  error log invalid class MESSAGEGROUPDECODER on TOTVS.PROTHEUS.BACKOFFICE.FISCAL.TCICLASS.TCIWRITTEN:GETDECODEDMESSAGES?
type: support-article
updated_at: '2026-01-08T14:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37354001232535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-corrigir-o-error-log-invalid-class-MESSAGEGROUPDECODER-on-TOTVS-PROTHEUS-BACKOFFICE-FISCAL-TCICLASS-TCIWRITTEN-GETDECODEDMESSAGES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37354044013719) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como corrigir o error log invalid class MESSAGEGROUPDECODER on TOTVS.PROTHEUS.BACKOFFICE.FISCAL.TCICLASS.TCIWRITTEN:GETDECODEDMESSAGES(BACKOFFICE.FISCAL.TAXCONFIGURATORINTEGRATION.TCICLASS.TLPP)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2210  
  
**Solução**  
Para correção do error log deve ser aplicado patch pontual abaixo:

12.1.2210:<https://r.totvs.io/p/1231475> ; 12.1.2310:<https://r.totvs.io/p/1231472> ; 12.1.2410:<https://r.totvs.io/p/1231473> ; 12.1.2510:<https://r.totvs.io/p/1231474> ;

**IMPORTANTE!!!**

**Esse pacote corrige pontualmente um falha no fonte com o erro, e deve ser aplicado no RPO do protheus e NÃO no RPO do TSS.**
