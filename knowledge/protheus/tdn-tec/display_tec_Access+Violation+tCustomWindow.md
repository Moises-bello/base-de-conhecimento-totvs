---
content_hash: 49c6e40c90071b804c14b2561db2930d196bffaca79a4ea4e5d1c7eeac60b3de
fetched_at: '2026-07-02T19:24:23.950196+00:00'
page_id: '451268253'
product: protheus
source: tdn-tec
title: Access Violation tCustomWindow
type: documentation
url: https://tdn.totvs.com/display/tec/Access+Violation+tCustomWindow
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Access Violation tCustomWindow |
| Correção | Ajustado rotina para que não seja acessado ponteiros inválidos caso janela "pai" seja deletada em um evento de click. |
| Informações adicionais | * Referente ao chamado: MTEC-2234 * Disponível em builds iguais ou superiores a [13.1.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.41) e [13.2.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.41). |
