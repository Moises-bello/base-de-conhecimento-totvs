---
article_id: 360020063172
category: Call Center - Telecobrança
content_hash: d1fef2aff64f3e5321adb09dc1da941a13e543dd8cfc8538178bbf3a7aec61b7
fetched_at: '2026-06-28T22:41:28.669063+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Operador Call_Center
  X Seleção de Titulos SK1
type: support-article
updated_at: '2022-06-22T17:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020063172-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Operador-Call-Center-X-Sele%C3%A7%C3%A3o-de-Titulos-SK1
---

**Dúvida**Por que ocorre de gerar um atendimento na agenda do operador (**tmka380**) com o operador X e o atendimento ficar com o campo operador diferente, com a informação do operador Y?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- a partir da versão 11.  
  
**Solução**

Isso ocorre pela regra de negocio de não efetuar a cobrança por dois operadores diferentes para o mesmo cliente.

Com isso se esse cliente já tiver uma atendimento em aberto com outro operador, ou seja um outro titulo aberto na **SK1** atrelado ao operador Y.

O sistema atrela todos os demais títulos desse cliente para o mesmo operador para que não ocorra de ser cobrado duas vezes por dois operadores diferentes.

Desta forma quando o operador X incluir o atendimento o mesmo ficara no nome do operador Y.

SAIBA MAIS: **[TMK0048\_Operador\_Call\_Center\_VS\_Seleção\_de\_Titulos\_SK1](http://tdn.totvs.com/pages/viewpage.action?pageId=286745506)**
