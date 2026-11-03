---
content_hash: 139f36345f364ad29ef485a96ade0208bf62da910b3baa05dbc58ca912ea6599
fetched_at: '2026-06-29T00:09:53.669439+00:00'
page_id: '440855249'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3921 DT Desconto por valor em uma parcela por crédito no plano
  de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440855249
version: 1
---

# DESCONTO POR VALOR EM UMA PARCELA POR CRÉDITO NO PLANO DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Plano de pagamento |
| **Situação/Requisito:** | Sistema não permite incluir uma parcela calculada por número de créditos informando um desconto por valor. |
| **Solução/Implementação:** | Sistema passou a validar o valor de desconto informado somente se a parcela for uma parcela fixa (por valor). Para parcelas calculadas por número de crédito, sistema não faz a validação se o valor informado para o desconto é maior que o valor da parcela. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
