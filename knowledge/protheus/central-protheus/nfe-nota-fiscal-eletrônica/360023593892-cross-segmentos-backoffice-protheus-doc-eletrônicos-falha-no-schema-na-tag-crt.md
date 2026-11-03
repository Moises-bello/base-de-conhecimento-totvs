---
article_id: 360023593892
category: NFe - Nota Fiscal Eletrônica
content_hash: 3513ca920f4dccaf9250f59aea0e3e1a809946016877a9ba99df9403665debfb
fetched_at: '2026-06-28T22:40:06.864469+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Falha no Schema  na
  TAG CRT
type: support-article
updated_at: '2025-07-15T11:49:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023593892-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Falha-no-Schema-na-TAG-CRT
---

**Dúvida**Como corrigir a falha de schema - CRT

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A falha no Schema ocorre devido a **TAG *CRT* que é obrigatória estar** preenchida.  
  
O ***CRT é destacado no XML*** para informar qual o ***regime tributário do emitente*** da Nota Fiscal Eletrônica.

1 - Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar** **MV\_CODREG:** 1 - Simples Nacional, 2 - Simples Nacional - excesso de receita bruta ou 3 - Regime Nacional.

2 - Após isso, **exclua a nota e gere novamente.**
