---
content_hash: 3252eafc448942c036471f9098916f9d69d12dc1c00ed7b8ae5cefd8e3cdf78e
fetched_at: '2026-07-02T19:24:20.440115+00:00'
page_id: '249266447'
product: protheus
source: tdn-tec
title: Access Violation na thread de monitoração de memória
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249266447
version: 3
---

Access Violation na thread de monitoração de memória

|  |  |
| --- | --- |
| Situação | Access Violation na thread de monitoração de memória |
| Ocorrência | Ao ocorrer o encerramento de uma thread no mesmo momento que a thread de monitoração de memória está lendo os dados para exibí-los ocorre o Access Violation |
| Correção | Correção para verificar se a thread ainda existe no momento de ler os dados de memória |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: TTEC-693 * Disponível em builds superiores a 7.00.131227A - 2.0.3 |
