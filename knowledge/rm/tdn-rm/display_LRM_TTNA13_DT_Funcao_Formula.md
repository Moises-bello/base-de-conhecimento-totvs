---
content_hash: 24925a97e8f32972d765a1612c67b0961f6e4a48b6042485eeffe4208afd8fa2
fetched_at: '2026-06-29T00:08:13.541937+00:00'
page_id: '244425789'
product: rm
source: tdn-rm
title: TTNA13_DT_Funcao_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNA13_DT_Funcao_Formula
version: 116
---

# FUNÇÃO FÓRMULA - GRAVACAMPOPL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Função de fórmula - GravaCampoPL.* |
| **Situação/Requisito:** | *Ao utilizar a função de fórmula GravaCampoPL para alterar o CODSTATUSRES, caso o aluno estivesse inadimplente na Biblioteca e o sistema estivesse parametrizado para realizar o bloqueio da alteração de situação de matrícula para alunos com inadimplência na Biblioteca, a fórmula não era executada e impedia que fosse informado um resultado final para o aluno.* |
| **Solução/Implementação:** | *Ajuste na função de fórmula GravaCampoPL para que não realize a validação de débitos na biblioteca quando a fórmula for chamada para alterar os campos CODSTATUSRES e CR. Para as demais alterações(CODSTATUS, PERIODO, CODTURMA) a função continuará validando a inadimplência com a Biblioteca.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TVIDVG.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
