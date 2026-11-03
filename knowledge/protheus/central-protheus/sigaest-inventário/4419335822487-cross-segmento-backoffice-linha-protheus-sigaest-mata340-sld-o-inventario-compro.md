---
article_id: 4419335822487
category: SIGAEST - INVENTÁRIO
content_hash: 4a8b52db193dbf2064e626a9234e76f5694cc9d11f23e42603366e673ad1076c
fetched_at: '2026-06-28T22:38:50.418373+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - SLD - >
  O inventario comprometeria o saldo atual do produto
type: support-article
updated_at: '2022-01-17T12:02:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419335822487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-SLD-O-inventario-comprometeria-o-saldo-atual-do-produto
---

**Dúvida**Ao executar o Acerto de Inventário é exibido o relatório de "Itens não Inventariados" com o motivo SLD - > O inventario comprometeria o saldo atual do produto. Como resolver este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Normalmente este motivo é exibido nos seguintes cenários:

* Se o saldo no SB2 for ficar negativo (MV\_ESTNEG = N)
* Se houver Saldo de Pedidos (Solicitação de Compra, Pedido de Compra, OP (B2\_SALPED)) e Qtde. Prevista (B2\_SALPRE ou B2\_QEMPPRE)
* Saldos de Pedidos de Vendas liberados no SC9
* A data do SB7 estar menor ou igual à data do SB2 (B2\_DINVENT)
* Existência de movimentação na tabela SD3 com data posterior ao Inventário.
* Produto com controle de Lote e/ou Endereçamento e saldo desbalanceado entre a tabela SB2 com as tabelas SB8 e/ou SBF.
  + Para cenário de Desbalanceamento, veja os artigos de apoio abaixo:
    - [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Parametrização para identificar divergência de saldos entre tabelas SB2 X SB8 X SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF?source=search)
    - [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tratamento-correto-de-desbalanceamento-de-tabelas-de-Lote-e-Endere%C3%A7o-em-todos-os-cen%C3%A1rios?source=search)

Com isso, basta tomar as ações necessárias (e, em caso de dúvida maior, acionar ao TI da empresa ou ao Suporte Padrão do módulo de Estoque/Custos para orientações).

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)*

*[MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada)*

*[MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data informada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada)*

*[Clique aqui e veja mais artigos sobre Inventário no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)*
