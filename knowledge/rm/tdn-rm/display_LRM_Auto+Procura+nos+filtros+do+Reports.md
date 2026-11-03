---
content_hash: 527e0d408355b98da19de454fa54c9be10c940b9ad61c85c615b011235bb673d
fetched_at: '2026-06-29T00:11:28.372218+00:00'
page_id: '73076338'
product: rm
source: tdn-rm
title: Auto Procura nos filtros do Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/Auto+Procura+nos+filtros+do+Reports
version: 25
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Exemplificar o uso de uma action no filtro para auto procura na pesquisa dos valores.

# Introdução:

---

false

**CONFIGURAÇÕES DE CONSTRUÇÃO**

Assistente de ConfiguraçãoCenárioPasso 1Cenário

Para utilizar o recurso de "***auto procura***" nos filtros de um relatório .Net, proceda da seguinte forma.

Primeiro insira na estrutura do relatório um campo da tabela que deseja criar o filtro. No exemplo iremos trabalhar com os campos "***Chapa***" e "***Nome***" da tabela de funcionários para pesquisarmos pela chapa.

Depois de incluso o campo vá ao ícone "Filtros" do relatório para inclusão do filtro com auto procura.

Tipo de GráficoPasso 2Tipo de Gráfico

Na tela seguinte que será apresentado clique no ícone "Reticências".

O sistema irá apresentar em seguida um formulário para seleção, criação, alteração, exclusão e renomeação de um filtro. Selecione a opção existente e clique no ícone "***Modificar***".

No formulário seguinte selecione a opção "Chapa do Funcionário", Operador "Igual". Atribua para o campo "Valor" dois colchetes ([]). Clique no botão "Adicionar".

Clique no ícone "Reticências" deste filtro. O sistema irá apresentar uma segunda tela. Onde deverá ser uma pesquisa pela "Action"\* que retorna as informações desejadas. Feita a seletiva da "Action" escolha o campo chave e campo de pesquisa a serem utilizados.

false

No exemplo estaremos utilizando a "FopFuncAction" que lista os funcionários na visão. Lembramos que o nome da Action que referencia a informação desejada deverá ser levantada junto ao suporte do aplicativo.

Salve as alterações para que o sistema armazene a Action que estará sendo executado no momento de execução do filtro.

AparênciaPasso 3Aparência

Feita a devida configuração de auto procura para o filtro. No momento da execução do relatório que o sistema apresentar as opções de filtro ao invés de clicar em reticências você deverá clicar no ícone"V".

Depois que você clicar no ícone informado será apresentado uma tela seguinte,clique no ícone "Reticências".

Será apresentada uma tela de pesquisa onde você poderá criar uma série de filtros a fim de consultar os registros existentes. No exemplo abaixo criei o filtro "Todos", onde todos os funcionários foram listados.

Selecione o registro desejado e clique no botão "OK". Em seguida bastará dar continuidade a execução do relatório.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Auto Procura nos filtros do Reports

falsefalse

**Status:** Em manutenção

false

**Data:** 15/06/2016

false

**Autores:**
