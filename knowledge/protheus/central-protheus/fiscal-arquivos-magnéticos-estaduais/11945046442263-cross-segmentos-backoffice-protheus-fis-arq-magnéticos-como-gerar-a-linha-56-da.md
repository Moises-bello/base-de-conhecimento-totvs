---
article_id: 11945046442263
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8d6fab2a3cc0b79748b07594c43ecf7c1f5e00e81c23ca800961a85d7e9adfbc
fetched_at: '2026-06-28T22:42:09.072561+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 56 da DAPI?
type: support-article
updated_at: '2024-06-13T17:46:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945046442263-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-56-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a **Linha 56 - Comunicação** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 56 - Comunicação**é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 56**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6301/6302/6303/6304/6305/6306/6307**
