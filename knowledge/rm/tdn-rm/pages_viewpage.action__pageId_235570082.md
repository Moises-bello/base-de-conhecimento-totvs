---
content_hash: 26c210261e9ab117055f44d793746800d82691e180819f4a9a6afcd76a7fe304
fetched_at: '2026-06-29T00:08:04.408168+00:00'
page_id: '235570082'
product: rm
source: tdn-rm
title: TULPAH_DT_Retorno_Cobrança_Lançamentos_Baixados_Parcialmente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235570082
version: 115
---

# RETORNO DE COBRANÇA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | *Retorno de Cobrança* |
| **Situação/Requisito:** | Existem vários lançamentos vinculados ao mesmo boleto, ao realizar a importação de Retorno de Cobrança para baixa de lançamentos foi observado que 2 destes lançamentos foi feita a baixa parcial e os demais teve a baixa completa. OBS: O valor de Baixa informado no arquivo de retorno é igual a soma do valor de baixa de todos os lançamentos vinculados. |
| **Solução/Implementação:** | Otimizado processo de retorno de cobrança para que seja realizada a baixa total dos lançamentos, quando o valor total do boleto informado no arquivo for igual a soma do valor da baixa dos lançamentos. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *FIN000169* |

divs
