---
article_id: 11903279039255
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7197305bb646ac39f5c997077dc1fa540fa2b888aad7d22a3efd3dd5d8ec4801
fetched_at: '2026-06-28T22:42:09.015805+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 40 da DAPI?
type: support-article
updated_at: '2024-06-13T18:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11903279039255-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-40-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a linha **40 - Uso e Consumo** da DAPI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 40 - Uso e Consumo** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 40**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**3556/3653**

E que no cadastro de **TES** utilizado o campo **Credita ICMS** **(F4\_CREDICM)** preenchido com **Não**e o campo**Material de Consumo** (**F4\_CONSUMO**) Preenchido com **Sim**
