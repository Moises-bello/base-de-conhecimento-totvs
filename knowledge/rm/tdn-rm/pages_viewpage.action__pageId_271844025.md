---
content_hash: 1717439e9517c940a50292ee4c04ebb4e8d374ecf5ac9676219ca18078bce4d5
fetched_at: '2026-06-29T00:08:28.681927+00:00'
page_id: '271844025'
product: rm
source: tdn-rm
title: 120845 MRH-3109 DT Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271844025
version: 112
---

# FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Analítica* |
| **Situação/Requisito:** | Ao gerar o relatório Folha Analítica pela MDI considerando funcionário com eventos zerados no envelope, o registro do funcionário é apresentado no relatório. Porém ao gerar o relatório em Delphi pelo módulo executável RM Labore o registro do funcionário com valores zerados no envelope não é considerado. |
| **Solução/Implementação:** | Ajuste ao gerar o relatório da Folha Analítica, para não considerar funcionário com eventos zerados no envelope,para que seja considerado a opção "Imprimir funcionários sem movimentação" deve estar marcada. |
| **Tickets relacionados:** | * [120845](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22120845%22 "120845") |

divs
