---
article_id: 11944648691223
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 44f3127ad80b16e2ee80001ffa1eca4ebe3d26f27ed5e5700c6cda881dbb39d3
fetched_at: '2026-06-28T22:42:09.064258+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 54 da DAPI?
type: support-article
updated_at: '2023-01-26T12:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944648691223-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-54-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a **Linha 54 - Devolução**  da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 54 - Devolução** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 54**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6201/6202/6205/6206/6207/6208/6209/6210/6410/6411/6412/6413/6503/6553/6556/6660/6661/6662**
