---
content_hash: e9cb9b7a215c3c13e92988d0a1e310102ee689d07b33a1661164ca70678a9bbd
fetched_at: '2026-06-29T00:09:15.536018+00:00'
page_id: '421385405'
product: rm
source: tdn-rm
title: Cálculo do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385405
version: 5
---

O valor do contrato será exibido após associar as tarefas ao contrato e aditivos caso exista.

Existem dois modos de cálculo do Contrato:

1) Se o parâmetro Geral ‘***[Permite realinhamento sobre o total do contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=421385201)***’ estiver selecionado:

O contrato será calculado considerando os valores atuais, ou seja, o somatório do valor total dos itens.  
Onde valor total do item = Qtde Contratada \* Valor unitário atual

2) caso não esteja selecionado:

O cálculo do contrato irá verificar se houve realinhamento de valor nos itens associados.  
Assim o valor do contrato será o somatório do valor total dos itens associados.  
Onde o Valor Total do Item = Qtde Medida \* Valor Unitário Liberado + (Saldo Qtde \* Valor Unitário Atual)  
Onde Saldo Qtde = Qtde Contratada – Qtde Medida  
  
Quando o usuário identificar que o valor do contrato não está igual ao somatório do valor (Qtde \* Valor Atual) dos itens associados, pode se tratar de um  
realinhamento de valor, onde o usuário deve analisar o anexo *Item de Contrato*.  
Nesse caso um ou mais itens do contrato serão duplicados na tela.  
O usuário deverá habilitar a visualização da coluna Valor Unitário Liberado (fica inativa por default).  
Assim será possível verificar qual era o valor unitário antigo associado ao item do contrato.  
Nesse cenário o usuário deve fazer o seguinte cálculo:  
Se a quantidade medida for menor ou igual a quantidade associada  
Qtde Medida \* Valor Unitário Liberado + (Saldo Qtde \* Valor Unitário Atual)  
Onde Saldo Qtde = Qtde Contratada – Qtde Medida  
Se a quantidade medida for superior a quantidade associada  
Qtde Contratada \* Valor Unitário Liberado  
Esse é o cálculo realizado para identificar o Valor Total do Item no contrato. O valor do contrato será o somatório do valor total dos itens associados.  
 

Ao realizar medição e liberá-lá o valor do contrato não será afetado, porém o saldo contratual será atualizado.
