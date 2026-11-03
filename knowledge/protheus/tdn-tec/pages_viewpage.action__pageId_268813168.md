---
content_hash: 9d3d1f0ef8de9fc7b898cdd936454a771b2a6183c174cca2d17c76916eb10e15
fetched_at: '2026-07-02T19:24:21.634914+00:00'
page_id: '268813168'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave ODBCConnectionPool
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268813168
version: 2
---

Informa ao ODBC Manager que um pool de conexões para este SGBD pode ser utilizado pela aplicaçãotrue

A informação contida neste documento aplica-se ao true, build 42.201410119 e superiores.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita (padrão) |
| 1 | Habilita pooling de conexão ODBC |

## Informações Adicionais

* Esta configuração somente será considerada caso o true estiver configurado para mapear as funções de ODBC da API 3.0 ou superior.
* Este recurso é habilitado mediante a inserção da chave ODBC30=1 na seção [general] do arquivo de configuração dbaccess.ini. Para informações sobre esta configuração, veja a documentação no link
* O recurso de Connection Pooling é disponibilizado pelo ODBC Manager do Sistema Operacional. Caso o Driver em uso pelo Banco de Dados não possua suporte a este recurso, o comportamento do true permanecerá inalterado.

## Exemplo
