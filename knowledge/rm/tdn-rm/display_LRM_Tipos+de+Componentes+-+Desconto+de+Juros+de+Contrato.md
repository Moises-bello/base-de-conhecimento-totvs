---
content_hash: e7434108a2aed11ab7f82978d6112f215c33e581c67c77efabe3fc5159172d35
fetched_at: '2026-06-29T00:09:50.248822+00:00'
page_id: '435105462'
product: rm
source: tdn-rm
title: Tipos de Componentes - Desconto de Juros de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Desconto+de+Juros+de+Contrato
version: 5
---

Quando os Componentes que usam o Tipo de Componente **Desconto de Juros de Contrato** são inseridos na Modalidade de Vendas ou diretamente nas Condições de Financiamento de um Contrato de Vendas, o sistema apresenta na tela, os campos abaixo para serem parametrizados:

**Percentual de desconto (%):** Define o percentual de desconto que incidirá sobre os Juros Contratuais, ou seja os Juros preestabelecidosno Contrato (não confundir com Juros Financeiros), caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão da venda;

**Início:** Informe a data de início do desconto caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente;

**Fim:** Informe a data de fim do desconto caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente.

Importante!

A parametrização deste Componente o mesmo não deve ser associado a nenhum Tipo de Parcela, porque o mesmo não gera parcelas avulsas.

Os Componentes que utilizam o Tipo de Componente Desconto de Juros de Contrato são utilizados para compor os Valores das Parcelas dos Grupos aos quais eles estão associados.

O *Surgimento destes Componentes* deve ser parametrizados para a *Geração do Plano de Financiamento*.
