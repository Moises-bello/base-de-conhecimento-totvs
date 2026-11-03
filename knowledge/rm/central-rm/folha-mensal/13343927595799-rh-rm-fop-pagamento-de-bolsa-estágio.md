---
article_id: 13343927595799
category: Folha Mensal
content_hash: e6c1c4829a4856ffd0b401a0085dc96c6e78e6a7ab80c1751d5b7568839d2f81
fetched_at: '2026-06-28T22:46:57.838644+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Pagamento de bolsa estágio
type: support-article
updated_at: '2025-01-21T19:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13343927595799-RH-RM-FOP-Pagamento-de-bolsa-est%C3%A1gio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:56 min  
  
Dúvida**Como realizar o pagamento de um estagiário no sistema?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Para realizar o pagamento da bolsa de um estagiário no sistemas existem duas opções.  
O evento de bolsa estágio hoje é lançado através dos códigos fixos do funcionário. Atualmente, não temos um código de cálculo do RM que faça o cálculo desse evento em específico. Dessa forma verifique o passo a passo:   
 

**1.** Cadastrar o evento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344175150359)  
Você pode incluir uma fórmula de valor no evento para que leve o valor do salário ou incluir um valor no evento manualmente.

No exemplo abaixo, foi utilizada uma fórmula: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344210141591)

**2.** Incluir o evento nos códigos fixos: [RH - RM - FOP - Códigos Fixos: Cadastro e Parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020421111-RH-RM-FOP-C%C3%B3digos-Fixos-Cadastro-e-Parametriza%C3%A7%C3%A3o?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344306821271)

**3.** Efetuar o lançamento através do grupo de eventos.

**Importante:** É necessário marcar a flag "Lançar códigos fixos":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344330774551)

Evento lançado no envelope: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344431536279)Sendo assim, você poderá criar um grupo de eventos apenas para lançamento de eventos de estagiários, informar o evento de Bolsa estágio em códigos fixos no cadastro do funcionário e marcar na aba "Identificação" a flag **"Lançar códigos fixos"**, na seleção de funcionários marque apenas para ser lançado para estagiários ou selecione a chapa do funcionário.  
  
**Saiba Mais**[RH - RM - FOP - Cadastro de estagiários e funcionários estrangeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409384230935-RH-RM-FOP-Cadastro-de-estagi%C3%A1rios-e-funcion%C3%A1rios-estrangeiros)
