---
article_id: 11958978475927
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1ad5212b452f06685207dd50a5edfcd8d0161842c2a41c8b1377215fc1b8f0a8
fetched_at: '2026-06-28T22:42:09.084085+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 60 da DAPI?
type: support-article
updated_at: '2024-06-13T17:46:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11958978475927-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-60-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 60 - Vendas** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 60 - Vendas** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 60**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**7101/7102/7105/7106/7127/7651/7654**
