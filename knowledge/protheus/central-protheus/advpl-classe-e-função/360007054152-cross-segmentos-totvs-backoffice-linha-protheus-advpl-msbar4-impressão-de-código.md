---
article_id: 360007054152
category: ADVPL - Classe e Função
content_hash: cbc4697951728441dd365f86668fa713f7b7e49ef942f21795a0171959710c2c
fetched_at: '2026-06-28T22:40:20.522179+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - MSBAR4 impressão
  de código de barras
type: support-article
updated_at: '2022-01-14T21:12:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007054152-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-MSBAR4-impress%C3%A3o-de-c%C3%B3digo-de-barras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Exemplo de customização não funciona:  
[MSBAR4 - Impressão de código de barras na impressora Deskjet HP e Laser](http://tdn.totvs.com/pages/releaseview.action?pageId=185738476)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Na Versão 12.1.17 deve-se utilizar a Classe Treport pois a função de impressão **SetPrint** foi descontinuada não sofrendo mais manutenções ou melhorias   
  
**Solução**Pra impressão de impressão de código de barra temos somente a [FWMSprinter](https://tdn.totvs.com/display/public/mp/FWMsPrinter)
