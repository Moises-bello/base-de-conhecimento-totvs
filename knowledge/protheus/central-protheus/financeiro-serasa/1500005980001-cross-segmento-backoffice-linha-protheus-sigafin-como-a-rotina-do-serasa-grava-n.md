---
article_id: 1500005980001
category: Financeiro - Serasa
content_hash: 3a99a664ab903f1b10cd35fe78a82c4cb912699d55d5c11f187eab2a5b5422a1
fetched_at: '2026-06-28T22:37:28.229275+00:00'
product: protheus
section_id: 35058289522071
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como a rotina do Serasa
  grava na tabela FWB a ocorrência 07- Negociado
type: support-article
updated_at: '2026-01-30T12:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005980001-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-a-rotina-do-Serasa-grava-na-tabela-FWB-a-ocorr%C3%AAncia-07-Negociado
---

**Dúvida**  
Como a rotina do SERASA grava na tabela FWB a ocorrência 07- Negociado no campo FWA\_STATUS?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12  
  
**Solução**  
Para transformar o campo **FWA\_STATUS** = 7 - Negociado, basta que o mesmo faça a alteração do vencimento do título quando o campo estiver com o conteúdo **FWA\_STATUS** = 3, ou seja, quando o título está no Serasa.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007935422)

Após Alterar o **Vencto** vai apresentar a mensagem

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007935602)

Clicar no **SIM** e veja

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007936042)
