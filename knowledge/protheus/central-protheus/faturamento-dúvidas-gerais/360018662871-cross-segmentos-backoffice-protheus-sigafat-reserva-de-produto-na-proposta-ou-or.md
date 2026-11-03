---
article_id: 360018662871
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: bd43e59677122fa89a000c8df72fb2561a697cd2f621f34f583add524e27a8a2
fetched_at: '2026-06-28T22:38:33.064999+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Reserva de produto na Proposta
  ou Orçamento do Faturamento
type: support-article
updated_at: '2025-02-11T10:46:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018662871-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Reserva-de-produto-na-Proposta-ou-Or%C3%A7amento-do-Faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29899765953559) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**

Como reservar os produtos orçados ao finalizar o orçamento Faturamento?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

No Orçamento de Vendas **(MATA415)** ou Contrato de Parceria **(FATA400)**, da mesma forma que ocorre no orçamento Call Center **(TMKA273)**, não efetua-se reserva de produto.

A reserva somente é efetuada a partir do Pedido de venda, visto que as etapas anteriores, conceitualmente, não há a certeza de que o mesmo será efetivado como venda.

Uma alternativa é gerar a Reserva do Produto manualmente através da rotina Controle de Reservas (**MATA430)** e depois, através do campo **C6\_RESERVA**, vincular a reserva ao Pedido para que esta seja baixada no sistema.

Detalhes em:

[**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Utilização da Rotina Controle de Reservas (MATA430)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019758251-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Utiliza%C3%A7%C3%A3o-da-Rotina-Controle-de-Reservas-MATA430)

**Observação**: Caso o campo C6\_RESERVA não aparecer no browser, acesse o dicionário de dados no Configurador, edite a tabela SC6 e marque o campo como usado e visível no browser (conforme print):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29899765954967)

Depois, salve as alterações (salvando o dicionário de dados) e reinicie o SmartClient (feche o Protheus e abra novamente) para que o sistema assuma as novas configurações.
