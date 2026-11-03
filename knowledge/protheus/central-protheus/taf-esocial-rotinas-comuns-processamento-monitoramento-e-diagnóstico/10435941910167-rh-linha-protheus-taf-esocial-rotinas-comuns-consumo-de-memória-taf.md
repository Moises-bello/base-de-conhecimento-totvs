---
article_id: 10435941910167
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: deac7a5626fe8dcfe5988c92801cf8b40b4ebd3233d83b2bd1d5a4359dafef86
fetched_at: '2026-06-28T22:45:21.178589+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Consumo de memória TAF
type: support-article
updated_at: '2026-06-26T12:15:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10435941910167-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Consumo-de-mem%C3%B3ria-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23692367066903) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**O serviço do TAF está consumindo muita memória.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões  
  
**Solução**Na situação que for observado consumo de memória, orientamos verificar se existe schedules ativados.

Pare os schedules e verifique se o consumos de memória é estabilizado.

A ativação de schedules para integrar eventos ao TAF, e transmissão automática ao eSocial, consome memória, mesmo que não tenha usuários no sistema, o schedule trabalha em segundo plano.

**Documentação relacionada:**

[RH - Linha Protheus - TAF - eSocial - Configuração - Como configurar o TAF para transmitir eventos automaticamente (Schedule) para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23472097356439)
