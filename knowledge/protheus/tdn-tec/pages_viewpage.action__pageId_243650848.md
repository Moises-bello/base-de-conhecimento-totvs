---
content_hash: bd09257691d6be9635fbdc0ccc8ebedcaa0d7008f707dbf9c5b6ea816f9e5b84
fetched_at: '2026-07-02T19:24:19.682483+00:00'
page_id: '243650848'
product: protheus
source: tdn-tec
title: Correção - Problemas com ColumnChanged(TGrid)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243650848
version: 1
---

|  |  |
| --- | --- |
| Situação | Ocorrência de error.log devido a ColumnChanged em uma rotina do ERP (Manutenção de Contratos) |
| Ocorrência | Problema ocorre devido a tentativa de selecionar uma linha inválida do TGrid, devido a discrepância da propriedade VisibleRows e o número de linhas realmente visíveis. |
| Correção | Propriedade VisibleRows atualizada no evento de Show e Resize do componente. |
| Informações adicionais | * Referente à ocorrência: TEC-7308 * Disponível em builds superiores a 131227A-20160714 |
