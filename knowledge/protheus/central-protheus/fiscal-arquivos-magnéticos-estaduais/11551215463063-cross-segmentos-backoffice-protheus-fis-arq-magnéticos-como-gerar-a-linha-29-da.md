---
article_id: 11551215463063
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 952142617907741001c55b4ddc982628c7c85b4959955a0fa76ace4f68502063
fetched_at: '2026-06-28T22:42:08.972565+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 29 da DAPI?
type: support-article
updated_at: '2023-01-10T12:16:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11551215463063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-29-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha** **29 - Energia Elétrica** da **DAPIMG?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha** **29 - Energia Elétrica** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha** **29 - Energia Elétrica**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**2251/2252/2253/2254/2255/2256/2257**
