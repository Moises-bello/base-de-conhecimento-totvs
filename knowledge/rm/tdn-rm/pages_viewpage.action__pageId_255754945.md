---
content_hash: d859c9642ddba11288e3aaf7281ae7b9841e4a264f2f94b00731c504a148354a
fetched_at: '2026-06-29T00:08:17.260868+00:00'
page_id: '255754945'
product: rm
source: tdn-rm
title: TVQZAW_DT_Solicitações_Via_Portal_Parcela_Extra_Data_Competência_Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=255754945
version: 115
---

# Solicitações Aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Sopitações aluno gerando parcela extra |
| **Situação/Requisito:** | A parcela extra gerada pela solicitação via portal, não está preenchendo a data de competência.  O sistema está parametrizado para considerar esta data como a data do lançamento contábil, e neste caso estava apresentando uma não conformidade ao contabilizar o lançamento financeiro.  Mensagem: Não foi possível setar a data de contabilização do lançamento de acordo com a data de competência da parcela |
| **Solução/Implementação:** | Realizamos um ajuste na geração da parcela proveniente das solicitações via portal para que a data de competência da parcela seja preenchida conforme a data de vencimento.  Isto somente irá acontecer se o serviço vinculado a parcela for do tipo contábil e o educacional estiver parametrizado para considerar a data da competência como data de contabilização. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVQZAW |
| **Requisito (ISSUE):** | *N/A* |

divs
