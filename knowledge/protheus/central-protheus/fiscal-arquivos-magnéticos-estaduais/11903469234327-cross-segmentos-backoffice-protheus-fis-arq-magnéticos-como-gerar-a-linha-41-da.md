---
article_id: 11903469234327
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ddc5c8f3ae4622e7fbf1ab33d3aa0750dc16b2505feaac192f610bd8b232d502
fetched_at: '2026-06-28T22:42:09.020354+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 41 da DAPI?
type: support-article
updated_at: '2023-01-24T18:06:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11903469234327-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-41-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a linha **41 - Outras** da DAPI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

A **41 - Outras** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 41,** no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**3930/3949**
