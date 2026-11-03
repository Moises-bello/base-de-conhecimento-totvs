---
article_id: 8346750447767
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 33542b6521ec81f45dc3ac5ffbae16f06747a60fcd60844ed8fb6aee810b80bd
fetched_at: '2026-06-28T22:38:54.382265+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar o
  Controle de Qualidade?
type: support-article
updated_at: '2022-08-22T17:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8346750447767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-o-Controle-de-Qualidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:58 min** **Dúvida**Como Desabilitar controle de C.Q?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para desabilitar o controle de qualidade, siga os passos abaixo:

**Garanta que o armazém de CQ esteja sem saldo para os produtos da empresa.**

Siga abaixo as orientações da documentação que aborda o assunto:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como limpar o saldo (resíduo) do Armazém de CQ (MV\_CQ)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012599901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-limpar-o-saldo-res%C3%ADduo-do-Armaz%C3%A9m-de-CQ-MV-CQ-)

**Efetue os ajustes Cadastrais para que os produtos não sejam direcionados ao Armazém de C.Q**

**Cadastro de Produtos (MATA010)**

**Nota Mínima** (B1\_NOTAMIN) - Este campo indica a Nota Mínima para o Controle de Qualidade para o Produto. Deixe o campo igual à zero (0)

**Produções C.Q** (B1\_NUMCQPR) - Define o intervalo de Produções em que o produto será enviado ao CQ. Deixe o campo igual à zero (0)

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8346449530647/mceclip0.png)

**Amarração de Produto/Fornecedor (MATA061)**

**Contr. Lote**(A5\_SKIPLOT) - Este campo define o intervalo de compras em que o material vindo do Fornecedor em questão será enviado ao C.Q. Se deixado como = 0, nenhuma compra feita deste fornecedor terá seu saldo enviado ao Armazém de CQ.

Exemplo:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8346692807063/mceclip1.png)

OBS: Efetue o procedimento para todas as amarrações entre produto/fornecedores que existirem.

 

Com isso, os saldos dos produtos, seja por Compra ou por Produção, não serão mais enviados ao Armazém de C.Q.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
