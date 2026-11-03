---
article_id: 360027922311
category: TAF - REINF
content_hash: 8ac873c265f9397aa61db5fccbc830ad97a03cc39393cd72b7f6d22fe9ce2086
fetched_at: '2026-06-28T22:41:33.576555+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Nota modelo 01 no TAF
type: support-article
updated_at: '2023-03-31T16:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027922311-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Nota-modelo-01-no-TAF
---

**Dúvida**Ao realizar a integração das notas com as espécies "RPS", "NFS" e "NFPS" o TAF sempre integrada como modelo 01 - Nota Fiscal ?  
   
 **Ambiente**TAF – Reinf – A partir da versão 12.1.17  
  
**Solução**

Na tabela 4.1.1 do sped fiscal, não existem códigos específicos para as espécies "RPS", "NFS" e "NFPS" que o cliente em questão está utilizando. Devido a isso foi realizada uma convenção interna onde ficou definido que para esses casos específicos, o extrator fiscal nos mandaria o código "01", pois não poderíamos receber esse campo em branco.
