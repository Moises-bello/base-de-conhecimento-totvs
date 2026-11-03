---
content_hash: 777b5cb37b230e28e6958e7f1871f55f96b1e2486bd29527563262a649110161
fetched_at: '2026-06-29T00:10:15.161366+00:00'
page_id: '463820499'
product: rm
source: tdn-rm
title: Utilizando a Atividade  "Criar Coluna" com loop em fonte de dados da atividade.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463820499
version: 3
---

# Sumário

---

Sumário

# Objetivo

---

     Esse documento tem por objetivo demonstrar como utilizar a atividade "Criar Coluna", utilizando o loop na fonte de dados da atividade "Localizar Registro na Tabela".

# Introdução

---

**Inserir duas atividades de "Criar Coluna"**

* A propriedade "Nome da Coluna" serve para definir o nome da nova coluna a ser criada.
* A propriedade "Tabela" refere a tabela que estamos na visão (no caso tabela GUSUARIO).
* A propriedade "Tipo" diz a respeito do tipo de campo que será a coluna (string/int/decimal...).

     As colunas a serem adicionadas na visão de Usuários são: **\_UserId** e **\_UserIDFluigIdentity,** onde o tipo das duas colunas serão **System.String**.

**Inserir a atividade "Executar Consulta SQL"**

* É necessário fazer uma Consulta SQL que retorne as chaves da tabela que diferenciarão os registros e os campos que serão utilizados. Neste exemplo a consulta retornará o código do usuário e as colunas userId e useridfluigidentity. (select CODUSUARIO,userid as \_UserID ,useridfluigidentity as \_UserIDFluigIdentity from gusuario).

  Atenção

  É muito importante saber os nomes das colunas que serão utilizadas, pois eles podem sobrescrever uma coluna que já existe na visão.

  Neste caso as colunas foram renomeadas com um \_ na frente das colunas para que seja possível identificar que esta coluna está sendo criada por uma Fórmula Visual.

    **Insira a atividade "Localizar Registro na Tabela"**

* A atividade de FindRecord (Localizar registro na tabela).

     **Configuração do FindRecord:**

* A ligação deve ser feita pela chave primária da consulta SQL para que não encontre mais de um registro.
* **Tabela:**Neste exemplo, a tabela de referência é o resultado da consulta SQL. (Activity=rmsConsSQLActivity1, Path=Tables[0].DataTable)
* ****Utilizar**Atividade como Fonte de Dados:**Esta propriedade informa se a atividade irá utilizar o loop interno da própria atividade: **True**.
* **KeyFields:** Não é necessário preencher quando a propriedade "****Utilizar**Atividade como Fonte de Dados**" estiver como True.
* **Lista de Items:** Onde será executado o loop interno. Neste caso na visão (Activity=RMSWorkflow, Path=Tables["GUSUARIO"].DataTable)
* **Pesquisar Por:** Campos que serão usados para pesquisar a referência dos registros. (CODUSUARIO)
* **Valor Calculado:** Campos que serão preenchidos na Lista de Items, onde os valores serão extraídos da fonte de dados Tabela. (\_UserID,\_UserIDFluigIdentity)

  Atenção

  É necessário que na consulta SQL referenciada à tabela contenha os campos Pesquisar Por e Valor Calculado.

  O Campo Pesquisar Por será utilizado para pesquisar as referências dos registros e saber qual registro aqueles valores irão pertencer.

  O Campo Valor Calculado será a referência da Coluna criada na visão para o retorno da consulta SQL inserida na propriedade Tabela, onde os valores serão inseridos na visão.

   

 **Configurando o Gatilho:**

**Resultado**

* Ao abrir a tela de Usuários, as colunas \_UserId e \_UserIDFluigIdentity serão exibidas na visão com os devidos valores retornados na consulta SQL.
