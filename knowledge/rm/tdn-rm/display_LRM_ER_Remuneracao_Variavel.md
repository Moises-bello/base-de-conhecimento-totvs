---
content_hash: 5724f403772b67d60f6d500d59a32d41d0bca7364c748effc675f25a4ad2280f
fetched_at: '2026-06-29T00:06:06.253695+00:00'
page_id: '201729408'
product: rm
source: tdn-rm
title: ER_Remuneracao_Variavel
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Remuneracao_Variavel
version: 5
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** | PCREQ-6307 | **Subtarefa1** | PDR\_RHU\_RHU007-77 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O objetivo deste documento é descrever melhorias que serão implementadas no TOTVS Gestão de Pessoas.

Estas melhorias permitirão o planejamento, controle e execução de Remuneração Variável. Isto será possível por meio de melhorias na Gestão de Metas e Benefícios.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Benefícios | Alteração | Valorização > Controle de Benefícios | - |
| Faixas de Valor | Alteração | Acompanhamento > Gestão de Metas | - |
| Cadastro de Targets | Criação | Acompanhamento > Gestão de Metas | - |

**1. Cadastro de Benefícios**

O Cadastro de Benefícios deve ser renomeado para “Benefícios e Remuneração Variável”. Esta alteração deve abranger menus, títulos e opções de segurança.

Os itens destacados abaixo devem ter suas descrições alteradas:

**2. Cadastro de “Fator Multiplicador”**

O cadastro de faixas de valores de uma Meta Valor deve conter um campo chamado “Fator Multiplicador”.  
O Fator Multiplicador será utilizado para cálculo de remuneração variável utilizando Metas. Para calcular o valor a ser pago para determinada meta, deve ser aplicado o fator da faixa de atingimento da meta.

**3. Cadastro de Targets**

O Cadastro de Targets deve ser um anexo do Cadastro de Metas. Neste cadastro podem ser cadastrados os targets de pagamentos de Remuneração Variável.  
Para cada target disponível, podem ser vinculadas as Funções às quais deve ser aplicado o target.  
Por exemplo:  
Target: Coordenação  
Bonificação: 2  
Funções: Coordenador I, Coordenador II, Coordenador III

No caso deste exemplo, o target Coordenação seria aplicado às funções de Coordenação. A bonificação seria 2, ou seja, multiplica o valor do cálculo por 2.

Uma função não pode estar em mais de um target de uma meta. Ao tentar incluir funções num target, devem ser listados apenas as funções que não estão vinculadas à meta até o momento.

**4. Funções de Fórmula**

Um dos objetivos deste projeto é utilizar um Benefício do TOTVS Gestão de Pessoas para pagamento de Remuneração Variável baseada em Metas.  
Para possibilitar a criação de uma fórmula capaz de calcular a remuneração variável, devem ser disponibilizadas algumas Funções de Fórmula para facilitar os cálculos.

CalculaMetaAgrupadora(Coligada, Chapa, MetaAgrupadora)  
Esta função deve ser capaz de:  
a. Encontrar as metas filhas da meta informada, que estejam atribuídas ao funcionário informado.  
b. Para cada meta valor, deve ser verificado qual o resultado da meta, localizar a faixa que o resultado se encontra e o fator multiplicador.  
c. Encontrar o target da meta agrupadora que se relacione com a função do funcionário informado.  
d. Multiplicar o target pela soma dos fatores multiplicadores.  
e. Aplicar o valor encontrado ao salário do funcionário.  
f. Retornar o valor encontrado.

MetaAtingida(Coligada, MetaValor)  
Esta função deve ser capaz de:  
a. Buscar a forma de avaliação da meta.  
b. Verificar se a meta foi atingida ou se está numa faixa de valor que a define como cumprida.  
c. Retornar um valor sim/não.

BuscarTargetMediaMeta(Coligada, Chapa, MetaAgrupadora)  
Esta função deve ser capaz de:  
a. Identificar as funções desempenhadas pelo funcionário informado no período de vigência da meta.  
b. Calcular a média ponderada de targets de acordo com os targets das funções desempenhadas.  
c. Retornar a média calculada.

BuscarTargetFinalMeta(Coligada, Chapa, MetaAgrupadora)  
Esta função deve ser capaz de:  
a. Identificar a função do funcionário informado na data final de vigência da meta.  
b. Buscar o target para a função encontrada.

BuscarFatorMultiplicador(Coligada, MetaValor)  
Esta função deve ser capaz de:  
a. Identificar a faixa de valor de atingimento da meta informada.  
b. Retornar o fator multiplicador da meta para a faixa.

BuscarFatorMultiplicador(Coligada, Chapa, MegaAgrupadora)  
Esta função deve ser capaz de:  
a. Identificar dentro de uma meta agrupadora, a meta valor que esteja atribuída ao funcionário informado.  
b. Identificar a faixa de valor de atingimento da meta valor.  
c. Retornar o fator multiplicador da meta para a faixa.

SalFunc(Coligada, Chapa)  
Esta função deve ser capaz de retornar o valor do salário do funcionário.

BuscarProporcionalidade(Coligada, Chapa)  
Esta função deve ser capaz de:  
a. Verificar quantos meses do ano o funcionário trabalhou (mesma regra do 13º).  
b. Retornar o resultado de (meses / 12).

ResultadoMetaPeriodo(MetaAgrupadora, Mês, Ano, ConsideraFator)

Esta função deve ser capaz de retornar o valor do lançamento das metas de tipo valor, para quando tiver atribuição e o primeiro e último dia da meta valor bater com o parâmetro informado. Considera somente lançamentos aprovados

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
