---
article_id: 360053509253
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 2b454373a900f3a65348b0b668a2aeaf90fe40d669a1564aa1accf7966748733
fetched_at: '2026-06-28T22:45:21.075503+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - TOP Error -19 - MEMO FIELD CONTENT TOO
  BIG
type: support-article
updated_at: '2024-09-24T19:43:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053509253-RH-Linha-Protheus-TAF-eSocial-TOP-Error-19-MEMO-FIELD-CONTENT-TOO-BIG
---

**Dúvida**

Ao transmitir os eventos para o e-Social, ocorre o erro: **TOP Error -19 - MEMO FIELD CONTENT TOO BIG**

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - À partir da release 12.1.33

**Solução**

1 - Acesse o arquivo de configuração do *DBAccess* **(dbaccess.ini)** e nesse arquivo adicione ou altere os parâmetros conforme abaixo na seção **[GENERAL]**:

**TopMemoMega=3**

**MaxStringSize=30**

2 - Abre o arquivo **appserver.ini** do TSS e adicione ou altere o parâmetro na seção **[GENERAL]**:

**TopMemoMega=3**

**MaxStringSize=30**

3 - Reinicie os serviços do TAF (Protheus) e reavalie as pendências no monitor do e-Social.
