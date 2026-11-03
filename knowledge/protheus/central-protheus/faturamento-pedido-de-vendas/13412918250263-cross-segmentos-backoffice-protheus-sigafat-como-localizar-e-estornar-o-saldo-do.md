---
article_id: 13412918250263
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ae2c55db3b43daebf92ed15b9d38c5d6f1396bf705d5b5309d6087884286b43a
fetched_at: '2026-06-28T22:38:39.724734+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como localizar e estornar
  o saldo do campo "Qtd. Reserva" (B2_RESERVA) de um produto
type: support-article
updated_at: '2026-04-01T15:01:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13412918250263-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-do-campo-Qtd-Reserva-B2-RESERVA-de-um-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21220625695383) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**

Como localizar e retirar o saldo do campo "Qtd. Reserva" (B2\_RESERVA) de um produto?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**  
Quando um produto possui saldo no campo **"Qtd. Reserva" (B2\_RESERVA)**, este saldo está reservado ao processo, não sendo possível usar em qualquer movimentação. Muitas vezes é preciso localizar esse saldo para remover a liberação, para usa-lo em outros processos.

**Solução**

No processo de Faturamento, há algumas maneiras de alimentar a **"Qtd. Reserva" (B2\_RESERVA)** de um produto, para estorno da **"Qtd. Reserva" (B2\_RESERVA)**, existem alguns processos dependendo do tipo de Reserva que se pretende estornar, cheque os 3 tópicos a seguir para liberar seu campo **"Qtd. Reserva" (B2\_RESERVA)**:

1. **Liberando o produto** em um Pedido de Vendas, após liberação de estoque, assim alimentando a tabela de **Pedidos Liberados (SC9)**;  
   [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) de um Pedido Liberado (SC9)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21253646074519-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-de-um-Pedido-Liberado-SC9);
2. **Realizando inserção de uma reserva** na rotina "**Controle de Reservas" (MATA430)**, automaticamente ou manualmente, assim alimentando a tabela de **Reservas para Faturamento (SC0)**  
   [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) das "Reservas para Faturamento" (SC0)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254220747799-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-das-Reservas-para-Faturamento-SC0)
3. Reserva vinculada à um Orçamento, **do módulo SIGALOJA**, não finalizado, assim alimentando a tabela de **"Itens do Orçamento" (SL2)**  
   [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) dos "Itens do Orçamento" (SL2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254628360215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-dos-Itens-do-Or%C3%A7amento-SL2).
4. Caso, mesmo após a validação e estorno de todas as reservas vinculadas ao produto, ainda exista quantidade indevida no campo B2\_RESERVA, pode haver resíduo ou inconsistência de saldo gerado por movimentações anteriores.

   Nessa situação, para garantir a correção do saldo reservado e a integridade das informações de estoque, recomenda-se a execução da rotina Refaz Empenhos (MATA215) e Refaz Saldo (MATA300), conforme orientações do material abaixo:

* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es)
* [MATA215 - Refaz Acumulados](https://tdn.totvs.com/display/PROT/MATA215+-+Refaz+Acumulados)

**Saiba mais:**

* [Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO)
