---
content_hash: f240380a5ddce4f7cea042a1c80a9f07acc79c6efc5119491706e58cf3aa44d3
fetched_at: '2026-06-29T00:09:52.473115+00:00'
page_id: '439682339'
product: rm
source: tdn-rm
title: Vínculos de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439682339
version: 5
---

Os vínculos de contratos só aparecem para contratos a pagar e do tipo timesheet.

Para contrato de insumos do tipo Timesheet surgiu a necessidade de se criar uma opção de vínculo entre contratos, que será feita através de um novo anexo.

Esse vínculo entre contratos apenas poderá ocorrer se o vínculo for entre um contrato a pagar vinculado a um a receber.

O vínculo entre contratos apenas poderá ocorrer se os dois contratos obtiverem o mesmo número de períodos, caso contrário o vínculo não será feito.

Este processo apenas será considerado na liberação de períodos, onde o contrato que contém o vínculo só terá o seu período liberado, se o período correspondente do contrato vinculado já estiver liberado.

Caso o parâmetro de controle de status do contrato esteja habilitado, será possível vincular contratos se o status do contrato estiver em Andamento, caso o controle não esteja habilitado o vínculo poderá ser feito em qualquer status.

No exemplo acima, foi definido no momento do vínculo, que o período “0001” do contrato “001/2013” está vinculado ao período “0001” do contrato “002/2013”, sendo assim, os outros períodos serão vinculados automaticamente, considerando a sequência, como mostram as cores do exemplo.

Informações Complementares

[Timesheet](http://tdn.totvs.com/display/LRM/Timesheet)
