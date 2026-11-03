---
article_id: 4407179650455
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 6f39b6ceff78b4bce01a5994e8a9d7113663817cf0dc1bd3ae9fb87b957ce243
fetched_at: '2026-06-28T22:39:47.819461+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como criar uma
  condição de pagamento que não gera financeiro
type: support-article
updated_at: '2021-08-30T19:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407179650455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-criar-uma-condi%C3%A7%C3%A3o-de-pagamento-que-n%C3%A3o-gera-financeiro
---

**Dúvida**Como criar uma condição de pagamento que não gera financeiro no módulo SIGAEIC?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Para criar uma condição de pagamento que não gere o financeiro é só acessar a rotina de **Condição de Pagamento (EICA060)** ir campo Cobertura (Y6\_TIPOCOB) e informar a opção ***Sem Cobertura***. Ao informar a condição de pagamento no **Purchase Order(EICPO400)** NÃO será criado financeiro.

![SEM_COBERTURA.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407179547671/SEM_COBERTURA.PNG)
