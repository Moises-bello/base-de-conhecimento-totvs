---
content_hash: 9c43ecafe0e7fe2cf314e86a1aa42dac775d96d5bfc543ea3bcc2324d8916313
fetched_at: '2026-06-29T00:10:25.332374+00:00'
page_id: '502827139'
product: rm
source: tdn-rm
title: Código de Calculo 414-Adiantamento de 13º Licença maternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502827139
version: 6
---

Evento tipo Desconto,valor.

Este evento será calculado em Dezembro quando uma rescisão for calculada posterior ao lançamento da segunda parcela de 13º salário, para funcionários com afastamento por licença maternidade.  

Este código de cálculo conterá somente o valor que foi pago no evento com código de cálculo 371 -( Segunda parcela 13º Licença Maternidade Provento ) separando do restante do 13

**Exemplo:**

Funcionária afastada Licença Maternidade durante o ano de 2019.

Dezembro:

Período 1: Pagamento da segunda Parcela de 13º .

 Neste envelope será lançado os proventos com CC 371 ( Segunda parcela 13º Licença Maternidade Provento ) e o evento com CC102 ( 2º Parcela de 13º Salario).

 Período 2: Rescisão

No envelope da rescisão será calculado no evento com CC51(Adiantamento 2º Parcela de 13º ) onde será  abatido o valor do evento com CC102 (  Segunda parcela de 13 º )e o valor do evento com CC371 (Segunda Parcela 13º Licença maternidade Provento) será abatido no evento com CC414(Adiantamento de 13º Licença Maternidade)
