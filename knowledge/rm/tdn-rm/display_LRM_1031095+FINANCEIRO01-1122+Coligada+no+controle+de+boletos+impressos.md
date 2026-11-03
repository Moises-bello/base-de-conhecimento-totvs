---
content_hash: 8729b0e58e6054cc32531efb5ba4d0438db47f39ad25f2ab5025da4a71b28639
fetched_at: '2026-06-29T00:08:43.039116+00:00'
page_id: '301184981'
product: rm
source: tdn-rm
title: 1031095 FINANCEIRO01-1122 Coligada no controle de boletos impressos
type: documentation
url: https://tdn.totvs.com/display/LRM/1031095+FINANCEIRO01-1122+Coligada+no+controle+de+boletos+impressos
version: 97
---

# ARMAZENAMENTO DE COLIGADA NO CONTROLE DE BOLETOS IMPRESSOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Controle de boletos impressos. |
| **Situação/Requisito:** | Existia na tabela que armazena os boletos impressos registros com o campo Coligada no valor zero. Ao executar a rotina **Remoção dos Boletos impressos** somente os registros da coligada corrente eram excluídos. |
| **Solução/Implementação:** | Os registros de boletos impressos serão criados sempre com o campo Coligada no valor corrente mesmo que o relatório executado seja global (visível em todas as coligadas). Ao executar o processo de exclusão dos registros, além daqueles da coligada corrente, também serão excluídos os que possuem coligada zero (registros antigos criados antes dessa alteração). |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1031095 |
| **Requisito:** | FINANCEIRO01-1122. |

divs
