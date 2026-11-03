---
article_id: 360022206212
category: Call Center - Dúvidas Gerais
content_hash: 77df509c219458858eda3ce13a425c085b5119b510433eb263620d46a9e65632
fetched_at: '2026-06-28T22:41:26.970788+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagem:
  array out of bounds [0] of [4] on A70VEREND'
type: support-article
updated_at: '2021-11-17T20:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022206212-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagem-array-out-of-bounds-0-of-4-on-A70VEREND
---

**Dúvida**

Ocorrência da mensagem: array out of bounds [0] of [4] on A70VEREND no Cadastro de Contato.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Causa**

Ocorre quando os campos **AGA\_PADRÃO** e **AGA\_END** não estão marcados como **Usado** na tabela AGA do configurador, ou ainda os campos não existem no SX3 e no banco de dados.

**Solução**

Marque os campos **AGA\_PADRÃO e AGA\_END** como **Usados** na tabela **AGA**.

Caso os campos não existam na tabela, atualize o Dicionário de Dados do ambiente e execute o UPDDISTR: [**Atualizador de dicionário de Dados UPDDISTR**](https://tdn.totvs.com/x/nJLYCg)
