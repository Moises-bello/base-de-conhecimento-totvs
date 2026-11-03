---
article_id: 1500004820081
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 78e25fbf2d857204e1e48c0758c897fb1c07ae32b29828fd3d11032bacee2d4f
fetched_at: '2026-06-28T22:38:28.558832+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Estrutura de
  Vendas
type: support-article
updated_at: '2021-05-13T18:22:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004820081-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Estrutura-de-Vendas
---

**Dúvida**Qual a diferença das rotinas  FATA070 e CRMA240  (Estrutura de Negócios) ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Versão 12

**Solução**A configuração/Estrutura para o módulo Faturamento (**FATA070**) e CRM (**CRMA240**) são diferentes e independentes. 

A Estrutura de Negocio do CRM está associada diretamente ao Cadastro do Vendedor no módulo SIGACRM. Apesar de as rotinas terem o mesmo Layout, são rotinas diferentes, onde a Estrutura de Negócio do SIGACRM possui funcionalidades a mais em comparação a rotina via Faturamento.

No CRM o sistema sempre irá validar a tabela AO4 que é referente sobre privilégios.   
O Faturamento não tem o controle e validação pela tabela AO4, o controle são das tabelas:

* AA3 - Representantes
* ACA - Grupos de Representantes
* SA3- Cadastro de Vendedores

O cadastro pelo Faturamento  permite organizar, de forma hierárquica, os grupos, representantes e Unidades de Negócio de uma estrutura. A partir da definição da estrutura é possível consultar as oportunidades de venda e suas etapas, efetuar apontamentos de visita, agendar visitas de representantes, entre outras opções.

**Saiba mais  
<https://tdn.totvs.com/x/iw1tFQ>**

**<https://tdn.totvs.com/x/1KPCF>**
