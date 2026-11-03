---
content_hash: 9d5ce08587298ad279c7ff5b2fc38d99231a7f3e1aafec96e6aa0b410d006588
fetched_at: '2026-06-29T00:06:06.382737+00:00'
page_id: '201731079'
product: rm
source: tdn-rm
title: TTDOMU_DT_Alteracao_Situacao_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDOMU_DT_Alteracao_Situacao_Matricula
version: 1
---

# ALTERAÇÃO DE SITUAÇÃO DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Alteração de situação de matricula* |
| **Situação/Requisito:** | *Ao executar a alteração de matrícula do aluno (RA: 0000160; Período letivo: 2014/1; Situação Atual: Matriculado; Nova situação: Pré-matrícula) ocorre o seguinte erro:*  *- Processo de Envio de Email. Houve erro ao enviar o email: O índice estava fora do intervalo. Ele deve ser não-negativo e menor que o tamanho da coleção. Nome do parâmetro: index.*  *O erro acontece quando a situação de matrícula de destino (Pré-matrícula) está parametrizada para enviar e-mail e não possui nenhum relatório anexado.* |
| **Solução/Implementação:** | **Execução de teste para verificar se existe arquivo para ser anexado ao e-mail ao alterar-se a situação de matrícula.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.40.106 e 11.82.41* |
