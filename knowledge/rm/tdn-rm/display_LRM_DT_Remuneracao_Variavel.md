---
content_hash: e39c4d194e058fb3f8822826c4616c8d362dcb7d1efac0b9edb073bc7b1de1cb
fetched_at: '2026-06-29T00:06:24.273033+00:00'
page_id: '224115508'
product: rm
source: tdn-rm
title: DT_Remuneracao_Variavel
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Remuneracao_Variavel
version: 3
---

# REMUNERAÇÃO VARIÁVEL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Benefícios* | *Controle de Benefícios* | | *Faixas de Valor* | *Gestão de Metas* | | *Cadastro de Targets* | *Gestão de Metas* | |
| **Versões/Release:** | *12.1.10* |

## Descrição

O TOTVS Gestão de Pessoas permite o planejamento, controle e execução de Remuneração Variável. Isto é possível por meio de Gestão de Metas e Benefícios.

## Procedimento para Utilização

CADASTRO DE BENEFÍCIO

O Cadastro de Benefícios deve ser renomeado para “Benefícios e Remuneração Variável”. Esta alteração deve abranger menus, títulos e opções de segurança.

CADASTRO DE ''FATOR MULTIPLICADOR''

O cadastro de faixas de valores de uma Meta Valor contém um campo chamado ''Fator Multiplicador'' utilizado para o cálculo de remuneração variável utilizando metas. Para calcular o valor a ser pago para determinada meta, deve ser aplicado o fator da faixa de atingimento da meta.

CADASTRO DE TARGETS

O Cadastro de Targets é um anexo no Cadastro de Metas que serve para o cadastramento de targets de Pagamentos de Remuneração. Para cada target disponível podem ser vinculadas as Funções às quais deve ser aplicado o target. Por exemplo, Target: Coordenação; Bonificação: 2; Funções: Coordenador I, Coordenador II, Coordenador III.

No caso deste exemplo, o target Coordenação seria aplicado às funções de Coordenação. A bonificação seria 2, ou seja, multiplica o valor do cálculo por 2.

Uma função não pode estar em mais de um target de uma meta. Ao tentar incluir funções num target, devem ser listados apenas as funções que não estão vinculadas a meta até o momento.

FUNÇÃO DE FÓRMULA

CalculaMetaAgrupadora (MetaAgrupadora)

Esta função serve para encontrar as metas filhas da meta informada, que estejam atribuídas ao funcionário informado; Para cada meta valor, deve ser verificado qual o resultado da meta, localizar a faixa que o resultado se encontra e o fator multiplicador; Encontrar o target da meta agrupadora que se relacione com a função do funcionário informado; Multiplicar o target pela soma dos fatores multiplicadores. Aplicar o valor encontrado ao salário do funcionário; Retornar o valor encontrado.

MetaAtingida (MetaValor)

Esta função serve para buscar a forma de avaliação da meta; Verificar se a meta foi atingida ou se está numa faixa de valor que a define como cumprida; Retornar um valor sim/não.

BuscarTargetMediaMeta (MetaAgrupadora)

Esta função serve para identificar as funções desempenhadas pelo funcionário informado no período de vigência da meta; Calcular a média ponderada de targets de acordo com os targets das funções desempenhadas; Retornar a média calculada.

BuscarTargetFinalMeta (MetaAgrupadora)

Esta função serve para identificar a função do funcionário informado na data final de vigência da meta e buscar o target para a função encontrada.

BuscarFatorMultiplicador (MetaValor)

Esta função serve para identificar a faixa de valor de atingimento da meta informada e retornar o fator multiplicador da meta para a faixa.

BuscarFatorMultiplicador (MegaAgrupadora)

Esta serve para identificar dentro de uma meta agrupadora, a meta valor que esteja atribuída ao funcionário informado; Identificar a faixa de valor de atingimento da meta valor e retornar o fator multiplicador da meta para a faixa.

SalFunc (Chapa)

Esta função serve para retornar o valor do salário do funcionário.

BuscarProporcionalidade (Chapa)

Esta serve para verificar quantos meses do ano o funcionário trabalhou (mesma regra do 13º)e retornar o resultado de (meses / 12).

ResultadoMetaPeriodo(MetaAgrupadora, Mês, Ano, ConsideraFator)

Esta função serve para retornar o valor do lançamento das metas de tipo valor, para quando tiver atribuição e o primeiro e último dia da meta valor bater com o parâmetro informado. Considera somente lançamentos aprovados
