---
article_id: 4407194847511
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 694522203636c5ff13b1e3777e5d9b89673ff3b250bb63ea51a24be333f3e878
fetched_at: '2026-06-28T22:38:55.663432+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - Como desativar
  a mensagem: " O produto digitado não faz parte da estrutura do produto, confirma
  movimentação?"'
type: support-article
updated_at: '2021-08-26T20:39:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407194847511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Como-desativar-a-mensagem-O-produto-digitado-n%C3%A3o-faz-parte-da-estrutura-do-produto-confirma-movimenta%C3%A7%C3%A3o
---

**Dúvida**

Ao fazer um Documento de Entrada colocando o número da ordem de produção em um produto que não faz parte da estrutura aparece o help abaixo, existe como desabilitar essa mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407181026199/mceclip0.png)

O que fazer para desabilitar essa mensagem?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Esse help é um alerta do sistema informando que a matéria prima que está sendo requisitada no Documento de Entrada não está na estrutura do produto e que quando confirmado vai gerar empenho para o produto a ser produzido.

Caso desejar que esse help não apareça, temos o ponto de entrada A103VSG1 que desabilita a aparecer a mensagem, conforme própria documentação:

[A103VSG1 - Valida a Existência do produto informado na OP.](https://tdn.totvs.com/pages/releaseview.action?pageId=6085262)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
