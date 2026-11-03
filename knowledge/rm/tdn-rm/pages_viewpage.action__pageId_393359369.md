---
content_hash: 356419f627ccfd8f58e9778b49573145aa36c4d3542fa9c5534973a23e49fa7c
fetched_at: '2026-06-29T00:09:09.292846+00:00'
page_id: '393359369'
product: rm
source: tdn-rm
title: 3398466 DT EDUCACIONAL01-6169 Fórmula Visual executada no CRM para matricular
  em disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393359369
version: 2
---

# FÓRMULA VISUAL EM SOLICITAÇÕES DO EDUCACIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Solicitações de Atendimento |
| **Situação/Requisito:** | No Totvs Gestão de Relacionamento com o Cliente, ao avançar etapa de um atendimento gerado pelo Educacional, a fórmula visual utilizada para matricular em disciplina apresentava incorretamente mensagem de erro:  "A matriz aplicada e/ou matriz curricular esta inativa. A matrícula não pode ser realizada para o curso selecionado porque sua matriz curricular e/ou aplicada não está ativa". |
| **Solução/Implementação:** | Otimizado a execução de fórmula visual para matricular em disciplina, onde a mesma contenha a atividade “rmsAddTableRowActivity” utilizando a tabela “SMATRICULA”. Deverá ser preenchido a propriedade “Nível de Ensino” com o campo "CODTIPOCURSO" da estrutura. Por exemplo: Activity=rmsForEachActivity1, Path=Fields["CODTIPOCURSO"].AsInteger. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
