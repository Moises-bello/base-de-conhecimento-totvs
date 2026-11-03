---
article_id: 23687885851927
category: Materiais - Compras (SIGACOM)
content_hash: 8a2f08d1e2b59ec741807f5f4328b3a3364e35bb9be10cabd0391d7badc35705
fetched_at: '2026-06-28T22:41:16.039303+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Restringir a Inclusão
  de Pedidos Apenas para Usuários Compradores?
type: support-article
updated_at: '2024-05-23T12:54:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23687885851927-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Restringir-a-Inclus%C3%A3o-de-Pedidos-Apenas-para-Usu%C3%A1rios-Compradores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23687896472983) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

É possível configurar o sistema para permitir apenas que usuários compradores incluam pedidos de compras?"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Protheus Compras - Todas as versões

**Solução**

Temos uma configuração específica que Restringe a inclusão de Pedidos de Compra sem Solicitação de Compra vinculada aos Usuários Compradores. Para ativá-la, é necessário preencher o parâmetro **MV\_RESTINC** com **S**.

Quando um usuário que não seja Comprador tentar incluir um Pedido de Compras e o parâmetro **MV\_RESTINC** estiver definido como **S**, será exibido o Help abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23687896474775)

Para permitir que usuários Compradores possam incluir Pedidos de Compras sem Solicitação de Compras, mesmo com o parâmetro **MV\_RESTINC** habilitado, acesse a rotina **COMA087** - **Cadastro de Compradores** e configure o campo **'Ped sem SC' (Y1\_PEDIDO)** como **'1-Sim'** conforme print abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23687896477719)**

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que é o Cadastro de Compradores MATA087 / COMA087 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024650292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-%C3%A9-o-Cadastro-de-Compradores-MATA087-COMA087?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao selecionar a opção incluir no pedido de compras, o sistema apresenta help A120COMP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024404532-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-selecionar-a-op%C3%A7%C3%A3o-incluir-no-pedido-de-compras-o-sistema-apresenta-help-A120COMP?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao salvar o pedido de compras, o sistema apresenta help A120RESTR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4500895030039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-salvar-o-pedido-de-compras-o-sistema-apresenta-help-A120RESTR?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
