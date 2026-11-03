---
article_id: 27165563548183
category: SIGAEST - PODER DE TERCEIROS
content_hash: d104d6c9c69f2363708f159ebecb75b5768c1e99c3fa3473a8d47e63b2380112
fetched_at: '2026-06-28T22:39:03.196455+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP: BLOQLOC3'
type: support-article
updated_at: '2025-03-12T11:40:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27165563548183-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-BLOQLOC3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27165570607127) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Ao realizar uma movimentação de entrada/saída (**MATA103**, **MATA410**) controlando poder de terceiros o help **BLOQLOC3** é apresentado. O que fazer?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165563495831)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Este help é apresentado quando a **TES** informada controla poder de terceiros (**F4\_PODER3 = Remessa/Devolução)**, mas o produto em questão está em um armazém do tipo **"Próprio" (NNR\_TIPO = 2 Próprio).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165563501335)

O próprio campo "**NNR\_TIPO**" explica (ao clicar em F1 com o campo selecionado) referente a cada tipo de armazém:

**"Campo utilizado para definir o tipo de saldo a ser movimentado no armazém.**

**Padrão: será permitido movimentar qualquer tipo de saldo.**

**Próprio: será permitido movimentar qualquer tipo de saldo exceto saldo de terceiros.**

**Terceiros: somente será permitido movimentar saldo de terceiros."**

Ou seja, para que o **HELP** **não seja apresentado**, não deve efetuar movimentação sob poder **de/em terceiros utilizando este armazém**, pois por ele ser próprio o conceito do tipo não permite esta ação.

Uma possibilidade seria selecionar outro armazém com os tipos "**padrão**" ou "**terceiros**", que possibilitaria este tipo de movimentação.

**Saiba mais****:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
