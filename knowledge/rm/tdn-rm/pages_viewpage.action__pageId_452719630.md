---
content_hash: 50a11124fe385fd68a953e58d8f829e160482c5b940e5e09024312f33e229fa8
fetched_at: '2026-06-29T00:10:09.323595+00:00'
page_id: '452719630'
product: rm
source: tdn-rm
title: Lançamentos Financeiros - Rateio por Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719630
version: 13
---

Quando a parametrização é "Utiliza Cálculo por Centro de Custo", o sistema fará a distribuição dos Lançamentos Financeiros conforme o rateio por Centro de Custo parametrizado no RM Labore. Este recurso só estará

disponível para os clientes que tem a base Integrada com o sistema RM Fluxus e o rateio do Lançamento Financeiro só será visualizado no RM Fluxus.

**Atenção:**

1.    Quando houver rateio por centro de custo e as férias não tiverem sido lançadas, os valores dos rateios do lançamento IRRF de Férias serão calculados verificando o campo "Centro de custo do evento" no cadastro do evento, caso não esteja preenchido, o sistema buscará o rateio fixo do funcionário. Para os demais casos, será considerada a movimentação por centro de custo.

2.    O sistema utiliza o centro de custo informado no Rateio Fixo do cadastro de funcionários para o lançamento financeiro da pensão alimentícia sobre as férias, quando não houver evento de pensão na movimentação por centro de custo no período selecionado.

**Possíveis erros e suas respectivas explicações**

**[Erro] Erro na geração do lançamento de IRRF**. - O campo obrigatório Conta/Caixa deve ser preenchido. Os lançamentos não foram realizados.

O usuário deve verificar se na parametrização do sistema RM Fluxus o parâmetro "Conta/Caixa Obrigatório no lançamento" está marcado.

Na parametrização do Imposto de Renda do RM Fluxus, verificar o código do campo "Fornecedor" e informar a Conta/Caixa deste Fornecedor nos Cadastros de Clientes/Fornecedores.

[Voltar a pagina inicial](http://tdn.totvs.com/pages/viewpage.action?pageId=452719571)
