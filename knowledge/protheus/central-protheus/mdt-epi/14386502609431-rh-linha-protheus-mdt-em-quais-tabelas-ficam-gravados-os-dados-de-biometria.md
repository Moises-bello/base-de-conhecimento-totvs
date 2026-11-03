---
article_id: 14386502609431
category: MDT - EPI
content_hash: f6377359ab0a42ba7c9dcd9abfb75da535604695fd5bad4ec96498f890a15d6a
fetched_at: '2026-06-28T22:44:25.435287+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Em quais tabelas ficam gravados os dados de Biometria
type: support-article
updated_at: '2024-07-04T12:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14386502609431-RH-Linha-Protheus-MDT-Em-quais-tabelas-ficam-gravados-os-dados-de-Biometria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24649885970455) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Em quais tabelas ficam gravados os dados de Biometria?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O registro da Biometria da Ficha Médica (MDTA005), fica salvo na tabela de Ficha Médica (TM0), no campo **TM0\_REGBIO** (Biometria) o dado salvo é em criptografia.  
  
Para entrega de EPI por Biometria, fica gravado na tabela TNF, campo **TNF\_ENTBIO** (Entrega Biometria) e devolução **TNF\_DEVBIO** (Devolução Biometria).  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Como configurar o uso da Biometria no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
