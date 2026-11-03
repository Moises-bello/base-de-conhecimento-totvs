---
content_hash: 6f67f8f5138b579559112a2b139f93ce0b077fe1edeaec61b37d9cd7718923d6
fetched_at: '2026-06-29T00:10:53.206488+00:00'
page_id: '577914914'
product: rm
source: tdn-rm
title: Gerar workflow de aprovação para Pedido e Pedido Extra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577914914
version: 6
---

**Pedido**

Quando a  estiver ativa para Requisição de material, nos parâmetros do projeto corrente, será exibido o processo para Gerar Workflow de Aprovação na tela de pedido:

Esse processo deve ser executado após a criação de um pedido de material, gerando um workflow no TAA, de acordo com o tipo de atendimento informado no parâmetro do projeto.

Após a execução desse processo, é gerado um WF de aprovação que poderá ser consultado através do anexo , conforme abaixo:

Quando o workflow for aprovado, será possível enviar o pedido para Suprimentos/Faturamento, para que seus itens possam ser providenciados:

Caso o workflow seja reprovado, será possível efetuar correções e gerar novo workflow para análise:

**Pedido Extra**

Se a opção "Utilizar fluxo de aprovação para pedido extra" estiver habilitada e mesmo assim optar por utilizar o workflow de aprovação pelo processo ao ativar a integração com o TOTVS Aprovações e Atendimento será exibida uma mensagem perguntando se deseja seguir com a nova parametrização desativando o fluxo antigo.

Ao optar por sim o parâmetro workflow antigo será desabilitado

Quando a  estiver ativa para Requisição de material, nos parâmetros do projeto corrente, será exibido o processo para Gerar Workflow de Aprovação na tela de pedido extra:

Esse processo deve ser executado após a criação de um pedido de material, gerando um workflow no TAA, de acordo com o tipo de atendimento informado no parâmetro do projeto.

Após a execução desse processo, é gerado um WF de aprovação que poderá ser consultado através do anexo , conforme abaixo:
