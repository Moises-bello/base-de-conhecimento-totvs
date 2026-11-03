---
article_id: 21254628360215
category: Faturamento - Integrações
content_hash: 503d652ecbf919ed8401546877d2cf3250f7fd6acc58e4c5dfb86c41014b47ba
fetched_at: '2026-06-28T22:38:26.539530+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como localizar
  e estornar o saldo da "Qtd. Reserva" (B2_RESERVA) dos "Itens do Orçamento" (SL2)
type: support-article
updated_at: '2025-03-21T18:25:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254628360215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-dos-Itens-do-Or%C3%A7amento-SL2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21254568371351) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Como localizar e retirar o saldo do campo "Qtd. Reserva" (B2\_RESERVA) de um produto?  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**

Quando um produto possui saldo no campo **"Qtd. Reserva" (B2\_RESERVA)**, este saldo está reservado ao processo, não sendo possível usar em qualquer movimentação. Muitas vezes é preciso localizar esse saldo para remover a liberação, para usa-lo em outros processos.

No processo de Faturamento, há algumas maneiras de alimentar a **"Qtd. Reserva" (B2\_RESERVA)** de um produto:

1. **Liberando o produto** em um Pedido de Vendas, após liberação de estoque, assim alimentando a tabela de **Pedidos Liberados (SC9)**;
2. **Realizando inserção de uma reserva** na rotina "**Controle de Reservas (MATA430)**", automaticamente ou manualmente, assim alimentando a tabela de **Reservas para Faturamento (SC0)**;
3. Reserva vinculada à um Orçamento, **do módulo SIGALOJA**, não finalizado, assim alimentando a tabela de **"Itens do Orçamento" (SL2)**.

**Observação: Para saber como Localizar/Estornar as reservas das tabelas de** **Pedidos Liberados (SC9)**

**e** "**Reservas para Faturamento" (SC0)****, consulte o "Saiba mais" no final da documentação.**

**Solução**

Para estorno da **"Qtd. Reserva" (B2\_RESERVA)**, é necessário realizar os processos abaixo.

**Verificar/Estornar reservas na tabela de "Itens do Orçamento" (SL2):**

A reserva que alimenta a **"Qtd. Reserva" (B2\_RESERVA)** está vinculada à um **Orçamento não finalizado**, o sistema faz a seguinte verificação para manter o saldo reservado:

* Campo **"Numero PDV" (L2\_PDV)** está vazio;
* Campo **"Num.Reserva" (L2\_RESERVA)** está preenchido;
* Campo **"Orc.Reserva" (L2\_ORCRES)** está vazio;
* Campo **"Num. Pedido" (L2\_PEDRES)** está vazio;
* Campo **"Status" (L2\_VENDIDO)** está diferente de "S".

Caso o item do Orçamento esteja com o preenchimento indicado acima, o sistema reserva a quantidade do produto no campo **"Qtd. Reserva" (B2\_RESERVA)**.

* A reserva que está vinculada à um orçamento não finalizado, pode ser excluída automaticamente dependendo das configurações do parâmetro "**MV\_DTLIMIT**" e do campo **"Dias p/Res." (LJ\_DIASRES)**;
* Também pode ser realizado via rotina "**Depuração de Reservas (LOJA540)**".

**Observação:** Dúvidas sobre o processo no módulo SIGALOJA contate o nosso Suporte direcionando à equipe **"Protheus Automação Comercial"**.

**Saiba mais:**

* [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) de um Pedido Liberado (SC9)](https://totvssuporte.zendesk.com/knowledge/editor/01HP7TMM84EM0SA3BX10WPXCZS/pt-br?brand_id=1509248&template_id=115015907188)
* [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) das "Reservas para Faturamento" (SC0)](Como%20localizar%20e%20estornar%20o%20saldo%20da%20%22Qtd.%20Reserva%22%20(B2_RESERVA)%20das%20%22Reservas%20para%20Faturamento%22%20(SC0))
