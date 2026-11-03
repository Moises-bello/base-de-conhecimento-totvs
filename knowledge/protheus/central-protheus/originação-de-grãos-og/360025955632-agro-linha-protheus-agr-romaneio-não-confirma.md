---
article_id: 360025955632
category: Originação de Grãos (OG)
content_hash: 23cadbf723323bba04ae658b02c8a334e983cef9c347744f80f44f8624d00a69
fetched_at: '2026-06-28T22:45:44.844243+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio não confirma
type: support-article
updated_at: '2025-05-30T19:25:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025955632-Agro-Linha-Protheus-AGR-Romaneio-n%C3%A3o-confirma
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20649298237463)***Tempo aproximado para leitura: **00:00:30 min****Dúvida**Por que na rotina de **Originação de Grãos - OGA250** ao cadastrar um romaneio do **Tipo 2 - Remessa para Depósito** e tentar a confirmação do registro, não ocorre erro, porém o romaneio não é **Confirmado**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**É necessário validar no dicionário de dados o tamanho dos campos referentes ao código do Romaneio. Caso o tamanho dos campos esteja incoerente é necessário aplicar o compatibilizador **UPDOG**.  
Para validar o tamanho dos campos de código de **Romaneio** é necessário acessar o **APSDU** - **SX3** - **CTRL + F** e filtrar por **CODROM**.
