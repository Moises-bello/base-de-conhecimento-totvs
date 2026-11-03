---
content_hash: 0d6e00f45e6a90d2c60bcf0f185bd65ed2fc8c38c7de996a81953e227e2090c2
fetched_at: '2026-06-29T00:11:13.138228+00:00'
page_id: '656802950'
product: rm
source: tdn-rm
title: Faixa de Crédito (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656802950
version: 6
---

## Visão Geral do Programa

O objetivo deste dataserver é possibilitar a inclusão e alteração de faixa de crédito através de webservice.

Através do dataserver "**EduFaixaCredData**" é possível, por meio do método **SaveRecord**, realizar a manutenção das faixas de créditos, assim como na tela de Faixa de Crédito no TOTVS Gestão Educacional.

Documentações WebService

A documentação à seguir, foram criada, pois existe particularidade **apenas** no método **SaveRecord** no webservice através do dataserver "**EduFaixaCredData**".   
Para outros métodos do WebServices, deve-se seguir as recomendações da Framework TOTVS.

### Método SaveRecord

Este método realiza a inclusão ou alteração de uma faixa de crédito. Deve ser informando o código da coligada e o id da faixa de crédito, além das outras informações que compõe a faixa de crédito.

O sistema irá realizar uma inclusão da faixa de crédito caso o id da faixa de crédito não exista na base. Se o id já existir, a faixa de crédito será alterada de acordo com as informações passadas.

Validações de casas decimais

Este processo foi incluída uma regra de validação de casas decimais para que a utilização dos dados via webservices seja compatível com o número de casas decimais configuradas no sistema.

Ambos os processos de webservice como da tela de Faixa de Crédito, possuem restrições de quantidade de numero de casas decimais para os campos abaixo:

A quantidade de casas decimais para os campo abaixo deve ser conforme a parametrização em  **Educacional | Parâmetros | Tesouraria | Geral 2/3 | Créditos Financ**

* Crédito Inicial (<CREDINICIAL>)
* Crédito Final (<CREDFINAL>)

A quantidade de casas decimais para os campo abaixo deve ser conforme a parametrização em **Financeiro| Parâmetros | Conta a Receber | Manutenção de Lançamentos | Lançamento | Opções Gerais | No Casas Decimais**

* Valor por Crédito (<VALCRED>)
* Valor Fixo (<VALFIXO>)

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o id da faixa de crédito inserida no item SaveRecordResult
