---
content_hash: 185e38d7d2e96c1939e48897c2033f4d18c3751edcf719f2b3a9bce1d36f649a
fetched_at: '2026-06-29T00:08:23.784739+00:00'
page_id: '270091299'
product: rm
source: tdn-rm
title: 173039_DT_Contabilização_da_Transferência_de_Controle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270091299
version: 113
---

# Contabilização da Transferência de Controle

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Contabilização da Transferência de Controle |
| **Situação/Requisito:** | Na contabilização da transferência de controle o valor de depreciação acumulada está buscando o saldo do mês atual da transferência. Isto faz com que o valor da conta de depreciação acumulada no relatório de agrupamento fique diferente do valor apresentado para a mesma conta no balancete. |
| **Solução/Implementação:** | Ajustar o retorno dos valores da transferência de controle para que busque o valor no mês anterior ao mês da transferência e caso não encontre registro busque na tabela de saldo do patrimônio. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
