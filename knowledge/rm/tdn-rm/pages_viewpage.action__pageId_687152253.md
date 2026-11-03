---
content_hash: 1ba632b9a4d2e037c546ae5035b9ea713146501cd890ddec226c1fc659baf173
fetched_at: '2026-06-29T00:11:20.568015+00:00'
page_id: '687152253'
product: rm
source: tdn-rm
title: Cálculo de Produção Agrária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687152253
version: 11
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cálculo de Produção Agrária**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Por esse módulo será feito o cálculo da produção agrária atualizando a produção já existente no cadastro e lançando tarefas de acordo com a parametrização.

Para ser feito o lançamento o usuário poderá determinar o escopo selecionando a parametrização no processo de acordo com a Quebra de seção, Seleção de funcionários e Período.

Observação: O cálculo filtra por funcionários do tipo R - Rural

Os cálculos serão processados de acordo com os parâmetros marcados:

* Lançar CAT e ou afastamento pela previdência
* Lançar feriados
* Lançar complemento de diária
* Atualizar preços segundo cadastro de teste e diária
* Atualizar percentual Homem-Dia

Além dos lançamentos de acordo com os parâmetros acima existem também os lançamentos com parametrização especifica:

* Pausa Remunerada
* Lançamento do DSR

Para cada regra de cálculo incluída deverá atualizar os campos abaixo:

* Código da coligada: Será a de contexto
* Chapa do Funcionário: A que estiver em processamento
* Unidade Agrária / Fração Agrária / Programação Agrária será
  1. O último lançamento em que a finalidade da regra de cálculo da Tarefa seja “Tarefa de produção” e no dia havendo mais de uma Tarefa de produção pegar a que tiver o maior valor em que:
     1. Primeiro do próprio funcionário;
     2. Segundo da seção em que o funcionário está lotado.
  2. Se não existir tarefa no dia assumir os valores default parametrizado em Parametrizador / Folha agrária / Parâmetros da Filial / Valores Default. Exemplo quando tem afastamento integral.

A ordenação nas linhas de produção será feita de acordo a prioridade da regra de cálculo.

A prioridade de cálculo sugerida é:

* Empreita - 10
* Diária - 10
* Corte - 10
* Complemento de produção - 20
* Complemento de afastamento - 30
* Complemento de diária mínima - 40

Sugestão criar uma regra para cada tipo de cálculo porque o depende de outras tarefas será utilizado para vários tipos de tarefas FERIADO, FERIADO EM DOBRO, COMPLEMENTO DE DIÁRIA, AFASTAMENTOS

Para a atualização da Produção Agrária será seguida a seguinte regra:

* Caso o valor unitário obtido seja zero deverá:
  + Se existe na produção excluir, exceto quando a regra de cálculo da Tarefa tenha sua finalidade marcada como Tarefa de produção.
  + Se não existe ignora e não inclui

* Caso valor unitário seja maior que zero deverá:
  + Sobrepor se já existir;
  + Incluir se não existir.

Atualização da Unidade Agraria

Assim que realizado o calculo da produção agraria, é efetuado uma varredura nas tarefas de produção para a atualização da Unidade Agraria das tarefas de "não produção".   
É executada também uma regra para tal atualização, utilizando o valor ganho. As tarefas de não produção irão assumir a Unidade Agraria da tarefa de produção que contenha o maior valor ganho do dia. Caso não haja nenhuma tarefa de produção no dia, será considerado a unidade agraria do dia anterior.  
  
Sendo assim, temos o seguinte exemplo:  
  
Para a CHAPA 00025 temos os seguintes valores para o dia 11/05/2021 antes do calculo da produção:  
  
  
  
E após o calculo será alterado a unidade agraria da tarefa de pausa:

## **02. EXEMPLO DE UTILIZAÇÃO**

Links para regras específicas de cálculos da folha agrária com seus respectivos exemplos:

[Lançar CAT e ou afastamento pela previdência](https://tdn.totvs.com/pages/viewpage.action?pageId=687154015)

[Lançar feriados](https://tdn.totvs.com/pages/viewpage.action?pageId=687154149)

[Lançar complemento de diária](https://tdn.totvs.com/pages/viewpage.action?pageId=687154804)

[Atualizar preços segundo cadastro de teste e diária](https://tdn.totvs.com/pages/viewpage.action?pageId=687155166)

[Atualizar percentual de Homem-Dia](https://tdn.totvs.com/display/LRM/Atualizar+percentual+de+homem+dia)

[Pausa Remunerada](https://tdn.totvs.com/pages/viewpage.action?pageId=687156371)

[Cálculo do DSR](https://tdn.totvs.com/pages/viewpage.action?pageId=687156467)

## **03.** **TELA Cálculo de Produção Agrária**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetros | Veja explicação em cada link do item 02 |

## **04. TABELAS UTILIZADAS**

* PPRODUCAOAGRARIA
