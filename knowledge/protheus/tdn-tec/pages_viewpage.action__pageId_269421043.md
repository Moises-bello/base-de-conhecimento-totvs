---
content_hash: 1a93a78515b2fd0c82bc96cb99d7507e89ebe63bfc34c42c72dabfe3193ec921
fetched_at: '2026-07-02T19:24:22.326194+00:00'
page_id: '269421043'
product: protheus
source: tdn-tec
title: Correção de loop infinito de thread Telnet
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269421043
version: 2
---

Correção de loop infinito de thread Telnet

|  |  |
| --- | --- |
| Situação | Na deleção de codeblock que estava em execução poderia causar loop. |
| Ocorrência | Na deleção de um codeblock do SIGAACD ocorria loop. |
| Correção | Proteção na deleção do codeblock para verificar se não está em uso. |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - NG 2.0.11 |
