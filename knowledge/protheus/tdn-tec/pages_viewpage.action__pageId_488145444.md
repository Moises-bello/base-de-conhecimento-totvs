---
content_hash: 3579a5934d3783d135f9b7f65266b0dcece23733a04a5903eba503c4fd1da8b3
fetched_at: '2026-07-02T19:24:24.309677+00:00'
page_id: '488145444'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave UseLockInDB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=488145444
version: 4
---

Esta chave permite habilitar (ou desabilitar) o uso de lock nativo do banco de dados em processos transacionados  true.

| Valor | Descrição |
| --- | --- |
| 1 | Habilita o uso de locks (bloqueio de registros) nativos em transação no SGDB |
| 0 | Desabilita o uso de locks (bloqueio de registros) nativos em transação no SGDB |

## Observações

Esta configuração exerce influencia sobre os processo de:

* Bloqueio de registros para alteração -- dbrlock() , msrlock(), reclock() – dentro de um bloco transacionado em AdvPL
* Apenas os bancos de dados MSSQL, ORACLE e POSTGRES suportam este recurso

* Funcionalidade disponível a partir do DBAccess 20181212 Build 18.2.1.0, habilitada por default para os bancos MSSQL, ORACLE e POSTGRES.
* A partir do DBAccess Build 20191119, esta configuração por padrão está desabilitada.
