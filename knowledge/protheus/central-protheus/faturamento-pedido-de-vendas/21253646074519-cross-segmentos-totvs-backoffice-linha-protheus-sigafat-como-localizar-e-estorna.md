---
article_id: 21253646074519
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 72e768b62df2fccd50de5c043562d4c41d9a8d5e0382af5f09b0d34a5d4aa58a
fetched_at: '2026-06-28T22:38:42.655502+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como localizar
  e estornar o saldo da "Qtd. Reserva" (B2_RESERVA) de um Pedido Liberado (SC9)
type: support-article
updated_at: '2024-02-09T21:34:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21253646074519-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-de-um-Pedido-Liberado-SC9
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21253617410967) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Como localizar e retirar o saldo do campo "Qtd. Reserva" (B2\_RESERVA) de um produto?  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**

Quando um produto possui saldo no campo **"Qtd. Reserva" (B2\_RESERVA)**, este saldo está reservado ao processo, não sendo possível usar em qualquer movimentação. Muitas vezes é preciso localizar esse saldo para remover a liberação, para usa-lo em outros processos.

No processo de Faturamento, há algumas maneiras de alimentar a **"Qtd. Reserva" (B2\_RESERVA)** de um produto:

1. **Liberando o produto** em um Pedido de Vendas, após liberação de estoque, assim alimentando a tabela de **Pedidos Liberados (SC9)**;
2. **Realizando inserção de uma reserva** na rotina "**Controle de Reservas (MATA430)**", automaticamente ou manualmente, assim alimentando a tabela de **Reservas para Faturamento (SC0)**;
3. Reserva vinculada à um Orçamento, **do módulo SIGALOJA**, não finalizado, assim alimentando a tabela de **"Itens do Orçamento" (SL2)**.

**Observação: Para saber como Localizar/Estornar as reservas das tabelas de**"**Controle de Reservas (MATA430)**" **e** **"Itens do Orçamento" (SL2), consulte o "Saiba mais" no final da documentação.**

**Solução**

Para estorno da **"Qtd. Reserva" (B2\_RESERVA)**, é necessário realizar os processos abaixo.

1. **Verificar/Estornar reservas na tabela de Pedidos Liberados (SC9):**

Para localizar essas reservas:

* Acesse o relatório **"Pedidos a Faturar" (MATR700)**;
* Acesse a opção "**Outras Ações**" e depois a opção **"Parâmetros"**;
* Deixe os parâmetros com a configuração mais aberta e com um intervalo de procura "De/Até" alto, como por exemplo abaixo;
* No parâmetro **"Produto De/Até"** coloque o produto específico que quer liberar o saldo:

![01-Reservas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21253617414423)

* Aplicar e gerar o relatório;
* Localizar os pedidos que possuem conteúdo na cédula "Qtd.Liberada":

![2-Reserva.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21253617415959)

Caso retorne algum registro no filtro com conteúdo na cédula "Qtd.Liberada" (como na imagem acima), considere Estornar a Liberação do Pedido de Vendas. Se necessitar de ajuda para estornar, veja um vídeo a respeito do assunto:

* [How To | MP - SIGAFAT - Qtd. Pedido de Vendas e Qtd. Reservada](https://youtu.be/O7fAb_aznxE?si=Rbd1ufQ1vtXXGXPp)
