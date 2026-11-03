---
article_id: 360053754213
category: Faturamento - Cadastros
content_hash: 667f5cbd0e5477519cd7201d499da6cbb22937c7d6754fca04a634778cbff8d2
fetched_at: '2026-06-28T22:38:35.412334+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Alteração no cadastro cliente
  pela analise crédito manual
type: support-article
updated_at: '2025-11-05T11:53:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053754213-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Altera%C3%A7%C3%A3o-no-cadastro-cliente-pela-analise-cr%C3%A9dito-manual
---

**Dúvida**É possível quando o usuário clicar no botão manual da análise de crédito (**MATA450**), opção cliente, o sistema habilite o campo **"Lim Credito**" para alteração?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458334)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088597093)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**

Neste momento da avaliação de crédito (**MATA450**), o cadastro de cliente (**CRMA980**), Posição de cliente (**FINC010**), Pedido (**MATA410**) e Estoque (**saldo da SB2**) é apenas para consulta:

* **Posição** - *Esta opção possibilita a consulta à **[Posição de Clientes](https://tdn.totvs.com/x/mDwXFg)**.*
* ***Clientes -*** *Possibilita a consulta aos dados cadastrais do cliente.*
* **Pedido** - *Esta opção apresenta o pedido de venda do cliente.*
* **Estoque** - *Apresenta a posição em estoque do produto.*

Não há configuração para tratá-lo como modo de alteração, mesmo que seja de alguns campos e nem ponto de entrada para essa questão.

**Saiba mais:**   
[**Liberação de Crédito Manual (MATA450 - SIGAFAT)**](https://tdn.totvs.com/x/cqDaFQ)  
[**Pontos de Entrada da rotina MATA450**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051175653-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-da-rotina-MATA450)
