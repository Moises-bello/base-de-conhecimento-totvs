---
content_hash: 102f452c40d06f14deeda51a0bec0424a23374f634a86bbe0b3a71ccbcbf70ee
fetched_at: '2026-06-29T00:06:04.072775+00:00'
page_id: '200905272'
product: rm
source: tdn-rm
title: TSKMP0_DT_Inclusão_Previsão_Financeira_Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200905272
version: 2
---

# Inclusão Previsão Financeira Contrato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Inclusão de Previsão Financeira no Contrato |
| **Situação/Requisito:** | Ao faturar o contrato, as previsões financeiras geradas não eram excluídas automaticamente. |
| **Solução/Implementação:** | O problema estava ocorrendo porque as previsões financeiras estavam sendo geradas com a data diferente do faturamento. Ai no momento do faturamento, o sistema não conseguia excluir a previsão prevista porque as datas não coincidiam. Foi feito uma melhoria na geração das previsões financeiras para corrigir o problema. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 11.82.41 |
