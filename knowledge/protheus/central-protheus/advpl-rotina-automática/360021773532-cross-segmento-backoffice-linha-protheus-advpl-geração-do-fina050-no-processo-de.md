---
article_id: 360021773532
category: ADVPL - Rotina Automática
content_hash: 052bb78ae613ae768c8d21defa14c5ff320a6ef0075cf3a9423b21b3d96135b6
fetched_at: '2026-06-28T22:40:24.114914+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Geração do Fina050 no
  processo de exclusão
type: support-article
updated_at: '2021-12-29T20:07:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021773532-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gera%C3%A7%C3%A3o-do-Fina050-no-processo-de-exclus%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Utilizando o link como referência -> <http://tdn.totvs.com/pages/releaseview.action?pageId=6070752>. Fiz uma exclusão como informa o delete, porém o msexecauto esta deletando a parcela "01" do titulo de outro fornecedor exemplo.

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para essa implementação de acordo com a documentação é necessário que seja atribuído as informações no array para mais eficácia no processo conforme exemplo abaixo.

```
#include 'protheus.ch'  
#INCLUDE 'TBICONN.CH'  
  
User Function cFINA050()  
  
Local aArray := {}  
Local nY := 0  
Local cxTitulo := "YX0220011"  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
PRIVATE lMsErroAuto := .F.  
dbselectarea("SE2")  
dbgotop()  
//For nY := 1 To 5  
 aArray := { { "E2_PREFIXO","Y20" , NIL },;  
 { "E2_NUM" ,cxTitulo , NIL },;  
 { "E2_TIPO" , "NF " , NIL },;  
 { "E2_PARCELA", " " , NIL },;  
 { "E2_NATUREZ","500 " , NIL },;  
 { "E2_FORNECE","002 " , NIL },;  
 { "E2_CONTAD" , "002 " , NIL },;  
 { "E2_LOJA" ,"01" , NIL },;  
 { "E2_HIST" , "TESTE DE INCT001 " , NIL },;  
 { "E2_EMISSAO" , CtoD("10/01/2019"), NIL },;  
 { "E2_VENCTO" , CtoD("10/01/2019"), NIL },;  
 { "E2_VENCREA" , CtoD("10/01/2019"), NIL },;  
 { "E2_VALOR" , 5500 , NIL }}  
   
MsExecAuto( { |x,y,z| FINA050(x,y,z)},aArray,,3) // 3 - Inclusao, 4 - Alteração, 5 - Exclusão  
   
   
 If lMsErroAuto  
 MostraErro()  
 Else  
 Alert("Título incluído com sucesso!"+cxTitulo)  
 Endif  
 //cxTitulo:= SOMA1(cxTitulo)  
 //Next nY  
 RESET ENVIRONMENT  
   
Return  
  
  
/*  
User Function AltRodaPe(lAtu)  
DEFAULT lAtu:= .f.  
  
nTIPI := MaFisRet(,"NF_VALIPI")  
nTICM := MaFisRet(,"NF_VALICM")  
  
If lAtu   
 nTIPIAtu:= nTIPI  
 nTICMAtu:= nTICM  
  
Return .t.
```
