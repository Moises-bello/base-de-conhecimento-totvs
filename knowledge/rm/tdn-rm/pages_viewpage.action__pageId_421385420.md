---
content_hash: 26f9c49afa17bf3a51360b1bb7770e141eefe71f28e23f2d822fc67eb0c24884
fetched_at: '2026-06-29T00:09:15.585788+00:00'
page_id: '421385420'
product: rm
source: tdn-rm
title: Apropriação de lançamentos Financeiros Avulsos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385420
version: 2
---

Para que a apropriação seja realizada é necessário que o título não esteja vinculado a nenhum movimento e que o mesmo possua rateio, informando projeto e tarefa.

Para que os Lançamentos sejam apropriados o é necessário informar nos parâmetros de projeto (F6)|Financeiro|Geral, que possui integração com  Totvs Gestão Financeira  e qual a data a ser considerada pelo Totvs obras Projetos, quanto ao título financeiro e o campo de Referencia data da apropriação pode ser alterada de acordo com cada necessidade. A apropriação será feita pelo valor original do lançamento e rateio, sendo assim, caso haja um valor inferior ou superior na baixa do lançamento, o mesmo não será considerado na apropriação. A partir daí os valores das apropriações aparecerão no cronograma, como é feita a apropriação de movimentos.

**Este processo de apropriação no cronograma através de movimentações de títulos no financeiro pode conter três fluxos:**

**1.** Ao gerar um movimento através de contrato do Totvs Obras e Projetos é gerado movimento no Núcleos. Ao emitir a Nota Fiscal no Núcleos desse movimento, o valor dessa Nota Fiscal é apropriado no Cronograma. Caso esse movimento em que foi emitido a Nota Fiscal gere financeiro é gerado um lançamento no módulo Financeiro. A partir desse lançamento gerado no financeiro, qualquer movimentação seguinte, como Emissão de Fatura e Acordo Financeiro não são mais apropriados, uma vez que a Nota Fiscal emitida no Núcleos já o apropriou. (Para que a Nota Fiscal gerada no Núcleos Aproprie, o tipo de movimento deve estar configurado "Gerar Apropriação" em seus parâmetros).  
 **2.** Caso envie um movimento do Totvs Obras e Projetos de um contrato que gere diretamente o movimento financeiro sem que seja emitido uma Nota Fiscal no Núcleos, este movimento será apropriado no cronograma diretamente. Caso seja realizada alguma movimentação posterior com esse lançamento como a Inclusão da Fatura ou Acordo Financeiro, o mesmo não será apropriado novamente, uma vez que sua geração do Totvs Obras e Projetos para o Financeiro já gerou essa apropriação no cronograma.  
 **3.** Os lançamentos financeiros incluídos **manualmente** e que tenham preenchidos as informações de rateio de **Projeto e Tarefa** são apropriados diretamente no Cronograma. A partir dessa apropriação, qualquer movimentação nesse lançamento como Acordo Financeiro e Emissão de Fatura, não vão ser mais apropriados, uma vez que essa apropriação foi realizada na inclusão manual do lançamento.   
 **Importante:** A apropriação é realizada apenas para movimentos do tipo "A PAGAR", sendo assim, movimentos do tipo "A RECEBER" não são considerados como apropriação.  
 Outro ponto de atenção é que o movimento gerado diretamente no financeiro respeitará os parâmetros do tipo de movimento. Ou seja, caso exista parâmetros que alterem o valor do movimento, como por exemplo, fórmulas para calculo do valor líquido, esta alteração deverá ser considerada no cronograma apropriado.
