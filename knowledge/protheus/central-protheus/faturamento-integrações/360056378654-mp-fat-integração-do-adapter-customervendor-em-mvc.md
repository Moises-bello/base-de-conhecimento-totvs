---
article_id: 360056378654
category: Faturamento - Integrações
content_hash: 006f9397ae4bc34fd35c873e768c2a0fd8b6d3aa2ee607f2adbf446bcbcaf830
fetched_at: '2026-06-28T22:38:26.592042+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP_FAT_INTEGRAÇÃO DO ADAPTER CUSTOMERVENDOR EM MVC
type: support-article
updated_at: '2021-04-28T15:14:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056378654-MP-FAT-INTEGRA%C3%87%C3%83O-DO-ADAPTER-CUSTOMERVENDOR-EM-MVC
---

**Dúvida**Como incluir o ADAPTER CUSTOMERVENDOR em MVC?  
  
**Ambiente**

**Protheus – FATURAMENTO – A partir da versão P12.1.23**

**Solução**

Se o parâmetro  **MV\_MVCSA1**estiver igual a .T., o cadastro de clientes será executado em MVC, ou seja, será utilizada a rotina **CRMA980**.

A configuração do Adpter deve ser:

Rotina = **CRMA980**

Método = Assíncrono

Canal de envio = EAI - PAD.APP

FORMATO = JSON

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095704974/mceclip1.png)
