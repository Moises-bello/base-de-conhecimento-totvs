---
article_id: 11959483816343
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 9018a76d0159e78f409dfc40f41dda8f963e58ea3292c4d8670994aadca39ddb
fetched_at: '2026-06-28T22:42:09.088990+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 61 da DAPI?
type: support-article
updated_at: '2024-06-13T17:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11959483816343-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-61-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 61 - Devolução**  da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 61 - Devolução** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 61**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**7201/7202/7205/7206/7207/7210/7211/7553/7556**
