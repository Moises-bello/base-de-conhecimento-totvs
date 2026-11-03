---
article_id: 360019918332
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6059476a0ba92cb408debb5222c1006195c12a7321929b4a573c7cd0d13e27cc
fetched_at: '2026-06-28T22:38:41.111247+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como liberar
  itens do pedido de venda conforme o estoque
type: support-article
updated_at: '2026-03-09T18:54:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019918332-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-liberar-itens-do-pedido-de-venda-conforme-o-estoque
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16372929507095) Tempo aproximado para leitura: 00:02:00 min****

**Dúvida**

Como liberar itens do pedido de venda conforme o estoque?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - todas as versões.  
  
**Solução**

Para liberação de itens do pedido, gere 1 registro liberado pela quantidade disponível em estoque e gere outro bloqueado.

Na inclusão do Pedido de Venda, o campo **Tp Liberação** do cabeçalho, deve ser igual a **1=Libera por item,** e o primeiro parâmetro desta rotina acessado via **F12** deve estar com: **Sugere Qtd Liberada =** **Sim;**

Na liberação de pedidos com saldos parciais é necessário acertar os seguintes parâmetros:

* **MV\_GERABLQ**para**S;**
* **MV\_GRVBLQ2**para**T.**

E os parâmetros da rotina **Liberação de Pedidos** acessados via **F12**, devem estar com os respectivos conteúdos:

* Transfere Armazém = **Não;**
* Libera só com estoque = **Sim**;
* Sugere Qtd Liberada = **Sim**.

**MV\_AVALEST** = 3 - Pode definir que todo o pedido bloqueie por estoque independente de ter saldo.

**Observação**: Caso a configuração desta documentação esteja ativa, ao inserir no pedido uma quantidade, no campo **"Quantidade" (C6\_QTDVEN)**, **superior ao saldo** do produto no estoque, o pedido **não será** **liberado** **automaticamente**.

Com relação ao uso de **lote econômico** **(B1\_LE),** esse conceito não é utilizado para liberação do pedido de venda (**Mata440**), a informação deste campo indica  a quantidade ideal para compra e produção do produto.  Com base na informação do lote econômico são calculadas possíveis quebras de quantidade nos processos de ***geração de solicitações de compra (Mata110)*** ou **ordens de produção (Mata650)**.

Veja nosso Webinar: **[Análise e Bloqueio de Estoque no Faturamento (SIGAFAT)](https://youtu.be/6XfctVxULuY)**
