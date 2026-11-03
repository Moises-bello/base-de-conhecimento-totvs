---
content_hash: ac5b412613c8fe8b04ff54c27d7c27df89f1a1ce8fe69d9b0e1ed5b4fb823737
fetched_at: '2026-06-29T00:08:45.597848+00:00'
page_id: '311632324'
product: rm
source: tdn-rm
title: Relacionamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Relacionamentos
version: 17
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona tela de Cadastro de Relacionamentos.

# Introdução:

---

       São utilizados para criar um relacionamento entre as [Entidades](http://tdn.totvs.com/x/viGTEg) criadas anteriormente.

       Os relacionamento são criados visando utilizá-los posteriormente, no [Design do Relatório](http://tdn.totvs.com/x/3yGTEg), para criar um relatório do tipo Mestre Detalhe, entre outros.   

# Como criar:

---

       Para criar um novo Relacionamento, basta clicar em "+ Novo" e informar os campos abaixo:

***Nome do relacionamento:***Informe o nome do relacionamento, deve ser um nome único e é por ele que o relacionamento será identificado.

***Entidade pai:*** Informe qual será a entidade pai, ou seja, a entidade mais forte.  (Ex: Funcionários)

***Entidade filha:*** Informe qual será a entidade filha, ou seja, a entidade que depende da pai. (Ex: Dependentes\_Funcionários)

***Colunas Entidade Pai:*** Selecione qual coluna será relacionada.

***Colunas Entidade Filha:*** Selecione qual coluna será relacionada.

***Adicionar Relação:*** Clique no botão para que a relação seja adicionada.

Para adicionar outras colunas à relação, selecione as colunas em "Colunas Entidade Pai" e "Colunas Entidade Filha" e clique em "Adicionar Relação".

***Exemplo prático abaixo:***

Caso deseje excluir a relação entre as colunas, basta clicar em "Remover"

# Utilizando uma conexão com um Provedor Integrado:

---

       Caso as Entidades selecionadas estejam vinculadas à um mesmo Provedor Integrado que possua informações de relacionamentos, os mesmos serão carregados automaticamente.

Para que o relacionamento automático seja retornado, é necessário que no cadastro de Entidades, todas as colunas que compõem a relação sejam selecionadas.

       Caso haja mais de um Relacionamento disponível entre as Entidades selecionadas, será exibido um combobox para selecionar o relacionamento desejado.

       Também é possível remover as relações carregadas automaticamente e selecionar as colunas manualmente.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Cadastro Relacionamentos

falsefalse

**Status:** Pendente

false

**Data:** 08/11/2017

false

**Autores:**
