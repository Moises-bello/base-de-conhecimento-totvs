---
content_hash: 8797333363118a23b62618c4c036eb25a3023e65b7e747531e147ef09a89fb74
fetched_at: '2026-06-29T00:06:17.758034+00:00'
page_id: '213984886'
product: rm
source: tdn-rm
title: TTDKUR_DT_FUNCAO_FORMULA_VFER
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDKUR_DT_FUNCAO_FORMULA_VFER
version: 1
---

# Fórmula

|  |  |
| --- | --- |
| **Linha de Produto:** | *Construção e Projetos* |
| **Segmento:** | *RM.* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Execução da Função de Fórmula VFER* |
| **Situação/Requisito:** | A função de fórmula VFER no Delphi não estava considerando o período aquisitivo em aberto, e por isso estava obtendo mais período aquisitivo e buscando no recibo de férias que não era do período aquisitivo em aberto. E .Net busca somente no período aquisitivo em aberto. |
| **Solução/Implementação:** | Atualizado a função de fórmula VFER em delphi para considerar somente o período aquisitivo em aberto para retornar o valor do evento do respectivo recibo de férias. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDKUR.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
