---
content_hash: 0015daeb1d293b7f870af15a71010680a8464a76faff75b8c048b7aa0416307c
fetched_at: '2026-06-29T00:09:10.654726+00:00'
page_id: '403046417'
product: rm
source: tdn-rm
title: 1304955 FOPCALCULO01-1012 DT Rescisão Coletiva Componente de Calendário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403046417
version: 79
---

# Rescisão Coletiva

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Rescisão Coletiva |
| **Situação/Requisito:** | No processo de rescisão coletiva ao selecionar através do calendário uma data correspondente ao último dia da competência, o sistema informada erro alertando que a data da rescisão não poderia ser maior que o último dia da competência. |
| **Solução/Implementação:** | Foi feito um ajuste na validação da data da rescisão pois o sistema estava considerando a hora, assim divergindo da data da competência que não utiliza hora. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 1304955 |

divs
