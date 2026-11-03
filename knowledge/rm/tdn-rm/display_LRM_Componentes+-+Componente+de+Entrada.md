---
content_hash: 996c894df1f014a66a5f94ccbba94e1d0cc2c510efe84904c938811a42002625
fetched_at: '2026-06-29T00:09:48.567394+00:00'
page_id: '435105192'
product: rm
source: tdn-rm
title: Componentes - Componente de Entrada
type: documentation
url: https://tdn.totvs.com/display/LRM/Componentes+-+Componente+de+Entrada
version: 10
---

Dentro deste componente é possível definir os valores da parcela de entrada.   
Esta tela possui os seguintes campos:

**Tipo entrada**  
Os valores podem ser definidos utilizando Percentual ou Valor.   
Se for selecionado Percentual o sistema irá habilitar o campo Principal (%), se for selecionado Valor o sistema irá habilitar o campo Valor Financiado.  
  
Principal (%):  
Caso a empresa trabalhe com Tabela de Preço, informe o % sobre o qual o valor da parcela de Entrada será calculado em relação ao valor da subunidade caso este seja fixo. Se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.

Exemplo

Se um apartamento custa R$ 100.000,00 e no campo % estiver com o valor 10, o valor total deste componente será R$ 10.000,00;

Valor Financiado:  
Informe o valor total do componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.

Quantidade de Parcelas:  
Informe o número de parcelas que serão criadas para este componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.

Fórmula para Calcular o Valor Total ou Percentual:  
Informe uma fórmula para calcular o valor percentual ou o valor financiado, para que no momento da cópia da modalidade o valor financiado a regra geradora seja preenchido.

Fórmula para Cálculo:  
Informe uma fórmula para que no momento da geração do plano seja calculado o valor da parcela da geradora.  
  
**Vencimento**

Periodicidade:  
Informe a periodicidade das parcelas de entrada que serão criadas caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.

Exemplo

```
1 mês, 3 meses, 15 dias, etc;
```

Prioridade de Vencimento:  
Informe a prioridade de vencimento da parcela deste componente caso este seja fixa, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.   
Este campo serve para determinar qual parcela irá vencer primeiro caso tenha outras vencendo na mesma data.

Quantidade de Dias Úteis:  
Informe o dia útil para o vencimento da parcela deste componente caso este seja fixa, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.

Este campo somente estará habilitado se a *flag "*Considerar dia útil no cálculo do vencimento" estiver marcada.

**Portal**A fim de atender a demanda do Portal de Venda de Incorporação (PVI) e de outros eventuais portais de venda que possam vir a integrar com o TOTVS Incorporação, foram criados os seguintes campos informativos:

Meses de Carência para Início da Parcela:  
Será informado o número de meses para que o portal calcule da data de início da parcela baseado na data da proposta Web, que equivale da data da venda, para isso foi criado o campo no "Componente da Modalidade da Venda" associado a Tabela de Preço.  
Percentual mínimo aceito na Proposta de Venda:  
Campo destinado ao controle de aprovação de proposta no portal, onde o usuário deverá indicar o percentual mínimo sobre o valor total da proposta que o componente da venda deve representar. Este campo está associado a Tabela de Preço.

Exemplo

Deve ter no mínimo 30% no componente de sinal.

Percentual máximo para dedução da comissão:  
Campo destinado ao controle de aprovação de proposta no portal, onde o usuário indicará qual será o percentual máximo em cada parcela do componente que poderá descontar o valor da Comissão. Este campo está associado a Tabela de Preço.

Exemplo

Supondo uma venda de R$ 100.000,00 onde o sinal será de 3%, ou seja R$ 3.000,00.  
Já a comissão do vendedor será de R$ 2.000,00.  
O campo "Percentual máximo para dedução da comissão" é igual a 50%  
Só poderá ser descontada da parcela a título de comissão um valor máximo de R$ 1.500,00.

false

Informações Complementares

---
