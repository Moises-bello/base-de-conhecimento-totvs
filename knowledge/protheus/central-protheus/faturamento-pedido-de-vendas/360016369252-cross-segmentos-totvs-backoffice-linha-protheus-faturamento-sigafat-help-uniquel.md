---
article_id: 360016369252
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9b7e2df55016feb75814fdf0cf5344f7c957db74b7a6b25b294cdfddf5aae1c3
fetched_at: '2026-06-28T22:38:41.042328+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - HELP UNIQUELINE (Linha Duplicada) no Controle de Reservas MATA430
type: support-article
updated_at: '2022-12-30T18:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016369252-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-HELP-UNIQUELINE-Linha-Duplicada-no-Controle-de-Reservas-MATA430
---

**Dúvida**Ao cadastrar uma reserva com mesmo produto apresenta o **Help Uniqueline** linha duplicada no controle de reservas MATA430.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- a partir da versão 11.80.  
  
**Causa**Ocorre quando é cadastrado itens mais de uma vez no controle de reservas, para o mesmo produto com o mesmo código, porém com lote, endereço, número de série diferente.

**Solução**Esse Help é um comportamento padrão do sistema, sendo assim cadastre um novo controle de reservas quando se tratar do mesmo código do produto.

A forma mais comum  de reproduzir o **Help Uniqueline** é incluir o mesmo produto com a mesma data de validade ou com lote diferente.

Observe, que em meu teste o produto 01 esta em duplicidade com a data validade de 08/06/2019 e ele apresenta o Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029705772/mceclip0.png)

Nesse outro teste, ele possui data de validade e lote diferente, porem é o mesmo produto e apresenta o help:

![help.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741999373079/help.png)

Para gerar a reserva nesses casos, crie duas reservas separadas uma pra cada lote do produto.

Caso o item esteja correto, verifique se já possui Controle de Reserva com esse código, filial, armazém e lote cadastrado. Caso tenha, crie uma outra reserva diferente para atender a solicitação.

**Saiba mais****[Help Uniqueline - Linha Duplicada no controle de Reservas](http://tdn.totvs.com/display/PROT/FAT0249+Help+Uniqueline+-+Linha+Duplicada+no+controle+de+Reservas)**
