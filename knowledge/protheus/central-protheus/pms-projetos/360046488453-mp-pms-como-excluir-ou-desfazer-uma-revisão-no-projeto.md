---
article_id: 360046488453
category: PMS - Projetos
content_hash: c36bcb19156e166d9c7701f53e71668c0c640a5d2908441a7ba4854174e43fb6
fetched_at: '2026-06-28T22:37:15.008679+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Como excluir ou desfazer uma revisão no projeto
type: support-article
updated_at: '2021-04-29T21:12:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046488453-MP-PMS-Como-excluir-ou-desfazer-uma-revis%C3%A3o-no-projeto
---

**Dúvida**É possível excluir, desfazer ou alterar uma revisão realizada no projeto?

**Ambiente**Microsiga Protheus – Gestão de Projetos – A partir da versão 11.80  
  
**Solução**Por padrão não é possível alterar, desfazer ou excluir uma revisão realizada no projeto.

O parâmetro**MV\_PMSRBLQ**,indica se o início de uma revisão será obrigatório para efetuar a alteração na estrutura do projeto.

* **Conteúdo**
  + S – Sim: não permite executar alteração na Estrutura do Projeto sem antes Iniciar uma revisão;
  + N – Não: permite executar alteração na Estrutura do Projeto sem antes Iniciar uma revisão. Não recomendado, pois permite ao usuário realizar alterações na Estrutura do Projeto sem registrar no histórico de revisões, perdendo assim totalmente o seu propósito.
