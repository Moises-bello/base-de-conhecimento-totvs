---
content_hash: d3d099c168ba62382928a0be8829f4180cc4120844062a84e5b1f58fb897ec49
fetched_at: '2026-06-29T00:08:06.015208+00:00'
page_id: '236427379'
product: rm
source: tdn-rm
title: TUDOPH_DT_Template de Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDOPH_DT_Template+de+Acordo
version: 117
---

# Template de Acordo

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeria* |
| **Função:** | Template de Acordo |
| **Situação/Requisito:** | O Template de Acordo na Aba de Regras, no campo Quantidade máxima por parcela está parametrizado como 0, ao gerar o acordo com 3 parcelas o sistema apresenta o seginte erro:  Não é possível concluir o processo de geração de acordo porque a quantidade 3 de parcelas informada é superior a quantidade parametrizada no template 3-1 do acordo. |
| **Solução/Implementação:** | Criado validação no processo de geração de Acordo para o parâmetro "Quantidade máxima de parcelas" seja tratado da seguinte forma:   * Vazio: Aceita qualquer número de parcelas; * Diferente de vazio (incluindo zero): Será validado a quantidade máxima parametrizada contra a quantidade informada no acordo. |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | FIN000287 |

divs
