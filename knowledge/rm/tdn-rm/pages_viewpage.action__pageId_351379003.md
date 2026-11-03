---
content_hash: 2581a334fa7af1e6485d7daa9f0776c8809aa7bd3341c533855e188db0fc9e95
fetched_at: '2026-06-29T00:08:56.527790+00:00'
page_id: '351379003'
product: rm
source: tdn-rm
title: 2603002 EDUCACIONAL01-4585 DT Transferência Interna no Censo da Educação Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351379003
version: 1
---

# TRANSFERÊNCIA INTERNA NO CENSO DA EDUCAÇÃO SUPERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Ao enviar o arquivo do censo para o portal do INEP, é retornada a mensagem: códigos dos cursos de ‘origem’ e ‘destino’ não podem ser iguais. No caso, essa situação é observada com os alunos que realizaram troca de turma/turno. Nessa situação, o código do curso do MEC é o mesmo para todas as matrizes aplicadas do curso. |
| **Solução/Implementação:** | A rotina de geração dos dados do Censo foi alterada para não gravar o ID do curso de origem para as transferências que não envolvam mudança do curso do MEC. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
