---
article_id: 360019755091
category: NFe - Nota Fiscal Eletrônica
content_hash: 9261fd994d49ac87ef72b4cca03c5659da32ef75ec4cce55a5d84c3d67b30ed7
fetched_at: '2026-06-28T22:40:03.712579+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 0 notas transmitidas
type: support-article
updated_at: '2026-06-12T19:28:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019755091-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-0-notas-transmitidas
---

**Dúvida**Como corrigir a mensagem **“Foram transmitidas 0 nota(s) em 00:00”**na transmissão da nota?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Para todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Este erro de **0 notas transmitidas**, ocorre pelos seguintes motivos:

1 - Verifique se a série utilizada está vinculada a especie SPED através do parâmetro **MV\_ESPECIE Ex: 1=SPED;** (isso se verifica no configurador)

![MV_ESPECIE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11543397742359)

Ao gerar a nota os campos **F2\_ESPECIE ou F1\_ESPECIE, F3\_ESPECIE e FT\_ESPECIE** devem estar como **SPED**

**![F1_ESPECIE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11544147516055)**

2 -  Verifique se a nota foi gerada na tabela **SF3, SFT e CD2 ?**

Se o TES utilizado na nota estiver com os campos **L. Fiscal ICM = Não, L. Fiscal IPI = Não** (quando houver incidência de IPI) não serão gerados os valores destes impostos nas tabelas SF3 / SFT. Quando os impostos não são gerados nas tabelas ***SF3 / SFT*** o sistema não gera o XML e não há transmissão da nota.

![LIVRO_ICM_E_IPI.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11544333193111)
