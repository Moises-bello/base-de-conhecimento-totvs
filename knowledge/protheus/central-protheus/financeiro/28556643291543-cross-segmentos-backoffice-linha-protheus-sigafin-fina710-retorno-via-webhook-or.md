---
article_id: 28556643291543
category: Financeiro
content_hash: 2fa1b0f1437ec7539083bbd69404b1d4017663a8bb80559175a9aed4b7a05e83
fetched_at: '2026-06-28T22:38:03.106590+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 Retorno via
  Webhook - Orientações de configurações
type: support-article
updated_at: '2024-12-16T12:15:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28556643291543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Retorno-via-Webhook-Orienta%C3%A7%C3%B5es-de-configura%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28556643270423) Tempo aproximado para leitura: **00:15:00 min****Dúvida**Retorno via Webhook - Orientações de configurações  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - 12.1.2310]  
  
**Solução**

O banco do Brasil precisa de acesso completo em uma única API para enviar dados dos boleto "**/api/fin/v1/bb/bol/receivables/**"

Porém a empresa não poderá fornecer acesso em todas as API´s que possuem de modo externo, pois caso isso aconteça, qualquer pessoa externa terá acesso as API´s da empresa.

Então a solução seria a empresa publicar um endpont, e esse terá somente acesso a API que o banco do Brasil precisa, ao invés de ter acesso a todas as API´s.

Exemplo:

**https://seuendereco:suaporta/api/fin/v1/bb/bol/receivables/**

**seuendereco:suaporta** → Informar endereço e porta do serviço REST configurado no arquivo appserver.ini.

**/api/fin/v1/bb/bol/receivables/** → API disponível no serviço REST padrão do Protheus preparada para receber o payload de cobrança(boletos) do Banco do Brasil.

**Qual porta deverá ter no endpont publicado?**

Até o momento da criação deste documento, no site do Branco do Brasil está informando que:

Atualmente é permitido o uso apenas da porta padrão HTTPS (443) com a URL ou de uma das portas alternativas (3001 e 50900)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/28556643271959)](https://apoio.developers.bb.com.br/referency/post/64f8763d286aca00129b2ce4)

Após definir a porta, a empresa deverá configurar o seu REST

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/28556653517463)](https://tdn.totvs.com/pages/releaseview.action?pageId=185747842)

**Saiba Mais:**

[Documentação do Banco do Brasil](https://apoio.developers.bb.com.br/referency/post/64f8763d286aca00129b2ce4)

[Webhook - Baixa Títulos (retorno)](https://tdn.totvs.com/pages/releaseview.action?pageId=673798283)

[Web Services REST/Server](https://tdn.totvs.com/pages/releaseview.action?pageId=185747842)
