---
content_hash: ad92c605060a4978ea3af8e5191b08e483ad90e464a54222347aac9cc724f9e4
fetched_at: '2026-06-29T00:08:15.853126+00:00'
page_id: '244926009'
product: rm
source: tdn-rm
title: TVMVTA_DT_Bolsa_Retroativa_Baixa_Com_Mais_Formas_Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMVTA_DT_Bolsa_Retroativa_Baixa_Com_Mais_Formas_Pagamento
version: 112
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Inclusão / Exclusão de Bolsa Retroativa |
| **Situação/Requisito:** | Ao incluir uma bolsa retroativa para um aluno cuja a parcela já esteja baixada e foi utilizada duas formas de pagamento (exemplo: 400,00 cartão e 150,00 dinheiro) o sistema estava refazendo a baixa, porem a baixa referente ao valor de 150,00 estava ficando com o valor original igual a zero e o lançamento estava ficando como baixa parcial. |
| **Solução/Implementação:** | Ajustado para que o valor de pagamento a “maior” e “menor” sejam atualizados considerando as duas formas de pagamento desta forma a baixa ficará com o valor correto e lançamento ficará baixado total. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
