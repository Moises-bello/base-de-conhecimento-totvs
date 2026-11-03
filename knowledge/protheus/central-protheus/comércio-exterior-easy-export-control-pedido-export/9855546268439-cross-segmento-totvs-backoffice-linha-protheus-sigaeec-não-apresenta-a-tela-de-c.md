---
article_id: 9855546268439
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: fe2ce08e2ce21ad78d59458e14dd82a7d8a91710564f89d5ceb89ab5d723b0c7
fetched_at: '2026-06-28T22:36:59.080892+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEEC - Não apresenta a
  tela de contabilização ao incluir um Recebimento Antecipado (RA)
type: support-article
updated_at: '2022-10-28T17:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9855546268439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-N%C3%A3o-apresenta-a-tela-de-contabiliza%C3%A7%C3%A3o-ao-incluir-um-Recebimento-Antecipado-RA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Não apresenta a tela de contabilização ao incluir um Recebimento Antecipado (RA), como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**A contabilização é efetuada pelo módulo Financeiro e existe um tratamento para que a tela não seja exibida quando a integração estiver sendo efetuada via rotina automática. A inclusão do Adiantamento é efetuada pelo módulo de Exportação através de uma rotina automática com o Financeiro, desta forma a tela da contabilização não é apresentada, a não ser que haja alguma inconsistência no lançamento padrão.  
Esta é uma regra atual do módulo Financeiro que está efetuando a contabilização.
