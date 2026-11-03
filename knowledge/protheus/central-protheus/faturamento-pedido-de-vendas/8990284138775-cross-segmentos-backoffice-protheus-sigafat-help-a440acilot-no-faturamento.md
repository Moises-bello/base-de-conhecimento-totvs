---
article_id: 8990284138775
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 23e725f0f801ed6d454b69b8c77fa1f25ee9e3b5fb7c2856c532fa8cd918e082
fetched_at: '2026-06-28T22:38:39.835159+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A440ACILOT no Faturamento
type: support-article
updated_at: '2024-07-26T12:07:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8990284138775-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A440ACILOT-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25160293930903) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**

Help A440ACILOT.  
  
**Causa**

Inserir  uma certa quantidade no campo ''Quantidade" '(C6\_QTDVEN) com o campo "Quantidade Liberada" (C6\_QTDLIB) preenchido com uma quantidade liberada maior da que o lote possui.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Soluções**

Existem algumas opções para a tratativa:

* Retirar o valor da "Quantidade Liberada" (C6\_QTDLIB), ajustando o campo C6\_QTDVEN e inserir uma quantidade que haja saldo no lote novamente nos campos ''Quantidade" (C6\_QTDVEN) e "Quantidade Liberada" (C6\_QTDLIB)
* Inserir mais saldo no lote para que este comporte a quantidade.  
  Dúvidas nessa opção, contate a Equipe Estoque/Custos/ACD.
* Verificar se  pedido de venda (C5\_EMISSÃO)  é mais recente do que a criação do lote no campo B8\_DATA;
* Liberar o lote bloqueado/vencido na rotina MATA275 - Bloqueio de Lote caso identifique que seja necessário;
* Verificar se outro pedido de venda já foi liberado usando o saldo do mesmo lote na tabela de Pedidos Liberados SC9;

   
Exemplos para a ocorrência do **HELP A440ACILOT**

* B8\_LOTECTL = LOTE00001
* B8\_QTDORI = 5
* B8\_SALDO = 4
* C6\_LOTECTL = LOTE00001
* C6\_QTDLIB = 6
* C6\_QTDVEN = 1 (Pode botar qualquer valor)

**OBS:** O HELP é gerado, pois ao inserir qualquer valor no campo ''Quantidade'' (C6\_QTDVEN) será validado o campo ''Qtd. Liberada'' (C6\_QTDLIB) e identificrá que é maior que o (B8\_SALDO).  
  
Exemplo que não apresenta a mensagem A440ACILOT:

* B8\_LOTECTL = LOTE00002
* B8\_QTDORI = 7
* B8\_SALDO = 7
* C6\_LOTECTL = LOTE00002
* C6\_QTDLIB = 2
* C6\_QTDVEN = 2

**OBS:** O HELP ocorre pois ao inserir qualquer valor no campo ''Quantidade'' (C6\_QTDVEN) validará que o campo ''Qtd. Liberada'' (C6\_QTDLIB) é menor que B8\_SALDO, que é a quantidade disponível no lote.  
  
**Saiba mais:**

[Cross Segmentos TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Mensagem de lote vencido no faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014095387)

[MP - SIGAEST - MATR425 - Posição de Estoque por Lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063392673-MP-SIGAEST-MATR425-Posi%C3%A7%C3%A3o-de-Estoque-por-Lote)
