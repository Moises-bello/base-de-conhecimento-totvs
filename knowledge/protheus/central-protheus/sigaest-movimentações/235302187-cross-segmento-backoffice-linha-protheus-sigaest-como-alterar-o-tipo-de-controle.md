---
article_id: 235302187
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 263554d4d8903b727b3f01bfbbbef5cf58c92215498c055ebf2dcc9a921d20d4
fetched_at: '2026-06-28T22:38:54.357101+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o tipo
  de Controle de Rastreabilidade no Protheus?
type: support-article
updated_at: '2025-11-27T11:38:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302187-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-tipo-de-Controle-de-Rastreabilidade-no-Protheus
---

**Dúvida**

Como alterar o tipo de Controle de Rastreabilidade de "Lote" para "Sublote" e vice versa?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para alterar o tipo de Controle de Rastreabilidade, sem gerar problemas nos saldos dos produtos com rastro, antes de incluir qualquer movimentação, é necessário:

1. Efetuar o Fechamento do Período estoque (MATA280);
2. Acessar ao Cadastro de Produtos (MATA010) e alterar o campo "**Rastro"**para o tipo desejado sendo **L=Lote** ou **S=Sublote**.

A realização do Fechamento de Período impede que Movimentações anteriores ao fechamento sejam alteradas, pois o parâmetro **MV\_ULMES**terá a data do fechamento e todas as rotinas de movimentações só permitem atualização no estoque com data posterior à data gravada no conteúdo deste parâmetro.

**Observações**:

* Se for necessário alterar o tipo de controle de rastreabilidade de Lote para Sublote, é imprescindível que seja feito logo após o Fechamento de Estoque com saldo zerado nos lotes. Caso contrário apresentará a mensagem: "Não pode ser alterado. Já ocorreram movimentos deste produto após o último fechamento.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
