---
content_hash: 3b847d538ae7dc8746c56bb5b5a678620a94d327649d8bf278cea0fb1a4f1b65
fetched_at: '2026-06-29T00:08:45.582415+00:00'
page_id: '311632312'
product: rm
source: tdn-rm
title: Fonte de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Fonte+de+Dados
version: 50
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona a tela de Fonte de Dados.

# Introdução:

---

       É necessário informar a Fonte de Dados para utilizar uma tabela do banco ou até mesmo uma consulta SQL personalizada. Essa fonte de dados é a base para os dados que serão enviados para o relatório posteriormente.

# Como criar:

---

       Para criar uma nova Fonte de Dados, basta clicar em "+ Novo" e informar os campos abaixo:

***Nome da fonte de dados:***Informe o nome da fonte de dados, deve ser um nome único e é por ele que a fonte de dados será identificada.

***Conexão:*** Defina em qual [Conexão](http://tdn.totvs.com/x/sSGTEg) os dados serão buscados.

***Tipo:*** Informe se a fonte de dados será uma Tabela do banco ou uma Sentença SQL.

falseDados Relacionais1Tabelas

       Caso o usuário selecione a opção "Tabela", basta informar o campo abaixo:

***Nome da tabela:*** Informe o nome da tabela, exatamente como no banco de dados.

***Exemplo prático abaixo:***

Conexão com Provedor Integrado

       Caso a busca por tabelas tenha sido implementada pelo Provedor Integrado utilizado, será apresentada uma lupa no campo de preenchimento do nome da tabela, onde há um lookup para que a tabela desejada seja selecionada.

Caso o nome completo da tabela seja conhecido pelo usuário é possível digitar o nome da tabela e teclar "Tab" para que a mesma seja selecionada.

       Para pesquisar o nome da tabela, basta clicar no lookup para realizar a busca.

A busca será realizada após digitar pelo menos uma letra e clicar na lupa ou teclar "Enter"

***Exemplo prático abaixo:***

2Consultas SQL

       Caso o usuário selecione a opção "Sentença SQL", basta digitar a sentença desejada e em seguida clicar em "Teste de conexão com o provedor". Caso tudo esteja "OK", será exibida a mensagem de "Sucesso ao realizar teste".

***Exemplo prático abaixo:***

3Sentença SQL com parâmetro

       Caso o usuário deseje vincular um parâmetro a sua consulta SQL, basta adicionar " : " seguido pelo nome do parâmetro.

Como no exemplo:

SELECT \*  
FROM GCOLIGADA  
WHERE CODCOLIGADA =**:CODIGO**

Note que a opção "Ligar parâmetros" aparece na tela. Clique nela para vincular os parâmetros da sentença aos parâmetros cadastrados.

Caso o parâmetro ainda não tenha sido cadastrado, clique na opção "Adicionar parâmetros" para adicionar um novo parâmetro e vincular o mesmo à sua consulta SQL.

Em seguida, basta clicar em "Confirmar" e posteriormente em "Salvar".

4API

       Quando o tipo de “Conexões” for definido uma conexão do tipo “API” ao escolher a fonte de dados o sistema irá apresentar as seguintes opções;

Caso uma API selecionada não esteja de acordo com o padrão de listas do Guia de API's da TOTVS, será exibida uma mensagem de erro. A especificação deverá ser ajustada pela equipe responsável.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou superior

false

**Processo:** Fonte de Dados.

falsefalse

**Status:** Pendente

false

**Data:** 08/11/2017

false

**Autores:**
