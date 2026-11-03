---
article_id: 360018717051
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: c46c6c9c0aaf13ceffaf2ebfa568449aa40df861033065f8b90306ee844f4fcf
fetched_at: '2026-06-28T22:40:44.466797+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB : ECD Campos bloqueados.'
type: support-article
updated_at: '2022-06-03T21:32:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018717051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Campos-bloqueados
---

**Dúvida**

Wizard da ECD (CTBS001) Os seguintes campos estão bloqueados para seleção: Indicador Empr Grande Porte, Tipo da ECD (SCP) e Plano de contas referencial.

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

Para solucionar a ocorrência, verifique se o ambiente possui os campos:

* CVN\_CODPLA e CVD\_CODPLA

E as datas dos fontes:

* CTBS010 > ou = 05/04/2017
* PMSXFUN > ou = 19/01/17

**![](http://tdn.totvs.com/download/attachments/273307963/image2017-4-19%2010%3A51%3A5.png?version=1&modificationDate=1492612697000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/273307963/image2017-4-19%2010%3A53%3A25.png?version=1&modificationDate=1492612697000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/273307963/image2017-4-19%2010%3A52%3A5.png?version=1&modificationDate=1492612697000&api=v2)**
