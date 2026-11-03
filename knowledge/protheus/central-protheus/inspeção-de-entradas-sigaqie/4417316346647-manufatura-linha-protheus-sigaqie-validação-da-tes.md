---
article_id: 4417316346647
category: Inspeção de Entradas (SIGAQIE)
content_hash: 30930ab6c42899493e772782e11c45e81487441d2201e5bbfde2a14d4a79c88a
fetched_at: '2026-06-28T22:42:27.186369+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Validação da TES
type: support-article
updated_at: '2021-12-29T11:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417316346647-Manufatura-Linha-Protheus-SIGAQIE-Valida%C3%A7%C3%A3o-da-TES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min** **Dúvida**Como a **TES - Tipo Movimento Entrada e Saída** pode interferir na integração com o **SIGAQIE - Inspeção de Entradas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Se a **TES** utilizada no documento de entrada estiver cadastrada para não controlar estoque, ou seja, quando o campo **F4\_ESTOQUE - Atu. Estoque** da rotina **MATA080 - Atualização da TES** estiver como **N-Não**, não será realizada a integração deste documento de entrada com o **SIGAQIE** mesmo que o produto em questão esteja com todas as parametrizações necessárias para esta integração.
