---
article_id: 360022355252
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: c73209bb5814256b65380520e9fe18282b0be79a2e672eb359d23d7545a835e2
fetched_at: '2026-06-28T22:41:55.491054+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF  - Errorlog : type mismatch
  on compare on MENUDEF(ATFA036.PRW) 09/11/2017 15:38:04 line : 143'
type: support-article
updated_at: '2023-11-20T16:28:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022355252-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Errorlog-type-mismatch-on-compare-on-MENUDEF-ATFA036-PRW-09-11-2017-15-38-04-line-143
---

**Dúvida**

THREAD ERROR ([7859], adm, usuario) 01/12/2018 08:24:20  
type mismatch on compare on MENUDEF(ATFA036.PRW) 09/11/2017 15:38:04 line : 143  
   
 **Ambiente**  
Microsiga Protheus – Ativo Fixo – A partir da versão P12

**Causa**Para solucionar essa ocorrência, os arquivos de dicionários "SXSBRA" e "SDFBRA" que ficam na pasta systemload, devem estar atualizados e necessário realizar o UPDDISTRconta  
  
**Solução**

Verifique também o dicionário SX1, filtrando o grupo AFA036, este deve possuir 4 perguntas conforme abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019543311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019664612)
