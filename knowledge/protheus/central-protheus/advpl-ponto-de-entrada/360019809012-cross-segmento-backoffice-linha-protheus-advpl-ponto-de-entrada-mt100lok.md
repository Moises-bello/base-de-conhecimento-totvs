---
article_id: 360019809012
category: ADVPL - Ponto de Entrada
content_hash: 03e9dd89059995b68992e65f8de64e94284710369d1201386e76726b5ef60591
fetched_at: '2026-06-28T22:40:11.579999+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada MT100LOK
type: support-article
updated_at: '2021-12-21T20:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019809012-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MT100LOK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como validar as informações digitadas através do Ponto de Entrada MT100LOK?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para buscar os valores da linha para a validação do ponto é necessário acessar o **aCols** da rotina no momento do ponto.

**![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015662432/Capturar.JPG)**

```
#Include 'Protheus.ch'  
  
User Function MT100LOK()  
Local _nCC := acols[1][20] // centro de custo da primeira linha.  
Local bRet  
  
IF Empty(_nCC)  
  bRet := MsgNoYes('Não tem centro de Custo, deseja bloquear?','Bloqueio')  
ELSE   
   bRet := .t.   
ENDIF  
  
Return bRet
```

**Saiba mais**[MT100LOK](http://tdn.totvs.com/pages/releaseview.action?pageId=6085397)
