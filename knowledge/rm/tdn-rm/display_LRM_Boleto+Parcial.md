---
content_hash: 3b3f8d0b5f8509ae92e8c58dd44477d1e48912dbb098b4c253fab4716e18547b
fetched_at: '2026-06-29T00:09:18.086003+00:00'
page_id: '421388661'
product: rm
source: tdn-rm
title: Boleto Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/Boleto+Parcial
version: 3
---

Na inclusão de boleto de cobrança o usuário poderá optar por gerar boleto parcial informando o valor desejado.

Essa opção só estará disponível para boleto de cobrança onde o lançamento com status "Em aberto" ou "Baixado Parcialmente" e não poderá ser utilizada se o boleto for de Débito Automático. Nesse caso, o valor do boleto será o valor informado no processo de inclusão, não podendo ser alterado o valor do boleto após a emissão. O sistema realiza a validação para que não seja permitido informar um valor maior do que o valor líquido do lançamento.

O boleto poderá ser parcial, com o controle através do parâmetro do Financeiro em: "Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber | Manutenção de Lançamento / Permitir inclusão de boleto parcial", que deve ficar desabilitado se o Parâmetro "Não gerar outro boleto para lançamento após baixa parcial" estiver habilitado.

Caso o parâmetro "Não gerar outro boleto para lançamento após baixa parcial" estiver marcado, não será permitido a inclusão de boletos parciais e também não será permitido vinculo de um novo lançamento a um boleto parcial.  
 O valor do boleto será o valor informado no processo de inclusão e o sistema realizará a validação para que não seja permitido informar um valor maior do que o valor líquido disponível no lançamento.  
 Os boletos poderão assumir o status Inativo quando o valor total líquido do lançamento for baixado.

Por exemplo, um lançamento vinculado a 3 boletos, onde um deles foi incluído com o valor total do lançamento e os outros dois com valores parciais para o mesmo lançamento. Ao baixar um boleto Parcial, a baixa deve ser realizada com o valor parcial que o boleto foi gerado, e ao realizar a baixa do boleto gerado com o valor integral, a baixa será realizada com o valor restante do lançamento. O boleto não baixado, terá o status alterado para inativo não podendo ser realizada nenhuma ação sobre ele.

**Importante:**

Caso por algum motivo, no arquivo de retorno, o banco apresentar um valor de baixa a menor ou a maior para o boleto parcial, o sistema não irá validar os campos "Diferença a Menor" e "Diferença a Maior", considerando apenas o valor baixado no arquivo de retorno.

 Informações Complementares

* [DT - Inclusão de Boleto Parcial](http://tdn.totvs.com/pages/viewpage.action?pageId=285648551)
