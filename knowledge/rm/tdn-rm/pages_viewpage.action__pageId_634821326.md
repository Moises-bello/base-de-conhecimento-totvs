---
content_hash: b2022edae4a74aadcfe03f0e215a7d1f0e0f445f8d1681ca09541778424834f6
fetched_at: '2026-06-29T00:11:06.427096+00:00'
page_id: '634821326'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Etapas do funil de vendas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634821326
version: 3
---

Portal de Imóveis possui uma visão dos processos de venda através de um funil parametrizável. Este funil consiste em demonstrar o processo da venda desde o cadastro da pessoa até a finalização da venda com sucesso ou não.

Parametrizar o funil de vendas consiste basicamente em definir os nomes das etapas do funil e associar a estas etapas as situações de proposta. Feito esta parametrização teremos a visão do funil de vendas no menu CRM > Funil de Vendas, conforme imagem acima.

Para realizar a parametrização acesse backend > globais > Etapas Funil Vendas

Na parametrização do funil as etapas Clientes Novos e Em Atendimento são fixas e não podem ser excluídas.

* **Clientes Novos** – estarão registrados nesta etapa todos os clientes cadastrados e sem nenhuma anotação na timeline  e sem nenhum interesse registrado. Esta será sempre a etapa de numero 1 do funil - *Obs: para acessar a timeline do cliente no menu CRM > Pessoas, edite uma pessoa cadastrada.*

* **Em Atendimento** – são todos os clientes que possuem anotações de acompanhamento na timeline ou possuem interesses registrados. Esta será sempre a etapa de número 2 do funil

Parametrização do funil 

Ao cadastrar novas etapas devemos somente preencher os campos solicitados de acordo com as descrições abaixo:

* **Titulo**: nome da etapa
* **Ordem**: posicionamento da etapa na tela do funil.
* **Vincular com situações de propostas:** quando marcado abrirá uma janela que permitirá selecionar qual situação de proposta está vinculada com a etapa do funil de vendas. Quando parametrizamos este vinculo, o funil de vendas movimenta de forma automática as propostas pelas etapas definidas no funil

* **Configurações de alertas**:

+ **Dias sem atividade**: quantidade de dias sem nenhuma movimentação na proposta
+ **Cor** que a janela do funil ficara para propostas que atingirem os dias sem atividade
+ **Enviar e-mail para superior**: informará ao superior que a proposta já está parada no funil de vendas a X dias (definidos no primeiro parâmetro)
+ **E-mails adicionais**: outras contas de e-mail além do superior que receberão esta notificação.
