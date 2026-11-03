---
content_hash: ddbb191308594babf6384327f98ef488ad7d74c0b004d8cc8fba9a5ddce53166
fetched_at: '2026-06-29T00:09:58.137972+00:00'
page_id: '451262345'
product: rm
source: tdn-rm
title: Contabilização de Mútuo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451262345
version: 6
---

A contabilização de mútuo é um processo que realiza a contabilização de extratos em uma coligada diferente da utilizada. Ou seja, da coligada "01" para coligada "02".  
Este processo poderá ser originado a partir da visão de lançamentos, da emissão de cheques ou do processo de transferência, pelo cadastro de extrato de caixa.

**Contabilização a partir de lançamentos (Baixa/Cheque)**

Ao baixar um lançamento ou emitir cheque, usando a conta/caixa global que foi cadastrada a contabilização do lançamento será feita na coligada "01"  e a contabilização do extrato de caixa será feita na coligada "02". Se os defaults da conta caixa e os defaults contábeis de Mútuo estiverem preenchidos na conta caixa, o processo de geração/contabilização do extrato será realizado automaticamente.

Caso não estejam informados, será exibida uma tela para se atribuir os dados para a geração do extrato e sua respectiva contabilização.

**Contabilização a partir do extrato (Saque Transferência)**

Ao incluir um extrato manual utilizando a operação Transferência e a conta caixa de mútuo, o extrato de deposito e sua contabilização serão gerados na coligada de destino.

Veja Também

[Procedimentos para realizar Contabilização do mútuo](http://tdn.totvs.com/pages/viewpage.action?pageId=493640244)
