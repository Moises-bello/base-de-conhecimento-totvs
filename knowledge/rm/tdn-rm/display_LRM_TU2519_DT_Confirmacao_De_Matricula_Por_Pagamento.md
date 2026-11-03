---
content_hash: 70f2e6cd8032f5975d390f346e162da0e66306fae778e72cadc467dacb0faa82
fetched_at: '2026-06-29T00:06:24.060183+00:00'
page_id: '224111209'
product: rm
source: tdn-rm
title: TU2519_DT_Confirmacao_De_Matricula_Por_Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TU2519_DT_Confirmacao_De_Matricula_Por_Pagamento
version: 119
---

# MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Confirmação de matrícula por pagamento* |
| **Situação/Requisito:** | *1) O log exibido ao final da execução do processo está incorreto. Ele informa que a mesma matrícula de um aluno foi confirmada e não confirmada.*  *2) Quando a opção "verificar comportamento de inadimplência da bolsa de crédito" está marcado e aluno não possui bolsa de crédito, os lançamentos não baixados não estão sendo verificados.* |
| **Solução/Implementação:** | *Alterado processo de confirmação de matrícula por pagamento para que os lançamentos vencidos sejam verificados mesmo quando não existir bolsa para o aluno.* |
| **Conversores e Parâmetros:** | *Educacional | Matrícula | Bloquear mudança de situação de matrícula para inadimplentes* |
| **Chamados relacionados:** | *TUEHUR* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *11.82.42.116*  *12.1.10* |

divs
