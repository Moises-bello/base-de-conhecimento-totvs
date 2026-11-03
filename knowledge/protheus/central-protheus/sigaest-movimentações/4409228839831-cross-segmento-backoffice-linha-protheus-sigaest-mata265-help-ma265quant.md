---
article_id: 4409228839831
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b7ae9e0f1109615f4f9f73bd721b471de73f8fffe8ac7a1f10873b453c331ffa
fetched_at: '2026-06-28T22:38:57.065487+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - HELP MA265QUANT
type: support-article
updated_at: '2025-03-12T11:41:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409228839831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-HELP-MA265QUANT
---

**Dúvida**  
Oque fazer quando ocorre o Help MA265QUANT?  
  
**Ambiente**

A mensagem de validação MA265QUANT está verificando se a quantidade disponível não ultrapassou o saldo à ser distribuído, com isso além de validar a quantidade na 1a unidade, válida também a segunda unidade para o endereçamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409217883671)

Pode ser validado o saldo atual do produto, pressionando a tecla F4 em cima do cadastro do produto.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409217906583)

Veja que o saldo disponível, é menor que o saldo a ser endereçado.

**Solução**Diminua a quantidade a ser distribuída. Verifique também se o campo DA\_QTSEGUM está preenchido corretamente com o fator de conversão. Confira o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26957774160663)

Caso o campo esteja em branco, é necessário excluir o movimento gerado e lançá-lo novamente para que o fator de conversão correto seja apresentado.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
