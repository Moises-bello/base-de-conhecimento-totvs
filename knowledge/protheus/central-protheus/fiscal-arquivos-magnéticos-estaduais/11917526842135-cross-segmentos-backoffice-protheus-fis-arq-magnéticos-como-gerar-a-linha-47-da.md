---
article_id: 11917526842135
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f19e1ddfc1b00013ff4889ea7b4f594e252a3a7fbc93ec5a61cd9a71e432c611
fetched_at: '2026-06-28T22:42:09.037767+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 47 da DAPI?
type: support-article
updated_at: '2023-01-25T12:42:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11917526842135-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-47-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 47 - Energia Elétrica** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 47 - Energia Elétrica** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 47**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5251/5252/5253/5254/5255/5256/5257/5258**
