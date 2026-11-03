---
article_id: 360056055273
category: CRM - Dúvidas Gerais
content_hash: fbb65d5f1957e4f291e593f8196da80c5fc72ae038bf3d7ab87624fc65e3fc92
fetched_at: '2026-06-28T22:40:27.494257+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Parâmetro MV_CRMUAZS
type: support-article
updated_at: '2024-04-25T12:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056055273-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Par%C3%A2metro-MV-CRMUAZS
---

**Dúvida**

Configuração do parâmetro MV\_CRMUAZS.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Solução**

A configuração do parâmetro MV\_CRMUAZS  é para determinar qual configuração de permissão é priorizada ao ao logar no módulo CRM:

* **MV\_CRMUAZS = .T.** (é priorizado a configuração do **Papéis de Usuários CRMA600** do módulo CRM)
* **MV\_CRMUAZS = .F.** (é priorizado a configuração do **Papel de Trabalho CFGA550** do Configurador)
