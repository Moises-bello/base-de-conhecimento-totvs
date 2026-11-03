---
content_hash: ef4bbd490c167173176a29a2cfac6a10d9c3ac823349223eb37484c183c865e5
fetched_at: '2026-06-29T00:08:38.537271+00:00'
page_id: '285664123'
product: rm
source: tdn-rm
title: 1004986 FINANCEIRO01-1591 Layout Gerador Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285664123
version: 103
---

# Segmento J52 - Remessa de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Layout Gerador de Saídas - Remessa de Pagamento |
| **Situação/Requisito:** | Ao gerar o layout de remessa de pagamento "FINLAY0052 - Cob. Reg. Itau (CNAB240)\_ajustado" a posição '004 a 007' não foi gerada corretamente. |
| **Solução/Implementação:** | Foi feito o ajuste no layout de gerador de saídas "FINLAY0052 - Cob. Reg. Itau (CNAB240)\_ajustado" para que posição fosse gerada corretamente, foi inserida uma expressão  no campo para corrigir a situação. A posição '004 a 007' do segmento J52 deve ser idêntica à posição '004 a 007' do segmento J. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1096915, 1102086 |
| **Requisito:** | Informe o requisito relacionado. |

divs
