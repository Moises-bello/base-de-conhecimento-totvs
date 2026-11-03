---
article_id: 4412153252375
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 637a9bb5ce73579c2630da6e6a7c6e09e9d843db6cc860c0c6797bf3d5fd49c2
fetched_at: '2026-06-28T22:39:47.800515+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tabela responsável
  pela descrição da condição de pagamento
type: support-article
updated_at: '2021-11-04T13:07:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412153252375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tabela-respons%C3%A1vel-pela-descri%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento
---

**Dúvida**Qual a tabela das descrições da rotina de condição de pagamento dos campos **descrição em português (Y6\_DESC\_P)** e **descrição em Inglês (Y6\_DESC\_I)**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Todo o campo memo vem com uma chave de código de informada. É só acessar via APSDU ou via banco de dados, pesquisar na tabela SY6 qual a chave da condição de pagamento que foi criada:

![sy6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412157798679/sy6.PNG)

Ao copiar estas chaves e só efetuar a pesquisa na tabela **SYP (descrição dos campos MEMO)** que a descrições da condição de pagamento português e inglês serão exibidas.

![SYP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412152876567/SYP.PNG)
