---
content_hash: ad3e24805e32f19c688f4aa4932ee3e41144c6645bfa41d9062cdf223b9751f8
fetched_at: '2026-06-29T00:06:21.640599+00:00'
page_id: '223174440'
product: rm
source: tdn-rm
title: TTLJAG_DT_LANCAMENTO_FINANCEIRO_COM_RATEIO_FIXO
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLJAG_DT_LANCAMENTO_FINANCEIRO_COM_RATEIO_FIXO
version: 3
---

# GERAR LANÇAMENTO FINANCEIRO PARA FUNCIONÁRIOS COM RATEIO FIXO COM CENTRO DE CUSTO INVALIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Gerar lançamento financeiro para funcionários com rateio fixo com o centro de custo invalido* |
| **Situação/Requisito:** | Ao gerar o lançamento financeiro quando não existe rateio fixo para a chapa, é apresentado mensagem de referência de objeto. |
| **Solução/Implementação:** | Realizado verificação se existe o centro de custo informando no rateio fixo. Caso não exista é inserido no log conforme já era realizado. |
| **Chamados relacionados:** | TTLJAG |
| **Versões/Release:** | *12.1.9* |

divs
