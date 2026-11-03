---
content_hash: 59836e73951238727f986b4bc8e9d3771d02df0b518ebfe0e50301dd323034f2
fetched_at: '2026-06-29T00:09:17.395631+00:00'
page_id: '421388579'
product: rm
source: tdn-rm
title: Layout de Código de Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388579
version: 2
---

Através do layout de código de barras você configura alguns campos que serão utilizados para a geração do código de barras dos lançamentos.

**Tamanho do Nosso Número**

Informe o tamanho do nosso número, ou seja, a quantidade de dígitos que o nosso número terá no código de barras. Os dados desse campo serão utilizados para a geração do nosso número para determinados bancos.

* Banco ABN AMRO Real S.A.

* Banco do Brasil S.A.

**Valor Utilizado**

Informe o valor que será utilizado para a geração do Código de Barras.

* Valor Líquido: O sistema irá utilizar o valor líquido do lançamento calculado na data de vencimento do título.
* Valor Original: O sistema irá utilizar o valor original do lançamento.
* Valor Parcial: O sistema irá utilizar o valor parcial do lançamento, que é o mesmo cálculo do valor líquido acima mencionado, porém com uma diferença:
* Em relação aos valores opcionais que descontam, serão considerados apenas os que tiverem o respectivo parâmetro "Até Vencimento" desmarcado.
* Valor Zero: O sistema irá utilizar o valor zero.
