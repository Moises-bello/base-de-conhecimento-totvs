---
article_id: 7446885427223
category: Faturamento - Cadastros
content_hash: 7fdc7111e60d13328d591d04d92d61f563277d496e06340864188478559e8565
fetched_at: '2026-06-28T22:38:35.364775+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Mashup e Api
  Carol não funcionam no crma980
type: support-article
updated_at: '2022-07-13T20:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7446885427223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Mashup-e-Api-Carol-n%C3%A3o-funcionam-no-crma980
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00  min** **Dúvida**Mashup e API CArol não funcionam no crma980.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- a partir da release  12.1.27.  
  
**Solução**

Para o correto funcionamento da **API Carol** e do **Mashup** na nova rotina **crma980** é preciso ativar o parâmetro **mv\_mvcsa1 para .T.**, mesmo para os casos onde a rotina foi incluída diretamente no menu do SIGAFAT, para que o sistema passe a ler a rotina **crma980** corretamente , e deixar de considerar o **mata030**, que encontra-se descontinuado desde 04/04/22 para as releases 12.1.27 e 12.1.33.

**Obs. Somente a partir da nova release 12.1.2210, quando não haverá mais a chamada da rotina mata030 no menu de faturamento e sim a rotina crma980, que não será mais necessário a ativação do parâmetro mv\_mvcsa1.**
