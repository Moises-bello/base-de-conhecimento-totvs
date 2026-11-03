---
article_id: 360047905693
category: Comércio Exterior - Easy Siscoserv - Importação
content_hash: f142473104efc97645d08f2ef47ca3c5862a912b6e887538465442c2d86d276f
fetched_at: '2026-06-28T22:39:39.590645+00:00'
product: protheus
section_id: 1500001538321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Desconto (EEQ_DESCON)
  informando na liquidação
type: support-article
updated_at: '2022-06-21T20:44:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047905693-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Desconto-EEQ-DESCON-informando-na-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao informar o campo Desconto(EEQ\_DESCON) é considerado no registro do Siscoserv?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 12.  
  
**Solução**Ao informar o desconto (EEQ\_DESCON) na liquidação do título este será gravado na posição do título (SE5), conforme abaixo:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068905254/mceclip0.png)  
  
Para realizar a integração ao Siscoserv  não será considerado o valor de desconto, este pode ser verificado na rotina Atualizações\Importação\RAS (ESSRA400), posicione no processo e selecione no Pagamento (RP) a parcela a ser visualizada:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068905734/mceclip1.png)

Verifique que o valor câmbio será total, ou seja, não irá considerar o valor de desconto:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068905834/mceclip2.png)
