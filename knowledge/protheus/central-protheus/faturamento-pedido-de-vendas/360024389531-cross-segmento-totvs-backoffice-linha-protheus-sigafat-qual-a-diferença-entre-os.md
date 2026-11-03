---
article_id: 360024389531
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2c167a57072867c075d2b3995aef461863fda81d1950774766a5c96ddd03f30c
fetched_at: '2026-06-28T22:38:38.610901+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Qual a diferença
  entre os campos "Bloqueio (C6_BLOQUEI)" e "Status Blq (C6_BLQ)" no pedido de venda
  (MATA410)
type: support-article
updated_at: '2023-01-06T16:47:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024389531-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-a-diferen%C3%A7a-entre-os-campos-Bloqueio-C6-BLOQUEI-e-Status-Blq-C6-BLQ-no-pedido-de-venda-MATA410
---

**Dúvida**

Qual a diferença entre os campos "**Bloqueio**" (C6\_BLOQUEI) e "Status Blq" (C6\_BLQ) no pedido de venda (MATA410)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O campo "**Bloqueio" (C6\_BLOQUEI)** indica bloqueio do pedido de venda (**MATA410**) por Verba de Vendas ou Regra de Negócios, podendo receber os conteúdos:

 C6\_BLOQUEI = 1 - Regra de Negócios (**FATA100**)

 C6\_BLOQUEI = 2 - Verba de Vendas (**FATA190**)

**Obs.: A liberação desses bloqueios podem ser efetuadas via liberação manual na Rotina Liberação de Regras (FATA210).**

Já o campo "**Status Blq" (C6\_BLQ)** é mais utilizado para tratamento de eliminação de resíduo do pedido (**MATA500**), mas o campo pode receber os seguintes conteúdos:

R - Resíduo

S - Pedido Bloqueado

N - Não Bloqueado

**Obs2: Uma vez eliminado o resíduo, caso seja necessário, o conteúdo do campo "Status Blq" (C6\_BLQ) pode ser alterado manualmente para o status "S", mantendo o pedido bloqueado para uso ou para "N", liberando o seu uso, valide apenas se o parâmetro MV\_RSDOFAT está habilitado para efetuar alteração do pedido, após a eliminação do resíduo.**
