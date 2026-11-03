---
article_id: 360019322771
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 75aee9f62acf649a9ea8b2fd2e801926a1d250e4bbbde74faadfac4fef1cf354
fetched_at: '2026-06-28T22:39:22.246880+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: MP - SIGAFIS - Apuração de ICMS UF PR Configuração Parâmetro MV_CRPREPP
type: support-article
updated_at: '2021-04-29T19:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019322771-MP-SIGAFIS-Apura%C3%A7%C3%A3o-de-ICMS-UF-PR-Configura%C3%A7%C3%A3o-Par%C3%A2metro-MV-CRPREPP
---

**Dúvida**Qual parâmetro deverá ser ativado para que a linha 006.01 da apuração do **ICMS** para o estado do Parana referente ao Artigos 406 a 416 do RICMS (Microempresa e EPP) não seja demonstrada automaticamente?

**Ambiente**Protheus - Fiscal - A partir da versão 11.80

**Solução**

É obrigatório informar código de lançamento quando existem lançamentos / ajustes na Apuração de **ICMS**, com o Código 006.01 - **Artigos 406 a 416 do RICMS (Microempresa e EPP)**

Esse lançamento é gerado automaticamente nas notas fiscais ME / EPP

Caso seja um lançamento indevido, configurar o Parâmetro: **MV\_CRPREPP** = .F.
