---
content_hash: 956fb1771cf3ea9608098a8f8fbadf55ba58dc80b80b86e7815f03670e69dcaf
fetched_at: '2026-06-29T00:11:37.927517+00:00'
page_id: '780766283'
product: rm
source: tdn-rm
title: DT - Cadastro Global da Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780766283
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão Global |
| País: | Brasil |
| Story : | [DRHCALCRM-4842](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4842) |

## **02. SITUAÇÃO/REQUISITO**

É necessário que em determinada data de demissão o funcionário deixe de ter acesso ao portal e essa data somente será cadastrada pelo gestor quando o funcionário tiver seu desligamento efetivado, mas no caso o parâmetro rescisão calculada fica setado e o funcionário deixa de ter acesso ao portal naquele momento.

Tem então a necessidade de cadastrar apenas os dados da rescisão do funcionário sem calcular para que o parâmetro fique setado com 0(zero) e tenha a data que vai cessar o acesso ao portal.

## **03. SOLUÇÃO**

Será feito um módulo com os seguintes moldes:

Cadastrar os dados da rescisão individual de um grupo de funcionários de acordo com a seleção do usuário

Validações de acordo com o cadastro da rescisão individual e da rescisão coletiva 

Continua com a mesma validação do cadastro para rescisão no futuro, ou seja, somente pode cadastrar no mês e no próximo mês.

Situação do funcionário: 

* Mudança de A para D se a data for no mesmo mês de competência
* Continua na situação A se a data for para o próximo mês - sendo que não pode recalcular o envelope de pagamento após o cadastro da rescisão para o próximo mês.

Na tela de recálculo da rescisão haverá um parâmetro que o usuário poderá escolher informar parâmetros de cálculo da rescisão no momento do recálculo porque no cadastro da rescisão global não será possível selecionar esses parâmetros que tem a ver com o cálculo.

## **04.** **ASSUNTOS RELACIONADOS**

* [Cadastro Global Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=780016519)
