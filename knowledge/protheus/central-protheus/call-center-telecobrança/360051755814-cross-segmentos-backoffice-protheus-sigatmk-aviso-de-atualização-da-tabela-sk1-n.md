---
article_id: 360051755814
category: Call Center - Telecobrança
content_hash: 6816957922c4266d7358b138ab588d4a0bcec2fcd101af29df3d719d5c327d8c
fetched_at: '2026-06-28T22:41:28.561569+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Aviso de atualização da tabela
  SK1 na criação da lista de cobrança
type: support-article
updated_at: '2024-04-25T14:07:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051755814-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Aviso-de-atualiza%C3%A7%C3%A3o-da-tabela-SK1-na-cria%C3%A7%C3%A3o-da-lista-de-cobran%C3%A7a
---

**Dúvida**

Ao tentar inserir uma lista de cobrança, ocorre um mensagem de atenção:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082254994)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

A mensagem em questão não é um erro, o sistema está  informando que já tem algum tempo que a rotina de seleção de títulos (**TMKA180**) para geração da  tabela **SK1** foi efetuada, desta forma, para a geração da lista de cobrança será necessário efetuar o processo da rotina de seleção de títulos para atualização da tabela SK1.

Para processar a seleção de títulos basta ir em Call Center, Atualizações, Telecobrança, Seleção de títulos.

Clique no botão gerar e preencha os parâmetros, conforme exemplo abaixo e clique em ok:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082255214)

Ao efetuar a atualização erá possível gerar a lista de cobrança em que a mensagem de atenção apareça novamente.
