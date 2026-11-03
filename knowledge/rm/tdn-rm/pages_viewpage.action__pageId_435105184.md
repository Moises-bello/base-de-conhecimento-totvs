---
content_hash: 51a004dd8ee9ddf5cf42953dc11b54ddf8549e047f10421e5b34438db18c7f82
fetched_at: '2026-06-29T00:09:48.536962+00:00'
page_id: '435105184'
product: rm
source: tdn-rm
title: Componentes - Componente Correção Monetária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105184
version: 9
---

Ao cadastrar ou editar o componente de Correção Monetária da Modalidade da Venda, informe os seguintes campos:

* **Moeda**: Informe qual índice de reajuste será usado para corrigir as parcelas caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.
* **Coeficiente**: Informe se além da variação do índice, a parcela será acrescida de outro percentual caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel. Este percentual é calculado sobre o valor do componente do tipo Principal somado ao valor do componente de CM.

ExemploÍndice IGP-M + 5% - Informe no campo moeda "IGP-M" e no campo coeficiente "1,05".Será calculado 5 % sobre a soma do componente do Tipo Principal + componente de CM. Este resultado, será somado ao valor de CM.

* **Meses de Defasagem**: Informe qual a defasagem que o sistema usará para buscar a cotação do índice de correção caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel. No Modelo Padrão o cálculo da defasagem é feito da seguinte forma: (Valor) +1

Exemplo

Se for informado valor 0 (zero) a defasagem será 1. Se informar valor 1 a defasagem será 2 e assim por diante.

Já nos outros modelos o valor informado corresponde exatamente a defasagem.

* ****% Desconto Moeda:**  
  Se preenchido o valor, o reajuste irar descontar a moeda todo mês antes de acumular o valor total, antes de ignorar a deflação ou qualquer outro parâmetro, ou seja, buscou a contação do mês, aplicou o desconto e depois aplica os demais parâmetros.  **Exemplo:**INCC 01/2021 = 0,8% apliquei desconto de 50%, o valor a ser reajustado será de 0,4%, e assim para os demais casos.**
* **Prazo de Reajuste (meses)**:Informe o prazo mensal para realização dos reajustes de Correção Monetária caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel. **Referência da Entrega para o Componente**: Informe qual será a data de referência para determinar se o componente terá ação antes ou após a entrega do empreendimento. As datas podem ser:

* + Data da Entrega do Empreendimento
  + Data do Habite-se
  + Data da Entrega das Chaves
  + Data da Assinatura

Esta opção somente estará habilitada se o Modelo de cálculo escolhido no componente do tipo Principal desta modalidade for MODELO PADRÃO.

* **Data de referência para a correção**: Informe a data em que o sistema tomará como referência para efetuar os reajustes de Correções. As Referências podem ser:

* + Data da Venda;
  + Data de vencimento da parcela;
  + Data de vencimento da primeira parcela;
  + Data base da venda;
  + Data base do componente.

* **Tipo de Moeda**: Informe se o sistema irá usar para corrigir a correção Monetária a Cotação (Moeda) ou Variação Mensal (índice). Na Cotação (Moeda) iremos informar a cotação acumulada mensalmente. Na Variação Mensal (Índice) iremos informar diretamente o Índice Mensal no cadastro de cotação.

O sistema irá buscar a cotação do dia da data de referência, se não encontrar a cotação do dia, irá buscar a cotação do dia 01 do mês em questão.

Ao parametrizar um componente de Correção Monetária na Modalidade de Venda ou diretamente nas Condições do Plano de Financiamento dela, caso a Moeda/Índice parametrizada seja do Tipo Índice Mensal, ela **não** pode utilizar mais de 2 casas decimais à esquerda na cotação dela, pois esta combinação de parametrizações gera uma variação mensal extremamente alta e por consequência o valor do reajuste aplicado nas parcelas será também alto.

**Exemplo:**

Cadastramos o componente de *Correção Monetária* utilizando a *Moeda TINPAD* e parametrizamos o seu *Tipo*, como *Índice Mensal*:

A Moeda TINPAD é do Tipo Moeda:

Cadastramos uma Cotação para esta moeda cujo valor é igual (ou maior) que 100%,, ou seja com mais de duas casas decimais à esquerda da vírgula:

Ao tentarmos salvar este componente com esta parametrização o sistema apresenta a exceção abaixo:

*"O campo tipo da moeda é do tipo mensal para o componente [4] do grupo [1], sendo que o índice da última moeda [100,0000%] supera o número de 2 casas a esquerda, o que é incorreto para esse tipo de moeda. Favor trocar o tipo de moeda para acumulado que realiza a divisão do índice atual pelo índice do mês anterior."*

Caso já se tenha na base alguma venda efetivada com este cenário, o sistema realizará o cálculo do reajuste normalmente e exibirá a mensagem de alerta acima, ao usuário, solicitando que se revejam estas parametrizações, a fim de evitar que o reajuste gere valores super inflacionados.

* **Correção das parcelas**: Informe se este componente de correção irá reajustar as parcelas vincendas, vencidas ou ambas. O sistema toma como base a data do reajuste para verificar se as parcelas estão vincendas ou vencidas.

Este parâmetro só irá aparecer se o tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade for Modelo Padrão ou Tabela Price.

Informações Complementares

---
