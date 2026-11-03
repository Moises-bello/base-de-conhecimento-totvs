---
article_id: 16581230919959
category: Comércio Exterior - Easy Import Control - Entreposto
content_hash: ab572be653a750a5447cd84d850fa95edd299ee538b2ebe691449098d64b21bc
fetched_at: '2026-06-28T22:39:46.045516+00:00'
product: protheus
section_id: 1500001549622
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEIC - Help AVG0000107
type: support-article
updated_at: '2023-08-08T11:46:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16581230919959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Help-AVG0000107
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16581236466839)Tempo aproximado para leitura: **02:00 min** **Dúvida**Como corrigir o Help: AVG0000107 "Este pedido não pode ser zerado, pois não é um pedido de nacionalização"?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16581016929815)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 12.1.33.

**Solução**Para que a mensagem não seja apresentada ao zerar o saldo, deve-se verificar se o pedido se trata de uma nacionalização, há uma validação de gravação no campo "**W2\_HAWB\_DA"**, caso não seja um pedido de nacionalização o campo estará vazio e será apresentado a mensagem. Help: ("AVG0000107"  "Este pedido não pode ser zerado, pois não é um pedido de nacionalização".
