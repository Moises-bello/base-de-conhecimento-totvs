---
content_hash: 466eb25ed963c03c44c9c805cf09bdab41a4a8750789d32d89e75c5e48142cb5
fetched_at: '2026-06-29T00:11:13.180835+00:00'
page_id: '657775268'
product: rm
source: tdn-rm
title: Lançamento da Produção para a Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=657775268
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Lançamento da Produção para a Folha**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Por esse módulo será feito o lançamento dos itens que estão em Folha Agrária / Produção Agrária para o envelope de pagamento do funcionário, seguindo a parametrização feita anteriormente.

## **02. EXEMPLO DE UTILIZAÇÃO**

Será somado por evento na produção para cada funcionário em que os eventos serão obtidos Folha Agrária / Mais / Associação de Regra de Cálculo e Tarefa Agrária. As produções a serem consideradas deverão estar entre as datas lançadas dentro do Período Global de Produção e com os campos Mês, Ano e Período não preenchidos.

Para o lançamento para folha, será considerado o período de produção global.

**Exemplo:**

Em Parametrizador / Folha Agrária / Parâmetros da Filial, o período global está informado de **25/01/2022 a 25/02/2022****.**

A competência atual é **02/2022** e tem lançamentos dos dias **25/01/2022 a 28/02/2022** com os campos mês, ano e período em branco.

Serão lançadas as produções compreendidas entre as datas do período Global **25/01/2022 a 25/02/2022.**

Caso na produção tenha registro de feriado em dobro, deverá lançar os eventos “Feriado Normal” e “Feriado em Dobro” cadastrados em Parametrizador / Folha Agrária / Parâmetros da Filial na inclusão ou edição - Pasta Cálculo considerando o mesmo valor do feriado em dobro, ou seja, serão realizados dois lançamentos com o mesmo valor, um como “Feriado Normal” e outro para “Feriado em Dobro”. As tarefas de produção do dia do feriado não poderão ser lançadas, já que estão contempladas nos eventos do feriado.

Será apresentado o Período Global de Produção com os dados informados em Parametrizador / Folha Agrária / Parâmetros da Filial na inclusão ou edição - Pasta Cálculo.

A competência apresentada será a atual, sendo que tanto o Período Global de Produção como a competência estarão desabilitados.

Para o lançamento do evento na ficha financeira deverá:

* **Adicionar:**
  + Inclui na ficha financeira se não existir
  + Soma aos valores existentes se existir
  + Preenche o campo mês, ano e período da produção agrária com o mês e ano da competência da tela de parâmetros e período da ficha financeira.

**Exemplo:**

Funcionário com lançamentos discriminados abaixo e todos lançamentos para o evento 7001

Produção importada e já lançada para a folha de pagamento - Mês, Ano e Período preenchidos

01/05/20XX - 100

02/05/20XX - 200

03/05/20XX - 300

Lançamento do evento 7001 já efetuado no envelope do funcionário com o valor de 600

Produção ainda não lançada para a folha de pagamento - Mês, Ano e Período sem preenchimento

04/05/20XX - 400

Efetuando o lançamento com o parâmetro “Adicionar” marcado somará 600 + 400 = 1000

* **Sobrepor:**
  + Incluir se não existir na ficha financeira
  + Sobrepor se já existir
  + Preenche o campo mês, ano e período da produção agrária com o mês e ano da competência da tela de parâmetros e período da ficha financeira.

**Exemplo:**

Funcionário com lançamentos discriminados abaixo e todos lançamentos para o evento 7001

Produção importada e já lançada para a folha de pagamento - Mês, Ano e Período preenchidos

01/05/20XX - 100

02/05/20XX - 200

03/05/20XX - 300

Lançamento do evento 7001 já efetuado no envelope do funcionário com o valor de 600

Produção ainda não lançada para a folha de pagamento - Mês, Ano e Período = NULL

04/05/20XX - 400

Efetuando o lançamento com o parâmetro “Sobrepor” marcado vai sobrepor os 600 substituindo o valor para 400

Não será lançado para o funcionário que o período estiver bloqueado.

**ATENÇÃO:** Será necessário o recálculo do envelope após lançamento.

## **03.****TELA **Lançamento da Produção para a Folha****

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de seção | Informar a Quebra de seção |
| Seleção de Funcionários | Informar para quais funcionários será feito o lançamento |
| Período global de produção | Apresenta o período cadastrado no parametrizador |
| Competência | Apesenta a competência atual |
| Ação no lançamento: Adicionar | Adiciona todos os valores do mesmo evento |
| Ação no lançamento: Sobrepor | Sobrepõe o evento com os novos valores lançados |
| Forma de exibição do log: Simples | Simples |
| Forma de exibição do log: Detalhado | Detalhado |

## **05. TABELAS UTILIZADAS**

* PPARAMFILIAL
* PRGRCALCTAREFAAGRARIA
* PPRODUCAOAGRÁRIA
* PFFINANC
