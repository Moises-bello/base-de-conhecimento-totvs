---
article_id: 10318565159063
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 854b56f741abcf9420d0908def11feec0c2353f3c3879b1087c6916166f936bd
fetched_at: '2026-06-28T22:42:02.620414+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos -SPEDFISCAL -
  REGISTRO 0200 COMPO 09, QUANDO A NOTA FISCA FOR DO SIGAEIC.
type: support-article
updated_at: '2022-11-18T13:22:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10318565159063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-REGISTRO-0200-COMPO-09-QUANDO-A-NOTA-FISCA-FOR-DO-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar o campo 09 do **registro 0200** do arquivo do **SPED FISCAL**, quando a **Nota Fiscal** for de origem do **SIGAEIC**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Atualmente o campo existente no cadastro de **produtos (B1\_EX\_NCM**) é destinado as **exceções do IPI** e carrega essa informação ao **EFD ICMS/IPI**, onde é gravado no **campo 09 do registro 0200**, quanto a **informação de exceção do II poderá ser incluída no campo B1\_EX\_NBM** que é destinado a outras exceções ou ainda somente informado no **módulo do SIGAEIC**.

Quando estiver sendo utilizado o modulo do **SIGAEIC**, o fonte do **spedfiscal** irá verificar se o campo **EIJ\_EX\_IPI** tem informação e desta forma ira ser gerado a informação no **campo 09** do **registro 0200** do **arquivo EFD ICMS/IPI**.

Obs: Esta orientação será aplicada apenas para os cliente que utilizam o **modulo do SIGAEIC**, e que possuem a necessidade de gravar a informação **EX TARIFÁRIO II** - quando houver a exceção do **IPI (EXTIPI).**
