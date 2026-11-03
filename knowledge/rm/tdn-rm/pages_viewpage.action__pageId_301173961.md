---
content_hash: 41e5db24e17136a8aba2776ce6b8bab91780738c38e968f68479ee4c234c1121
fetched_at: '2026-06-29T00:08:42.939868+00:00'
page_id: '301173961'
product: rm
source: tdn-rm
title: Limpar Log de Calculo dos Funcionários (PLOGFUNCIONARIO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301173961
version: 4
---

# **Foi identificado que existem mais de 10.000 registros na tabela PLOGFUNCIONARIO de sua base, por questão de performance na atualização recomendamos que sejam realizados os passos abaixo:**

### 1.Criação da tabela PLOGFUNCIONARIO\_TOTVS backup da tabela PLOGFUNCIONARIO.

CREATE TABLE PLOGFUNCIONARIO\_TOTVS

AS

SELECT EXECID,

             CHAPA,

             STATUS,

             TO\_LOB(MENSAGEMERRO) MENSAGEMERRO,

             RECCREATEDBY,

             RECCREATEDON,

             RECMODIFIEDBY,

             RECMODIFIEDON,

             CODCOLIGADA

FROM   PLOGFUNCIONARIO;

### 2. Realização da limpeza da tabela PLOGFUNCIONARIO.

TRUNCATE TABLE PLOGFUNCIONARIO;

### 3. Atualização da Base de Dados para a versão 12.1.18.

### 

### 4.\*Após finalizar a atualização é necessário restaurar os dados da tabela de backup PLOGFUNCIONARIO\_TOTVS para a tabela original PLOGFUNCIONARIO.

INSERT INTO PLOGFUNCIONARIO (EXECID,CHAPA,STATUS,CODCOLIGADA,RECCREATEDBY,RECCREATEDON,RECMODIFIEDBY,RECMODIFIEDON,MENSAGEMERRO) 

SELECT EXECID,CHAPA,STATUS,CODCOLIGADA,RECCREATEDBY,RECCREATEDON,RECMODIFIEDBY,RECMODIFIEDON,MENSAGEMERRO FROM PLOGFUNCIONARIO\_TOTVS;

### 5. Remove a tabela de backup PLOGFUNCIONARIO\_TOTVS.

DROP TABLE PLOGFUNCIONARIO\_TOTVS;

 

\* Recomendamos que no momento de restaurar os dados da tabela PLOGFUNCIONARIO\_TOTVS para a tabela PLOGFUNCIONARIO, seja realizado um filtro com o mínimo de registros necessários para sua operação, para que não exista perda de performance na aplicação.
