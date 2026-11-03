---
article_id: 360042819814
category: Financeiro - Contas a Receber - LCDPR
content_hash: ffbf44c5dcfc5bd1c85f639a655ab545ebad0a4bebe9780d44d69a946c789055
fetched_at: '2026-06-28T22:38:15.793505+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Dados necessários para
  configuração do LCDPR
type: support-article
updated_at: '2022-03-24T19:05:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042819814-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Dados-necess%C3%A1rios-para-configura%C3%A7%C3%A3o-do-LCDPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:02 min**

**Dúvida**Quais os dados necessários para configuração e utilização do LCDPR ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12

**Solução**

1. Realizar o **Cadastro de pessoas** através da rotina (**FINA031**).

 2. Realizar o **Cadastro de imóveis** através da rotina (**FINA029**).

 3. Acessar a rotina **Cadastro de Bancos (MATA070)**.

* Para que determinada conta bancária (**tabela SA6**) esteja disponível para seleção no Extrator **LCDPR**, é necessária a definição dessa conta como sendo de Titularidade Própria e o campo “**Pais conta**” esteja preenchido conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058431353/mceclip0.png)

4. Acessar a rotina **Cadastro de Naturezas (FINA010)** e preencher o campo que se encontra na aba “**Outros**” como “**SIM**”, conforme abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058431433/mceclip1.png)

**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=520110581>
