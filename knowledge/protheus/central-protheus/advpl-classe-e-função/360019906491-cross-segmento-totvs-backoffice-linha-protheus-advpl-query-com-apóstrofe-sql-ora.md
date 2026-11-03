---
article_id: 360019906491
category: ADVPL - Classe e Função
content_hash: 163fbdbaa74a48ac02792dffcf9e006dbe941c92cb4bdd468a070f1f81142ed5
fetched_at: '2026-06-28T22:40:17.131674+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Query com apóstrofe
  SQL / Oracle
type: support-article
updated_at: '2022-06-13T21:15:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019906491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Query-com-ap%C3%B3strofe-SQL-Oracle
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como utilizar uma Query com apóstrofe na String em rotinas ADVPL ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Ao utilizar querys com apóstrofe em comandos ADVPL irá apresentar erros de estrutura, para esta correção deverá um incluir mais uma aspas simples na String, exemplo:

```
Local cMunCli := "SANTA BARBARA D'OESTE"  
  
deverá ficar  
  
Local cMunCli := "SANTA BARBARA D''OESTE"
```

Exemplo de um fonte.

```
#include 'totvs.ch'  
#INCLUDE "TBICONN.CH"  
#INCLUDE "topconn.ch"  
  
user Function TSTTquery  
  
Local cMunCli := "SANTA BARBARA D''OESTE"  
Local cUFCli := "SP"  
Local cQuery := ""  
Local cSql := ""  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
  
   
  
cMunCli := "SANTA BARBARA D''OESTE"  
  
cUFCli := "SP"  
  
cQuery := " Select CC2_CODMUN From " + RetSqlName("CC2") + " "  
cQuery += " Where CC2_EST = '"+UPPER(cUFCli)+"' "  
cQuery += " And CC2_MUN LIKE '%"+cMunCli+"%' "  
cQuery += " And D_E_L_E_T_= ' ' "  
  
If ChkFile("_MUN")  
DbSelectarea("_MUN")  
Dbclosearea()  
Endif  
  
TcQuery cQuery New Alias "_MUN"  
  
Return nil
```
