---
content_hash: 81d19282bef1d3b495c4e6014a67d67cccba0e57f445302522dd0d87dafd2231
fetched_at: '2026-06-29T00:09:29.291646+00:00'
page_id: '423938864'
product: rm
source: tdn-rm
title: Rateio dos Valores Financeiros
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+dos+Valores+Financeiros
version: 13
---

Os valores extras de 3 a 10 estão disponíveis a partir da versão 12.1.2606.

A parametrização de rateio permite 3 possibilidades, são elas:

* Não aplicar: o rateio não será aplicado ao valor em questão;
* Rateio Proporcional: o rateio será calculado, proporcionalmente, pelo valor bruto interno (KQT \* KPU).
* Rateio Condicional: o rateio será calculado através de média ponderada. O peso aplicado a cada valor de item do movimento é dado por meio da fórmula. A fórmula é definida pelo usuário e deve ser informada por meio do campo **Fórmula do Peso do Rateio para o Item**.

A partir da versão 12.1.2606, devido a inclusão dos campos **Valor Extra 3** ao **Valor Extra 10**, a parametrização de rateio encontra-se organizada em 4 subtópicos. Caso contrário, a parametrização apresentará somente 2 subtópicos, sendo o primeiro e o último da lista abaixo:

Rateio dos Valores Financeiros 1/4

São definidas as parametrizações do movimento para o rateio de **Frete**, **Seguro**, **Desconto**, **Despesa** e/ou **Frente do CTRC**.

Rateio dos Valores Financeiros 2/4

São definidas as parametrizações do movimento para o rateio dos campos **Valor Extra 1** ao **Valor Extra 5**.

Rateio dos Valores Financeiros 3/4

São definidas as parametrizações do movimento para o rateio dos campos **Valor Extra 6** ao **Valor Extra 10**.

Rateio dos Valores Financeiros 4/4

São definidas as parametrizações do movimento para o rateio de **Dedução de Material**, **Dedução de Subempretada** e/ou **Outras Deduções**.

* Caso seja utilizado **Rateio Proporcional** ou **Rateio Condicional**, o Tipo dos [Valores Financeiros](https://tdn.totvs.com/x/1spEGQ) deverá estar configurado como **Percentual** ou **Ambos** para casos que seja necessário proporcionalizar os valores, exemplo: recebimento parcial. Com a opção configurada a pasta Outros Valores apresentará os valores distribuídos nos itens do movimento.
* No item de movimento pasta 'Outros Valores', existe uma lista de campos com a participação do rateio de cada um dos valores financeiros do movimento.   
  Todos estes campos podem ser acessados através de fórmula e podem ser utilizados na rotina de cálculo da base de cálculo.
* Nos casos em que no tipo de movimento está parametrizado que o Desconto do Item e/ou Despesa do item **Afeta o Desconto/Despesa do Movimento**, o respectivo valor do Desconto e/ou Despesa do movimento não é rateado para os itens de movimento.
* Nome dos campos utilizados no Rateio (útil na criação de fórmulas, por exemplo na função TABITM):
  + **RATEIODEDMAT**: Rateio da Dedução de Material;
  + **RATEIODEDOUT**: Rateio de Outras Deduções;
  + **RATEIODEDSUB**: Rateio de Dedução de Subempreitada;
  + **RATEIODESC**: Rateio do Desconto;
  + **RATEIODESP**: Rateio da Despesa;
  + **RATEIOEXTRA1**: Rateio do Valor Extra 1;
  + **RATEIOEXTRA2**: Rateio do Valor Extra 2;
  + **RATEIOFRETE**: Rateio do Frete;
  + **RATEIOFRETECTRC**: Rateio do Frete CTRC;
  + **RATEIOSEGURO**: Rateio do Seguro;
  + **RATEIOEXTRA3**: Rateio do Valor Extra 3;
  + **RATEIOEXTRA4**: Rateio do Valor Extra 4;
  + **RATEIOEXTRA5**: Rateio do Valor Extra 5;
  + **RATEIOEXTRA6**: Rateio do Valor Extra 6;
  + **RATEIOEXTRA7**: Rateio do Valor Extra 7;
  + **RATEIOEXTRA8**: Rateio do Valor Extra 8;
  + **RATEIOEXTRA9**: Rateio do Valor Extra 9;
  + **RATEIOEXTRA10**: Rateio do Valor Extra 10.
