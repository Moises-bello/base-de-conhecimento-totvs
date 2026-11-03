---
article_id: 11900165448727
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0f15cf7ae7e23e8129e69225ce228fa50297b7bd680d21586ff8abe3c96edf59
fetched_at: '2026-06-28T22:42:09.011342+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 39 da DAPI?
type: support-article
updated_at: '2023-01-24T13:43:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11900165448727-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-39-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **L****inha 39 - Ativo Permanente**da **DAPIMG?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 39 - Ativo Permanente** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 39,** no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**3551/3553**
