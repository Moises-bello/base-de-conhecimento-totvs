---
content_hash: 7ce6e0ec4bbc70bfacc6192bc23d696c7c2de34006313d462c35cadb991ed4f1
fetched_at: '2026-06-29T00:09:28.765923+00:00'
page_id: '423938790'
product: rm
source: tdn-rm
title: Tipo de Movimentos - Tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+de+Movimentos+-+Tributos
version: 3
---

**Objetivo**

Atender as necessidades de nossos clientes que após gerarem movimentações no sistema, resolvam alterar alguns dados referentes à Inserção ou Exclusão de tributos, alteração do conteúdo da fórmula da base de cálculo ou Alíquota dos tributos associados aos parâmetros do tipo de movimento que foram gerados os respectivos movimentos.  
 Após realizarem as alterações relatadas acima, o sistema possui uma rotina de corrigir a tributação simultaneamente de todos os movimentos selecionados através de uma faixa de Numeração Inicial e Final ou até mesmo por Data Inicial e Final dos movimentos gerados baseados na parametrização atual das tributações associadas ao respectivo tipo de movimento filtrado.

**Critérios da seleção dos Movimentos a serem corrigidos:**

* Tipo de movimento: Seleção do Tipo de movimento a ser executado. O sistema permite apenas um tipo de movimento por processo.
* Numeração Inicial e Final: Especificação de uma faixa de numerações de movimentos criados a serem corrigidos.
* Data do Movimento/Data Extra1/Emissão: Especificação de um período de movimentos criados a serem corrigidos.
* Estimativas: Quantidade de movimentos que sofreram alterações ao longo do processo.
* Processo de correção de tributos associados ao movimento.
* O processo de correção dos tributos abrange a reformulação dos dados de acordo com a parametrização atual dos movimentos e seus respectivos lançamentos gerados através da integração dos sistemas.

**Impactos que o processo de corrigir tributação irá afetar:**

* Atualização dos dados referente ao lançamento financeiro.
* Ao gerar o processo de corrigir tributação em um movimento que gerou um lançamento financeiro, o processo deve atualizar os valores do respectivo lançamento desde que o lançamento financeiro não esteja baixado.
* Atualização dos dados referente ao lançamento Contábil.
* Ao gerar o processo de corrigir tributação em um movimento que gerou um lançamento contábil, o processo deve atualizar os valores do respectivo lançamento desde que o lançamento contábil não esteja integrado ao lote zero.
* Atualização dos dados referente ao controle de estoque do produto associado ao item.
* Ao gerar o processo de corrigir tributação em um movimento de compra, o sistema deve atualizar o custo médio do produto. (Resultado da fórmula do valor Financeiro / Quantidade).
* Atualização dos dados referente ao valor do bem - Geração de um movimento contendo um ativo imobilizado.
* Ao gerar o processo de corrigir tributação em um movimento que gerou um lançamento para o RM Bonum, o processo atualiza o valor do bem.
* Atualização dos dados referente ao Rateio gerado no movimento
* Ao gerar o processo de corrigir tributação em um movimento que consta de rateio de centro de custo/departamento, o processo deve atualizar proporcionalmente os valores do rateio associado ao movimento.
* Atualização dos dados referente aos movimentos gerados de CTRC
* Ao gerar o processo de corrigir tributação em um movimento de CTRC ou de seus movimentos indicados, o processo deve atualizar a totalidade dos valores associado ao mesmo.
* Atualização dos dados referente ao controle orçamentário
* Ao gerar o processo de corrigir tributação em um movimento que controla orçamento, o processo deve atualizar os valores orçados.
