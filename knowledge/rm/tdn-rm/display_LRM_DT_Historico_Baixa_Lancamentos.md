---
content_hash: 8d9a9eacfef533d3fa598d51ac23ecb1178dcc1b4d4f641c03acd01b3afb8e92
fetched_at: '2026-06-29T00:06:28.690170+00:00'
page_id: '233758063'
product: rm
source: tdn-rm
title: DT_Historico_Baixa_Lancamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Historico_Baixa_Lancamentos
version: 124
---

# Histórico das tabelas da Baixa de Lançamentos Financeiros

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Financeira* |
| **Função:** | *Informe a função.* |
| **Situação/Requisito:** | *Histórico de Baixa de Lançamentos* |
| **Solução/Implementação:** |  |
| **Requisito (ISSUE):** |  |

**Descrição**

As informações da baixa do lançamento financeiro, onde inclui os valores da baixa, valores de integração, rateio por centro de custo, rateio por departamento e tributos, serão armazenadas na criação do registro de  .

Para visualização dos dados de histórico de baixa, acessar no TOTVS Gestão Financeira o menu **Contas a Pagar/Receber | Lançamentos | Anexo Histórico de Alterações**,  visualizar o registro de Histórico de Lançamento desejado e acessar a aba **Baixas**.

Quando ocorrer a Liberação de Período no TOTVS Gestão Financeira, devem ser excluídos todos os registros das tabelas de Histórico de Baixa juntamente com o Histórico de Lançamento. O processo é chamado através do menu **Utilitários -> Liberação de Período**.

Novas funções de fórmula permitem acessar a posição financeira da baixa do lançamento numa data específica. Serão baseadas nos dados das tabelas de histórico de baixa com o registro selecionado como indicado no tópico “[Posição Financeira](http://tdn.totvs.com/display/LRM/ER_Historico_Alteracao_Lancamentos)”:

* + TABLANBAIXAPF: Valor de um campo do item de baixa do lançamento numa determinada data.
  + TABLANBAIXARATCCUPF: Valor de um campo do rateio por centro de custo do item de baixa do Lançamento numa determinada data.
  + TABLANBAIXARATDEPPF: Valor de um campo do rateio por Departamento do item de baixa do lançamento numa determinada data.
  + VALORTRBLANBAIXAPF: Valor do tributo do item de baixa do lançamento numa determinada data.
  + VALORINTEGRACAOLANBAIXAPF: Valor para um campo de integração do item de baixa do lançamento numa determinada data.
* As funções de fórmula acima, terão o mesmo conjunto de parâmetros de entrada da sua correspondente, que exibe os dados do estado atual do lançamento acrescentando somente parâmetro de data da posição financeira desejada. O retorno será sempre sobre os dados das tabelas de histórico correspondente.

divs
