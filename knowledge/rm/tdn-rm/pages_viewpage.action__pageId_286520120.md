---
content_hash: 29a53d25418a73bc01278524ded44474f82c22eaf74704b426ea48d126e270d1
fetched_at: '2026-06-29T00:08:41.248540+00:00'
page_id: '286520120'
product: rm
source: tdn-rm
title: 1172655 FINANCEIRO01-2202 DT Inclusao de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286520120
version: 103
---

# Inclusão de lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Inclusão de Lançamentos |
| **Situação/Requisito:** | Ao incluir movimentos que geram financeiro, onde o movimento está parametrizado para utilizar rateio por natureza (MovFinLancamentoParams.TipoRateioCCuNat), neste caso é gerado um item de rateio para o lançamento sem informações do centro de custo. Como este campo é nulo acontece o erro de referência de Objeto. |
| **Solução/Implementação:** | Ajustado serviço de inclusão de lançamentos. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000254 |

divs
