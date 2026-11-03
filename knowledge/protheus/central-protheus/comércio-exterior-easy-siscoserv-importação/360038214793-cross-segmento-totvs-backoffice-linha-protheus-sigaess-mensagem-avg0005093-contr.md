---
article_id: 360038214793
category: Comércio Exterior - Easy Siscoserv - Importação
content_hash: fec9c9c2490d3138a330dbd457ca38c6a8469ed901fe150541ed2fba57c30d8a
fetched_at: '2026-06-28T22:39:39.607485+00:00'
product: protheus
section_id: 1500001538321
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Mensagem - AVG0005093:
  Contratação Não Efetuada. Valor da Taxa Deve Ser Preenchido !'
type: support-article
updated_at: '2022-06-21T19:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038214793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Mensagem-AVG0005093-Contrata%C3%A7%C3%A3o-N%C3%A3o-Efetuada-Valor-da-Taxa-Deve-Ser-Preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como corrigir a Mensagem - AVG0005093: Contratação Não Efetuada. Valor da Taxa Deve Ser Preenchido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 12.1.17  
  
**Solução**Ao apresentar a mensagem, deve ser preenchido o campo Taxa Cambio (EEQ\_TX), com a taxa de liquidação do título.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050407093/mceclip0.png)

Campos que devem ser informados para liquidação da parcela:  
**Dt.Cred.Ext (EEQ\_DTCE) , Sol.Cambio  (EEQ\_SOL), Dt.Negociac. (EEQ\_DTNEGO), Dt.Liq.Cont (EEQ\_PGT), Nr.Operacao (EEQ\_NROP), Taxa Cambio (EEQ\_TX).**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050407653/mceclip2.png)

Na aba Contrato de Câmbio informar banco para baixa:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049517014/mceclip1.png)
