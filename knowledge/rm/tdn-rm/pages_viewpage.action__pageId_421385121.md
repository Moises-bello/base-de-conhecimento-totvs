---
content_hash: 0c730af8761c1c09dbe5909614408c2e20f25bfe49370ab5130090d631e1536a
fetched_at: '2026-06-29T00:09:14.094028+00:00'
page_id: '421385121'
product: rm
source: tdn-rm
title: Alteração de Item Contratado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385121
version: 7
---

Ao editar o aditivo é possível decrescer ou aumentar a quantidade de um item, isso implicará na alteração dos valores da medição e no valor total do contrato que irá aumentar ou diminuir de acordo com o que for informado.

A alteração da quantidade do item irá diminuir ou aumentar a quantidade de um ou mais itens de contrato. Não haverá restrição a qual item de contrato/item de aditivo (Em andamento) pode ter a sua quantidade contratada decrescida ou aumentada. Haverá restrição em quanto poderá ser decrementado da quantidade, pois o saldo do item contratado não deve ser inferior a zero. Caso já existam medições para o item que sofrerá o decréscimo, só será permitido diminuir até o valor correspondente a medição, pois o valor que já foi medido não pode ser alterado.

Foi contratada a quantidade 100 de um item, e feita à liberação de 20. Ao alterar a quantidade esta pode chegar até a quantidade 20 do item, mas não diminuindo até a quantidade 19, pois já existe medição com a quantidade 20. As informações de decréscimo de quantidade entram em vigor quando o status esta "Em andamento", desde que seja possível reduzir a quantidade.

Quando o aditivo for de supressão ao calcular o contrato o sistema calculará considerando o valor do contrato inicial  mais o valor de aditivo como valor do contrato . E o saldo considerará o valor do contrato menos o valor medido.
