---
article_id: 360012761091
category: Ativo-Fixo - Error log
content_hash: 0952e3631dbdd3ac8566aa59fc1f72622af4d2fd47673c610c3079bdb2667a57
fetched_at: '2026-06-28T22:41:54.831715+00:00'
product: protheus
section_id: 1500001547442
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - CTBAATF: on MPSYSEXECSCALAR(MPSYSOPENTABLES.PRW)'
type: support-article
updated_at: '2023-11-30T19:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012761091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CTBAATF-on-MPSYSEXECSCALAR-MPSYSOPENTABLES-PRW
---

**Ocorrência**Na **Contabilização Offline** do **Ativo Fixo - SIGAATF**, ocorre o erro abaixo:

*TOTVS Build 7.00.131227A-20170918 NG*  
*THREAD ERROR ([5024], thabata.castilho, PC-TI02) 07/08/2018 10:37:34*  
*variable does not exist MPI\_VALUE*  
*( PREVIOUS ERROR : type mismatch on + )*  
 *on MPSYSEXECSCALAR(MPSYSOPENTABLES.PRW) 18/01/2018 15:10:51***Ambiente**Microsiga Protheus - Versão 12 - Ativo Fixo (SIGAATF)  
  
  
**Causa**Este **erro** ocorre devido a inconsistências nas configurações de **lançamentos padrão** do módulo **Ativo Fixo**.  
   
  
 **Solução**Para realizar a correção deste erro, siga as instruções descritas abaixo:  
-Filtre, no arquivo **ERROR.log**, a variável **CPadrao**;  
-Através desta variável, teremos o código do lançamento padrão;  
![LP801.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360008786132)  
-Na rotina **CTBA080** (Cadastro de Lançamento Padrão), avalie as configurações implementadas no LP, e em todas as suas **sequências**.
