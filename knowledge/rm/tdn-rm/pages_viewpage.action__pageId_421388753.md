---
content_hash: 2b2ab9336055df9c305902e9d6582f38023fd78b150570c6736fad4ddd9c6c0f
fetched_at: '2026-06-29T00:09:18.694678+00:00'
page_id: '421388753'
product: rm
source: tdn-rm
title: Reajuste utilizando a Emissão de Cheque do Totvs Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388753
version: 4
---

Na Emissão de Cheque a receber o serviço de cálculo do valor líquido também deverá reajustar os valores de integração do lançamento para calcular o valor líquido do Lançamento.  
Na associação do cheque ao Lançamento Financeiro deve ser chamado o reajuste e exibir em tela os valores atualizados até uma data que será estabelecida.  Os valores serão efetivados no banco de dados, ao efetivar a  Emissão do Cheque.

Somente as parcelas que estão associadas ao Cheque devem ser reajustadas e caso ocorra o cancelamento do cheque as parcelas devem voltar ao valor de reajuste igual as demais parcelas do grupo.   
Uma vez a parcela estando associada a um cheque e ficar caracterizado uma baixa total a mesma não deve sofrer novos reajustes, caso fique caracterizado uma Baixa Parcial, somente o restante do valor em aberto poderá sofrer novos reajustes (Saldo Devedor).

No Cancelamento do Cheque é chamado o serviço de cancelamento do  [Totvs Imobiliári](http://tdn.totvs.com/x/HLjbCw)o onde será validado se a parcela não tem mais Cheque associado e remover eventualmente o status de cheque associado.   
No cálculo do valor líquido, os juros de mora e a multa por atraso serão calculados baseado na data utilizada para o reajuste e nos valores reajustados. Esses valores serão considerados nas fórmulas. A data da Baixa utilizada pelas fórmulas será a mesma data de referência para os cálculos.

Cheques para o dia (À vista)

Podem ser recebidos para parcelas vencidas, com vencimento hoje e vincendas. A data do reajuste será definida pela parametrização do Plano de Financiamento. Caso a regra seja reajustar até o vencimento, as parcelas vencidas serão reajustadas apenas até o vencimento.

* Parcelas Vencidas – Reajustar a parcela conforme Plano de Financiamento e calcular o encargos financeiros até a data do Cheque.
* Vencimento Hoje – Reajustar a parcela conforme Plano de Financiamento e não há encargos financeiros.
* Parcelas Vincendas – Reajustar a parcela até a data do cheque e não há encargos financeiros.

No caso do Cancelamento do Cheque será chamado o reajuste do Totvs Imobiliário, mas desta vez é necessário que seja verificar a última data de reajuste do grupo para que esta parcela fique reajustada igual as demais parcelas do seu grupo de financiamento. Não haverá problema se for a ultima parcela do grupo pois buscaremos a última data de reajuste da regra que gerou a parcela pois teremos como buscar essa informação do TIN.

Cheques Pré datado

Podem ser recebidos para parcelas vencidas e com vencimento hoje. Quanto a data para reajuste é importante observar o seguinte:

* Parcelas Vencidas – Reajustar a parcela até o vencimento e calcular o encargos financeiros até a data do cheque.
* Vencimento Hoje – Reajustar a parcela até o vencimento e calcular o encargos financeiros até a data do cheque.

Baixa de Cheque pelo Item de Baixa

Será possível realizar o processo de Baixa para cada item de Cheque recebido separadamente.  
Implementado processo na visão de itens de baixa "Baixa de Lançamentos com Cheque Emitido / Recebido".  
Utilizando essa opção, é possível marcar apenas os cheques que devem ser baixados para um lançamento e o processo irá considerar apenas  esses itens na baixa, mantendo os demais cheques em aberto.   
Se existirem cheques baixados e cheques em aberto para o mesmo lançamentos, o status ficará como "parcialmente baixado".
