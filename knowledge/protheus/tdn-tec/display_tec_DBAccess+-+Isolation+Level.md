---
content_hash: 2d021cc27787c64307d0514dba5bfbe12c82ec058c8d3377c745b43b664be443
fetched_at: '2026-07-02T19:24:19.693452+00:00'
page_id: '243654263'
product: protheus
source: tdn-tec
title: DBAccess - Isolation Level
type: documentation
url: https://tdn.totvs.com/display/tec/DBAccess+-+Isolation+Level
version: 3
---

Nível de isolamento

Quando tratamos de banco de dados, o *isolation level* determina como as transações serão tratadas durante falhas e os efeitos colaterais durante acessos simultâneo aos dados.

## ISO

O padrão ISO, define quatro níveis de isolamento de transação:

1. Leitura não confirmada (*read uncommitted*)
2. Leitura confirmada (*read committed*)
3. Leitura repetida (*repeatable read*)
4. Serializável (*serializable*)

## Nível de isolamento adotado pela aplicação

Comportamento legado

Aplicações ISAM migradas tendem a adotar, assumir e esperar um nível mais baixo de isolamento.

O true foi construído de modo que uma aplicação legada, que somente acessavam dados de arquivos DBF (ISAM), pudessem utilizar um banco de dados relacional e, para isso, um nível mais baixo de isolamento é definido durante a conexão realizada entre o true e o banco de dados.

| Banco de Dados | Isolation level |
| --- | --- |
| IBM DB2 | READ UNCOMMITTED |
| IBM Informix | DIRTY READ |
| Microsoft SQL Server | READ UNCOMMITTED |
| MySQL | READ UNCOMMITTED |
| Oracle | READ COMMITTED |
| PostgreSQL | READ COMMITTED |
| Sybase | READ UNCOMMITTED |
