---
content_hash: b43317d7d9ff6b16ae78c25cf4a52b7769ccb7fc7fafbd1bb8cc385ee7aeb5e6
fetched_at: '2026-06-29T00:08:45.714535+00:00'
page_id: '315231794'
product: rm
source: tdn-rm
title: 1531410 DEDUINTEGRACOES-945 DT Validação de inadimplência na matricula para
  lançamento acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315231794
version: 96
---

# Regra de validação de inadimplência

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Validação de inadimplência na matricula via portal |
| **Situação/Requisito:** | Ao realizar a matricula para um aluno que teve negociação via procedimento de Acordo em um boleto já remetido ao banco o sistema estava informando que o aluno estava inadimplente. |
| **Solução/Implementação:** | Com as mudanças realizadas pelo TOTVS Gestão Financeira em função de boleto registrado, o boleto já remetido ao banco não é mais cancelado ao fazer o acordo, e com isso foi necessário evoluir o serviço de validação de inadimplência para que não valide se o lançamento estiver com status baixado por acordo. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
|  |  |

divs
