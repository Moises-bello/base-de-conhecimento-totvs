---
article_id: 360021145991
category: ADVPL - Classe e Função
content_hash: 480c642ec70d24069f20f22198d9261505192a6b5392d0e1c2fa12aac1512fa1
fetched_at: '2026-06-28T22:40:18.212812+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Variable does not
  exist CACESSO on VERSENHA
type: support-article
updated_at: '2022-01-06T19:48:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021145991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Variable-does-not-exist-CACESSO-on-VERSENHA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao agendar via schedule uma rotina customizada gera erro or log

THREAD ERROR ([XXXX], XXXXXX, THIS)  xx/xx/xxxx  xx:xx:xx  
variable does not exist CACESSO on VERSENHA(MSLIB.PRW)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**O erro ocorre pois ao executar a rotina ele acessar o pergunte, mas se o ambiente não está preparado ocasiona o erro.  
  
**Solução**Utilize o **[Prepare Enviroment](http://tdn.totvs.com/pages/releaseview.action?pageId=6814708)** pois o *Schedule* só agenda a execução da rotina
