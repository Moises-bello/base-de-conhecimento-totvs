---
content_hash: 32d1fdfb695a90224a27c2f41b4d8d358dd6ab557145467a941252ceb0d029f3
fetched_at: '2026-06-29T00:11:06.859865+00:00'
page_id: '635968536'
product: rm
source: tdn-rm
title: Como Manipular os Índices de Forma Simples
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=635968536
version: 8
---

Criar um plano de financiamento Price ou Padrão, com os componentes de Juros e Correção Monetária. Sendo que a CM deve ser anual, pois com o reajuste mensal o cliente já pode alterar o índice.

No componente de Correção Monetária, associar uma moeda que tenha os índices anuais.

Depois associar a fórmula para reajustar o CM somente uma vez por ano, ao contrário da forma antiga, que mesmo sendo anual, reajustava mensalmente o plano.

Cadastro da Moeda IGPM\_ANUAL

Cadastro da Fórmula Reajustar Somente Anual

**Agora a configuração já está pronta para realizar o reajuste somente no aniversário do contrato e utilizando o índice anual.**

**Por exemplo:**  Desejo reduzir o valor do índice do IGPM anual que está acima de 20% apartir de Jan/2021 para 10%.

No cadastro da Moeda IGPM Anual altere todos as cotações de jan/2021 a maio/2021 para 10%.

Reajustar o contrato para o mês 01/2021 e verificar que o sistema utilizou o índice de 10%

Veja a memória de cálculo com o índice de 10%
