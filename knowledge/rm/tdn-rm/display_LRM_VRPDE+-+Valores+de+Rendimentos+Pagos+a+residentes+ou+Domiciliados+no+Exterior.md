---
content_hash: 300a9dab081d5842f87cee74b8b6286f4144cb91b2cc614890cc7fb7ae7da913
fetched_at: '2026-06-29T00:09:21.073926+00:00'
page_id: '422545798'
product: rm
source: tdn-rm
title: VRPDE - Valores de Rendimentos Pagos a residentes ou Domiciliados no Exterior
type: documentation
url: https://tdn.totvs.com/display/LRM/VRPDE+-+Valores+de+Rendimentos+Pagos+a+residentes+ou+Domiciliados+no+Exterior
version: 4
---

Valores de Rendimentos Pagos a residentes ou Domiciliados no Exterior.

**Campo 1: Identificador de registro (VRPDE)**

**Campo 2: Data de pagamento**

Gerado conforme o campo “Data Vencimento” (Integrações, aba “Dados Financeiro”).

**Campo 3: Código de receita**

Este campo é gerado de acordo com o campo Identificador do Código da Receita no Tributo do Lançamento. Caso o campo esteja vazio, o código será o do cadastro do tributo.

**Campo 4: Tipo de****rendimento**

 Gerado conforme o Campo "Tipo de Tributação" informada no "Pasta Outros Tributos do Lançamento".

**Campo 5: Rendimento pago**

Gerado conforme o Campo Base de Calculo informado na "Pasta Outros Tributos do Lançamento".

**Campo 6: Imposto retido**

Gerado conforme o Campo Valor do Imposto informado na "Pasta Outros Tributos do Lançamento".

**Campo 7: Forma de tributação**

Caso o  valor do campo “FORMATRIBUTACAO” informado na "Pasta Outros Tributos do Lançamento" seja diferente de “00”, o valor virá do campo “FORMATRIBUTACAO” da "Pasta Outros Tributos do Lançamento". Caso contrário, o valor virá do campo “FORMATRIBUTACAO” do Cadastro do Cliente\Fornecedor - Pasta Tributos.
