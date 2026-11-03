---
content_hash: 981cb12cdfb7fa9d69791d4d5605e2a84f6daeff697c328b5b73f427f563d621
fetched_at: '2026-06-29T00:10:21.936048+00:00'
page_id: '494975114'
product: rm
source: tdn-rm
title: Orçamento - Parametrizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494975114
version: 3
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela de parâmetros gerais orçamento**
4. **Tabelas modificadas**

## **01. VISÃO GERAL**

Foi adicionada uma nova seção os parâmetros de orçamento, no parametrizador, esta seção é a "Parâmetros Gerais de Orçamento", nesta seção foram adicionado quatro novos parâmetros. Os parâmetros que foram

adicionados são: "Bloquear edição de revisões quando uma nova revisão for criada.","Bloquear cálculo de revisões quando uma nova revisão for criada","Exibir revisões com bloqueio de cálculo ou de edição na tela de orçamento."

e "Habilitar controle de filtro de Seção x Função".

## **02. EXEMPLO DE UTILIZAÇÃO**

**Parâmetro: Bloquear edição de revisões quando uma nova revisão for criada.**

O parâmetro "Bloquear edição de revisões quando uma nova revisão for criada." tem como função bloquear a edição todas as revisões de orçamento quando uma nova revisão for criada.

Exemplo: Um orçamento está atualmente em sua revisão de nº 4, então o mesmo possuir as revisões 1,2 e 3, e essas revisões estão com a permissão de edição liberada, se o parâmetro

estiver marcado e uma nova revisão de orçamento for criada, a revisão nº 5 será criada e passará a ser a atual, as revisões de º 1,2,3 e 4 passarão a ter a sua permissão de edição bloqueada.

A mensagem é exibida para alertar o usuário, quando o parâmetro estiver marcado.

#### **Parâmetro: Bloquear cálculo de revisões quando uma nova revisão for criada.**

O parâmetro "Bloquear cálculo de revisões quando uma nova revisão for criada." tem como função bloquear o cálculo de  todas as revisões de orçamento quando uma nova revisão for criada.

Exemplo: Um orçamento está atualmente em sua revisão de nº 4, então o mesmo possuir as revisões 1,2 e 3, e essas revisões estão com a permissão de cálculo liberada, se o parâmetro

estiver marcado e uma nova revisão de orçamento for criada, a revisão nº 5 será criada e passará a ser a atual, as revisões de º 1,2,3 e 4 passarão a ter a sua permissão de cálculo bloqueada.

A mensagem é exibida para alertar o usuário, quando o parâmetro estiver marcado.

Quando os parâmetros "Bloquear edição de revisões quando uma nova revisão for criada." e "Bloquear cálculo de revisões quando uma nova revisão for criada" tiveram marcados, a mensagem

exibida é alterada:

#### **Parâmetro: Exibir revisões com bloqueio de cálculo ou de edição na tela de orçamento.**

Quando este parâmetro estiver marcado, as revisões que estejam com permissão de edição ou cálculo passam a ser exibidas na tela de orçamento. Quando este parâmetro estive desmarcado apenas as ultimas revisões de cada orçamento são exibidas.

#### **Parâmetro: Habilitar controle de filtro de Seção x Função.**

O orçamento possuem diferentes steps, que são telas ondem podemos setar diferentes configurações para um orçamento, em algumas dessas telas possuem um campo de lookup para funções.

Quando este parâmetro está habilitado uma validação é feita para ver se o usuário logado é chefe de uma seção, caso sim, os lookups de funções só retornam as funções que estão vinculadas a seção 

em que o usuário logado é chefe.

Exemplo:

Em uma determinada coligada existem duas seções, as seções 1.0 e 2.0, na seção 1.0 temos duas funções vinculadas sendo elas Diretor e Gerente de Projetos, na seção 2.0 temos três funções que são,

Analista de Suporte, Analista de Sistemas e Analista de Qualidade. No nosso caso o usuário logado que está fazendo o orçamento é o chefe da seção 2.0, então nas telas que possuem lookups de função só

vão retornar as funções pertencentes a seção 2.0 que são as funções Analista de Suporte, Analista de Sistemas e Analista de Qualidade. Caso o parâmetro esteja desmarcado todas as funções apareceram no

lookup normalmente.

Obs: Este parâmetro marcado não afeta outras partes do sistema que utilizam o lookup de função.

## **03. TELA DE PARÂMETROS GERAIS ORÇAMENTO**

## **04. TABELAS MODIFICADAS**

* A Tabela PORCAMENTO foi atualizada, nesta colunas foram adicionadas duas colunas novas:  
  A coluna EDICAOBLOQUEADA do tipo smallint pode ter dois valores 0 ou 1 e representa se uma revisão de orçamento tem permissão para ser editada.  
  A coluna CALCULOBLOQUEADO do tipo smallint pode ter dois valores 0 ou 1 e representa se uma revisão de orçamento tem permissão para ser calculada..

]]>
