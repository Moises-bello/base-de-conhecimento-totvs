---
article_id: 360035623673
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 759dd41216045cdd72228360b31b9b08ff580b8cd711262a1e0af3c401d8fecb
fetched_at: '2026-06-28T22:38:30.069881+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos -TOTVS Backoffice (Linha Protheus)-SIGAFAT-argument error
  in function Len() on FININCNAT(FINXLOAD.PRW) '
type: support-article
updated_at: '2022-07-24T20:25:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035623673-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-argument-error-in-function-Len-on-FININCNAT-FINXLOAD-PRW
---

**Ocorrência**Ao preparar a nota de saída (**MATA461**), ocorre o erro:

**argument error in function Len() on FININCNAT(FINXLOAD.PRW) 06/06/2019 17:02:58 line : 1429**

**Ambiente**

Cross Segmentos -TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões.  
  
**Causa**

O erro ocorre por que a natureza informada no parâmetro **MV\_ISS** está como numérico, e o parâmetro é carácter, veja o trecho do erro abaixo:  
  
STACK FININCNAT(FINXLOAD.PRW) 06/06/2019 17:02:58  
  
 Local 1: **CNATUREZA(N) :24011**  
  
\sx6010.dtc; Rdd:DBFCDX; Alias:SX6; Filter :; Recno:2973; Total Recs:11439; Order:2  
Index (0) :I\_RECNO   
Index (1) :\*\*SX60101  X6\_FIL+X6\_VAR  
Field 1: D\_E\_L\_E\_T\_E\_D(C) :  
Field 2: R\_E\_C\_N\_O(N) :2973  
Field 3: X6\_FIL(C) :       
**Field 4: X6\_VAR(C) :MV\_ISS**  
Field 6: X6\_DESCRIC(C) :Natureza utilizada para Imposto s/Servico         
**Field 15: X6\_CONTEUD(C) :24011**                                                                                                                                                                                                                                   
**Solução**

Para solucionar, entre no configurador, ambiente,cadastros, parâmetros, selecione o parâmetro **MV\_ISS** e coloque o valor entre aspas, para que o sistema entenda que se trata de um carácter**(MV\_ISS ="24011").**

**OBS...Este mesmo erro pode ocorrer com os parâmetros de IR (MV\_IRF ), INSS(MV\_INSS), Cofins (MV\_COFINS), Pis(MV\_PISNAT)e Csll(MV\_CSLL), uma vez que são do tipo caracter, a informação inserida nestes parâmetros deverá estar entre aspas duplas.**
