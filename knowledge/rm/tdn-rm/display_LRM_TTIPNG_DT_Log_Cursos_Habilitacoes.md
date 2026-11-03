---
content_hash: 926c7ddaab3965d40497c7dbe9df284c09f5b5fd87f7e69f89b308b37e0bb8f7
fetched_at: '2026-06-29T00:06:10.975030+00:00'
page_id: '203766334'
product: rm
source: tdn-rm
title: TTIPNG_DT_Log_Cursos_Habilitacoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIPNG_DT_Log_Cursos_Habilitacoes
version: 1
---

# LOG DO CADASTRO DE CURSOS / HABILITAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Log do cadastro de cursos / habilitações* |
| **Situação/Requisito:** | *O nome do campo motivo de alteração, ao marcar para exibir nome do campo, é mostrado como SHABILITACAOALUNO.NULL no cadastro de curso / habilitação. E o campo motivo de alteração referente ao campus é exibido SHABILITACAOALUNO.CODMOTIVO que está inconsistente, pois este log é gravado na SLOGCAMPUS.* |
| **Solução/Implementação:** | *Ajuste na exibição do campo Motivo de alteração referente ao cadastro do curso / habilitação, para que ao invés de exibir SHABILITACAOALUNO.NULL exibida SLOGHABILITACAOALUNO.CODMOTIVO que é a coluna correspondente a este campo. E ajuste na exibição do campo motivo de alteração também no cadastro do curso / habilitação, porém este campo é referente a alteração do campus. Onde a alteração consiste em exibir SLOGCAMPUS.CODMOTIVO ao invés de exibir SHABILITACAOALUNO.CODMOTIVO.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
