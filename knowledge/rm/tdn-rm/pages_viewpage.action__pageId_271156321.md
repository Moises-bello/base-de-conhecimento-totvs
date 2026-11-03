---
content_hash: d72c72c879ce80fc49e5443df5edbc57065313c9516a46ce4bff53384b7f6e47
fetched_at: '2026-06-29T00:08:25.787939+00:00'
page_id: '271156321'
product: rm
source: tdn-rm
title: MEDU-1890 DT Liberação de Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271156321
version: 113
---

# Liberação de Período

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Liberação de Período |
| **Situação/Requisito:** | Ao realizar o processo de Liberação De Período pelo financeiro o IDOPERACAO na tabela COPERACAO relacionado a ORIGEM igual a FLANBAIXA não e excluído, apenas o IDOPERACAO relacionado a origem FLAN e excluído |
| **Solução/Implementação:** | Ajuste no serviço de Liberação de Período do módulo financeiro para que o processo remova também as operações contábeis das baixas relacionadas ao lançamento que será excluído pelo processo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | ISSUE de homologação. |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
