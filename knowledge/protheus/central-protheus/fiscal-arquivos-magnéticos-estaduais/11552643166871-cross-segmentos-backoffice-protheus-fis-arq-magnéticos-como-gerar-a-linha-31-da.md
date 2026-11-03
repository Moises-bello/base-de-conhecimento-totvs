---
article_id: 11552643166871
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f0bb0dbf1bd809485f596921266871fcd536bc3f18b6a3fe408f4b99859bec0b
fetched_at: '2026-06-28T22:42:08.980516+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 31 da DAPI?
type: support-article
updated_at: '2023-01-10T12:10:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11552643166871-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-31-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**  
Como gerar a **L****inha 31 - Transporte** da **DAPIMG?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 31 - Transporte** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha 31**, no campo **Cod. Fiscal - D1\_CF**do lançamento deve conter uma das seguintes **CFOPs**:

**2351/2352/2353/2354/2355/2356/2931/2932**
