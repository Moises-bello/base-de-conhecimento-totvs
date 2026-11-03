---
article_id: 11945231563671
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: afbb560aa036a5e012e0cd54312d5daccd07099f078b3d99d1724a9e8f627801
fetched_at: '2026-06-28T22:42:09.076417+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 57 da DAPI?
type: support-article
updated_at: '2023-01-26T13:20:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945231563671-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-57-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 57 - Transporte** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 57 - Transporte**é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 57**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6351/6352/6353/6354/6355/6356/6357/6359/6360**
