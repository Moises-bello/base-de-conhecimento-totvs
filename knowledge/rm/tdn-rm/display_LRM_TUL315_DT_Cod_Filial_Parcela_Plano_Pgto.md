---
content_hash: d08298808b49b1082d43e794548d903f4c6d323d1340265d4e4cbe4c01141df1
fetched_at: '2026-06-29T00:08:04.041019+00:00'
page_id: '235334003'
product: rm
source: tdn-rm
title: TUL315_DT_Cod_Filial_Parcela_Plano_Pgto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUL315_DT_Cod_Filial_Parcela_Plano_Pgto
version: 115
---

# IMPORTADOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Importador: parcelas do plano de pagamento (tabela SPARCPLANO)* |
| **Situação/Requisito:** | *O layout de importação atual da tabela SPARCPLANO não permite informar qual o CODFILIAL do período letivo do plano de pagamento. Por isso, quando o plano de pagamento possui o código e código do período letivo iguais, o importador incluir a parcela no plano de pagamento da primeira filial encontrada.* |
| **Solução/Implementação:** | *Criação do campo CODFILIAL no layout de importação da tabela SPARCPLANO.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
