---
content_hash: 93bde69a584835be7c635fb8cd5ed4a366c147713f82f2e85741247d4100cce2
fetched_at: '2026-06-29T00:08:24.846642+00:00'
page_id: '270907375'
product: rm
source: tdn-rm
title: 292650_DT_Relatório_Retrospectiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270907375
version: 110
---

# Relatório Retrospectiva

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Retrospectiva |
| **Situação/Requisito:** | Ao realizar a emissão do relatório de Retrospectiva, quando a conta contábil contém 22 caracteres, o relatório corta a conta contábil e não emite o código da conta contábil toda, ou seja, o relatório corta a informação do código da conta contábil. |
| **Solução/Implementação:** | Ajuste na rotina que gera o relatório Retrospectiva para que as colunas que apresentam o código e a descrição da conta sejam gerados baseados nos tamanhos dos campos no seu tamanho máximo recuperado na consulta. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
