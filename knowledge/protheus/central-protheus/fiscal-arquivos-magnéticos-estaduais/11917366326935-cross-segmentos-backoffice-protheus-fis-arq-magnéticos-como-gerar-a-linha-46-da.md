---
article_id: 11917366326935
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ec2a96bbc8421c1c309b1ecab8b111bac7dca94e87cf8986d8a65373b08e601c
fetched_at: '2026-06-28T22:42:09.033089+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 46 da DAPI?
type: support-article
updated_at: '2023-01-25T12:40:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11917366326935-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-46-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 46 - Devolução**  da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 46 - Devolução** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 46**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5201/5202/5205/5206/5207/5208/5209/5210/5410/5411/5412/5413/5503/5553/5556/5660/5661/5662**
