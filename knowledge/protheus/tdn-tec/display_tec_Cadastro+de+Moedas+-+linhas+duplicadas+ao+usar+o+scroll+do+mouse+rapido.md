---
content_hash: 12e62262cea2da7aeb6f1483c90305eb7de9e97819adcb3cc7fb50d3ed3ffcdc
fetched_at: '2026-07-02T19:24:24.863334+00:00'
page_id: '490638278'
product: protheus
source: tdn-tec
title: Cadastro de Moedas - linhas duplicadas ao usar o scroll do mouse rapido
type: documentation
url: https://tdn.totvs.com/display/tec/Cadastro+de+Moedas+-+linhas+duplicadas+ao+usar+o+scroll+do+mouse+rapido
version: 2
---

|  |  |
| --- | --- |
| Situação | Após a inclusão, alteração ou visualização de um registro, ao realizar o scroll do mouse rapidamente, o componente duplica as linhas apresentadas no browse (TGrid) |
| Correção | Implementação de controle de tempo para o evento (keyCode) UP e DOWN, tanto para teclado quanto para scroll do mouse. |
| Informações adicionais | * Referente ao chamado:  Não há chamado associado * Referente à ocorrência: SCHTML-922 * Disponível a partir da build 7.00.131227A - 4.3.0 |
