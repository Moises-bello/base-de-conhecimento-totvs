---
content_hash: 8b0b2eb3c88c0f5b90d5b2098c97febaccdd4d8c3cccd0782eed87ddff6355bc
fetched_at: '2026-06-29T00:08:38.457788+00:00'
page_id: '285656564'
product: rm
source: tdn-rm
title: 973914 CONTROLADORIA01-275 DT Smart Analytics - Conceito "Fato - Controladoria
  - Orçamento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285656564
version: 102
---

# Conceito "Fato - Controladoria - Orçamento"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | GooData |
| **Função:** | Smart Analytics |
| **Situação/Requisito:** | A geração da chave na tabela HLC está incorreta pois não está considerando a coligada na montagem da mesma. A montagem dessa chave é feita pelo conceito “Fato – Controladoria – Orçamento” na parte de “ligações”. |
| **Solução/Implementação:** | Ajuste no conceito "Fato - Controladoria - Orçamento.concept" para que a coluna "HLC\_CCUSTO" seja montada a partir da origem tbOrcamento.CODCOLIGADA e tbOrcamento.CODCCUSTO fazendo com que a chave fique correta. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
