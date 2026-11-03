---
content_hash: 9422ab437367f7b69e4b66469e93bdbab9e7bb0d17b9ca9c01a2c41ad139976e
fetched_at: '2026-06-29T00:10:51.518628+00:00'
page_id: '568925872'
product: rm
source: tdn-rm
title: Balancete (Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568925872
version: 6
---

Através desse layout é possível extrair dados da contabilidade, de uma empresa ou organização, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

| ID | Formato | Tamanho | Dec | Descrição | Origem de dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 200 |  | Código da Conta contábil | Conta presente nas partidas existentes nos lançamentos contábeis. |  |
| 2 | Alfanumérico | 25 |  | Empresa | Código da coligada que deu origem ao lançamento contábil. |  |
| 3 | Data |  |  | Data de Início da extração | Data inicial do período em que a auditoria está sendo realizada. |  |
| 4 | Data |  |  | Data Fim da extração | Data final do período em que a auditoria está sendo realizada. |  |
| 5 | Alfanumérico | 25 |  | Ano Fiscal | Não aderente ao RM. |  |
| 6 | Alfanumérico | 25 |  | Período Fiscal | Não aderente ao RM. |  |
| 7 | Decimal |  | 2 | Saldo inicial na moeda funcional | Saldo anterior da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 8 | Decimal |  | 2 | Saldo final na moeda funcional | Saldo atual da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 9 | Alfanumérico | 25 |  | Código da Moeda Funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 10 | Decimal |  | 2 | Saldo inicial na moeda de apresentação | Saldo anterior da segunda moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 11 | Decimal |  | 2 | Saldo final na moeda de apresentação | Saldo atual da segunda moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 12 | Alfanumérico | 25 |  | Código da Moeda de apresentação | Moeda do segundo valor existente nos parâmetros do modulo contábil. |  |
