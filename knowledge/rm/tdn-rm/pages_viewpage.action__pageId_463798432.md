---
content_hash: 685e1d00b166064a8f839e8c0482ef1234bc8764de2bc2f30429b114db8e97f6
fetched_at: '2026-06-29T00:10:15.020922+00:00'
page_id: '463798432'
product: rm
source: tdn-rm
title: Parâmetros de Vinculações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463798432
version: 4
---

**Classificação da Vinculação/Tipo de Vinculação**

Este recurso tem por finalidade a associação de um movimento em outro, associar o movimento classificado como adiantamento em um movimento classificado como controla adiantamento. Para este processo será necessário trabalhar com dois tipos de movimentos distintos, onde um tipo de movimento, em sua parametrização, estará classificado como “Adiantamento” e o outro, classificado “Controla Adiantamento”.

**Retenções**

**Faturamento/Recebimento Parcial por Valor**

Valor Utilizado Movimento:

* Nenhum: O valor do movimento não será utilizado para faturamento parcial por valor.
* Valor Bruto: Será considerado para o faturamento/recebimento parcial o valor bruto do movimento, definido através da Fórmula do Valor Bruto em [Mov - Valores Financeiros 2/4](http://tdn.totvs.com/display/LRM/Valores+Financeiros).
* Valor do Documento: Será considerado para o faturamento/recebimento parcial o valor do documento do movimento, definido através da Fórmula do Valor do Documento em [Mov - Valores Financeiros 2/4](http://tdn.totvs.com/display/LRM/Valores+Financeiros).
* Valor Sub-Total: Será considerado para o faturamento/recebimento parcial o valor sub-total do movimento, definido através da Fórmula do Sub-Total em [Mov - Valores Financeiros 2/4](http://tdn.totvs.com/display/LRM/Valores+Financeiros).

Valor Utilizado Item Movimento: 

* Nenhum: O valor do item do movimento não será utilizado para faturamento parcial por valor.
* Valor Bruto Item: Será considerado para o faturamento/recebimento parcial o valor bruto do item.
* Valor Opcional 1: Será considerado para o faturamento/recebimento parcial o valor opcional 1 do item, definido através da Fórmula do Valor Opcional 1 em [item - Valores Financeiros](http://tdn.totvs.com/pages/viewpage.action?pageId=423938775).
* Valor Opcional 2: Será considerado para o faturamento/recebimento parcial o valor opcional 2 do item, definido através da Fórmula do Valor Opcional 2 em  [item - Valores Financeiros](http://tdn.totvs.com/pages/viewpage.action?pageId=423938775).
* Valor Total: Será considerado para o faturamento/recebimento parcial o valor total do item, parametrizado em [Item - Preços](http://tdn.totvs.com/pages/viewpage.action?pageId=423938806) ao habilitar o campo “Editar Preço Total”.
* Valor Rateio: Será considerado para o faturamento/recebimento parcial o valor do rateio do item, definido através da Fórmula do Rateio do Item em [Rateio C.Custo - Departamento](http://tdn.totvs.com/display/LRM/Rateio+de+Centro+de+Custo+e+Departamento).
