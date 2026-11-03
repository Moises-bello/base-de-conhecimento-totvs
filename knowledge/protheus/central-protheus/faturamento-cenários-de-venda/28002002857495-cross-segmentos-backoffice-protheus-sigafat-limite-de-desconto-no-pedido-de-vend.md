---
article_id: 28002002857495
category: Faturamento - Cenários de Venda
content_hash: 4ccc7445734cb57936913ff408146a79b6f9b0d46325e2537de90b76e154328f
fetched_at: '2026-06-28T22:38:34.026167+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Limite de desconto no pedido
  de venda (MATA410)
type: support-article
updated_at: '2024-11-22T19:32:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28002002857495-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Limite-de-desconto-no-pedido-de-venda-MATA410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28002017182615) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como estipular um limite de desconto no pedido de venda (MATA410)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**1 - Entrar na rotina "Regra de Negócios (FATA100)"

2 - Preencher a aba inferior "Descontos" no campo "% Desc.ate (ACN\_DESCON)":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28002002829975)

3 - Ir no "Pedidos de venda (MATA410)" e informar algum desconto, que faça o percentual "% Desconto (C6\_DESCONT)" ultrapassar o valor informado no campo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28002017185175)

Resultado ao ultrapassar (bloqueado por regra de negócio, legenda azul):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28002017185815)

Cheque como proceder no Saiba mais dessa documentação.

**Saiba mais:**  
**[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT )- Qual parâmetro habilitar para mostrar o motivo do bloqueio de regra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028562252-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Qual-par%C3%A2metro-habilitar-para-mostrar-o-motivo-do-bloqueio-de-regra)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - O que é Bloqueio e Liberação de Regra de Negócios e Verba de Vendas no Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028995872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-O-que-%C3%A9-Bloqueio-e-Libera%C3%A7%C3%A3o-de-Regra-de-Neg%C3%B3cios-e-Verba-de-Vendas-no-Pedido-de-Vendas)**
