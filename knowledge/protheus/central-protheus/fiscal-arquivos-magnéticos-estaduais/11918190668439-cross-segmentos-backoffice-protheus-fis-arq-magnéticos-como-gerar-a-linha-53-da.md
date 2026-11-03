---
article_id: 11918190668439
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: e75f768989cbebc12538d8705e2f1fd35e0f4fae65575c737f4d1cb86c3e16a5
fetched_at: '2026-06-28T22:42:09.060473+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 53 da DAPI?
type: support-article
updated_at: '2023-01-25T12:53:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11918190668439-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-53-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida** Como gerar a **linha 53 - Transferência** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 53 -****Transferência** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 53**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6151/6152/6153/6155/6156/6408/6409/6552/6557/6658/6659**
