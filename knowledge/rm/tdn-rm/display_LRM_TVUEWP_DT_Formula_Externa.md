---
content_hash: 6d9b73a9298021da0f44e0136dd522c75b02a9627a89ac45b38d638a116732f4
fetched_at: '2026-06-29T00:08:18.503288+00:00'
page_id: '263194090'
product: rm
source: tdn-rm
title: TVUEWP_DT_Formula_Externa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUEWP_DT_Formula_Externa
version: 115
---

# FÓRMULA EXTERNA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Fórmula Externa |
| **Situação/Requisito:** | Ao buscar uma fórmula do TOTVS Folha de Pagamento para definir os valores dos benefícios, usando a função FOREXTERNA o sistema não entende, somente se a fórmula vinculada retornar um valor fixo e não utilizar nenhuma função do sistema externo. |
| **Solução/Implementação:** | Realizado ajuste na execução de Fórmula Externa de forma a utilizarmos o serviço do sistema Folha de Pagamento quando a fórmula a ser executada pertencer a este sistema. Caso contrário continuaremos a utilizar o serviço da Lib. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVUEWP |
| **Requisito (ISSUE):** |  |

divs
