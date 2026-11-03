---
content_hash: fc4fabad31da6845f5c404f3fa4fe96f4a51bc921542681c70d5739828871bf0
fetched_at: '2026-06-29T00:08:45.813096+00:00'
page_id: '315899441'
product: rm
source: tdn-rm
title: 1625299 EDUCACIONAL01-3046 DT Avaliação Descritiva – Validações e Exclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315899441
version: 92
---

# AVALIAÇÃO DESCRITIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Avaliação Descritiva |
| **Situação/Requisito:** | Ao alterar o campo “Código da prova (Avaliação e pesquisa)”, no cadastro de Avaliações da Etapa,  o sistema não permitia caso existisse qualquer candidato cadastrado para esta prova no produto Totvs Avaliação e Pesquisa. |
| **Solução/Implementação:** | 1) Otimizações no Totvs Educacional:   - Ao alterar o cadastro de avaliação da etapa da turma/disciplina, será realizado a validação do campo “Código da prova (Avaliação e Pesquisa)”, somente se os candidatos da prova pertencerem à turma/disciplina da etapa. Não será permitido alterar o código da prova caso exista candidatos cadastrados nesta prova e que pertençam à turma/disciplina.    - Ao alterar o cadastro de avaliação da etapa da turma/disciplina, será realizado a validação do campo “Código da prova (Avaliação e Pesquisa)” e caso o candidato já tenha executado esta prova, não será permitido alterar o código da avaliação.    - No processo “Avaliação Descritiva” foi implementado opção para excluir o candidato da prova já cadastrada anteriormente. Ao escolher esta opção, o candidato será excluído tanto no Educacional (avaliação descritiva) quanto no Avaliação e Pesquisa (cadastro de candidato da prova)    2) Otimização no Totvs Avaliação e Pesquisa: no cadastro de candidato da prova, NÃO será permitido excluir o registro do candidato nas seguintes situações: - Status diferente de Pendente. - Caso o candidato pertença à uma Avaliação Descritiva do Totvs Educacional. Este candidato somente será excluído na tela do processo de Avaliação Descritiva do Totvs Educacional. - Caso o candidato pertença à uma Avaliação Institucional do Totvs Educacional. Este candidato somente será excluído na tela do processo de Avaliação Institucional do Totvs Educacional. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
