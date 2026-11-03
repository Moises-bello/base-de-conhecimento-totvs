---
content_hash: 2bb4a26df0b16be075b477b6cfcfe11f6be525976021a4f92787d87ca2833725
fetched_at: '2026-06-29T00:08:37.186249+00:00'
page_id: '284878629'
product: rm
source: tdn-rm
title: EDUCACIONAL01-1610 DT Desfazer inclusão de bolsa retroativa / Cancelamento
  de Baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284878629
version: 100
---

# DESFAZER INCLUSÃO DE BOLSA RETROATIVA / CANCELAMENTO DE BAIXA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Desfazer inclusão de bolsa retroativa / Cancelamento de Baixa de lançamentos |
| **Situação/Requisito:** | Processo de desfazer a inclusão da bolsa retroativa não permite desfazer quando é gerado vínculo, mesmo se todos os lançamentos estiverem em aberto.  Cancelamento de baixa não é permitido se o lançamento tiver vinculado com algum crédito gerado pela inclusão de bolsa retroativa. |
| **Solução/Implementação:** | (**Desfazer inclusão de bolsa**)  Ajuste para que consigamos desfazer a inclusão de bolsa retroativa mesmo que créditos de bolsas já estejam vinculados a algum lançamento do contrato.  Passamos a impedir o processo para desfazer a inclusão da bolsa somente nos casos abaixo conforme parametrização do sistema.    Caso o sistema esteja parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"***:***  Esse processo só poderá ser executado se as parcelas que tiveram lançamentos vinculados a créditos estiverem com os lançamentos "Em aberto" ou "Cancelados"  Caso o sistema esteja parametrizado para "***Usar conta corrente***  Esse processo só poderá ser executado se os créditos em conta corrente gerados pela inclusão da bolsa não tiverem sido utilizados em outro lançamento.    (**Cancelamento de Baixa**)  Excluída a validação do cancelamento de baixa quando o lançamento tiver vinculado com algum crédito gerado pela inclusão de bolsa retroativa pois não faz sentido o bloqueio do cancelamento e esse bloqueio poderia levar a uma situação em que o usuário ficaria sem ter o que fazer em lançamentos baixados que foram vinculados a créditos de bolsa retroativa, ou seja, se mantivéssemos o bloqueio, o usuário não conseguiria desfazer a inclusão da bolsa nem cancelar a baixa do lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
