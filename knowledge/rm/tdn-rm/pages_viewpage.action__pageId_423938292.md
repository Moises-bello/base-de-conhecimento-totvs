---
content_hash: 9922005fbe0327f8bdcbda03a8acbd43045365560710c2418f1a0987dc464fc2
fetched_at: '2026-06-29T00:09:26.178471+00:00'
page_id: '423938292'
product: rm
source: tdn-rm
title: 'Exemplo 2:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938292
version: 2
---

Quando no campo "Considerar no Valor de Aquisição" for selecionado "Valor Financeiro", o sistema não irá aplicar a regra Valor x Quantidade Informada, pois o Valor Financeiro já contempla o total do item da nota. Sendo assim, a regra inverte. O sistema irá considerar Valor / Quantidade Original para identificar o valor unitário de cada item, o resultado será o Valor x Quantidade Informada.   
Caso a nota a ser integrada tenha notas de devoluções associadas, o sistema irá desconsiderar nas quantidades, a quantidade que consta na nota de devolução.  
   
É realizada uma compra de 5 cadeiras, porém 2 cadeiras estão com defeito. Neste cenário no módulo de compras é realizada uma nota de devolução com quantidade igual 2.  
Ao integrar a nota fiscal identificamos a nota de devolução vinculada e são abatidos os dois itens que foram devolvidos, neste exemplo o sistema irá integrar apenas 3 itens. Ou seja, ao abrir a tela de composição de patrimônio será apresentado o campo "Quantidade" = 3.  
Nos casos de notas com devoluções associadas e parametrizado "Valor Financeiro" como valor de aquisição, o mesmo também será ajustado, pois o "Valor Financeiro" corresponde ao item com quantidade igual a 5, neste exemplo será ajustado para que o "Valor Financeiro" seja referente a quantidade igual a 3.  
Valor Financeiro = (Valor Financeiro / Quantidade Original) x (Quantidade Original – Quantidade Devolvida).
