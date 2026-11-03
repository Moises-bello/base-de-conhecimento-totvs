---
content_hash: ef9d2cfef091b5854b6998fd98133568a518c83c9dc7abd74085afa0712fbdb3
fetched_at: '2026-06-29T00:08:17.749577+00:00'
page_id: '258278419'
product: rm
source: tdn-rm
title: TVRLWJ_DT_Bolsa_Retroativa_Valor_Bolsa_Superior_Valor_Liquido_Lan
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRLWJ_DT_Bolsa_Retroativa_Valor_Bolsa_Superior_Valor_Liquido_Lan
version: 115
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Durante o processo de inclusão de bolsa retroativa está sendo apresentada a não conformidade:  Mensagem: Lançamento não atualizado. Valor líquido menor que 0.  Conforme o cenário documentado pelo suporte identificamos que a bolsa a ser incluída para o aluno é superior ao valor líquido do lançamento financeiro da parcela. A não conformidade ocorre porque o valor da bolsa é superior ao valor líquido do lançamento.  Exemplo:  Valor original: 1.269,00 Campo Opcional (Desc. Pontual): 550,00 Valor Baixado: 719,00  Conforme os descontos já concedido o valor da bolsa de 89,75% não é suportado no lançamento por isto é apresentado a mensagem ao executar o processo. |
| **Solução/Implementação:** | Melhoria no processo de inclusão de bolsa retroativa para que não seja apresentada nenhuma não conformidade quando o valor da bolsa for superior ao valor líquido do lançamento financeiro, neste caso será considerado como valor de bolsa o valor até o limite do valor líquido. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | TVRLWJ |
| **Requisito (ISSUE):** | N/A |

divs
