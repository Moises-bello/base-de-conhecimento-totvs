---
content_hash: d8f21e9ed89d6a7eaa112a774d6d5593d0ba71713fa8a045b71f87ae674dc583
fetched_at: '2026-06-29T00:09:09.752085+00:00'
page_id: '393366721'
product: rm
source: tdn-rm
title: DSAUGHFATF-1866 - ERRO AO TENTAR GERAR EXTRATO DE DEBITO NA CONTA DE PACIENTE
type: documentation
url: https://tdn.totvs.com/display/LRM/DSAUGHFATF-1866+-+ERRO+AO+TENTAR+GERAR+EXTRATO+DE+DEBITO+NA+CONTA+DE+PACIENTE
version: 1
---

# ERRO AO TENTAR GERAR EXTRATO DE DEBITO NA CONTA DE PACIENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Elaboração de contas |
| **Função:** | Extrato de débitos |
| **Situação/Requisito:** | O sistema não estava estava gerando o extrato de débito por estar com a consulta do relatório faltando um alias. |
| **Solução/Implementação:** | Foi alterada a consulta para colocar um alias quando a mesma for executada em uma base SQL SERVER |
| **Tickets relacionados:** | <https://totvssuporte.zendesk.com/agent/tickets/3543021> |
