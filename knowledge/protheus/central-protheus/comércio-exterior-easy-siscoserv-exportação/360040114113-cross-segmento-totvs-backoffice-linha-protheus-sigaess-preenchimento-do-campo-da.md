---
article_id: 360040114113
category: Comércio Exterior - Easy Siscoserv - Exportação
content_hash: 78ddd8901f89b9ec8ff2489cbf4ab4fe57f49f882be340f0bc4e537d2242635e
fetched_at: '2026-06-28T22:39:38.921404+00:00'
product: protheus
section_id: 1500001549402
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Preenchimento
  do campo Data de encerramento (EJY_DTENC)
type: support-article
updated_at: '2022-06-21T20:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040114113-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Preenchimento-do-campo-Data-de-encerramento-EJY-DTENC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como não preencher automaticamente o campo Data de encerramento (EJY\_DTENC) do RAS\RVS ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 11.80  
  
**Solução**Criado o parâmetro MV\_ESS0032, para o controle do campo EJY\_DTENC, no registro de pagamento, para que a data de encerramento não seja preenchido após a finalização do processo.  
Caso o parâmetro tiver com o valor .F., não será preenchido automaticamente a data do encerramento, caso esteja como .T. o sistema agirá normalmente de acordo com a regra.  
  
**Saiba mais**  
[Parâmetro para definir se preenche a data de encerramento na integração com o siscoserv](https://tdn.totvs.com/pages/releaseview.action?pageId=286516551)
