---
article_id: 39585167816087
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c01abe9c6dbb107b717241beade566d6925202b90998a5c5a2830edc5bc98f81
fetched_at: '2026-06-28T22:38:58.427718+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Uso do campo B1_ESTSEG
  para garantia de estoque
type: support-article
updated_at: '2026-04-07T20:59:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39585167816087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Uso-do-campo-B1-ESTSEG-para-garantia-de-estoque
---

O campo Segurança (B1\_ESTSEG) no TOTVS Protheus estabelece uma margem de reserva para evitar ruptura no estoque, garantindo saldo mínimo durante variações de demanda ou atrasos. O sistema usa esse valor como gatilho para gerar automaticamente Solicitação de Compra ou Ordem de Produção quando a necessidade ameaça consumir essa reserva, mantendo o saldo acima do limite definido.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39585196806935) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Qual é a finalidade do campo Segurança (B1\_ESTSEG) e como o sistema realiza o cálculo de necessidade de compras ou produção quando este campo está preenchido?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O campo Segurança (B1\_ESTSEG) tem como objetivo estabelecer uma margem de reserva para mitigar riscos de ruptura no estoque. Ele garante que o saldo de um produto não chegue a zero durante oscilações de demanda ou atrasos de fornecedores, evitando assim a paralisação da linha de produção.

**O sistema utiliza esse valor como um ponto de gatilho**: sempre que uma necessidade, como um empenho ou uma venda, ameaçar consumir essa reserva, o Protheus gera automaticamente uma Solicitação de Compra (SC) ou uma Ordem de Produção (OP) para manter o saldo acima do limite definido.

**Exemplos práticos de funcionamento:**

1. Produto com saldo zerado e **B1\_ESTSEG** configurado com 10:

   Ao gerar uma Ordem de Produção que exige o empenho de 100 unidades, o sistema identificará a necessidade de suprir o empenho (100) somada à reserva de segurança (10). O resultado será a geração automática de uma Solicitação de Compra de 110 unidades.
2. Produto com saldo de 10 unidades (garantia já em estoque) e **B1\_ESTSEG** configurado com 10:

   Caso seja gerado um novo empenho de 100 unidades, o sistema solicitará a compra de apenas 100 unidades. Isso ocorre porque a quantidade de segurança já está presente fisicamente no estoque, não sendo necessário criar uma nova reserva para esse montante.
3. Segue um print de exemplo do processo acima, caso venha efetuar a inclusão da nota sobre o produto que tenha o estoque de segurança com um saldo de 100 unidade, distribuindo para uma Ordem de Produção informado no campo **D1\_OP![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39585196807575)**

   Será apresentado o seguinte Help não se tratando de um erro, mas sim de um alerta sobre a quantidade empenhada em relação a quantidade que você vai efetuar o documento de entrada em relação ao estoque de segurança possuir um saldo de 10 unidades.

   **Não desejo essa validação, quero que o saldo seja referente ao valor empenhado no Documento de Entrada, o que fazer?**

   **R:** No padrão não existe essa possibilidade, apenas via customização no documento de entrada ou via Central Colaborativa.

   **Saiba mais:**

   [Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
