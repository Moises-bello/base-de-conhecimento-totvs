---
article_id: 360037717774
category: Call Center - Telemarketing
content_hash: 17c71085c4af30e2e54d19ddec3ac98fe22f474eeabdba39b11991b02515cde7
fetched_at: '2026-06-28T22:41:29.400386+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - variable is not an object  on
  TK272CARGATMK(TMKA272.PRW)
type: support-article
updated_at: '2024-04-25T12:40:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037717774-Cross-Segmentos-Backoffice-Protheus-SIGATMK-variable-is-not-an-object-on-TK272CARGATMK-TMKA272-PRW
---

**Ocorrência**

Ao consultar o histórico do cliente no Call Center, ocorre o erro:

**variable is not an object  on TK272CARGATMK(TMKA272.PRW) 15/05/2018 11:43:40 line : 1227**

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Causa**O erro era ocasionado devido a uma inconsistência no binário (APPSERVER).

**Solução**

A correção foi efetuada no **APPSERVER** a partir da **release oficial 13.2.3.48 para a release 12.1.17** e **17.3.0.25 - COMPATÍVEL COM RELEASE 12.1.23 E SUPERIORES,** já expedidas e publicadas na Central de Downloads.: **[https://suporte.totvs.com](https://suporte.totvs.com/),** seção de Downloads.

1. Efetue o download do último **APPSERVER,** conforme o release utilizado:

APPSERVER VERSAO 12 WINDOWS 13.2.3.48 ATÉ A RELEASE 12.1.17 -  **<https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657319>**

APPSERVER VERSAO 12 LINUX 13.2.3.48 ATÉ A RELEASE 12.1.17 - **<https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657318>**

APPSERVER LOBO GUARA VERSÃO 12 WINDOWS X64 BUILD 17.3.0.20-**<https://suporte.totvs.com/portal/p/10098/download#detail/737297>**

2. Atualize o APPSERVER do seu ambiente .

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
