---
article_id: 20123798485399
category: Financeiro
content_hash: 13865e740f477462ee2113f4888d81d9d6399e26933e9613b0318674c9ca1b4f
fetched_at: '2026-06-28T22:38:01.111783+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - BackOffice Linha Protheus - SIGAFIN - MATA090 - Dúvida sobre
  o tipo da Moeda "PX"
type: support-article
updated_at: '2023-12-27T14:18:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20123798485399-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-MATA090-D%C3%BAvida-sobre-o-tipo-da-Moeda-PX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20123862938647) Tempo aproximado para leitura: **03:00 min** **Dúvida**Ao gerar o título o campo E5\_MOEDA vem com o "PX" preenchido?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINANCEIRO - Todas as versões  
  
**Solução**E5\_TIPODOC -> BA: Baixa de Título que não altera o saldo bancário. A linha BA é para informar que houve a baixa (sem a movimentação bancária).

VL: Baixa de Título que altera o saldo bancário. A linha VL é para informar a movimentação bancária.  
   
O valor E5\_MOEDA PX é o PIX.
