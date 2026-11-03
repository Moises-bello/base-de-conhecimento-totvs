---
article_id: 11570621863063
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2d7a85facbe564183aadb4b323ad0500cf1184d7a9c592d7cff8560a9ac34f52
fetched_at: '2026-06-28T22:42:09.002097+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 37 da DAPI?
type: support-article
updated_at: '2023-01-10T18:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11570621863063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-37-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **L****inha 37 - Devolução** da **DAPIMG?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 37 - Devolução**  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha 37**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**3201/3202/3205/3206/3207/3211/3503**
