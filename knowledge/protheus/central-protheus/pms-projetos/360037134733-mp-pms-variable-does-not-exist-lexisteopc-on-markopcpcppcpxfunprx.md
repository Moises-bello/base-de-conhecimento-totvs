---
article_id: 360037134733
category: PMS - Projetos
content_hash: 3febd76c165cdd42db49a2a949d89c33c718f4bc0f73f333cb57c5aa96a79f8c
fetched_at: '2026-06-28T22:37:15.043221+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'MP - PMS - variable does not exist LEXISTEOPC on MARKOPCPCP(PCPXFUN.PRX) '
type: support-article
updated_at: '2021-04-29T21:13:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037134733-MP-PMS-variable-does-not-exist-LEXISTEOPC-on-MARKOPCPCP-PCPXFUN-PRX
---

**Ocorrência**

Ao incluir um item com estrutura na rotina de Projetos **PMSA410** apresenta o errorlog:  
*variable does not exist LEXISTEOPC on MARKOPCPCP(PCPXFUN.PRX).*

**Ambiente**

Microsiga Protheus – a partir da release 11.80.

**Causa**

O problema ocorre quando o parâmetro quando o parâmetro **MV\_SELEOPC**está ativo.  
   
**Solução**

Para solucionar essa ocorrência, desabilite o parâmetro **MV\_SELEOPC.**
