---
content_hash: 7d1ddf77e0922c7c14160fb6276772160fd02723d8a856e61a307d62419cad55
fetched_at: '2026-06-29T00:09:04.094327+00:00'
page_id: '382547543'
product: rm
source: tdn-rm
title: 3301375 FINANCEIRO01-7956 Contabilização baixa com rateio por centro de custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382547543
version: 1
---

# Exibição de contabilização de baixa do lançamento com rateio por centro de custo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Contabilização da Baixa. |
| **Situação/Requisito:** | Percentual de rateio por centro de custo gerado pela contabilização (por evento) é diferente do percentual para o mesmo rateio do lançamento. Isso porque o valor gerado pela contabilização, diferentemente do valor do rateio do lançamento, não está arredondado. Na exibição da tela é feita carga dos dados da Natureza Orçamentária Financeira do rateio da contabilização de baixa de acordo com o rateio do Lançamento, e nesse processo ocorria o problema de referência à variável de memória inexistente. |
| **Solução/Implementação:** | Ao comparar os percentuais, do rateio gerado pela contabilização e do lançamento, os valores são arrondados antes. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 3301375. |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
