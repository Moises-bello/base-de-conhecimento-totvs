---
content_hash: d91301294e04990658120d6ad1e225fbb9e4323f5d8c0f5325beebb77e1f0a4b
fetched_at: '2026-06-29T00:08:16.329475+00:00'
page_id: '244937144'
product: rm
source: tdn-rm
title: RPTMIG00000 - Migração 11.8x - 12.1.x - Introdução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244937144
version: 7
---

# Introdução

|  |  |
| --- | --- |
| **Produto:** | TOTVS Reports |
| **Versões:** | 12.1.1x |
| **Ocorrência:** | Conteúdo  ---  Conteúdo|Introdução|Galeria Consulta SQL Vinculada a Banda|Galeria Consulta SQL Não Vinculada a BandaMigração 1180 x 12.1  ---   O **motor** de execução do Reports a partir da versão **12.1.5** foi refeita (reescrita), para que diversas inconsistências relatadas fossem devidamente tratadas, o que inclui [**Performance**, **Execução de Controles**, como **Totalizadores no Rodapé**, entre outras melhoras.].  O antigo **motor** do Reports na versão **1180, não era performática** devido a sua estrutura baseada em **execução por demanda** onde cada controle vinculado ao relatório era executado por demanda, ou seja, cada controle tinha seu valor processado e impresso somente na hora da impressão do controle no relatório.    A **1180** tem como pontos positivos e negativos:   | Nº | Pontos Positivos | Descrição | | --- | --- | --- | | **1** | Execução Independente | Os controles do relatório são executados, ou seja, seus dados são recuperados de uma **tabela**, ou **consulta SQL**, no momento de sua impressão. |  | Nº | Pontos Negativos | Descrição | | --- | --- | --- | | **1** | Execução Nada Performática | A cada impressão dos controles do relatório, através da **execução por demanda,** (lembrando que esses controles podem ser impressos diversas vezes), eles executariam, por exemplo, a **consulta sql** ou a **procedure** ou a **fórmula** vinculada a ele, diversas vezes, tornando a execução do relatório nada performática. |     O novo **motor** do Reports, disponível a partir da versão **12.1.5** em diante, é dividido em duas partes:   | Nº | Fase | Descrição | | --- | --- | --- | | **1** | **Preparação** | Recupera todas as fontes de dados do relatório (**tabelas, consultas SQL, providers**) e cria uma única fonte de dados (**consulta SQL**), que engloba todas as fontes citadas anteriormente | | **2** | **Execução** | Preenche os componentes visuais com os seus devidos valores, provenientes dessa fonte única de dados, e as imprime no relatório. |     A **versão 12** tem como pontos positivos e negativos:   | Nº | Pontos Positivos | Descrição | | --- | --- | --- | | **1** | Execução dependente. | A **Fase de Execução** é fortemente dependente da **Fase de Preparação**. É necessário primeiramente o agrupamento dos dados das diferentes fonte de dados para depois os dados serem impressos no relatório. |  | Nº | Pontos Negativos | Descrição | | --- | --- | --- | | **1** | Execução performática | A **consulta SQL** gerada na fase de preparação é submetida ao banco de dados apenas uma vez, seus dados são postos na memória; Ao ser impresso o valor já está disponível, não sendo necessário realizar uma requisição ao banco de dados toda vez que imprimir o componente | |
| **Ambiente:** |  |
| **Passo a passo:** |  |
| **Observações:** |  |
