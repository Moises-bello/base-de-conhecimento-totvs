---
content_hash: d6fd6486ca51cf0ef971afdc44156003d396ae2b4fdfafbb6c1a717f8d4277b2
fetched_at: '2026-06-29T00:09:07.554541+00:00'
page_id: '384577743'
product: rm
source: tdn-rm
title: 2273638 DT DEDUINTEGRACOES-2882 Lentidão no processo Matricular Aluno, em Cursos/Habilitações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384577743
version: 4
---

# Processo de Matricula

1550058179889\_1803255082

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Processo Matricula |
| **Situação/Requisito:** | Lentidão ao executar a tela do processo de matricula do aluno na visão Aluno>Anexo>Cursos/Habilitações>Processos>Matricular Aluno. |
| **Solução/Implementação:** | - Orientamos ao cliente a executar o comandos SQL CHECKTABLE e DBREINDEX no banco de dados nas tabelas envolvidas (FLAN, SBOLSA, SBOLSALAN, SPARCELA, FLANBOLETO, FBOLETO, SCONTRATO)  - Realizamos uma melhoria na execução da validação de inadimplentes na execução do processo de matricula para que a validação não seja executada quando o sistema não estiver parametrizado para bloquear matricula de alunos inadimplentes. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
