---
content_hash: c0ec46cbf0abd0703742dc1baa413e627cd8ec13974bb45df3134267d1427332
fetched_at: '2026-06-29T00:09:47.236280+00:00'
page_id: '435105003'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Cancelar lançamentos financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105003
version: 7
---

A partir da versão 12.1.2209, estamos atualizando o comportamento do processo de exclusão de lançamentos, para, ao invés de excluir este passar a apenas cancelar lançamentos.

Isto deve-se ao fato de permitir uma melhor rastreabilidade destes lançamentos já cancelados, possibilitando uma posterior consulta ao mesmos.

No Contrato de Locação, o processo de cancelar lançamentos financeiros cancelará os lançamentos já integrados com TOTVS Gestão Financeira ou Protheus. Não são cancelados lançamentos baixados, vinculados a cheque e remetidos a banco, ou com contabilidade vinculada ao lote zero.

Caso o lançamentos se encontre nos status acima, será necessário uma intervenção do usuário neste lançamento para desfazer quaisquer tipo de pendências que impossibilite o cancelamento pelo TCGI.
