---
article_id: 360006664312
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: cd9fc6c7d041608ce53f43a68caa60035332f57585ff61dff163ba98452b6ceb
fetched_at: '2026-06-28T22:40:32.485018+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102: on FWOPENTEMP(CRIATRAB.PRG)'
type: support-article
updated_at: '2023-11-13T15:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006664312-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-on-FWOPENTEMP-CRIATRAB-PRG
---

**Ocorrência:**Na exclusão de lançamentos contábeis, ocorre o erro abaixo:  
*THREAD ERROR ([2200], benui.mangia, PROTHEUS12) 23/03/2018 10:37:28*  
*\_SC17: TOP Error -19 - [ERROR] Temporary Table definition [##TMPSC17\_85] already exists.*  
*( From tDBServer::CreateFile )*  
*Thread ID [28168] User [benui] IO [173988] Tables [58] MaxTables [60] Comment [CTBA102 - TCPIP - ThreadID(2200)] Status [] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/Protheus12] DBThread [(SPID 85)] Started [23/03/2018 09:34:52] LastIO [23/03/2018 10:37:28] IP [192.168.1.140:12002] RCV [20008773] SND [61945932] TCBuild [20161016-20170530]*   
*on FWOPENTEMP(CRIATRAB.PRG) 22/02/2018 16:52:34 line : 208*  
  
  
**Ambiente:**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - Versão 12  
  
  
**Causa:**Este erro é simulado quando a base de dados está com os pacotes de Lib e DBAccess desatualizados.  
  
  
**Solução:**A correção deste erro é efetuada quando ocorre a atualização dos pacotes de Lib e DBAccess.  
  
É recomendada também a atualização do Binário (AppServer e SmartClient).
