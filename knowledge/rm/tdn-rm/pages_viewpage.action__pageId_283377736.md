---
content_hash: 4bc0d3c5ab989a148436d88356f7e6fabedf84a224bff70a2f39151fe8538331
fetched_at: '2026-06-29T00:08:35.640852+00:00'
page_id: '283377736'
product: rm
source: tdn-rm
title: 858240 CONTROLADORIA01-250 DT Conversor de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=283377736
version: 106
---

# Conversor de Cálculo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Conversor de Cálculo |
| **Situação/Requisito:** | Ao iniciar o processo de Conversão do Cálculo do TOTVS Gestão Patrimonial o sistema apresenta uma mensagem de inconsistência. |
| **Solução/Implementação:** | A tabela ALL\_INDEXES não estava retornado um índice existente na base de dados, gerando uma inconsistência durante a execução do conversor de cálculo do módulo patrimonial. Para que a execução fosse realizada com sucesso foi necessário consultar a existência do índice na tabela ALL\_OBJECTS. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
