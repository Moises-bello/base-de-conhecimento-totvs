---
article_id: 360051144013
category: Escrita Fiscal - Impostos - Cálculos
content_hash: c9c421daf8cee980c053bef69a84c757cb797ae4b13c1ed135190286508c7e50
fetched_at: '2026-06-28T22:39:31.144630+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Rotina Automática
  - MATA930
type: support-article
updated_at: '2021-07-29T12:23:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051144013-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Rotina-Autom%C3%A1tica-MATA930
---

**Dúvida:**Como devo utilizar a Rotina Automática - MATA930?  
  
**Ambiente:**Microsiga Protheus  – Livros Fiscais – A partir da versão 11.80  
  
**Solução:**Esta rotina tem a finalidade de executar automaticamente o MATA930, Reprocessamento dos Livros Fiscais.

Exemplo de Rotina Automática MATA930

#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"

User Function MyMata930()   
Local aParam := array(11)  
Local lRotAut := .t.

PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FIS"

aParam[1] := '01/01/11' //Data Inicial  
aParam[2] := '31/01/11' //Data Final  
aParam[3] := 1 //1-Entrada 2-Saída 3-Ambos  
aParam[4] := '' //Nota Fiscal Incial  
aParam[5] := 'ZZZZZZ' //Nota Fiscal Final  
aParam[6] := '' //Série Incial  
aParam[7] := 'ZZZ' //Série Final  
aParam[8] := '' //Cli/For Inicial  
aParam[9] := 'ZZZZZZ' //Cli/For Final  
aParam[10] := '' //Loja Incial  
aParam[11] := 'ZZ' //Loja Final

MATA930(lRotAut,aParam)

RESET ENVIRONMENT
