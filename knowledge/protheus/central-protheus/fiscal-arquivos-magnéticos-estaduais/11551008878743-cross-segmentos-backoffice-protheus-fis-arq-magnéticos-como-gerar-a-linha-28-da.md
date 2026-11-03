---
article_id: 11551008878743
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8f8e3c34c4aa69674e70314c044bba4f3d6d88135051c9f4b50be133d426587c
fetched_at: '2026-06-28T22:42:08.968405+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 28 da DAPI?
type: support-article
updated_at: '2023-01-10T12:20:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11551008878743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-28-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 28 -Devolução** da DAPIMG?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 28 -Devolução** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de****Entradas** om algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha 28**, no campo **Cod. Fiscal - D1\_CF**do lançamento deve conter uma das seguintes **CFOPs**:

**2201/2202/2203/2204/2205/2206/2207/2208/2209/2410/2411/2503/2504/2660/2661/2662**
