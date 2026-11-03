---
content_hash: 7940a058984047d56f9fdeefba79243312ff7364215cb4f595d7273fde7ae236
fetched_at: '2026-06-29T00:10:58.321865+00:00'
page_id: '60523225'
product: rm
source: tdn-rm
title: Trabalhando com Consultas SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/Trabalhando+com+Consultas+SQL
version: 3
---

Talhando com Consultas SQL

**Introdução**

O objetivo deste documento é auxiliar os usuários da linha RM em como criar e configurar uma **Consulta SQL,** utilizando todos os recursos disponíveisdo aplicativo**.**

1. **Criando a Consulta SQL**

Para criarmos um Consulta SQL, devemos acessar ***Gestão /Consultas SQL / Incluir (CTRL + INS)***, inserir a sintaxe e definirmos as opções do cadastro. Essa sentença que iremos inserir a seguir retorna os lançamentos a receber em aberto.

**SELECT** FLAN.CODCOLIGADA,

FLAN.IDLAN,

FLAN.CODFILIAL,

GFILIAL.NOME,

FLAN.VALORORIGINAL,

FLAN.CODCXA,

FCXA.DESCRICAO

**FROM** FLAN

**JOIN** **FCXA** (**NOLOCK**) **ON (**FCXA.CODCOLIGADA = FLAN.CODCOLIGADA **AND** FCXA.CODCXA = FLAN.CODCXA)

**JOIN** **GFILIAL** (**NOLOCK**) **ON (**FLAN.CODCOLIGADA = GFILIAL.CODCOLIGADA **AND**

FLAN.CODFILIAL = GFILIAL.CODFILIAL)

**WHERE** FLAN.CODCOLIGADA = 1

**AND** FLAN.PAGREC = 1

**AND** FLAN.DATABAIXA **IS** **NULL**

**Dicas**

· As consultas SQL podem executar de qualquer query do sistema utilizando constantes de valores do contexto. Este campo pode ser por exemplo o Código da Coligada atual, Filial, Chapa, Projeto, Nível de Ensino, etc.

A sintaxe da consulta SQL deverá ficar assim:

SELECT CAMPO\_DA\_BASE FROM TABELA\_DA\_BASE

WHERE CAMPO\_DA\_BASE = :$CONSTANTE\_DO\_CONTEXTO

Atenção

Caso seja necessário adicionar aspas duplas " como texto na consulta SQL basta colocar o caractere \ antes do ".

Exemplo

REPLACE('1;2;3;4',';','"') ao salvar o registro as aspas duplas serão substituídas por aspas simples.

REPLACE('1;2;3;4',';','\"') adicionando o escape \ as aspas duplas não  serão substituídas.

O uso do “NOLOCK” nas consultas SQL melhora o desempenho e seu uso é incentivado principalmente nas consultas de tabelas muito grandes. Este recurso é exclusivo para bases SQL Server.

Veja como usar o "NOLOCK" em uma consulta:

SELECT \* FROM NOME\_TABELA (NOLOCK);

***Acesse: Gestão /Consultas SQL / Incluir (CTRL + INS)***

**Campos:**

* **Código** Digite um código alfanumérico para identificação da sentença. Este código tem finalidade exclusiva de identificação da sentença, não produzindo qualquer alteração no resultado desejado.

* **Título**

Informe uma descrição, um nome, ou um título que identifique mais facilmente a operação que

deverá ser executada.

* **Visível a todas Coligadas** Marque esta opção para que a consulta SQL fique disponível para todas as coligadas. Essas consultas serão representadas com um globo em seu ícone.

* **Disponível para RM Portal** Disponibiliza o resultado da Consulta SQL no RM Portal.

* **Botão Configurar** O nome definido na Descrição será o alias para o campo, e terá resultado na visualização de consultas SQL, no site do RM Portal.

* **Banco de Dados** Escolha uma conexão caso deseje fazer uma consulta SQL para um banco de dados externo.

* **Disponível para Execuções em Visões** Marque este campo caso queira que a sentença seja executada em visões.

* **Disponível para Filtros** Marque este campo caso queira que a sentença seja executada nos filtros.

* **Disponível para Relatórios** Marque este campo caso queira que a sentença seja executada nos relatórios.

* **Data da Última Alteração** Exibe a data e a hora da última alteração realizada na consulta.

* **Usuário Responsável** Exibe o último usuário que realizou alterações na consulta SQL que está sendo editada.

**2.** **Executando a Consulta SQL.**

***Acesse: Gestão /Consultas SQL***

Para executar a Consulta SQL, basta abrir o cadastro de consulta e dar um duplo clique na consulta desejada.

Após a execução da Consulta SQL, os dados gerados serão apresentados conforme tela abaixo.

**2.1** **Configurando a Consulta SQL.**

Após a geração dos dados começaremos a utilizar os recursos da Consulta SQL, na opção de colunas da visão estão todos os campos da sentença, os quais podem estar visíveis ou não na visão.

Na opção de formatação condicional, podemos definir a cor do fundo e da borda de uma célula ou linha, para isso precisamos definir a condição para a formatação ser aplicada.

Exibir Sentença SQL - Podemos exibir a sintaxe da consulta nesta opção.

Exportar Dados - Os dados gerados poderão ser exportados para as extensões CSV, XLS, PDF, XLSX, TXT e RTF.

Gráficos Instantâneos - Podemos gerar gráficos a partir dos dados da visão, basta selecionar os dados e definir o tipo de gráfico a ser utilizado.

Colunas Calculadas da Visão – Essa funcionalidade permiti a inclusão de colunas na visão, criados a partir de dados da própria visão.

Definições das Actions - Este recurso nos permite associar Actions a visão, podendo assim editar o registro a partir da visão.

Após a definição da action basta dar um duplo clique no registro e a action será apresentada.

Rodapé da Visão – Com essa funcionalidade podemos inserir um campo para cada coluna na visão, existe 5 tipo que podemos utilizar esse campo (Soma, Min, Máx, Contagem e Média).

Rodapé de Agrupamento – Esse recurso inseri uma linha de rodapé por agrupamento, possibilitando inserir um campo por coluna da visão (Soma, Min, Máx, Contagem e Média).

Caixa de Agrupamento – Exibi uma barra superior na visão com os campos os quais estão sendo utilizados para agrupar os dados da visão.

Exibição de Linhas Alternadas – Apresenta os dados da visão intercalando as linhas com duas cores distintas.

Layout – Podemos salvar os layouts e depois rapidamente voltar a eles, sem ter que refazer todos os agrupamentos e configurações.

Quando clicamos com o botão direito do mouse sobre a coluna é apresentada as opções abaixo.

* Ordenar ascendente / Descendente / Limpar Ordenação - Podemos ordenar os dados da visão instantaneamente.

* Agrupar por este Campo / Hide Group By Box – Definimos o agrupamento e exibimos a caixa de agrupamento na visão

* Remover Esta Coluna – Desabilita a coluna.

* Melhor Ajuste / Todas as Colunas – Ajusta a coluna aos dados

* Fixar – Congela a coluna para que a mesma permaneça sempre visível na visão.

Anexos Consulta SQL – Para inserir uma Consulta SQL como Anexo basta acessar Anexo / Inserir Consulta SQL , a seguir um exemplo da tela de cadastro de funcionários.

Segue detalhamento do processo.

Após selecionar a opção de Inserir Consulta SQL é apresentada o assistente de inserção de nova consulta SQL como Anexo.

Aqui definimos a consulta que será utilizada.

Nesta etapa é apresentada a tela de definições de parâmetros, toda Consulta SQL deverá possuir parâmetros, os quais serão utilizados como condições para consulta. Os parâmetros da consulta serão associados aos campos da visão.

Definição de Grupo de Visualização – Podemos definir que todos os usuários tenham acesso ao resultado da consulta ou Perfis / Usuários específicos.

Após a Execução do processo a Consulta SQL estará disponível em **Anexos / Consulta**.
