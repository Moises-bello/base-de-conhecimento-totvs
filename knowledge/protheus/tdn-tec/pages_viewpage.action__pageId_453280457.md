---
content_hash: 703df67872852177dde6f432b91320a4841599911e36de3b3ed094f231e8ed98
fetched_at: '2026-07-02T19:24:23.967520+00:00'
page_id: '453280457'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave AutoTranslate
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453280457
version: 1
---

Habilita o uso de **Auto Translate** para o SGBD **MS SQL Server**.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (**Padrão**) | Não usa Auto Translate |
| 1 | Habilita o Auto Translate |

## Observações

* A chave é específica para o SGBD **MS SQL Server**, não influenciando os demais SGBDs.
* Especificar a chave na seção [MSSQL] tem efeito sobre o valor default de todos os ambientes MSSQL configurados.
* Caso seja especificada dentro de uma seção de conexão MSSQL específica [MSSQL/ambiente], esta configuração será considerada sobre o default, para todas as conexões com esse ambiente.
* Essa chave é lida **somente** no DBAccess **Linux**.

## Exemplos

textfalse
