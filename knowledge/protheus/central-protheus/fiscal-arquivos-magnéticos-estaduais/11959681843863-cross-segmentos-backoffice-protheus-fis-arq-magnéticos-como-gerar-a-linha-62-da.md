---
article_id: 11959681843863
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: bc68ed71320e328cff3ff4e236045fb2cc78b29b93f13ce307d68690ccc1f21f
fetched_at: '2026-06-28T22:42:09.093037+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 62 da DAPI?
type: support-article
updated_at: '2023-01-26T19:48:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11959681843863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-62-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha 62 - Comunicação Transporte Energia Elétrica** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 62 - Comunicação Transporte Energia Elétrica** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 62**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**7251/7301/7358**
