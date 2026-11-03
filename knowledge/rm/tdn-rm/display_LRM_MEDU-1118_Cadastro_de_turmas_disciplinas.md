---
content_hash: a2c5012651bc294c1b2c1304b229b50f50d5a95fa0622e504f0576d62c354348
fetched_at: '2026-06-29T00:08:23.174548+00:00'
page_id: '269450783'
product: rm
source: tdn-rm
title: MEDU-1118_Cadastro_de_turmas_disciplinas
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1118_Cadastro_de_turmas_disciplinas
version: 114
---

# CADASTRO DE TURMAS DISCIPLINAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cadastrar turmas disciplinas |
| **Situação/Requisito:** | Ao executar o processo de cadastro de turma/disciplinas sem ter um período letivo selecionado o sistema exibe uma mensagem de erro de referência de Objeto. |
| **Solução/Implementação:** | Quando a turma não estava associada a uma matriz aplicada, o sistema tentava fechar o form sem tê-lo aberto. Sistema continua emitindo a mensagem para o usuário de que a turma não possui matriz aplicada mas não tenta mais fechar o form. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
