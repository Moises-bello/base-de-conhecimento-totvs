---
article_id: 4439340806039
category: Materiais - Compras (SIGACOM)
content_hash: 4a8dccc62afc7bb87a7766beae15e5d20feeb6b1452dfe9a3e5081f0e36d2f6c
fetched_at: '2026-06-28T22:41:15.803492+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é possível automatizar
  o cadastro de Produtos x Fornecedor ?
type: support-article
updated_at: '2024-07-01T16:29:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439340806039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-poss%C3%ADvel-automatizar-o-cadastro-de-Produtos-x-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19603405643159) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**É possível automatizar o cadastro de Produtos x Fornecedor ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**

É possível realizar a inclusão automática do Cadastro de Produto x Fornecedores, através das rotinas Documento de Entrada (MATA103) e Pedido de Compra (MATA121).

Na rotina de Documento de Entrada (MATA103), o parâmetro F12 **"Incluir Amarração**" precisa ser configurado igual a "**Sim**".

Abaixo imagem de como o parâmetro F12 do Documento de Entrada deve ficar:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439273173655)

Dessa forma, ao confirmar a inclusão do Documento de Entrada, será incluída automaticamente uma amarração com as informações básicas do Produto e do Fornecedor da NF, no cadastro de Produto x Fornecedor (MATA061) da tabela SA5.

Para realizar a inclusão automática do cadastro através da rotina Pedido de Compra (MATA121), o parâmetro F12 **"Incluir Amarração**" precisa ser configurado igual a "**Sim**".

![](https://totvssuporte.zendesk.com/attachments/token/MUEVVGVbpC6Gl8W3OAUNeAAhp/?name=image.png)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
