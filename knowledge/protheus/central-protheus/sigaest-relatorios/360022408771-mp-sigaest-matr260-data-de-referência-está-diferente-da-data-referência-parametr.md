---
article_id: 360022408771
category: SIGAEST - RELATORIOS
content_hash: 88870b30b41cc1a5a459641f15ac3f119c19a05046b0de81b65a434463a57cb5
fetched_at: '2026-06-28T22:39:05.993932+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: MP - SIGAEST - MATR260-  Data de referência está diferente da "Data Referência"
  parametrizada. Por qual motivo?
type: support-article
updated_at: '2021-04-28T15:09:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022408771-MP-SIGAEST-MATR260-Data-de-refer%C3%AAncia-est%C3%A1-diferente-da-Data-Refer%C3%AAncia-parametrizada-Por-qual-motivo
---

**Dúvida**

A "Data Ref" do cabeçalho do Relatório Posição de Estoque - MATR260 está diferente do campo "Data Referência" que parametrizei. Por quê?

**Ambiente**Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

Muitos usuários confundem a "Data de ref" do cabeçalho do relatório com a data de referência da parametrização utilizada na impressão de alguns fontes. Exemplificaremos no relatório MATR260, que possui a parametrização Data Referência.

Na impressão do relatório MATR260, no cabeçalho o campo **Dt. Ref:** faz referência com a data-base que esta logado no ambiente Protheus.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019466332/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019466532/mceclip1.png)

O campo **Emissao:** faz referência com a data do computador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019336491/mceclip2.png)

Na impressão do relatório MATR260, na parametrização a pergunta "**Data Referencia"** é utilizada em conjunto com a pergunta **"Saldo do Prod a Considerar" = "Movimento"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019336671/mceclip3.png)

Abaixo ilustrando as referências:

![data_referencia.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360019467472/data_referencia.jpg)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)*
