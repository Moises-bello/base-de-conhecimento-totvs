---
content_hash: 479d94cdd7b36933719966cae79ce39d3020e5cbefa1406ed2f07ec9d80f9ee7
fetched_at: '2026-06-29T00:08:27.447425+00:00'
page_id: '271412653'
product: rm
source: tdn-rm
title: 415182 MEDU-2395 Regerar Contabilidade Integrada Lote Zero
type: documentation
url: https://tdn.totvs.com/display/LRM/415182+MEDU-2395+Regerar+Contabilidade+Integrada+Lote+Zero
version: 109
---

# Lançamento - Regerar Contabilidade

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeiro. |
| **Função:** | Lançamento - Regerar Contabilidade |
| **Situação/Requisito/Story/Issue:** | Ao regerar a contabilização de inclusão de lançamento integrada ao lote zero, onde o evento contábil utiliza fórmula, e esta fórmula utiliza a data de previsão  de baixa, a mensagem de erro abaixa é exibida:  A fórmula XXXX não pode ser executada! Estouro de SqlDateTime. Deve estar entre 1/1/1753 12:00:00 AM e 31/12/9999 11:59:59 PM. |
| **Solução/Implementação:** | Ajustado serviço de re-geração de contabilização de inclusão de lançamento integrada ao lote zero.A partir de agora, este serviço passa a informar a data de previsão da baixa do lançamento para o serviço de contabilização do lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito (informe o requisito relacionado):** | FINTRF000027 |

divs
