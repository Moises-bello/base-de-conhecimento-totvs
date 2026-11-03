---
content_hash: e6c2a622b4aa635413ba244ed0922362b08008a079b4b25b614f8d7f97d43869
fetched_at: '2026-06-29T00:05:57.149307+00:00'
page_id: '165282395'
product: rm
source: tdn-rm
title: Utilizando a Atividade  "Criar Coluna"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165282395
version: 9
---

# Sumário

---

Sumário

# Objetivo

---

     Esse documento tem por objetivo demonstrar como criar uma coluna na visão do usuário.

# Introdução

---

**Inserir atividade "Criar Coluna"**

* A propriedade "Nome da Coluna" serve para definir o nome da nova coluna a ser criada.
* A propriedade "Tabela" refere a tabela que estamos na visão (no caso tabela GUSUARIO).
* A propriedade "Tipo" diz a respeito do tipo de campo que será a coluna (string/int/decimal...).

     A coluna a ser adicionada na visão de Usuários será a COLUNA\_TESTE.

**Inserir a atividade "Executar Consulta SQL"**

* É necessário fazer uma Consulta SQL que retorne todos os dados que serão utilizados. Neste exemplo a consulta retornará o código e o nome de todos os usuários.

    **Insira a atividade "Localizar Registro na Tabela"**

* A atividade de FindRecord (Localizar registro na tabela) deve estar dentro de um foreach para fazer a ligação entre o registro corrente da visão e o registro do resultado da consulta através das PKs.

     **Configuração do foreach****:**

     **Configuração d****a Sequência:**

     **Configuração do FindRecord:**

* A ligação será feita pela chave primária (PK) CODUSUARIO.
* **Tabela:**Neste exemplo, a tabela de referência é o resultado da consulta SQL.
* **KeyFields:** Os campos chaves para formar o relacionamento entre o resultado da consulta SQL e os registros da visão de usuários. Neste exemplo, o CODUSUARIO. Caso existam mais de um campo, basta separá-los com uma vírgula. Ex.: CODCOLIGADA,IDLAN
* **Parâmetros:** Após informar o KeyFields, os parâmetros devem ser preenchidos com a PK da visão.

     Inserir a atividade "Expressão"

* A Expressão irá montar o conteúdo da nova coluna. Neste exemplo a COLUNA\_TESTE será preenchida com o valor "TESTE + NOME DO USUÁRIO".

     **Configurando o Gatilho:**

**Resultado**

* Ao abrir a tela de Usuários, a COLUNA\_TESTE será exibida na visão:
