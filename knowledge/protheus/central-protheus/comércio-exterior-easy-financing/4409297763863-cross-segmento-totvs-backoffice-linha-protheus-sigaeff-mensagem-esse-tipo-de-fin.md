---
article_id: 4409297763863
category: Comércio Exterior - Easy - Financing
content_hash: 0d2927d369064d9e1e764dbd1b3bcc0e070c0211bfac175583e5016c195293fd
fetched_at: '2026-06-28T22:39:52.955042+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF -  Mensagem: Esse
  tipo de financiamento não pode ser utilizado pois não foi definido um numerário
  para a movimentação  financeira.'
type: support-article
updated_at: '2021-09-23T17:39:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409297763863-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Mensagem-Esse-tipo-de-financiamento-n%C3%A3o-pode-ser-utilizado-pois-n%C3%A3o-foi-definido-um-numer%C3%A1rio-para-a-movimenta%C3%A7%C3%A3o-financeira
---

**Dúvida**Ao criar um Manutenção de contrato (EFFEX400) do tipo ACE o sistema esta exibindo uma mensagem impeditiva no sistema **"AVISO - Esse tipo de financiamento não pode ser utilizado pois não foi definido um numerário para a movimentação financeira."**

![CONTRATO_ACE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409287041943/CONTRATO_ACE.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Finacing* – Todas versões  
  
**Solução**Esta mensagem esta sendo exibida pois o Numerário para movimento bancário no financeiro ERP não foi informado na rotina de tipo de financiamento.

1. Acesse o menu Atualizações\ Tabelas\ **Tipos de Financiamento (EFFFI100)**

2. Alterar o código de financiamento **02 - ACE** e informar o campo **Numerário (EF7\_NUMERA).**
