---
content_hash: 77fcfbb263c4b7d05ed5ce9e4d8555811d75b5318d67e6cb2ce6b35cb7aa0aab
fetched_at: '2026-06-29T00:08:26.296980+00:00'
page_id: '271172329'
product: rm
source: tdn-rm
title: 364938 MEDU-1991 DT Alteração de Situação de Matrícula Trancada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271172329
version: 111
---

# ALTERAÇÃO DE SITUAÇÃO DE MATRÍCULA TRANCADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Alteração de Situação de Matrícula Trancada* |
| **Situação/Requisito:** | *Ao tentar alterar a situação de matricula de um aluno de "TRANCADO" para "DESLIGADO" na versão 12.1.14 o sistema não está permitindo exibindo a mensagem que a situação da matrícula não pode ser alterada porque o aluno excedeu o número permitido de períodos trancados.* |
| **Solução/Implementação:** | *Ajuste na validação ao mudar uma situação de matrícula que indica trancamento para uma situação que não indica trancamento considerando o item "Aluno ativo" na validação. Ou seja, caso esteja alterando a situação de matrícula do período letivo de um status que indica trancamento para outro que não indica trancamento e possua o item "Aluno ativo" desmarcado a alteração é concluída, pois não é considerado como destrancamento da matrícula.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
