---
article_id: 360027851532
category: ADVPL - Classe e Função
content_hash: e805b290894010196fce8be2e789ba9b5276239a3384d439b2a0d32a25ca7a6a
fetched_at: '2026-06-28T22:40:18.096421+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TIBrowse não abre
  pagina na versão Lobo Guara
type: support-article
updated_at: '2022-06-14T18:17:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027851532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TIBrowse-n%C3%A3o-abre-pagina-na-vers%C3%A3o-Lobo-Guara
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min****Ocorrência**Após migração para Release P12.1.23 do Protheus o componente TIBrowse não está concluido abertura da pagina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027974492/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Causa**A Classe TIBrowse não  é Suportada. Conforme aviso presente na documentação da [TIBrowser](http://tdn.totvs.com/display/tec/TIBrowser), devido a problemas de compatibilidade do Windows 10 com as ferramentas ActiveX utilizadas pelo componente TIBrowser a partir da versão 12.1.23  
  
**Solução**Utilize o componente [TWebEngine](http://tdn.totvs.com/display/tec/TWebEngine), que possui as mesmas funcionalidades porém em um motor muito mais atual baseado no navegador Chromium®.
