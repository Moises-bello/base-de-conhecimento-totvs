---
content_hash: 8c00db01c21e6f9867f4ee85e97a30eed0ebe6a723320e56290aa7527c6a75a4
fetched_at: '2026-06-29T00:06:24.966238+00:00'
page_id: '224128051'
product: rm
source: tdn-rm
title: TTWEOY_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWEOY_DT_Lancamento_Financeiro
version: 122
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Lançamento financeiro* |
| **Situação/Requisito:** | Na geração da GRFC nota-se que no caso em que o funcionário possui um valor de base de 13 negativo o sistema está abatendo o valor negativo para efeito de lançamento financeiro da Guia e para a geração do arquivo da GRFC o valor é considerado corretamente. |
| **Solução/Implementação:** | Otimizado lançamento financeiro da GRFC, de forma que o lançamento seja condizente com a geração da GRFC e não abata valor no lançamento quando a base de 13 for negativa |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTWEOY TUECCP |
| **Requisito (ISSUE):** |  |

divs
