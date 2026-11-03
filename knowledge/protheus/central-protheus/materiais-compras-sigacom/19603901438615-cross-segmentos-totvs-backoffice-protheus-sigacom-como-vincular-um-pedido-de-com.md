---
article_id: 19603901438615
category: Materiais - Compras (SIGACOM)
content_hash: b68a48ed975c481a705e3dc1c30a27db38d6e846027ff553f6b4dc0a795d84b9
fetched_at: '2026-06-28T22:41:16.110922+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como vincular um pedido
  de compras de outra loja do fornecedor?
type: support-article
updated_at: '2024-07-25T12:22:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19603901438615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-vincular-um-pedido-de-compras-de-outra-loja-do-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19603869589655) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quando tenho um pré-documento de entrada e vou classificá-lo, ao tentar atrelar um pedido de compra, o sistema permite somente vincular pedidos do fornecedor com a mesma filial (loja) que digitada no cabeçalho da pré-nota.

**Ambiente**Protheus – Compras – A partir da versão 12.1.27  
  
**Solução**No F12 da rotina de pré-nota ( MATA140 ) e da rotina do documento de entrada ( MATA103 ) temos uma pergunta que permite ao sistema buscar os pedidos somente pelo código do fornecedor, sem verificar a loja, seguem prints abaixo  :  
   
MATA140  
![](https://totvssuporte.zendesk.com/attachments/token/gq43PRBPgLubVjtOZiaJ5FCZA/?name=image.png)  
   
MATA103  
![](https://totvssuporte.zendesk.com/attachments/token/VqtCnQCefWoXPXhuKaQ22sdTe/?name=image.png)  
   
Dessa forma, quando o conteúdo dos perguntes  .MTA14002. ou .MTA10307. estiverem com o conteúdo:

1. "Fornecedor + Loja" será possível vincular pedidos de compras apenas da mesma loja do fornecedor

2. "Fornecedor" será possível vincular pedidos de compras de qualquer loja do fornecedor em questão.

**Saiba mais em :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
