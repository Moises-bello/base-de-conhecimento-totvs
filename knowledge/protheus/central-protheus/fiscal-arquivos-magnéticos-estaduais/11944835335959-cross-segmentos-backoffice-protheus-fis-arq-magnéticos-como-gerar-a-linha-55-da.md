---
article_id: 11944835335959
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a6b612575fbd61155781e4561fdcedb35f1a345b765e26e55b152a312307b3c9
fetched_at: '2026-06-28T22:42:09.068279+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 55 da DAPI?
type: support-article
updated_at: '2023-01-26T13:25:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944835335959-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-55-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 55 - Energia Elétrica** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 55 - Energia Elétrica** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 55**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6251/6252/6253/6254/6255/6256/6257/6258**
