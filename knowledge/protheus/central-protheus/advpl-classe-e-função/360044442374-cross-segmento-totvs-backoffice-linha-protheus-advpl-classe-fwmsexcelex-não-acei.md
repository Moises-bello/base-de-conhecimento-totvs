---
article_id: 360044442374
category: ADVPL - Classe e Função
content_hash: c0b6acd57e404a8c68a6692490922e6b9d9321ec6ebc6dcf4bcb921fba882b93
fetched_at: '2026-06-28T22:40:14.578668+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWMsExcelEx
  não aceita acentuação
type: support-article
updated_at: '2021-06-25T12:14:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044442374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMsExcelEx-n%C3%A3o-aceita-acentua%C3%A7%C3%A3o
---

**Dúvida**Classe FWMsExcelEx não aceita acentuação no preenchimento das células utilizando o método ***addRow.***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O comportamento ocorre na criação da linha (***addRow***) devido a uma proteção interna na geração do xml do Excel onde os acentos são retirados do conteúdo recebido, isso ocorre desde os binários mais antigos.
