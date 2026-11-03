---
content_hash: c0c83426ae517e6a48d55cbc970d9dac71910ed384cbc7a1b4d5acf0dbf28f10
fetched_at: '2026-06-29T00:09:12.932324+00:00'
page_id: '418677888'
product: rm
source: tdn-rm
title: 4029849 EDUCACIONAL01-6657 DT Provas da Avaliação Descritiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=418677888
version: 2
---

# PROVAS DA AVALIAÇÃO DESCRITIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Processo - Avaliação Descritiva |
| **Situação/Requisito:** | Quando se tenta avançar de etapa de seleção de prova para a etapa de vínculo de aluno, a seguinte mensagem é apresentada: "Failed to enable constraints. One or more rows contain values violating non-null, unique, or foreign-key constraints." |
| **Solução/Implementação:** | Alteração na avaliação descritiva para aceitar registros que possuam a descrição da prova com tamanho maior que 60 caracteres e não aparecer a mensagem de erro: "Failed to enable constraints. One or more rows contain values violating non-null, unique, or foreign-key constraints." |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
