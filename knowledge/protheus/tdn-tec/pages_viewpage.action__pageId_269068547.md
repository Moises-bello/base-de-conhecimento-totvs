---
content_hash: 7ad168385d9fd165b242c0d2f2a267adc518648a8c83b9d2edf36b9fc988fef3
fetched_at: '2026-07-02T19:24:22.214771+00:00'
page_id: '269068547'
product: protheus
source: tdn-tec
title: Correção - Criar um TDialog e liberar com Free sem ativar, causa travamento
  do SmartClient
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269068547
version: 2
---

|  |  |
| --- | --- |
| Situação | Criar um TDialog e liberar com Free sem ativar, causa travamento do SmartClient |
| Ocorrência | O AppServer não deixava nenhuma outra janela ser fechada após o free de uma TDialog sem activate |
| Correção | Correção para ignorar a janela que não está visível ao receber Free. |
| Informações adicionais | * Referente ao chamado: TVWIW7 * Referente à ocorrência: TEC-7411 * Disponível a partir do build 7.00.131227a - 1.3.3 |
