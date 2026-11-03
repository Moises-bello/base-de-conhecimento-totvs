---
content_hash: 53788680a78f333cedc471f07bfd1bec057a112a95c25a2c38f7c403f2556af1
fetched_at: '2026-06-29T00:08:50.924638+00:00'
page_id: '334347509'
product: rm
source: tdn-rm
title: Importação de Consulta SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334347509
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo desse documento é exemplificar como importar uma Consulta SQL ou um Objeto Gerencial com uma Consulta SQL vinculada.

# Introdução:

---

       Após selecionar o Objeto em seu diretório, são exibidas algumas opções para finalizar o processo.

***Exemplificando cada opção:***

falseabasselecao-de-coligadasSeleção de Coligadas

Na aba "Seleção de Coligadas" estão disponíveis as seguintes opções para marcar:

***Coligada Atual:*** A consulta ficará disponível somente para Coligada atual.

***Todas as Coligadas:*** Qualquer Coligada poderá acessar a Consulta SQL.

***Lista de Coligadas:***Somente as Coligadas selecionadas abaixo poderão acessar a Consulta SQL.

selecao-de-sistemasSeleção de Sistemas

Na aba "Seleção de Sistemas" estão disponíveis as seguintes opções para marcar:

***Sistema Atual:*** A consulta ficará disponível somente para o Sistema atual. (por exemplo: Serviços Globais)

***Todas os Sistemas:*** Qualquer Sistema poderá acessar a Consulta SQL.

***Lista de Sistemas:***Somente os Sistemas selecionadas abaixo poderão acessar a Consulta SQL.

parametrosParâmetros

Na aba "Parâmetros" é possível configurar como a consulta SQL será importada, e qual o comportamento desejado caso já exista uma consulta com o mesmo nome.

**Automático**: A consulta será salva com o mesmo nome da consulta que está sendo importada, mas caso já exista alguma consulta com este nome, será adicionado numerais ao final do nome para que o nome se torne único e não conflite com o da consulta já existente. (Este modo não substitui consultas já existentes \*\*)

\*\* ⚠️ Atenção: Ao importar Objetos Gerenciais fornecidos pela TOTVS (com versão declarada), mesmo que seja no modo automático, a substituição da consulta existente ocorrerá.

**Fixo**: A consulta será salva com o nome informado, e caso já exista alguma consulta com este nome, **a consulta já existente será substituída**.

Ao digitar um novo Nome, não é possível adicionar os caracteres "-", ":" ou  ";", pois o Nome de uma Consulta SQL não pode possuir os mesmos.

Em seguida, basta clicar em "Executar" para finalizar o processo de Importação.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou superior.

false

**Processo:** Visões de Dados

falsefalse

**Status:** Finalizado

false

**Data:** 01/02/2018

false

**Autores:**
