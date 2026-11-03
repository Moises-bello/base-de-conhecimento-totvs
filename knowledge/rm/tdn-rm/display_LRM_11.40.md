---
content_hash: 4035a0058dd4389a6c07a13c11ba59787ded8f1e0909506d20fc15e847603a5f
fetched_at: '2026-06-29T00:09:23.224669+00:00'
page_id: '422546074'
product: rm
source: tdn-rm
title: '11.40'
type: documentation
url: https://tdn.totvs.com/display/LRM/11.40
version: 3
---

* **Cadastro de Natureza| Inclusão do Tipo de Receita na Natureza de Operação**

Implementado o Tipo de Receita podendo informar se a receita é de terceiros ou própria.

* **NF-e | Envio de NF-e com informações do ICMS60**

Foi Implementado o calculo automático da Base de Cálculo e Valor do ICMS-ST dos itens que tem tributação ICMS igual a 60.

* **Geração de Guias | Processo de Flexibilização do Processo de Geração de Guias**

Foi implementado o processo de Flexibilização de geração de Guias dos tributos ISS, IRRF PJ, INSS. Com esse processo é possível realizar o agrupamento das guias conforme a necessidade da empresa.

* **NF-e | Prestação de Serviços de Transporte (Produto Tipo Frete)**

Alterada a forma de realizar a transmissão de NF-e com frete tributado, a partir da versão 11.40 não é necessário utilizar os campos complementares, esse processo será parametrizado Tipo de Movimento, onde é informado o produto e vinculado na natureza de operação.

* **Tipo de Movimento | Tributação do Movimento: Buscar Alíquota no Serviço**

Alterado a forma que Totvs Gestão Entradas e Estoque realiza a busca do código de receita default na inclusão do movimento.
