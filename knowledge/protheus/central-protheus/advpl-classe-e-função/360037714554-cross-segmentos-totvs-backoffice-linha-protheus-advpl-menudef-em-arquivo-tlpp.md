---
article_id: 360037714554
category: ADVPL - Classe e Função
content_hash: eef2c1525f9d1cf9e9a5d422e2a013b01a03685c8f62e7198d9b85b8c8a99d42
fetched_at: '2026-06-28T22:40:20.504632+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - MenuDef em arquivo
  TLPP
type: support-article
updated_at: '2024-11-07T11:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037714554-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-MenuDef-em-arquivo-TLPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27622421702807)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao utilizar MenuDef em arquivo TLPP, não aparece as opções de menu  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – até a versão 12.1.2310  
  
**Solução**Para versões até a release 12.1.2310, o MVC padrão ADVPL não irá funcionar nos fontes com extensão .TLPP.  
Atualmente a linguagem TL++ não realiza a chamada de StaticCall() (chamar funções estáticas de outros fontes).

Porém a partir da release 12.1.2410 poderá utilizar o MVC em TLPP.

**Saiba mais:**

[MVC em TLPP - release 12.1.2410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27606833750423-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-criar-uma-rotina-em-MVC-utilizando-TLPP)
