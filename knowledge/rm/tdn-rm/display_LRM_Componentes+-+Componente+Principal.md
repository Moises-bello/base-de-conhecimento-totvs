---
content_hash: 6f36429b309a9f6d1b11a9d618a4084ccde7d7f7dcce374c5b608e63781c34c4
fetched_at: '2026-06-29T00:09:48.616259+00:00'
page_id: '435105205'
product: rm
source: tdn-rm
title: Componentes - Componente Principal
type: documentation
url: https://tdn.totvs.com/display/LRM/Componentes+-+Componente+Principal
version: 7
---

Dentro deste componente é possível definir os valores das parcelas principais.   
Esta tela possui os seguintes campos:  
  
**Tipo Principal**  
Os valores podem ser definidos utilizando Percentual ou Valor.   
Se for selecionado Percentual o sistema irá habilitar o campo Principal (%), se for selecionado Valor o sistema irá habilitar o campo Valor Financiado.

* **Principal (%)**: Caso a empresa trabalhe com Tabela de Preço, informe o % sobre o qual o valor da parcela de Entrada será calculado em relação ao valor da subunidade caso este seja fixo. Se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.

Se um apartamento custa R$ 100.000,00 e no campo % estiver com o valor 90, o valor total deste componente será R$ 90.000,00;

* **Valor Financiado**: Informe o valor total do componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.
* **Quantidade de Parcelas**: Informe o número de parcelas que serão criadas para este componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.
* **Modelo de Cálculo**: Informe o Modelo de Cálculo usado para geração e correção das parcelas financiadas. Para saber mais sobre os Modelos de Cálculos existentes no sistema clique aqui:
* **Fórmula para Calcular o Valor Total ou Percentual:** Informe uma fórmula para calcular o valor percentual ou o valor financiado, para que no momento da cópia da modalidade o valor financiado a regra geradora seja preenchido.
* **Fórmula para Cálculo:** Informe uma fórmula para que no momento da geração do plano seja calculado o valor da parcela da geradora.

No mesmo grupo de componentes, não podemos ter componentes com modelos de cálculos diferentes. Caso seja necessário, a modalidade de venda deverá ter obrigatoriamente mais de um grupo.

**Vencimento**

* **Periodicidade**: Informe a periodicidade das parcelas de entrada que serão criadas caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel. Ex: 1 mês, 3 meses.
* **Prioridade de Vencimento**: Informe a prioridade de vencimento da parcela deste componente caso este seja fixa, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda. Este campo serve para determinar qual parcela irá vencer primeiro caso tenha outras vencendo na mesma data.
* **Quantidade de Dias Úteis**: Informe o dia útil para o vencimento da parcela deste componente caso este seja fixa, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.
* **Data de Emissão**: Este campo já deverá vir preenchido com a data da venda ou a data do aditivo ou a data do distrato, caso o componente seja gerado pelo mesmo.

Este campo somente estará habilitado se a flag "Considerar dia útil no cálculo do vencimento" estiver marcada.

**Portal**  
A fim de atender a demanda do Portal de Venda de Incorporação (PVI) e de outros eventuais portais de venda que possam vir a integrar com o TOTVS Incorporação, foram criados os seguintes campos informativos:

* **Meses de Carência para Início da Parcela**: Será informado o número de meses para que o portal calcule da data de início da parcela baseado na data da proposta Web, que equivale da data da venda, para isso foi criado o campo no "Componente da Modalidade da Venda" associado a Tabela de Preço.
* **Percentual mínimo aceito na Proposta de Venda**: Campo destinado ao controle de aprovação de proposta no portal, onde o usuário deverá indicar o percentual mínimo sobre o valor total da proposta que o componente da venda deve representar. Este campo está associado a Tabela de Preço. Ex: Deve ter no mínimo 30% no componente de sinal.
* **Percentual máximo para dedução da comissão**: Campo destinado ao controle de aprovação de proposta no portal, onde o usuário indicará qual será o percentual máximo em cada parcela do componente que poderá descontar o valor da Comissão. Este campo está associado a Tabela de Preço.

Supondo uma venda de R$ 100.000,00 onde o sinal será de 3%, ou seja R$ 3.000,00, já a comissão do vendedor será de R$ 2.000,00, se o campo "Percentual máximo para dedução da comissão": for igual a 50% só poderá ser descontada da parcela a título de comissão um valor máximo de R$ 1.500,00.Atenção

Em caso de utilização de **fórmula para cálculo**, as propostas geradas pelo Portal de Venda de Incorporação (PVI) não garantem o total funcionamento da fórmula associada. Algumas funções de fórmula podem utilizar um contexto que ainda não existe no momento da execução. Desta forma garantimos apenas funções que utilizam dados dos componentes, como por exemplo quantidade de parcelas, valor financiado, entre outros.

Informações Complementares

---
