---
content_hash: 0168b26e018dfd8f8c9215ae5cc1d05dda91f83390a44ae8a7c8d3055141b57f
fetched_at: '2026-06-29T00:09:48.523085+00:00'
page_id: '435105180'
product: rm
source: tdn-rm
title: Tipos de Componentes - Principal
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Principal
version: 7
---

Ao cadastrar ou editar o componente Principal da Modalidade da Venda, informe os seguintes campos:  
  
**Valor Financiado:**  
Informe o valor total do componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.

Este campo poderá ser preenchido automaticamente se os campos Valor Unitário e Número de Parcelas já estiverem parametrizados. 

**Valor Unitário:**  
Informe o valor unitário da parcela de entrada.

Este campo poderá ser preenchido automaticamente se os campos Valor Total e Número de Parcelas já estiverem parametrizados.

**Quantidade de Parcelas:**  
Informe o número de parcelas que serão criadas para este componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.

Importante!

Os campos abaixo somente são apresentados quando o TCGI estiver parametrizado para utilizar a [Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766), para os Tipos de Componentes são do Tipo de Entrada ou Principal, não sendo apresentados quando os componentes são diferentes destes tipos (Minha Casa, Minha Vida, Juros, Multa, Correção, etc.):

**Valor da Comissão Paga Cliente:**

Este campo apresentará ao usuário o valor da comissão paga pelo Cliente na mesa de negociação e que foi descontado do Valor de Financiamento deste Componente

**Ordem de Desconto da Comissão:**O preenchimento deste campo é realizado no cadastro de [Modelos de Cálculo da Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766) e a sua edição somente pode ser realizada no momento do cadastro da [Proposta da Venda](https://tdn.totvs.com/pages/viewpage.action?pageId=569502422), no Portal de Imóveis, onde o Corretor, caso tenha permissão, pode alterar a ordem que a Comissão paga na Mesa e que será descontado dos componentes geradores de parcelas.

Na interface de cadastro das Condições de Financiamento do TCGI, este campo é somente para leitura,

Para ser priorizado, este campo deve ser preenchido com um valor numérico maior de 0 (zero).

**Data base para cálculo de vencimento inicial das parcelas:**  
Informe a data de vencimento **da primeira parcela**.

Se este componente de entrada já existir na Modalidade escolhida para esta venda, este campo poderá ser preenchido automaticamente com a data da venda.

**Periodicidade:**  
Informe a periodicidade de vencimento das parcelas de que serão criadas.

**Exemplo:**

* 1 para vencimento mensal;
* 3 para vencimento trimestral;
* 6 para vencimento semestral;
* 12 para vencimento anual.

**Modelo de Cálculo:**  
Informe o Modelo de Cálculo usado para geração e correção das parcelas financiadas. Para saber mais sobre os Modelos de Cálculos existentes no sistema clique aqui:

No mesmo grupo de componentes, não podemos ter componentes com modelos de cálculos diferentes. Caso seja necessário, a modalidade de venda deverá ter obrigatoriamente mais de um grupo.

**Valor Dia Útil:**  
Informe o dia útil para o vencimento da parcela deste componente caso este seja fixa, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.

Este campo somente estará habilitado se o parâmetro "Utiliza dia útil" estiver marcado.

**Data Emissão:**  
Informe a Data de Emissão para as parcelas do componente.  
**Código Ligação Entre Grupos:**  
Informe o Código Ligação Entre Grupos para a geração dos números de Nota Promissória.  
Para saber maiores informações sobre **Nota Promissória**.  
  
**Parâmetros:**  
  
**Utiliza dia útil:**  
Marque este campo quando for utilizar o campo Valor Dia Útil para o pagamento da parcelas.  
**Indica o tipo de parc. seguro:**  
Marque este campo para informar que este componente terá o valor do seguro calculado, caso exista um componente de seguro no mesmo grupo.  
**Filial:**  
Informe a Filial que será gerada para os lançamentos no RM Fluxus.  
**Departamento:**  
Informe o Departamento que será gerado para os lançamentos no RM Fluxus. Este campo será habilitado somente se o parâmetro "Editar Departamento", no cadastro de Componente dentro das Modalidades, estiver marcado.  
**Centro de Custo:**  
Informe o Centro de Custo que será gerado para os lançamentos no RM Fluxus. Este campo será habilitado somente se o parâmetro "Editar Centro de Custo", no cadastro de Componente dentro das Modalidades, estiver marcado.  
**Natureza Orçamentária Financeira a Receber:**  
Informe a Natureza Orçamentária Financeira a Receber que será gerada para os lançamentos no RM Fluxus.  
**Natureza Orçamentária Financeira a Pagar:**  
Informe a Natureza Orçamentária Financeira a Pagar que será gerada para os lançamentos no RM Fluxus.  
**Editar Tabela Opcional 1:**  
Marque este campo quando o usuário poderá incluir ou alterar a Tabela Opcional 1 que será gerado para os lançamentos no RM Fluxus.  
**Editar Tabela Opcional 2:**  
Marque este campo quando o usuário poderá incluir ou alterar a Tabela Opcional 2 que será gerado para os lançamentos no RM Fluxus.  
**Editar Tabela Opcional 3:**  
Marque este campo quando o usuário poderá incluir ou alterar a Tabela Opcional 3 que será gerado para os lançamentos no RM Fluxus.  
**Editar Tabela Opcional 4:**  
Marque este campo quando o usuário poderá incluir ou alterar a Tabela Opcional 4 que será gerado para os lançamentos no RM Fluxus.  
**Editar Tabela Opcional 5:**  
Marque este campo quando o usuário poderá incluir ou alterar a Tabela Opcional 5 que será gerado para os lançamentos no RM Fluxus.  
**Tipo de Receita:**  
Informe o Tipo de Receita que será gerado para os lançamentos no RM Fluxus. Este campo será habilitado somente se o parâmetro "Editar Receita na venda", no cadastro de Componente dentro das Modalidades, estiver marcado.  
**Tipo de Documento a pagar:**  
Informe qual o tipo de documento este componente irá utilizar no módulo financeiro. Este campo traz os dados cadastrados previamente no Empreendimento ou nos parâmetros do tipo de parcela. Este campo é utilizado quando o componente for de devolução (no distrato) ou algum outro componente que gera parcelas a pagar.  
**Tipo de Documento a receber:**  
Informe qual o tipo de documento este componente irá utilizar no módulo financeiro. Este campo traz os dados cadastrados previamente no Empreendimento ou nos parâmetros do tipo de parcela. Válido para qualquer componente gerador de parcelas a receber, como financiamento, sinal, anual, etc.
