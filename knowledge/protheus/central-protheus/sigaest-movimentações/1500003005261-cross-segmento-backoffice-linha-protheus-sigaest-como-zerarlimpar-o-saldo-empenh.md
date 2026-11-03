---
article_id: 1500003005261
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 74875d77e8bfe338be6bbadf150706816f5ef38a18bb8e2be0774c2edfa47522
fetched_at: '2026-06-28T22:38:55.423002+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como zerar/limpar
  o Saldo Empenhado?
type: support-article
updated_at: '2023-08-09T19:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003005261-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-zerar-limpar-o-Saldo-Empenhado
---

**Dúvida**Como zerar o saldo empenhado para determinado Produto no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Quando já houve o apontamento de alguma quantidade, o campo D4\_QTDEORI - Quantidade Empenho deve possuir a quantidade que foi empenhada e o campo D4\_QUANT - Saldo Empenho, o valor **0**, assim o Sistema identifica que daquele componente não há mais quantidade a ser requisitada.

**Como limpar o Saldo Empenhado para algum produto?**

* Via rotinas MATA380 - Empenho Simples ou MATA381 - Empenho Múltiplo, selecionar o registro desejado **> Alterar**> **Outras Ações** > **Zera Emp**;
* Zerando automaticamente quando realizar o apontamento total da **OP - Ordem de Produção**.

**Caso a OP estiver encerrada e mesmo assim possuir saldo empenhado**

* Acessar à rotina **MATA381** > **Alterar** > **Será apresentada a mensagem perguntando se deseja zerar o empenho** > Clicar em **Sim** > **OK** >  **Salvar**.

**Caso o produto possua controle de Lote e tenha saldo empenhado por motivo de bloqueio/vencimento**

* A limpeza deste saldo normalmente se dá por NF de Saída, ou alterando a data do vencimento do Lote via rotina MATA390, selecionando o Produto e Lote -> clicando em "Validade e Fabricação"
* Validar se possui algum documento com o lote em questão com status "Bloqueado" (Legenda vermelha), na rotina Bloqueio de Lotes MATA275. Para liberação basta clicar em "Liberar" e escolher a quantidade que será liberada.

Desta forma o saldo do empenho é zerado.

**Saiba mais:**

*[MP - SIGAEST - MATA275 - Faturar ou Inventariar produto com Lote Vencido que esta bloqueado para movimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-MP-SIGAEST-MATA275-Faturar-ou-Inventariar-produto-com-Lote-Vencido-que-esta-bloqueado-para-movimenta%C3%A7%C3%A3o)*

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
