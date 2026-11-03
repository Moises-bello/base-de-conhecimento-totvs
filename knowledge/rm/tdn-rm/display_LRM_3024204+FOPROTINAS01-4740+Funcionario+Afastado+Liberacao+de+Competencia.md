---
content_hash: 13c5d3e4f10fa3b68d97973775f78c4691d039d7a0e01a624557f9c56604ef25
fetched_at: '2026-06-29T00:09:01.685597+00:00'
page_id: '375229347'
product: rm
source: tdn-rm
title: 3024204 FOPROTINAS01-4740 Funcionario Afastado Liberacao de Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/3024204+FOPROTINAS01-4740+Funcionario+Afastado+Liberacao+de+Competencia
version: 7
---

# LIBERAÇÃO DE COMPETÊNCIA

1555604762428\_1635783406

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Liberação de Competência |
| **Situação/Requisito:** | Ao efetuar a liberação de competência, se houvessem funcionários com retorno de afastamento naquele mês a situação estava sendo alterada automaticamente para Ativa. |
| **Solução/Implementação:** | Foi criado um parâmetro em "06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Etapa 6 - Afastamento" : Manter a situação dos funcionários com afastamento na Liberação de Competência      Ao marcar o parâmetro, os funcionários que possuem retorno de afastamento no mês da nova competência continua com sua situação de afastamento. |
| **Conversores e Parâmetros:** | "Não Retornar funcionário com afastamento para situação "Ativo" na virada de competência no mês de retorno" |
| **Tickets relacionados:** | [3024204](https://totvssuporte.zendesk.com/agent/tickets/3024204 "Open ticket in Zendesk Support") |
