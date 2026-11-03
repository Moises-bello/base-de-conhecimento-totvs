---
content_hash: 0690475ac011cbead11f08ab6c8e69beeec3dd6de691f3291cf4c715b6521754
fetched_at: '2026-06-29T00:09:23.881399+00:00'
page_id: '422546149'
product: rm
source: tdn-rm
title: Prestações de Serviços de Transporte (NF-e Tipo Frete)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546149
version: 2
---

Existem situações em que o frete não é tributado da mesma maneira do que os itens do movimento de venda e seu valor não irão compor a base de calculo do ICMS. Para essas situações foi implementado no parametrizador do Tipo de Movimento na Etapa 63 – Fiscal – Escrituração Fiscal deverá ser informado um produto para o campo "Produto do Tipo Frete", que será utilizado no processo de Escrituração criando uma parcela tendo esse produto como item.

Será necessário também vincular esse produto cadastrado a uma ou mais natureza de operação onde será parametrizada sua tributação. Essa vinculação é realizada na aba regras de tributação, tendo como regra de tributação o produto referenciado no tipo de movimento.

Em movimentos que tem o campo "Produto Tipo Frete" preenchido, será exibido o campo Natureza Frete na Integração Fiscal (O campo Município deve ser informado também para transmissão de NF-e\*\*) onde deve ser informada a natureza configurada.

* Ao transmitir uma NF-e com Produto Tipo Frete informado as Tags do Grupo de Retenção do ICMS
* Do transporte será impressa no XML e devendo ser utilizado os seguintes CFOP's: 5.351, 5.352, 5.353, 5.354, 5.355, 5.356, 5.357, 5.359, 5.360, 6.351, 6.352, 6.353, 6.354, 6.355, 6.356, 6.357, 6.359, 6.360, 7.358.

Como Fazer

[NF-e Tipo Frete](http://tdn.totvs.com/display/LRM/NF-e+-+Produto+tipo+frete)
