---
content_hash: db676cff4c32fb0a41280a661183738a02bf0731760f49c67ed432564a5a70b5
fetched_at: '2026-06-29T00:08:38.999694+00:00'
page_id: '286004900'
product: rm
source: tdn-rm
title: CONTROLADORIA01-338 DT Desfazer Revisão Vida Útil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286004900
version: 102
---

# Desfazer Revisão de Vida Útil

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Desfazer Revisão de Vida Útil |
| **Situação/Requisito:** | Não está sendo possível desfazer a revisão de vida útil. O processo tenta excluir uma avaliação residual, porém ela não foi gerada pelo processo de revisão de vida útil, impossibilitando a exclusão da revisão realizada. |
| **Solução/Implementação:** | O processo de revisão de vida útil foi modificado para gerar, mesmo com valor zerado, uma avaliação residual. Após esta alteração foi possível excluir as revisões realizadas. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
