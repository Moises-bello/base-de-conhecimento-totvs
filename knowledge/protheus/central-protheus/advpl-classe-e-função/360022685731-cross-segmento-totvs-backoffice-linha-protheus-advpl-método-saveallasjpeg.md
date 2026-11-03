---
article_id: 360022685731
category: ADVPL - Classe e Função
content_hash: d6ba2817270c4e3c63be82f0e7d1e41993bfd56f9c6f43ffe982a9731bdd1e81
fetched_at: '2026-06-28T22:40:16.988568+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Método SaveAllAsJPEG
type: support-article
updated_at: '2022-02-02T12:14:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685731-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-M%C3%A9todo-SaveAllAsJPEG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**O método SaveAllAsJPEG() da classe TMSPrinter() não está funcionando corretamente.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A classe `TMSPrinter()` foi descontinuada e o método SaveAllAsJPEG() não é suportado pela classe FwMsPrinter.  
Assim sendo, torna-se necessário que a customização seja adaptada com a classe FwMsPrinter() para realização de impressão em \*.PDF.  
  
**Saiba mais**  
[FWMsPrinter](http://tdn.totvs.com/display/public/mp/FWMsPrinter)
