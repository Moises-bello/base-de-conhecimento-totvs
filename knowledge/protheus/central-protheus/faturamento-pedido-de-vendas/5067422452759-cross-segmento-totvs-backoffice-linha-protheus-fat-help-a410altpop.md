---
article_id: 5067422452759
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3e1d61be07135c93d5dfd2ce5a20cd66a7edd0ee15a0acbcb1b7f2460f52fecf
fetched_at: '2026-06-28T22:38:38.366392+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Help A410ALTPOP
type: support-article
updated_at: '2022-05-11T17:14:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5067422452759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Help-A410ALTPOP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao alterar o pedido de vendas que possui uma Ordem de Produção em aberto, esta sendo apresentado a mensagem de help **A410ALTPOP**.**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Causa**O pedido de vendas possui ordem de produção vinculada e o parâmetro **MV\_ALTPVOP** deve ser configurado para liberar a alteração do pedido.

**Solução** **1.** Verifique qual o conteúdo do parâmetro **MV\_ALTPVOP** (*O parâmetro indica se podem ser alterados Pedidos de Venda que geraram Ordem de Produção.*)

* Igual a S - Permiti alterar o pedido de venda com ordem de produção em aberto e vinculado;
* Igual a N - Não ira permitir alterar o pedido de venda com ordem de produção em aberto e vinculado.

Deixe o parâmetro igual a **S** para conseguir alterar o pedido de vendas com OP vinculada.  
  
**2.** Verifique se o parâmetro **MV\_ALTPVOP**  esta compartilhado (*quando o campo não tem filial preenchido*).  
Se estiver preenchido com alguma filial no campo, realizar o teste em homologação com o campo em branco.![parametro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5066849922327/parametro.png)
