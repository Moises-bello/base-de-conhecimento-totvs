---
content_hash: f0793b9d1d6e9f8cae9a5c36423e8db98f91127fe3eb68f40b964094874df3d2
fetched_at: '2026-06-29T00:06:08.129167+00:00'
page_id: '201746631'
product: rm
source: tdn-rm
title: GetAll - Exemplo de utilização do filtro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201746631
version: 13
---

Versão

 Disponível à partir da versão 12.1.8 da linha RM.

# GetAll com filtro

Retorna os registros do dataserver representado pelo identificador da URL {id}. Tal qual no método , no json retornado será acrescentado o campo id para cada registro. O registro inicial,a quantidade de registros a serem retornados, e um filtro podem ser definidos na url.

## Parâmetros

* start - Registro inicial a ser retornado. (padrão = "0")
* limit - Quantidade máxima de registros a serem retornados. (padrão = "0", retorna todos os registros)
* filter - Filtro para ser aplicado na leitura dos registros. (padrão = não possui filtro padrão)

## Regras para utilização do filtro

Para montar o parâmetro "filter" devemos obedecer as seguintes regras:

* + O objeto filter deve ser um array.
  + O índice 0(zero) desse array deve ser o schema do filtro, o schema segue o mesmo padrão já adotado na lib (CODCOLIGADA =:CODCOLIGADA)
  + O índice 0(zero) não aceita comandos : DLL, DML, DCL, TCL (create,alter,truncate,comment,rename,select,insert,update,delete,call,explain plan,lock table,grant,revoke,commit,savepoint,rollback,'," )
  + Para cada parâmetro adicionado schema do filtro, deverá ser um novo registro no array com o respectivo valor.
  + É extremamente necessário serilizar o filtro em json antes de fazer a chamada.

Para a montagem de um filtro com mais de um parâmetro siga esses passos:

**[...] filter =**  **["NOME\_DO\_CAMPO\_1 = :NOME\_DO\_PARAMETRO\_1 (AND/OR) **NOME\_DO\_CAMPO\_2 = :NOME\_DO\_PARAMETRO\_2 **(AND/OR) **NOME\_DO\_CAMPO\_N = :NOME\_DO\_PARAMETRO\_N"****, "VALOR\_1", "VALOR\_2", "VALOR\_3"]****

## Exemplo (Filtro Único)

Método: GET

Parâmetros Utilizados:

* start = 3;
* limit = 2;
* filter = ["CODCOLIGADA =:codcoligada", "1"];

URL: <http://localhost:8051/rmsrestdataserver/rest/EstLOCData?start=3&limit=2&filter=%5B%22CODCOLIGADA+%3D+:CODCOLIGADA%22>

js1Resposta (Filtro Único)truetrue

## Exemplo (Filtro com mais de um Parâmetro)

         Iremos utilizar o mesmo dataserver (EstLOCData) como exemplo, porém iremos utilizar os seguintes parâmetros:

**OBS:** Observe que vamos utilizar três filtros, em vez de um, como no exemplo anterior.

Método: GET

Parâmetros Utilzados:

* start = 0;
* limit = 5;
* filter = ["CODCOLIGADA =:codcoligada AND CODLOC =:codloc AND CODFILIAL =:codfilial", "1", "01", "1"]

URL: <http://localhost:8051/rmsrestdataserver/rest/EstLOCData?start=0&limit=5&filter=%5B%22CODCOLIGADA%20%3D%3Acodcoligada%20AND%20CODLOC%20%3D%3Acodloc%20AND%20CODFILIAL%20%3D%3Acodfilial%22%2C%20%221%22%2C%20%2201%22%2C%20%221%22%5D>

js1Resposta (Filtro com mais de um Parâmetro)truetrue

## Exemplo (Filtro com Like)

Iremos utilizar o mesmo dataserver (EstLOCData) como exemplo, porém iremos utilizar os seguintes parâmetros:

Método: GET

Parâmetros Utilzados:

* filter = ["NOME LIKE :NOME", "%SAO PAULO%"]

URL: http://localhost:8051/rmsrestdataserver/rest/EstLOCData?filter=%5B%22NOME%20LIKE%20%3ANOME%22%2C%20%22%25SAO%20PAULO%25%22%5D

js1Resposta (Filtro com Like)truetrue

## Exemplo (Implementação em Código)

1. Adicione os disclaimers que desejar:

* Crie o schema do filtro e adicione os respectivos valores.
* Na chamada do findRecords, o parâmetro filter deve ser serializado em JSON.

       3. A segunda opção pode ser substituída por essa:
