---
content_hash: 6e7f460e261ff40d4820f930cc532bc99de05fbb312b600f3f8a836c3f284d8f
fetched_at: '2026-06-29T00:06:04.665514+00:00'
page_id: '200910224'
product: rm
source: tdn-rm
title: TTBDIY_DT_Alteracao_Situacao_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBDIY_DT_Alteracao_Situacao_Matricula
version: 1
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
| **Versões/Release:** | *12.1.7* |
