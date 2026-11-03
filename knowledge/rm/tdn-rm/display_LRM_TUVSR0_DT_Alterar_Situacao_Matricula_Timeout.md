---
content_hash: e85adaaa800a18c415ad6f08cc34b60e31249b8390976b62a78927166d206df2
fetched_at: '2026-06-29T00:08:07.177987+00:00'
page_id: '237373419'
product: rm
source: tdn-rm
title: TUVSR0_DT_Alterar_Situacao_Matricula_Timeout
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVSR0_DT_Alterar_Situacao_Matricula_Timeout
version: 121
---

# MATRÍCULA NO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Alterar Situação de Matrícula* |
| **Situação/Requisito:** | *Ao tentar alterar a situação de matrícula do aluno, após 2 minutos de execução do processo, o Sistema apresentou mensagem de timeout.* |
| **Solução/Implementação:** | *Ajuste na consulta que busca os lançamentos vencidos do aluno para melhorar sua performance.* |
| **Conversores e Parâmetros:** | *Educacional | Matrícula | Movimento 1/3 | Durante a matrícula: Bloquear matrícula para inadimplentes.*  *Educacional | Matrícula | Movimento 1/3 | Durante a matrícula: Bloquear matrícula apenas para inadimplentes na mesma modalidade.*  *Educacional | Tesouraria | Geral 1/2: Verificar débitos do aluno em outras coligadas.* |
| **Chamados relacionados:** | TUWWI8 |
| **Requisito (ISSUE):** | *N/A* |

divs
