---
article_id: 360020719472
category: ADVPL - Classe e Função
content_hash: 348182be02a8061593467d713f012b6d926cd2fa84db31a0d4303b6aaa0c5ede
fetched_at: '2026-06-28T22:40:18.177341+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização da função
  LASTREC() retorna '0'
type: support-article
updated_at: '2022-06-14T18:08:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020719472-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-LASTREC-retorna-0
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**A função **LASTREC**() retorna "zero", quando na verdade o retorno da *Query* é maior que "zero"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**A função **LastRec**() retorna '0' devido estar utilizando *Query*, e a função **TcGenQry**() e que é especifica para execução de *Query's*, isto vale para o comando ADVPL TCQuery, que por trás executa **TcGenQry**().  
Uma *Query* aberta no AdvPL cria um cursor de leitura, que permite apenas duas instruções de navegação: **DBKSip**(), para avançar para o próximo registro do cursor, e DBGoTop() – que fecha o cursor e abre novamente, submetendo a query novamente ao Banco de Dados. Um cursor no AdvPL **não permite alteração** (DBRLock, REPLACE, FieldPut), **não permite voltar para registro anterior** – DbSkip(-1) – e **não permite ir direto ao último registro** – DBGoBottom().  
A **TCGenQry** só suporta statements de query (SELECT).

Funciona sim em Tabela Temporária e não em Query  
  
**Exemplo:**

```
/*EXEMPLO DE UTILIZAÇÂO DA FUNÇÂO LASTREC()*/  
  
#include 'protheus.ch'  
#include 'parmtype.ch'  
#include "TOTVS.ch"  
#include "RWMAKE.CH"  
#include "tbiconn.ch"  
  
/*/{Protheus.doc} TLastRec2  
//TODO Descrição auto-gerada.  
@author rodrigo.santiago  
@since 14/12/2018  
@version 1.0  
@return ${return}, ${return_description}  
@type function  
/*/  
  
user function TLastRec2()  
  
Local nHandle :=0  
Local cRDD :="TOPCONN"  
Local cBanco :="MSSQL/P1217"  
Local cServidor :="localhost"  
Local nPorta :=7890  
Local nI :=0  
Local cTable :="TMP"  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "010101"  
  
nHandle := TCLink( cBanco, cServidor, nPorta )  
  
If TCCanOpen(cTable)  
  TCDelFile(cTable)  
EndIf  
  
DBCreate('TMP', {{"FIELD_NAME", "C", 10, 0}, ;  
{"FIELD_ID", "N", 15, 4}}, cRDD)  
  
DBUseArea(.F., cRDD, cTable, cTable, .F., .F.)  
  
FOR nI :=0TO9  
DBAppend()  
(cTable)->FIELD_NAME := 'TEST' + CValToChar(nI)  
  
DOCASE  
  
CASE nI = 0  
(cTable)->FIELD_ID := 0  
  
CASE nI = 1  
(cTable)->FIELD_ID := 12345  
  
CASE nI = 2  
(cTable)->FIELD_ID := 12345.1234  
  
CASE nI = 3  
(cTable)->FIELD_ID := 1234567890  
  
CASE nI = 4  
(cTable)->FIELD_ID := -1234567890  
  
CASE nI = 5  
(cTable)->FIELD_ID := -1234567890.1234  
  
CASE nI = 6  
(cTable)->FIELD_ID := -1234567890.12345  
  
CASE nI = 7  
(cTable)->FIELD_ID := 0.123  
  
CASE nI = 8  
(cTable)->FIELD_ID := 0.1234  
  
CASE nI = 9  
(cTable)->FIELD_ID := 0.12345  
  
ENDCASE  
  
DBCommit()  
  
NEXT  
  
DBCloseArea()  
DBUseArea(.F., cRDD, cTable, cTable, .F., .F.)  
  
WHILE (cTable)->(!EOF())  
Conout('['+ (cTable)->FIELD_NAME +'] = '+CValToChar((cTable)->FIELD_ID))  
DBSkip()  
  
ENDDO  
conout("Total de registros da tabela Temporaria -> "+CValToChar( LastRec() ))  
DBCloseArea()  
Conout('------------------------------------------------')  
cQuery := 'SELECT * FROM ' + cTable  
  
DBUseArea(.F., cRDD, tcGenQry(, , cQuery), 'QRY', .T., .T.)  
WHILE QRY->(!EOF())  
Conout('['+FieldGet(1) +'] = '+CValToChar(FieldGet(2)))  
DBSkip()  
  
ENDDO  
  
conout("Total de registros de uma Query -> "+CValToChar( LastRec() ))  
DBCloseArea()  
TCunlink()  
  
Return
```

**Saiba mais  
[LastRec()](http://tdn.totvs.com/display/tec/LastRec)**
