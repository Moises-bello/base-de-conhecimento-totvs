---
content_hash: 10fca8e1754dc413e5c988903d8a8ef4e326f29c4c0b2052ec199e2807f749d9
fetched_at: '2026-06-29T00:10:12.535172+00:00'
page_id: '454828917'
product: rm
source: tdn-rm
title: '4330328 MATESTCNTFTOF01-4678 DT TOTVS Manutenção de Ativos x BackOffice RM
  - #CANCELREQUEST 1.000'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454828917
version: 1
---

# RETORNAR MENSAGEM DE INCONSISTÊNCIA NA MENSAGEM CANCELREQUEST

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice RM. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | CANCELREQUEST. |
| **Situação/Requisito:** | Ao realizar a exclusão de um item da baixa de estoque integrada ao SigaMNT que provocou alguma inconsistência no processo, o retorno era tratado como sucesso e o registro era cancelado/excluído no PROTHEUS, mas no RM não. |
| **Solução/Implementação:** | Realizado o ajuste para quando ocorrer alguma inconsistência, setar o status da execução do processo como "Error" e assim apresentar o motivo da inconsistência ao usuário. |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | 4330328. |
| **Requisito:** | MATESTCNTFTOF01-4678. |
| **Documento de Referência:** | . |
