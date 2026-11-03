---
content_hash: 3f32aa713821afba2931c4fe3908211d09ac863b9c8ecf281c75c59610c896c0
fetched_at: '2026-06-29T00:08:52.642172+00:00'
page_id: '342297139'
product: rm
source: tdn-rm
title: 2302117 EDUCACIONAL01-4179 DT Preparação de Dados para o Censo da Educação
  Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342297139
version: 2
---

# PREPARAÇÃO DE DADOS PARA O CENSO DA EDUCAÇÃO SUPERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Ao rodar o assistente para este curso em específico, o sistema emite o erro "String or binary data would be truncated." |
| **Solução/Implementação:** | Foi verificado que o tamanho do campo de curso de origem do Censo está menor do que deveria. O campo está com 8 posições ao invés de 12.  Foi criado um script para alterar o tamanho do campo de curso de origem do Censo Superior para 12 posições. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
