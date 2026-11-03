---
content_hash: 86e609ca261c2b5468faa408406c9274f3129f3b213063e247c0387bab5f2b0f
fetched_at: '2026-06-29T00:09:46.056689+00:00'
page_id: '435104766'
product: rm
source: tdn-rm
title: Componentes - Desconto de Correção Monetária e Desconto de Juros de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104766
version: 3
---

Quando os Componentes que usam os Tipos de Componentes **Desconto de Correção Monetária** ou o **Desconto de Juros de Contrato** são inseridos na [Modalidade de Vendas](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades) ou diretamente nas [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) de um Contrato de Vendas, o sistema apresenta na tela, os campos abaixo para serem parametrizados:

**Percentual de desconto (%):**Define o percentual de desconto que incidirá sobre a Correção Monetária ou os Juros Contratuais, ou seja os Juros preestabelecidosno Contrato (não confundir com Juros Financeiros), caso estes sejam fixos, se não forem fixos, deixe o campo em branco para ser informado posteriormente na inclusão da venda;

**Início:**Informe a data de início do desconto caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente;

**Fim:**Informe a data de fim do desconto caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente.

Importante!

A parametrização deste Componente o mesmo não deve ser associado a nenhum Tipo de Parcela, porque o mesmo não gera parcelas avulsas.

Os Componentes que utilizam o Tipo de Componente Desconto de Juros de Contrato são utilizados para compor os Valores das Parcelas dos Grupos aos quais eles estão associados.

O *Surgimento destes Componentes* deve ser parametrizados para a *Geração do Plano de Financiamento*.
