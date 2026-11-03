---
content_hash: 08caf4103e007be5caedf2894d48435ab3110907911059e7102c57d957ea3d54
fetched_at: '2026-06-29T00:08:17.740094+00:00'
page_id: '258278037'
product: rm
source: tdn-rm
title: TVQT89_DT_Extrato_de_Caixa_Cancelamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQT89_DT_Extrato_de_Caixa_Cancelamento
version: 117
---

# Extrato de Caixa - Cancelamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Extrato de Caixa - Cancelamento |
| **Situação/Requisito:** | Ao tentar cancelar um extrato de Saque CPMF o sistema apresenta erro é não permite prosseguir com o processo: Extrato XXXXX não pode ser estornado, conforme descrito abaixo: "O índice estava fora do intervalo. Ele deve ser não-negativo e menor que o tamanho da coleção. Nome do parâmetro: index". |
| **Solução/Implementação:** | Otimização no processo de cancelamento de extrato com operação Saque CPMF. Agora o sistema consegue cancelar o extrato com sucesso. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000029 |

divs
