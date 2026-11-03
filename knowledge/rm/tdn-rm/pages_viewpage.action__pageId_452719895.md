---
content_hash: a1e6e09ebc72a7f0611adcf75940c4cb372083255e867f142adb925a4fc3c666
fetched_at: '2026-06-29T00:10:10.641110+00:00'
page_id: '452719895'
product: rm
source: tdn-rm
title: Código de Cálculo 210 - Pensão Alimentícia Judicial RRA Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719895
version: 2
---

É o valor do evento do código de cálculo 197 - DIF PENSÃO ALIMENTÍCIA FÉRIAS referente as diferenças do ano anterior a competência atual.   
 Este evento é do tipo Base de Cálculo, valor e sem incidência.  
    
 **Exemplo**  
 Funcionário com cálculo de férias em 01/06/2017 a 30/06/2017  
 Em Junho de 2018 o Funcionário teve um aumento de salário retroativo ao mês 06/2017  
 Executando o processo de Cálculo de Diferença de Férias referente ao período de 2017.  
 O sistema calculou o evento abaixo:  
 CC 197 - R$ 191,39  
 CC 210 - R$ 191,39  
    
 **Observação**  
 Quando calculada a diferença utilizando o Cálculo de RRA, o valor do evento no campo Valor da Pensão Alimentícia é inserido no histórico de RRA vinculado ao funcionário. Esse valor é informado na DIRF, no campo correspondente, e estornando do valor da Pensão Alimentícia dos rendimentos tributáveis.   
    
 **Atenção**

* Este evento somente será lançado quando a Pensão Alimentícia de Férias do envelope original estiver com a incidência de desconto marcada 'Dedutível IRRF Férias'.
* Caso o Funcionário tenha dois períodos de gozo de férias para serem recalculados as diferenças e um deles foi calculado no ano atual, mesmo com o parâmetro marcado no parametrizador, não é considerado o valor do desconto de Pensão Alimentícia de férias correspondente ao período de gozo do ano atual.
* Na movimentação da Pensão de Dependente é inserido o registro com o valor referente ao evento de CC 197 e com o tipo de movimento 5 - Dif. Férias.

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

  ---

  Códigos de Cálculo
