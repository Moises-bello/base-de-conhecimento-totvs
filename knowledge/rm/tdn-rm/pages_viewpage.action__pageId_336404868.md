---
content_hash: a968bd4dd987fd4faf1c9354a77b4dd3aba963c11a46ebe980823a93e44edb27
fetched_at: '2026-06-29T00:08:51.095783+00:00'
page_id: '336404868'
product: rm
source: tdn-rm
title: 1796193 RMSAU-2115 DT Ajuste no cadastrando de recém-nascido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336404868
version: 1
---

# Ajuste no cadastrando de recém-nascido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Cadastro de recém nascido |
| **Situação/Requisito:** | Erro em tempo de execução não cadastrando recém-nascido porém criando diversos atendimentos de RN |
| **Solução/Implementação:** | Ajuste na rotina responsável por persistir na base de dados os registros referentes ao atendimento do paciente, em caso de erro o registro não será mais cadastrado, fazendo com que o registro não seja inserido no atendimento. |
| **Tickets relacionados:** | [Ticket #1796193](https://totvssuporte.zendesk.com/agent/tickets/1796193 "Open ticket in Zendesk Support") |
