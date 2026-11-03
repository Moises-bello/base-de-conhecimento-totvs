---
content_hash: b0b492be353d45f41ff56b2404d6371552c333ddbc73298ad57e05c96fd4463a
fetched_at: '2026-06-29T00:08:45.602874+00:00'
page_id: '311632327'
product: rm
source: tdn-rm
title: Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtro
version: 26
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona a tela de Filtros.

# Introdução:

---

       Os Filtros são aplicados nas Fontes de Dados do tipo Tabela, filtrando os resultados de acordo com o que o usuário cadastrar.

Observação

Os filtros podem ser aplicados apenas em Fontes de dados do tipo Tabela. No caso de Consultas SQL e Api, devem ser utilizados os [Parâmetros](http://tdn.totvs.com/x/tSGTEg).

# Como criar:

---

       Para criar um novo filtro, clique sobre a Entidade em que se deseja aplicar o filtro e informe todas as condições do filtro que serão aplicadas à ela.

Clique em "Adicionar" e informe os campos:

***Campo:*** Selecione em qual dos campos da tabela será aplicado o filtro.

***Operador:***Selecione a operação.

***Valor:***Informe qual valor o filtro terá.

Para campos do tipo "Data/Hora", será automaticamente disponibilizado um calendário para que a data possa ser selecionada.

O valor default para a hora é 00:00:00, mas pode ser alterado manualmente.

***E/OU:***Em caso de mais de uma condição adicionada:

Selecione "E" para que só apareçam os dados que satisfazem todas as condições do filtro.

Selecione "OU" caso deseje que os dados apareçam satisfazendo apenas uma ou mais condições do filtro.

Ativo?

Caso essa opção esteja marcada (Sim), o filtro será aplicado à Entidade. Caso contrário (Não), o filtro será desativado e os dados da respectiva tabela não serão filtrados.

***Exemplo prático abaixo:***

Entidade com campos relacionais

Caso a Entidade selecionada contenha campos relacionais, é possível também adicionar Filtro à eles.

Basta selecionar o campo, que sera mostrado da seguinte forma "**NOME.TABELA.ORIGEM\_NOME.DO.CAMPO**" e preencher as demais informações.

***Exemplo prático abaixo:***

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Filtros

falsefalse

**Status:** Pendente

false

**Data:** 08/11/2017

false

**Autores:**
