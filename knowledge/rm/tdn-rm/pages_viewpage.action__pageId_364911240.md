---
content_hash: 33fb3d3cbcf618e872c39689d5f4f6b1968eaceee7c41189399d2dab15bb2485
fetched_at: '2026-06-29T00:08:59.745781+00:00'
page_id: '364911240'
product: rm
source: tdn-rm
title: 2913537 RMSAU-3929 DT Erro Módulo de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364911240
version: 1
---

# CORREÇÃO DA VALIDAÇÃO DE CPF PARA INCLUSÃO DE NOVOS PACIENTES NO REGISTRO DE INTERNAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Registro de Internações |
| **Situação/Requisito:** | Ao tentar incluir um paciente com CPF que já exista em outro paciente cadastrado, o sistema exibia uma mensagem de validação de CPF, porém ignorava a validação após desistir da inclusão do registro. |
| **Solução/Implementação:** | Removido o bloco de código onde era incluído o paciente, mesmo após a desistência do cadastro. |
| **Tickets relacionados:** | [2913537](https://totvssuporte.zendesk.com/agent/tickets/2913537) |
| **Requisito:** | RMSAU-3929 |
