---
article_id: 360045205793
category: PMS - Projetos
content_hash: d773a39adcb94640e930958d789e2dcac0fb6e6eea62ccc267517572e225311e
fetched_at: '2026-06-28T22:37:14.986889+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS -  FLUXO DE CAIXA NO GESTÃO DE PROJETOS
type: support-article
updated_at: '2021-04-29T21:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045205793-MP-PMS-FLUXO-DE-CAIXA-NO-GEST%C3%83O-DE-PROJETOS
---

**Dúvida**

Como visualizar o Fluxo de Caixa nos projetos e como o Fluxo de Caixa é preenchido?

**Ambiente**

Microsiga Protheus - A partir da release 11.80.  
   
**Solução**O fluxo de caixa permite ver de forma analítica as obrigações e as receitas que serão geradas pelo projeto. É importante ter ciência que o fluxo não está relacionado com o desempenho ou o valor ganho pelo projeto.  
  
Esta consulta refere-se a valores previstos de compras, vendas, despesas, receitas, saldo do dia, variação do dia (em %), entradas, saídas e saldos acumulados, considerando que:

* Os dados realizados não aparecem no fluxo;
* As entradas e saídas são previstas;
* Existem custos não refletidos no fluxo de caixa (por exemplo, utilização de material que não gerou compra, pois já estava disponível).

Representa simplesmente o valor de caixa que será necessário para afrontar os próximos períodos do projeto.  
Os valores considerados pelo fluxo são:

* Pedidos de vendas (é considerada a condição de pagamento para saber a data da receita);
* Pedidos de compras (é considerada a condição de pagamento para saber a data da despesa);
* Receitas (contas a receber);
* Despesas (contas a pagar).

**Para que apresente os valores de forma correta no Fluxo de Caixa é de extrema importância que o campo na TES F4\_MOVPROJ (Movimentação do Projeto) esteja preenchido.**

* **Despesa** para as operações que gere o títulos a pagar, como o Documento de entrada.
* **Receita** para as operações de venda, quando gera o título contas a receber.

**Demostração de como pode ser visualizado o fluxo de caixa do projeto:**Menu - Consultas - projetos - Painel de Controle.  
Selecione o projeto - clique em outras ações - Fluxo de Caixa.

**![fluxo_de_caixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360061271354/fluxo_de_caixa.gif)**
