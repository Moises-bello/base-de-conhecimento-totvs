---
article_id: 11336665011863
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f2b39dabff0948879fa852eaab8812876d0d49473215e3624c34bf7f17b61069
fetched_at: '2026-06-28T22:38:42.621502+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Depuração manual do controle de reservas
type: support-article
updated_at: '2022-12-30T20:19:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11336665011863-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Depura%C3%A7%C3%A3o-manual-do-controle-de-reservas
---

**Dúvida**Qual o comportamento e configuração da funcionalidade de depuração manual de reservas no Faturamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.  
  
**Solução**

Essa opção tem a função de excluir as reservas com prazo de validade vencido. Apenas as reservas cujo saldo esteja igual à quantidade original, ou seja, não tenham sido utilizadas, poderão ser depuradas.

Caso a reserva esteja vencida, mas vinculada a um pedido de venda, não é possível depurar a reserva.

**Caminho:** Atualizações > Pedidos > Controle Reservas > Outras Ações > **Depurar**

Parâmetros utilizados na opção depurar (Manual):

* MV\_PZRESER (Prazo padrão de validade das reservas (em dias), utilizado no campo **C0\_VALIDA**)

**Saiba mais:**

[FAT0131 Rotina Controle de Reservas (MATA430)](https://tdn.totvs.com/x/P5AjDw)
