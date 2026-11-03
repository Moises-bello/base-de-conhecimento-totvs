---
article_id: 360042322754
category: Financeiro - Contas a Receber
content_hash: 22ab79d2ed704015b174b937334ab5235124076236f7662271c8abc274b76772
fetched_at: '2026-06-28T22:38:12.664773+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA040 - Funcionalidade do campo Taxa Moeda
type: support-article
updated_at: '2025-06-05T20:12:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042322754-MP-SIGAFIN-FINA040-Funcionalidade-do-campo-Taxa-Moeda
---

**Dúvida**Qual a funcionalidade do campo **Taxa moeda** na rotina **FINA040**?  
  
**Ambiente**Migrosiga Protheus - Financeiro - A partir da versão 12. 

**Solução**

Diferentemente da variação cambial, cujo valor da moeda pode ser atualizado no momento do login no sistema ou por meio da rotina **MATA090 ("Moeda")**, a **taxa contratada (taxa fixa)** é informada exclusivamente no momento da criação do título, por meio do preenchimento do campo "Taxa Moeda".

Uma vez definida, essa taxa não sofre alterações decorrentes de variação cambial no momento da baixa, independentemente do valor da moeda cadastrado no sistema na data da operação.
