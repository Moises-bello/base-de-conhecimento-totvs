---
article_id: 7248910756375
category: Faturamento - Cadastros
content_hash: f07e38b0118d0e642e37d50bd530c06c3ebc49765a56e6a0c1b842d3d9e00bd3
fetched_at: '2026-06-28T22:38:36.520250+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – SIGAFAT– Criação de códigos
  de países DDI
type: support-article
updated_at: '2024-03-11T19:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7248910756375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-de-pa%C3%ADses-DDI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Como criar códigos de países na tabela DDI?

**Ambiente**

Cross Segmento - Backoffice (Linha Protheus) – SIGAFAT– todas as versões

**Solução**

Parar criar a tabela de **DDI** com os códigos dos países, será atribuído na tabela **ACJ.**

A inclusão do código**DDI** pode ser realizado clicando na consulta padrão do campo. Através das rotinas:

Cadastro de clientes **(CRMA980)** – Faturamento e CRM

Cadastro de fornecedores **(MATA020)** – Compras

Cadastro de DDI **(TMKA370)** – Call Center

Basta clicar na lupa do campo referente a criação da informação de países com código **DDI** em qualquer das rotinas acima, e depois Incluir na janela que aparecer.

***OBSERVAÇÃO:** A tabela usada no processo é a **ACJ – Códigos DDI***

**Exemplo:**

**Passo 1:** Localizar o campo em qualquer rotina especificada acima (rotina utilizada no exemplo é a de **Cadastro de clientes – CRMA980**)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248753614359/mceclip0.png)

**Passo 2:** Incluir

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248754768407/mceclip1.png)

**Passo 3:** Preencher os campos da tabela **ACJ** e salvar para utilizar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248802104087/mceclip2.png)
