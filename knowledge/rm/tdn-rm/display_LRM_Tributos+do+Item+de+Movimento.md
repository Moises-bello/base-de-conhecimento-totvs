---
content_hash: c69b2e0aa258e60dd3ace085748e53029ec9bd21241eec17b4b49447af046dbb
fetched_at: '2026-06-29T00:11:40.057688+00:00'
page_id: '793836769'
product: rm
source: tdn-rm
title: Tributos do Item de Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Tributos+do+Item+de+Movimento
version: 14
---

## 1. Visão Geral

A tela **Tributos do Item de Movimento** apresenta os impostos incidentes sobre o item selecionado, permitindo a visualização, cálculo automático e eventual edição dos valores.

A tela é dividida em duas áreas principais:

1. **Grid de Tributos (parte superior):** lista os tributos aplicáveis ao item, mostrando:

   * **Código do Tributo**
   * **Base de Cálculo**
   * **Alíquota**
   * **Valor**
   * **Manter Valor**
2. **Detalhamento do Tributo (parte inferior):** exibe informações complementares e campos específicos de acordo com o tributo selecionado na grid.  
   Essa área é **dinâmica** e se adapta ao tributo em destaque (por exemplo, CBS, IBS, ICMS).
3. **Preenchimento de dados dos tributos IBS/CBS:**

Ao definir o produto os tributos são carregados de acordo com a parametrização do tipo de movimento, como por exemplo a alíquota e, caso o cliente seja um órgão publico, o % de redução para compras governamentais ().

Ao selecionar a "Regra tributária" do item de movimento (aba "Fiscal") os tributos IBS/CBS, caso existam como tributos do item, tem suas informações recuperadas e preenchidas preenchidas (CST/Situação tributária, Classificação tributária, Percentual de redução de alíquota, Código de crédito presumido, Percentual de crédito presumido e Percentual de diferimento) e os valores são calculados (Valor crédito presumido, Valor diferido e Alíquota).

A atualização dos campos de percentuais destes tributos também acionam o recálculo dos respectivos valores destes percentuais. Tais valores são calculados conforme o valor da base de cálculo.

## 2. Cálculo dos valores

Todas as informações tributárias e valores exibidos são carregados e calculados automaticamente pelo **Serviço de Tributação**, considerando:

* **Natureza de Operação,**
* **Tipo de Movimento e**
* **Regras Tributárias**

Apesar do cálculo automático, o usuário pode **editar manualmente** os valores, quando necessário.

O campo **Manter Valor** define a origem e o comportamento do valor informado no tributo. Ele pode assumir duas situações:

* **Calculado:**

  + Situação padrão ao incluir um item.
  + Indica que os valores foram gerados automaticamente pelo Serviço de Tributação.
* **Editado:**

  + Quando o usuário altera manualmente o valor da **Base de Cálculo** ou do **Imposto**.
  + O sistema atualiza automaticamente o campo para “Editado”.

### Retorno para "Calculado"

Mesmo após edição, o usuário pode alterar manualmente o campo de volta para **Calculado**.  
Neste caso, ao utilizar a opção **Refazer Tributação** (ícone ou tecla de atalho **F7**), o sistema recalculará os valores de acordo com as regras definidas no Serviço de Tributação.

## 3. Outras informações

Regra Tributária - Preenchimento Automático

Quando o item do movimento está devidamente parametrizado para preenchimento da regra tributária e o mesmo não for preenchido o sistema vai utilizar a regra de seleção para tentar realizar esse preenchido de forma automática ao salvar obdescendo a seguinte regra:

1. Apenas se não vier preenchido vai tentar realizar o preenchimento.
2. Executa a regra de seleção de regra tributária para o item
   1. Se retornar apenas uma regra possível então vai preencher a regra tributária.
   2. Se retornar nenhum ou mais de um a regra permanece vazia.
3. A consistência verifica apenas se a regra definida é uma regra válida, ou seja, está na lista de regras da seleção automática
   1. Em caso de regra inconsistente uma mensagem de falha vai ser retornada.
