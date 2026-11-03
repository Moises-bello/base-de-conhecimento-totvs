---
content_hash: b19a6de9d8df62e4a64dc452314706e89ec1dc607025a13b33ecea0018c39257
fetched_at: '2026-06-29T00:09:08.974787+00:00'
page_id: '390408125'
product: rm
source: tdn-rm
title: 3348642 PORTALMOBILE01-5183 DT Obrigatoriedade de matrícula em subturmas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390408125
version: 1
---

# Obrigatoriedade de matrícula em SubTurmas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Educacional |
| **Módulo:** | Educacional |
| **Função:** | Matrícula Online |
| **Situação/Requisito:** | Quando a matrícula online do Corpore.Net está parametrizada em "Portal - Matrícula / Geral 5/5 > Matricular em Sub Turmas"  como "Permitido com obrigatoriedade de seleção", e a situação de matrícula do aluno bloqueia a exclusão de disciplinas durante a matrícula, em casos que o aluno ainda não estava matriculado em uma Subturma, o portal exibia as disciplinas que possuíam subturmas, e selecionavam automaticamente a primeira subturma disponível. Não permitindo que o aluno fizesse alteração ou exclusão, podendo ocorrer erros de choque de horário, impedindo a matrícula. |
| **Solução/Implementação:** | Quando o aluno visualizar as disciplinas disponíveis durante a matrícula, a seleção da subturma irá refletir com as disciplinas já matriculadas. Se em uma turma/disciplina o aluno já estiver em uma subturma, a matrícula online irá exibir o combobox de Subturma já preenchida.  Caso contrário, o aluno não terá selecionado a subturma, mantendo-se desabilitada respeitando a parametrização para não permitir exclusão de disciplina. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
