---
article_id: 16079891330327
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 653373891e485ac847e8e1975d462a3ff37665617a34cf99c9e4dbeaa8e790d6
fetched_at: '2026-06-28T22:38:38.663457+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- (RA) - Help A410CONDNADT
  na Inclusão do Pedido de Venda
type: support-article
updated_at: '2025-01-10T20:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16079891330327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-RA-Help-A410CONDNADT-na-Inclus%C3%A3o-do-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16079878487575) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao tentar salvar um pedido de venda apresenta a mensagem;

**Help: A410CONDNADT**

**Problema: Condição de Pagamento utilizada não é de adiantamento**

**Solução: Desmarque os adiantamentos vinculados**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.17;

**Incidente**

O Help: **A410CONDNADT** é apresentado, quando tenta salvar o Pedido de Venda que esta vinculado a um **Adiantamento Antecipado**, mais foi alterada a Condição de Pagamento, para uma que não faz a validação de **RA**.

**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

**Se o Pedido de Venda, não for usar o Adiantamento Antecipado.**

1. Acessar o Pedido de Venda **"Condição de Pagamento - C5\_CONDPAG"**, e selecionar uma condição de pagamento que controle adiantamento;

2. Ir em **Outras Ações >> Adiantam.**, selecionar **"Relacionar Adiantamentos"** dar um duplo clique na título, para que seja desvinculado o RA do Pedido de Venda, com o isso o sistema permite salvar sem a condição de pagamento com RA.

**Se o Pedido de Venda for usar Adiantamento Antecipado.**

1. Acessar o Pedido de Venda **"Condição de Pagamento - C5\_CONDPAG"**, e selecionar uma condição de pagamento que controle adiantamento

2. Ao selecionar a condição de pagamento com controle de Adiantamento, o sistema permite salvar o Pedido de Venda, sem apresentar o help.

![RA](https://centraldeatendimento.totvs.com/hc/article_attachments/16079897784087)

Saiba Mais

* [Encerramento do PV faturado parcialmente com Adiantamento](https://tdn.totvs.com/x/SEcxIQ)
* [Como vincular ou Desvincular RA no Pedido de Vendas pela Rotina MATA410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-vincular-ou-Desvincular-RA-no-Pedido-de-Vendas-pela-Rotina-MATA410)
* [Webinar | MP - SIGAFAT - Adiantamento (RA) em Pedidos de Venda](https://youtu.be/zXZxJ8DknQM?si=K4bsuwhWdhpTp3_w)
* [Adiantamento no Pedido de Vendas](https://tdn.totvs.com/x/-pgcKw)
