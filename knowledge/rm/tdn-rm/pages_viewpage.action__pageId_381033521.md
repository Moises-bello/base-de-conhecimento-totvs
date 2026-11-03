---
content_hash: b3c4f13b4c54b6d0391fb41642a664728c31b106653f13d94f13118155fc66a4
fetched_at: '2026-06-29T00:09:02.942492+00:00'
page_id: '381033521'
product: rm
source: tdn-rm
title: DSAUGHSCC-816 - Após prescrição no PEP 2, os medicamentos apresentam nas movimentações
  de estoque como processados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381033521
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Prescrição |
| **Situação/Requisito:** | Ao prescrever através do PEP 2, as inalações estavam sendo mostradas na movimentação de estoque como Processadas, porém não estavam indo para a conta. |
| **Solução/Implementação:** | Foi implementada a função de envio para a conta das inalações no momento da checagem através do PEP 2. Isso devido a configuração dos produtos que estavam marcados ("Item de fracionamento de uso individual e que é faturado na checagem" e "Item de uso coletivo e que é faturado somente na checagem"). Nesses casos o item é faturado no momento da checagem através do PEP 2. |
| **Tickets relacionados:** | [Ticket #3183052](https://totvssuporte.zendesk.com/agent/tickets/3183052 "Open ticket in Zendesk Support") |
