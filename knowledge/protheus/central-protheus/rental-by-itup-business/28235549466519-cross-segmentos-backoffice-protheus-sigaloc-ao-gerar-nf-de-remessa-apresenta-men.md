---
article_id: 28235549466519
category: Rental by ItUp Business
content_hash: 6456f19a15d6df54932f4c76688108326911a4dd61514e1e0aca8d97d2b4b504
fetched_at: '2026-06-28T22:36:20.497905+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Ao gerar NF de Remessa apresenta
  mensagem A410NATUSO
type: support-article
updated_at: '2026-04-09T12:50:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28235549466519-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Ao-gerar-NF-de-Remessa-apresenta-mensagem-A410NATUSO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28235585928599) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao gerar NF de Remessa apresenta mensagem A410NATUSO.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - P12.1.2310.  
  
**Solução**  
Para gerar a NF de Remessa no Rental, é premissa utilizar configurações nos parâmetros:

* MV\_1DUPNAT confiugure SC5->C5\_NATUREZ;
* MV\_LOCX066 informe o código do Cadastro da Natureza para os pedidos de remessa do Rental.

Este comportamento é um conceito do módulo SIGALOC, onde utiliza a natureza informada no parâmetro MV\_LOCX066 e coloca no campo C5\_NATUREZ pra gerar o pedido.
