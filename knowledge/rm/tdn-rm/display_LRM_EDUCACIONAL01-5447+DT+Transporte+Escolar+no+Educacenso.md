---
content_hash: 3a5d3406c8837f0f21f5c2b94ae66d9f1036b3ef1af43edc2e11bbbf0bb56b7c
fetched_at: '2026-06-29T00:09:01.209914+00:00'
page_id: '372557041'
product: rm
source: tdn-rm
title: EDUCACIONAL01-5447 DT Transporte Escolar no Educacenso
type: documentation
url: https://tdn.totvs.com/display/LRM/EDUCACIONAL01-5447+DT+Transporte+Escolar+no+Educacenso
version: 1
---

# TRANSPORTE ESCOLAR NO EDUCACENSO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Censo da Educação Básica |
| **Situação/Requisito:** | Ao informar que o aluno utiliza transporte escolar, o sistema está gerando errado as informações de veículo utilizado no transporte escolar. Os campos estão aparecendo vazio e deveriam estar com valor 0 (zero). |
| **Solução/Implementação:** | A consulta 80 do Educacenso foi alterada para verificar se os registros de tipo de veículo utilizado no transporte escolar (campos 13 a 23) estão nulos e retornar 0 quando o aluno utilizar transporte escolar (campo 11 = 1) |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
