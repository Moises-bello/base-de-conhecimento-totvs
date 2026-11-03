---
article_id: 360020863311
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a9de38db9d2121587d5f7264fc9b802c298918c65057688b32c7a3eb47b8049e
fetched_at: '2026-06-28T22:38:53.994403+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível criar saldo
  do produto no armazém de destino na Transferência de Produtos?
type: support-article
updated_at: '2021-07-06T14:55:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020863311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-criar-saldo-do-produto-no-armaz%C3%A9m-de-destino-na-Transfer%C3%AAncia-de-Produtos
---

**Dúvida**

É possível criar saldo do produto no armazém de destino automaticamente nas transferências via MATA260/MATA261?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Quando se tenta realizar a transferência do saldo de um produto cujo este mesmo não possui saldo no armazém destino, é apresentada a mensagem de Help **A260LOCAL**

**Problema:**O armazém informado como destino não existe para este produto

Desta forma, se faz necessário criar o saldo inicial do produto via MATA220 (mesmo que zerado) para posteriormente efetuar a respectiva transferência do saldo.

**Solução**

Mediante esta necessidade, é possível realizar a configuração do parâmetro MV\_VLDALMO para que no ato da transferência não seja validada a existência na tabela SB2 do saldo existente no devido armazém e seja criado automaticamente o respectivo saldo em seu local de destino:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017234271/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017234311/mceclip1.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
