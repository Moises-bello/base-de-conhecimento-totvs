---
content_hash: a07e27c8d71e5182643a2aa60a354b9cf6b538aa652cbe380ff3ec0a04735f65
fetched_at: '2026-06-29T00:10:58.842422+00:00'
page_id: '607354601'
product: rm
source: tdn-rm
title: Relatórios de Orçamento de Pessoal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607354601
version: 4
---

Para facilitar a analise dos dados gerados do orçamento, foi desenvolvido dois relatórios no formato de cubo. O arquivo Cubos Orçamento SQL.TotvsCube (para base SQL) ou Cubos Orçamento Oracle.TotvsCube (para base ORACLE) deve ser importados usando o recurso de [cubos](https://tdn.totvs.com/display/LRM/Cubos.Net) do RM.

Os relatórios que contem no arquivo são:

**Relatório das Vagas orçadas x Vagas ocupadas**

* Formato de Saída :  Cubo RM.
* Exportação Excel
* Listado mês a mês do orçamento - vagas orçadas, vagas realizadas,  diferenças vagas e totais.
* Possibilidade de filtrar no Cubo por Filial, seção RH
* Visualização dos dados dentro da coligada do contexto. No caso de visualização do HeadCount de outra coligada,  deverá acessar a outra coligada.
* O cubo será disponibilizado pelo RM.EXE  Desktop
* Vagas Ocupadas terão origem após a admissão do funcionário.

Premissas 

* Deverá gerar mensalmente o cálculo do HeadCount para atualização das vagas ocupadas (realizado).

Abaixo o Modelo do relatório disponibilizado no Cubo RM.

Na no relatório gerado é possível fazer filtros por filial ou seção:

 

**Relatório do Quadro de Pessoal Orçado**

* Formato de Saída :  Cubo RM.
* Exportação Excel
* Listado mês a mês do orçamento - Salários, Horas Extras, Benefícios, Férias no mês, Encargos e Totais.
* Possibilidade de filtrar no Cubo por Filial, seção
* Visualização dos dados dentro da coligada do contexto. No caso de visualização do Valores de outra coligada,  deverá acessar a outra coligada.
* O cubo será disponibilizado pelo RM.EXE  Desktop

Premissas 

* Deverá configurar no produto os itens do orçamento informando as verbas por grupo.

**Exemplo** :

Grupo 1 -  Salário : Deverá informar os eventos Código Cálculo 2 Dias Trabalhados ou  Código Cálculo1 - Horas Normais

Grupo 2 -  Benefícios : Deverá informar os eventos Base de Cálculo que geram os Benefícios Parte Empresa, como ticket , plano saúde, etc.

Grupo 3 - Hora Extra - Informar os códigos de eventos pagos como Hora extra.

Obs.: Férias, Folha, Encargos, 13º Salário não será necessário parametrização.

Abaixo o Modelo desenvolvido no Cubo RM.
