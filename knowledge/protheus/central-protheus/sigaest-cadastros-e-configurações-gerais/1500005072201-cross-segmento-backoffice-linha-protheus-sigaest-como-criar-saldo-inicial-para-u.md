---
article_id: 1500005072201
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f2527ded56f8727fd9acc120c826707918a1289c48964826beb7212f7989f113
fetched_at: '2026-06-28T22:39:08.127992+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como criar Saldo Inicial
  para um produto que utiliza controle de Lote/Sub-lote?
type: support-article
updated_at: '2024-03-01T20:59:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005072201-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-criar-Saldo-Inicial-para-um-produto-que-utiliza-controle-de-Lote-Sub-lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21745835583895) Tempo aproximado para leitura: **00:04:30 min****

**Dúvida**

Como dar Saldo Inicial em produto novo que irá fazer controle de rastreabilidade por Lote?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Veja abaixo como dar este Saldo Inicial em um produto após cadastrá-lo via MATA010:

**- 1°** - Acesse à rotina Saldos Iniciais - MATA220 e clique em "Incluir";

**- 2°** - Preencha as informações do produto, além de Qtd Inic. Mes (Quantidade Inicial) e Sld. Ini Mês (Saldo financeiro Inicial);

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006881082)

**- 3°** - Clique em "Outras Ações" -> Inf. Lote (Informa Lote);

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007066961)

**- 4°** - Preencha o código do Lote (e sub-lote se necessário);

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006881302)

**- 5°** - Com isso basta clicar em Salvar;

**- 6°** - Com isso é criado, tanto nas tabelas SB2 quanto SB8, o Saldo indicado na rotina MATA220;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007067241)

|  |
| --- |
| ***Informações importantes******:***    Para os casos em que esta incluindo um produto que ***já tem Saldo no sistema***, deve revisar as instruções da FAQ abaixo com um passo a passo para esse cenário.    [SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDIwNjcyNjEyLCJleHAiOjE3MDkzMjI1NzF9.yJy9rNjmt2Xt7vceUIiNvp8WxYwSfBYTYJBWkZiKATE) |

**Saiba mais:**

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
