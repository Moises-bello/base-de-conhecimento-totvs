---
content_hash: c5b6ae95497902ca33680855df16d568415653534f6e6261e1c569860634d250
fetched_at: '2026-06-29T00:06:04.641664+00:00'
page_id: '200910048'
product: rm
source: tdn-rm
title: TSNLP6_DT_Alteracao_Situacao_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TSNLP6_DT_Alteracao_Situacao_Matricula
version: 3
---

# ALTERAÇÃO DE SITUAÇÃO DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Alteração de situação de matricula* |
| **Situação/Requisito:** | *Em situação de matrícula >> Status no período letivo >> Envio de email. Deparamo-nos com a seguinte situação: Ao parametrizar o sistema para quando o aluno assumir determinada situação de matrícula o sistema enviar email para esse aluno, mesmo o relatório contendo todos os filtros obrigatórios o sistema exibe a seguinte mensagem de erro ao fim do processo de alteração de situação de matrícula: Processo de Envio de Email. Houve erro ao enviar o email: Operand type clash: nvarchar is incompatible with image. Obs: O erro em questão ocorreu somente em base de dados SQL 2012.* |
| **Solução/Implementação:** | **Utilização do novo método que envia e-mail, onde o mesmo que estava sendo utilizado estava obsoleto.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.40 e 11.82.41* |
