---
article_id: 360028301632
category: Materiais - Compras (SIGACOM)
content_hash: 07a771ab7d94703c75894da39d866a72cd1beabca1a0726184dfb965e0fd8e43
fetched_at: '2026-06-28T22:41:22.085981+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pedido nasce Liberado
  e Log de Aprovação apresenta que o Documento não possui Controle de Aprovação
type: support-article
updated_at: '2024-02-09T19:59:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028301632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pedido-nasce-Liberado-e-Log-de-Aprova%C3%A7%C3%A3o-apresenta-que-o-Documento-n%C3%A3o-possui-Controle-de-Aprova%C3%A7%C3%A3o
---

**Ocorrência**No módulo de compras , ao inserir pedido com controle de alçada e entidade contábil, nasce como LIBERADO. E ao visualizar os aprovadores apresenta o mensagem "Este Documento não possui controle de aprovação ou deve ser aprovado pelo controle de alçada"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028872112/mceclip0.png)

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Causa**O erro ocorre no ambiente, porque SAL contem as 03 entidades compartilhadas e que provavelmente não bate com DBL.  
  
**Solução**Conforme o retorno de nosso desenvolvimento informou que estas duas tabelas necessitam que o compartilhamento sejam iguais, pois a DBL é filha da SAL. 

O sistema validar se a tabela SAL - Grupos de Aprovacao e DBL - Entidades Contabeis X Grp Apr possuem o mesmo compartilhamento.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
