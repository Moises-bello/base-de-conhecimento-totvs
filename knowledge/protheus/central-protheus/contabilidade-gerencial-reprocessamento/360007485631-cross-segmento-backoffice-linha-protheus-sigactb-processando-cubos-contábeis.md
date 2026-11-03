---
article_id: 360007485631
category: Contabilidade Gerencial - Reprocessamento
content_hash: be9785047e615cca201131400f47fe739bb9445f6b414c9b2fb2c736dd637e91
fetched_at: '2026-06-28T22:40:41.988645+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Processando Cubos Contábeis
type: support-article
updated_at: '2022-05-23T20:25:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007485631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Processando-Cubos-Cont%C3%A1beis
---

**Ocorrência**Após o reprocessamento contábil sistema entra em loop e exibe a mensagem "Processando Cubos Contábeis"

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
   
  
 **Solução:**

Desative o parâmetro:   
  
MV\_CTBCUBE, igual a 0 (zero), para desativar esse reprocessamento.
