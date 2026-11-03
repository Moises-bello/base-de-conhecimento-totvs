---
article_id: 1500004896162
category: SIGAEST - PODER DE TERCEIROS
content_hash: e35cb3c173c90b5de2131ab5c745ad7ac16828dcff6c7989a8cde950cb070a3a
fetched_at: '2026-06-28T22:39:03.282953+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: MP - SIGAEST - É possível fazer o retorno (devolução) de remessa de Poder de
  Terceiros com custo diferente da remessa?
type: support-article
updated_at: '2021-04-28T15:10:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004896162-MP-SIGAEST-%C3%89-poss%C3%ADvel-fazer-o-retorno-devolu%C3%A7%C3%A3o-de-remessa-de-Poder-de-Terceiros-com-custo-diferente-da-remessa
---

**Dúvida**Ao efetuar uma remessa para o Poder de Terceiros, o produto foi enviado à custo X. Na devolução (e baixa) do Poder de Terceiros, é possível que o custo seja diferente do custo da remessa?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Sim, é possível desde que o custo seja menor do que a remessa. Para isso, basta criar/habilitar o parâmetro MV\_LIBESB6 conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006465622/mceclip0.png)

Observação: Para este parâmetro funcionar, o parâmetro **MV\_BLOQSB6** precisa estar desabilitado, ou seja, com conteúdo = **.F.**ou caso não existir no ambiente, não é necessário criá-lo.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)
