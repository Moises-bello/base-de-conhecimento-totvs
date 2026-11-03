---
content_hash: 51941dbf4dc8b513cb916eb34db31efbe5d2f7821f461c6f40e487301ec71607
fetched_at: '2026-06-29T00:10:14.503214+00:00'
page_id: '461908163'
product: rm
source: tdn-rm
title: 4751288 MATESTCNTFTOF01-4862 DT Cancelamento de Item do Contrato x Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461908163
version: 5
---

# CANCELAR/DESCANCELAR ITEM DO CONTRATO X ORÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Funções:** | Cancelar Item do Contrato.  Descancelar Item do Contrato. |
| **Situação/Requisito:** | Ao incluir um item de contrato cujo valor excede o orçado para o período, a parcela do orçamento fica bloqueado corretamente, porém se for executado o processo Cancelamento de Item de Contrato, os saldos do orçamento não são estornados, permanecendo na Consulta de Valores Orçados. |
| **Solução/Implementação:** | Ao executar o processo de **Cancelar Item do Contrato**, caso o contrato afete o orçamento, os saldos do orçamento serão estornados.  Ao executar o processo de **Descancelar Item do Contrato**, caso o contrato afete orçamento, os saldos do orçamento serão recriados com base nos valores informados. |
| **Conversores e Parâmetros:** | Informe os conversores/parâmetros. |
| **Tickets relacionados:** | 4751288. |
| **Requisitos:** | Cancelar Item do Contrato: CtrCancelarItemContratoProcAction  Descancelar Item do Contrato: CtrDescancelarItemContratoProcAction |
| **Documento de Referência:** | . |
