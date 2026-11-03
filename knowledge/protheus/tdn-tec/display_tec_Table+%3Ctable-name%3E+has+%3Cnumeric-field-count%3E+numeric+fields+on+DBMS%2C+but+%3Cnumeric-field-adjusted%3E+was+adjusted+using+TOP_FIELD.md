---
content_hash: 14d77b99c8b541b759ce1035aa303fecaebc1049ee87f0285ebd4f9167d5f1bb
fetched_at: '2026-07-02T19:24:24.293650+00:00'
page_id: '485856777'
product: protheus
source: tdn-tec
title: Table <table-name> has <numeric-field-count> numeric fields on DBMS, but <numeric-field-adjusted>
  was adjusted using TOP_FIELD
type: documentation
url: https://tdn.totvs.com/display/tec/Table+%3Ctable-name%3E+has+%3Cnumeric-field-count%3E+numeric+fields+on+DBMS%2C+but+%3Cnumeric-field-adjusted%3E+was+adjusted+using+TOP_FIELD
version: 1
---

INLINE

A mensagem é registrada quando a rotina de tratamento de campos numéricos identifica que a quantidade de campos numéricos ajustados com base na TOP\_FIELD difere da quantidade de campos numéricos na estrutura da tabela.

| Parâmetro | Descrição |
| --- | --- |
| <table-name> | Corresponde ao nome da tabela ajustada pela rotina de tratamento de campos numéricos |
| <numeric-field-count> | Corresponde a quantidade de campos numéricos identificados na estrutura da tabela <table-name> |
| <numeric-field-adjusted> | Corresponde a quantidade de campos numéricos ajustados com base na TOP\_FIELD |

## Causa

Dentre as causas possíveis temos:

* A criação direta/externa da tabela, ou seja, sem o uso das funções de integração com o banco de dados - Se true, sem o uso da função dbCreate()
* A manutenção direta/externa da tabela TOP\_FIELD - tabela interna de uso exclusivo do true
