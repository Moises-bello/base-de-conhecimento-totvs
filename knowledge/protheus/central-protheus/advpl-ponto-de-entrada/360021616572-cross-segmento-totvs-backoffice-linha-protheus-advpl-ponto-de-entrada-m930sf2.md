---
article_id: 360021616572
category: ADVPL - Ponto de Entrada
content_hash: a1a9386f1b9953c45fb98e5533a92c2cae5b4b1f4ef9fb5615d5dde7df70f40c
fetched_at: '2026-06-28T22:40:11.846715+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  M930SF2
type: support-article
updated_at: '2021-12-29T19:19:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021616572-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M930SF2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao realizar o reprocessamento pela **MATA930** o PE **M930SF2** não é acionado.  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois o ponto de entrada faz a chamada de uma função interna **A930RepLoc()** que faz o reprocessamento de outros países, tratativa realizada nos fontes da versão 11.  
  
**Solução**Para essa finalidade utilize o PE **MT930SF3,**que atua após o reprocessamento de cada **SF3.**O ponto de entrada é executado após a atualização do SF3 com base nas tabelas **SD1/SF1 e SF2/SD2**. O único arquivo posicionado com segurança é o **SF3**.  
  
**Saiba mais**  
[**MT930SF3**](http://tdn.totvs.com/pages/releaseview.action?pageId=6077079)
