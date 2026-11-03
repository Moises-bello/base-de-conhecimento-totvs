---
content_hash: 28bc6ecac9708ea2df5162d2a6b278347327216837937bf2fe5ebc0f443904e9
fetched_at: '2026-06-29T00:08:07.788676+00:00'
page_id: '237390257'
product: rm
source: tdn-rm
title: TTIVA9_DT_Lançamento_Cálculo_do_Valor_Líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237390257
version: 118
---

# Lançamento - Cálculo do Valor Líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Lançamento - Cálculo do Valor Líquido |
| **Situação/Requisito:** | Alterar parametro para calculo automático de valor líquido na visão de lançamentos, para que seja incluída uma nova opção que servirá para calcular o valor líquido do lançamento somente quando o registro for selecionado. |
| **Solução/Implementação:** | Alterada a opção nos parâmetros do Totvs Gestão Financeira, Lançamentos a pagar, Inclusão, retirando o parâmetro de marcação, e adicionando um seletor com as opções: - Não calcular Valor Líquido automaticamente na Visão - Calcular Valor Líquido automaticamente na Visão - Calcular Valor Líquido ao selecionar Lançamento  Para opção "Não calcular Valor Líquido automaticamente na Visão", não haverá cálculo automatico de valor líquido na visão de lançamentos. Para opção "Calcular Valor Líquido automaticamente na Visão", será mantido o funcionamento normal do cálculo de valor líquido ao abrir/executar filtro na visão de lançamentos. Para nova opção "Calcular Valor Líquido ao selecionar Lançamento" a coluna de valor líquido será atualizada ao marcar o lançamento, na visão de lançamentos. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000021 |

divs
