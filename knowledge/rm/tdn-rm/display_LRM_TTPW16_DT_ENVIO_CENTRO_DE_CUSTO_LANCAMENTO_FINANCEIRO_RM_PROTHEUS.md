---
content_hash: b1621b2cff73f71e5436ee2f0a41325fd2122d5951cdba8d1d0415f99d33fbdc
fetched_at: '2026-06-29T00:06:22.548166+00:00'
page_id: '223920867'
product: rm
source: tdn-rm
title: TTPW16_DT_ENVIO_CENTRO_DE_CUSTO_LANCAMENTO_FINANCEIRO_RM_PROTHEUS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPW16_DT_ENVIO_CENTRO_DE_CUSTO_LANCAMENTO_FINANCEIRO_RM_PROTHEUS
version: 122
---

# INTEGRAÇÃO RM x PROTHEUS - LANÇAMENTO FINANCEIRO LABORE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Integração RM x Protheus - Lançamento Financeiro Labore* |
| **Situação/Requisito:** | O cliente queria que a informação do Centro de Custo fosse enviada para o protheus nos documentos à pagar, mas no RM essa informação existe apenas no rateio do centro de custo, não no documento em si. |
| **Solução/Implementação:** | Foi feita uma alteração para quando não houver rateio, ser criado um rateio com valor zerado e percentagem de 100% com o código de centro de custo. Foi criado um patch também no Protheus para interpretar essa nova mensagem para gravar o centro de custo no documento no Protheus. |
| **Chamados relacionados:** | *TTPW16* |
| **Versões/Release:** | *12.1.9* |

divs
