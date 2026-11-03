---
article_id: 360012658392
category: Ativo Fixo - Taxa Regulamentadas
content_hash: 4209e2469048f1104b73edf55a2d8a793e3ee25de54a26db79841151901dcbb4
fetched_at: '2026-06-28T22:41:51.476696+00:00'
product: protheus
section_id: 1500001536121
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA010 e ATFA030
type: support-article
updated_at: '2023-12-04T18:59:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012658392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA010-e-ATFA030
---

**Ocorrência**

Após migrar da **versão 11.80 para a versão 12 do Protheus** não consigo mais utilizar as rotinas **ATFA010 e ATFA030 no módulo de Ativo Fixo**.

**Ambiente**

Protheus – Contabilidade Gerencial – 12.1.17

**Causa**

Isso ocorre devido as rotinas **ATFA010** (Cadastro de Ativo)**e ATFA030** (Baixa de Ativo) **estarem descontinuadas**.

**Solução**

Para substituir a rotina de Cadastro de Ativo, foi criada a rotina **ATFA012(Cadastro de Ativo)**, a razão dessa alteração, foi a necessidade das mudanças de algumas funcionalidades para **MVC.**

**Mais detalhes:**<http://tdn.totvs.com/display/public/PROT/ATF0016-+CTRDES12_Cadastro+de+Ativo_ATFA012_P12>

Para substituir a rotina de Baixa de Ativo, foi criada a rotina **ATFA036(Baixa)**, que foi alterada pelo mesmo motivo da ATFA010.
