---
content_hash: 6487346c1863757a0b3267175e8ad3a0fba1f6326d3bf16c448cd7e0c5ee6733
fetched_at: '2026-06-29T00:09:49.166640+00:00'
page_id: '435105248'
product: rm
source: tdn-rm
title: Aditivo - Alteração de Vencimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105248
version: 8
---

Este tipo de aditivo permite que o usuário altere a data de vencimento das parcelas do plano de financiamento de uma determinada venda.    
Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento. O Sistema permite que o usuário selecione uma nova data para a Parcela desejada, selecionando um novo valor no Campo 'Nova Data de Vencimento'.

Importante!

A partir do Release 12.1.2310 e superiores foi implementada uma Melhoria neste tipo de aditivo, para atualizar a data base dos componentes de juros dos grupos selecionados for do tipo PRICE e neste aditivo, o usuário alterar todas as parcelas em aberto e a data base dele for do tipo de data do componente e no mês do primeiro vencimento e no mês anterior.

Esta melhoria está disponível nos patchs específicos a partir do release citado acime, com data de disponibilização superior à 10/08/2024.

**Restrições e Regras de Validação na Efetivação**  
Ao efetivar um aditivo de alteração de vencimento, o sistema realiza o recálculo do saldo devedor e a simulação de reajustes monetários. Para evitar erros de cotação ou inconsistências financeiras, atente-se aos seguintes pontos:

1. **Boletos Emitidos e Vencidos**  
   Caso existam boletos vencidos e em aberto vinculados às parcelas que estão sendo alteradas, o sistema tentará realizar o reajuste monetário até a data da negociação.  
   Comportamento: Se a moeda do contrato (ex: INCC, IGPM) não possuir cotação cadastrada para o período de atraso ou para o mês de referência do aditivo, o sistema retornará o erro: "A moeda [X] não possui cotação cadastrada para o período: MM/AAAA".  
    **Solução**:   
   1.1.  Verifique se há boletos vencidos e em aberto vinculados às parcelas que estão sendo alteradas.  
   1.2.  Cancele os boletos que estejam em aberto/vencidos antes de processar o aditivo.  
   1.3.  Alternativamente, cadastre as cotações faltantes para o período indicado na mensagem de erro.
2. **Data do Último Reajuste**  
   Certifique-se de que a Data do Último Reajuste do contrato não seja superior à data atual (data no futuro). Datas de reajuste inconsistentes forçam o sistema a buscar cotações inexistentes, impedindo a conclusão do aditivo.

Possui os seguintes tipos de alteração de vencimento:

* + **Alteração:** Este tipo de aditivo permite que o usuário altere a data de vencimento das parcelas do plano de financiamento de uma determinada venda.
  + **Antecipação:** Este tipo de aditivo permite que o usuário antecipe o pagamento das parcelas do plano de financiamento de uma determinada venda, inserindo um desconto de antecipação e alterando a data de vencimento.
  + **Prorrogação:** Este tipo de aditivo permite que o usuário prorrogue o pagamento das parcelas do plano de financiamento de uma determinada venda, inserindo Juros de Prorrogação e alterando a data de vencimento.

[**Utiliza mês comercial no Aditivo de troca de vencimento.**](https://tdn.totvs.com/pages/viewpage.action?pageId=545642153)   

* **Incrementar mensalmente a data de referência:** Ao marcar essa opção, selecionando mais de uma parcela e inserindo um valor no campo Data referência. Ao clicar no botão Aplicar, a primeira parcela selecionada terá como novo vencimento a data inserida no campo, e as demais parcelas irá incrementar um mês o novo vencimento, de acordo com a ordem que se encontra.
* **Fixar todas com a mesma data de referência:** Ao marcar essa opção, selecionando mais de uma parcela e inserindo um valor no campo Data referência. Ao clicar no botão aplicar, todas as parcelas selecionadas terão a mesma data inserida no campo Data de referência.
* **Data referência:** Campo utilizado para inserir uma data, que servirá com base para os novos vencimentos das parcelas.
* **Ignorar Reajuste:**Ao marcar este parâmetro, as parcelas alteradas não serão mais reajustadas pelo sistema.
* **Aplicar:** Esse botão tem como função aplicar o processo de nova data de vencimento as parcelas selecionas, explicados nos parâmetros acima.
* **Limpar:** Esse botão tem como função limpar as alterações realizadas nas parcelas selecionadas.
* **Calcular:** Nos tipos Antecipação e Prorrogação, esse botão tem como função realizar o cálculo de Desconto ou Juros das parcelas selecionadas;
* **Tipo cálculo vencimento:** Possibilita selecionar o tipo de cálculo para a geração de Desconto de Antecipação ou Juros para a prorrogação. Esse campo só exibido quando selecionado os tipos Prorrogação ou Antecipação.
* **Tipo de Cálculo de Vencimento Antecipação:**
* + **Valor Presente:** Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente. A taxa de Juros será convertida para diária e verificado o número de dias de Antecipação.
  + **Valor Presente Parcial:** Este modelo funciona conforme o tipo "Valor Presente", más é para antecipações parciais
  + **Valor Presente Meses:** Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente.
  + **Valor Presente Meses Parcial:** Este modelo funciona conforme o tipo "Valor Presente Meses", más é para antecipações parciais
  + **Percentual Fixo:** Neste modelo, é necessário informar um percentual da Taxa de Juros Fixo. Esta taxa será descontada independente da quantidade de meses de antecipação.
  + **Valor Fixo:** Neste modelo, ao editar as parcelas e informar a nova data de vencimento, podemos informar um valor fixo de desconto na parcela. Não será realizado nenhum cálculo.
  + **Número de Meses Percentual:** Neste modelo, é necessário informar um percentual da Taxa de Juros. Esta taxa será descontada de acordo com a quantidade de meses de antecipação
  + **Número de Meses Valor:** Neste modelo, é necessário informar um Valor de Desconto. Este valor será descontado de acordo com a quantidade de meses de antecipação.
  + **Deságio Mensal:**Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente. A taxa de Juros será convertida para diária e verificado o número de dias de Antecipação, utilizando o cálculo de ano comercial (360 dias) ao invés de ano corrido (365 dias).

* **Tipo de Cálculo de Vencimento de Prorrogação:**

* + **Valor Futuro:** Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Prorrogação de acordo com a fórmula de Valor Futuro. A taxa de Juros será convertida para diária e verificado o número de dias de Prorrogação.
  + **Valor Futuro Parcial:** Este modelo funciona conforme o tipo "Valor Futuro", más é para Prorrogações parciais.
  + **Valor Futuro Meses:** Neste modelo, é necessário informar o percentual da Taxa de Juros Futuro para que o sistema calcule a Prorrogação de acordo com a fórmula de Valor Futuro."
  + **Valor Futuro Meses Parcial:** Este modelo funciona conforme o tipo "Valor Futuro Meses", más é para Prorrogações parciais.
  + **Percentual Fixo:** Neste modelo, é necessário informar um percentual da Taxa de Juros Futuro Fixo. Esta taxa será Inserida independente da quantidade de meses de Prorrogação.
  + **Valor Fixo:** Neste modelo, ao editar as parcelas e informar a nova data de vencimento, podemos informar um valor fixo a ser inserido na parcela. Não será realizado nenhum cálculo.
  + **Número de Meses Percentual:** Neste modelo, é necessário informar um percentual da Taxa de Juros Futuro. Esta taxa será inserida de acordo com a quantidade de meses de Prorrogação.
  + **Número de Meses Valor:** Neste modelo, é necessário informar um Valor a ser inserido. Este valor será inserido de acordo com a quantidade de meses de Prorrogação.

* **Valor Atual Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas sem as alterações.
* **Valor Novo Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas com as alterações.
* **Valor total correção monetária:** Soma dos valores de correção monetária das parcelas.
* **Valor total juros de contrato:** Soma dos valores de juros do contrato das parcelas.
* **Valor total principal:** Soma dos valores principais das parcelas.
* **Valor total líquido em aberto:** Soma dos valores líquido em aberto do contrato.
* **Valor total multas de atraso:** Soma de valores de multa de atraso das parcelas do contrato.
* **Valor total juros de mora:** Soma de valores de juros de mora de atraso das parcelas do contrato.
* **Valor Juros acordo total:** Soma dos valores de juros acordo das parcelas do contrato.
* **Valor Desconto total:** Soma dos valores de desconto das parcelas do contrato.

false

Veja Também

---
