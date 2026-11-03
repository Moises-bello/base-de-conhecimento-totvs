---
article_id: 29586316481559
category: Materiais - Compras (SIGACOM)
content_hash: b2d0b37fa3b599184d8c69fc2490b82ae0a4e459b2afd0e61b97d703e9b0bb70
fetched_at: '2026-06-28T22:41:11.859806+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Ponto de Pedido - Solicitação de Compras
  Repetida
type: support-article
updated_at: '2025-01-29T11:37:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29586316481559-Cross-Segmentos-Backoffice-Protheus-Ponto-de-Pedido-Solicita%C3%A7%C3%A3o-de-Compras-Repetida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29586316466583) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Quando já existe uma Solicitação de Compras e a rotina de ponto de pedido é executada, ela gera a solicitação novamente toda vez que for rodada.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Todas as Versões

**Solução**

Toda vez que o Sistema detectar a falta de um material, somando saldo em estoque, pedidos e solicitações de compras em aberto e esta for menor que o Ponto de Pedido definido em seu cadastro de Produto é gerado uma **Solicitação de Compras**.

O mesmo acontece para **Geração de Ordens de Produção** quando falamos de lote econômico e lote mínimo, também definidos em cadastro de produtos, é gerada uma ordem de produção.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29586316467351)

**Ponto de Pedido**: É neste campo que informamos a quantidade Mínima para o estoque, que uma vez atingida, pode iniciar o processo de compras a partir da Geração de Solicitação de Compras por ponto de pedido.

**Lote Econômico**: Esta preenchido com a quantidade padrão a ser comprada

**Lote Mínimo**: Esta preenchido com a quantidade padrão inferior ao lote econômico a ser considerada para Produção.

***Saiba Mais:***

[Solicitações de compras baseado no ponto de pedido](https://tdn.totvs.com/pages/releaseview.action?pageId=556376507)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
