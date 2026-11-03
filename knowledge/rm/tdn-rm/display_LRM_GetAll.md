---
content_hash: b79b223fa40f6041d3d94ff5557d8b0b7b62fe8182c2c583e2943b62badfcda8
fetched_at: '2026-06-29T00:05:59.441526+00:00'
page_id: '190518549'
product: rm
source: tdn-rm
title: GetAll
type: documentation
url: https://tdn.totvs.com/display/LRM/GetAll
version: 4
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

# GetAll

Retorna os registros do dataserver representado pelo identificador da URL {id}. Tal qual no método , no json retornado será acrescentado o campo id para cada registro. O registro inicial e a quantidade de registros a serem retornados podem ser definidos na url.

## Parametros

* start - Registro inicial a ser retornado. (padrão = "0")
* limit - Quantidade máxima de registros a serem retornados. (padrão = "0", retorna todos os registros)
* filter - Filtro para ser aplicado na leitura dos registros

## Exemplo de utilização

Método: GET

URL: <http://localhost:8051/rmsrestdataserver/rest/EstLOCData?start=3&limit=2>

### Resposta da requisição
