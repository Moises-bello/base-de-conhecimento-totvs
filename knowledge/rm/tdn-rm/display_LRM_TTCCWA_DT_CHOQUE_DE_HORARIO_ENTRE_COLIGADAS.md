---
content_hash: 10de5e312b9048b139015fb9e6289e1ee610340c57ae8ec181de899588b43a14
fetched_at: '2026-06-29T00:06:05.541355+00:00'
page_id: '201723999'
product: rm
source: tdn-rm
title: TTCCWA_DT_CHOQUE_DE_HORARIO_ENTRE_COLIGADAS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCCWA_DT_CHOQUE_DE_HORARIO_ENTRE_COLIGADAS
version: 1
---

# CHOQUE DE HORARIO ENTRE COLIGADAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | *Educacional* |
| **Função:** | *Choque de horario entre coligadas* |
| **Situação/Requisito:** | *Ao tentar realizar o processo de matricula em disciplinas o sistem está validando o choque de horario, mas em alguns momentos não valida. Caso o horario esteja com a mesma data da turma disciplina o sistema está permitindo o choque de horario mesmo não possuindo permissão. Se estiver sem data, exibe o choque.* |
| **Solução/Implementação:** | *A validação do componente responsavel pela exibição dos horarios selecionados, estava considerando a coluna CODHORARIO, enquanto que para validar o choque de horario entre cologadas, ê necessario que seja utilizado as datas e horario inicio e fim.* |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *12.1.7* |
