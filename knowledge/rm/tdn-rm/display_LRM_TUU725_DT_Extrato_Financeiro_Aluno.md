---
content_hash: 0f17c5d7dbecec2db4c313f4b12045968399607ece9b3440744317f601dc43aa
fetched_at: '2026-06-29T00:08:07.870481+00:00'
page_id: '237394087'
product: rm
source: tdn-rm
title: TUU725_DT_Extrato_Financeiro_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TUU725_DT_Extrato_Financeiro_Aluno
version: 117
---

# EXTRATO FINANCEIRO - PORTAL ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Extrato financeiro no portal do aluno.* |
| **Situação/Requisito:** | *Quando o aluno tinha um lançamento com duas baixas, sendo que uma baixa realizada com cheque, uma mensagem de erro era exibida ao acessar Extrato Financeiro no portal do aluno.* |
| **Solução/Implementação:** | *Ajuste na consulta SQL que retorna os detalhes dos lançamentos do aluno. A visão do extrato financeiro vai retornar os lançamentos do aluno, mesmo que tenha lançamentos com duas ou mais baixas e pelo menos uma baixa está vinculada ao cheque.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | **TUYNTA** |
| **Requisito (ISSUE):** | *N/A.* |

divs
