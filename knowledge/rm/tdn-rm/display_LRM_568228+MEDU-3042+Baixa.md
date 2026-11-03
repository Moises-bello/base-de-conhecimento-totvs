---
content_hash: 583b17a076188d5615c57fd8ec21017441e38ef648ac44e5c4ef97d4614a84c6
fetched_at: '2026-06-29T00:08:30.414105+00:00'
page_id: '272431173'
product: rm
source: tdn-rm
title: 568228 MEDU-3042 Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/568228+MEDU-3042+Baixa
version: 106
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa. |
| **Situação/Requisito:** | Ao realizar a baixa de vários lançamentos financeiros simultaneamente, se os mesmos possuírem rateios por centro de custo ou departamento e estiverem inclusos em um Borderô e o parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa” estiver marcado, é exibido o erro:  "O processo de baixa foi concluído com ressalvas.  A baixa dos lançamentos [XXXXX] foi concluída com sucesso.     Não foi possível concluir o processo de baixa para o(s) lançamento(s) [YYYYYYY]. Violação de concorrência: DeleteCommand afetou 0 dos registros 1 esperados." |
| **Solução/Implementação:** | Ajustes no serviço de baixa de lançamentos, para fazer o update dos rateios de centro de custo e departamento dos itens de baixa gerados pela inclusão do borderô de pagamento, quando o sistema estiver parametrizado para baixa one log (parâmetro: "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa” habilitado). |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000040. |

divs
