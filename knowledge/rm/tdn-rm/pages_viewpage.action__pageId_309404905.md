---
content_hash: c2690af0e8515a9dc59374fcb961c3bb9feec0f05b4451430eaaa20cc0f8a0c2
fetched_at: '2026-06-29T00:08:44.870009+00:00'
page_id: '309404905'
product: rm
source: tdn-rm
title: 1538618 DEDUINTEGRACOES-764 DT Regeração de Lançamento Carregando Default de
  Conta Caixa / Convenio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309404905
version: 96
---

# Regeração de Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Regeração de lançamento |
| **Situação/Requisito:** | Ao regerar o lançamento financeiro pelo TOTVS Educacional o sistema sempre esta carregando o convenio default parametrizado na conta caixa, o problema deste cenário é o caso em que o cliente altera o convenio pelo TOTVS Financeiro, e em função de um ajuste nos valores precise regerar o lançamento no Educacional, neste caso o sistema esta voltando com as informações default.  E ai é esta sendo necessário alterar o convenio novamente pelo TOTVS Financeiro. |
| **Solução/Implementação:** | Evolução na regeração de lançamento pelo TOTVS Educacional para que seja mantido a conta caixa, convenio e dados bancários do lançamento.  Entendemos que a regeração do lançamento tem como principal objetivo atualizar os valores e neste caso vamos manter o mesmo comportamento que é aplicado pelo processo da bolsa retroativa em que não altera a conta caixa, convenio e informações bancarias nos casos de regeração. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
