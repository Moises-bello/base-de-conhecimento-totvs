---
content_hash: 1c6e99d2bd64ca3ce3666927735733aa7c891e9999157ccf492a23b59998f6b0
fetched_at: '2026-06-29T00:10:31.691514+00:00'
page_id: '521651036'
product: rm
source: tdn-rm
title: Utilização de Filtro como parâmetro em consultas SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521651036
version: 36
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento tem por objetivo orientar a utilização do componente Filtro do Reports como parâmetro para uma consulta SQL utilizada no relatório.

# Introdução:

---

       É possível utilizar filtros de um relatório como parâmetros para execução de consultas SQL, desde que o relatório possua um ou mais controles do tipo "Filtro".

falseExemplos de FiltroFiltros1Inserindo Filtro no RelatórioInserindo Filtro no Relatório

       Para inclusão de um filtro no relatório acesse seu design. Para isso selecione o relatório, clique no menu “Processos | Editar Estrutura”. Depois de acessar o design do relatório selecione o menu “Inicio | Estrutura | Filtros”. Para exemplo incluiremos um filtro “Chapa” no relatório.

       Informações sobre regras e condições de criação de um filtro acesse: [Filtros](https://tdn.totvs.com/x/ogSxAw)

2Inserindo o Controle FiltroInserindo o Controle Filtro

       Para inserir o controle do tipo Filtro, primeiramente é necessário criar um filtro em seu relatório, conforme mencionado no processo “Inserindo Filtro no Relatório”.

       Depois de criado o filtro em seu relatório acesse a barra “Caixa de Ferramentas”, selecione o controle do tipo “Filtro” e arraste-o para estrutura do seu relatório.

       Depois de incluído o controle do tipo Filtro no seu relatório é necessário configurá-lo para que seja apresentada as informações desejadas. Lembramos que o valor configurado será o valor repassado a consulta SQL.

       Para exemplo configuraremos o filtro chapa criado no processo “Inserindo Filtro no Relatório” para que apresente o valor da chapa somente e não toda a condição do filtro que seria “Chapa = ‘00001’”.

       Selecione o controle e acesse as propriedades deste controle teclando F4 em seu teclado. No grupo de propriedades “Diversos” selecione na propriedade “Filtro” o valor “Filtro Relatório”. Em seguida na propriedade “Clausula” selecione o filtro desejado e para finalizar em “Valor” selecione a opção para que o valor do filtro seja apresentado, no exemplo utilizaremos o valor da chapa.

false

       Lembramos que filtros são passiveis de criação somente em relatórios com uma fonte de dados do tipo tabela associada a banda do relatório.

       Para habilitar a barra de Caixa de Ferramentas acesse o menu “Exibição | Janelas | Caixa de Ferramentas”.

3Filtro - Parâmetro em SQLFiltro - Parâmetro em SQL

       Para exemplificarmos a usabilidade do filtro como parâmetro criarmos a seguinte consulta SQL para incluí-la no relatório.

sqlConsulta Exemplo

       Esta consulta SQL foi adicionada ao sub-detalhe do relatório. A estrutura do relatório resultou ficou da seguinte forma.

       Como parâmetro utilizaremos o nome do Controle Filtro (***Filtro1***) na condição da consulta SQL. Desta forma ao executarmos o relatório o sistema irá utilizar o valor do Controle Filtro como parâmetro. O resultado do relatório será o seguinte.

4Filtro - Tipo DataFiltro - Tipo Data

       Para uso de filtros que utilizam valores de dada como parâmetros é necessário que a consulta SQL tenha um tratamento de conversão do parâmetro para correta execução.

       Neste exemplo abaixo temos uma consulta SQL sem nenhum tratamento para receber o valor do Controle Filtro.

falsesqlConsulta Incorreta

       Neste exemplo a mesma consulta SQL, porém com os devidos ajustes para que o valor data do filtro seja compreendido corretamente.

falsesqlConsulta Corretafalsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Filtros como parâmetros em consultas SQL

false

**Relatório Utilizado:**  (Versão: 12.1.27)

falsefalse

**Status:** Finalizado

false

**Data:** 26/11/2019

false

**Autores:**
