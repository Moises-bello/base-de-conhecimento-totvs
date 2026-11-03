---
article_id: 360018940971
category: ADVPL - Ponto de Entrada
content_hash: 5ac8c9b7ea87866f4b342ea9704907985f03c87bd6140e61b733c32d8d0f93b9
fetched_at: '2026-06-28T22:40:12.782725+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  SPDPCIMOB gera registro para todas as filiais
type: support-article
updated_at: '2021-12-30T17:03:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018940971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-SPDPCIMOB-gera-registro-para-todas-as-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Registro F200 está sendo replicada para todas as filiais e deveria estar apenas em uma  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para que os registros criados pelo ponto de entrada SPDPCIMOB sejam gerado apenas para filiais específicas, é necessário adicionar um bloco condicional avaliando a variável CFILANT.  
A seguir um exemplo do ponto de entrada, que gera os registros F200, F205 e F210 apenas na filial '01';

```
#Include 'Protheus.ch'  
  
User Function SPDPCIMOB()  
Local aRetF200 := {}  
Local aRetF205 := {}  
Local aRetF210 := {}  
Local nPosF200 := 0  
Local nPosF205 := 0   
Local nPosF210 := 0  
Local nX := 0  
   
If CFILANT == '01' //Gera somente para filial 01  
 //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ   
 //³REGISTRO F200 - Sera gerado 1 para cada F010 do SpedPisCofins³   
 //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ  
 For nX:=1 To 2  
 Aadd(aRetF200,{})  
  
nPosF200 := Len(aRetF200)  
  
If nX == 1   
 Aadd(aRetF200[nPosF200],"F200") //01-REG   
 Aadd(aRetF200[nPosF200],"01") //02-IND_OPER   
 Aadd(aRetF200[nPosF200],"01")//03-UNID_IMOB  
 Aadd(aRetF200[nPosF200],"TOTVS")//04-IDENT_EMP  
 Aadd(aRetF200[nPosF200],"Descricao Resumida Totvs")//05-DESC_UNID_IMOB  
 Aadd(aRetF200[nPosF200],"123456789")//06-NUM_CONT  
 Aadd(aRetF200[nPosF200],"36403560808")//07-CPF_CNPJ_ADQU  
 Aadd(aRetF200[nPosF200],"13062018")//08-DT_OPER  
 Aadd(aRetF200[nPosF200],50000.00)//09-VL_TOT_VEND  
 Aadd(aRetF200[nPosF200],20000.00)//10-VL_REC_ACUM  
 Aadd(aRetF200[nPosF200],10000.00)//11-VL_TOT_REC  
 Aadd(aRetF200[nPosF200],"01")//12-CST_PIS  
 Aadd(aRetF200[nPosF200],50000.00)//13-VL_BC_PIS  
 Aadd(aRetF200[nPosF200],0.65)//14-ALIQ_PIS  
 Aadd(aRetF200[nPosF200],325.00)//15-VL_PIS  
 Aadd(aRetF200[nPosF200],"01")//16-CST_COFINS  
 Aadd(aRetF200[nPosF200],50000.00)//17-VL_BC_COFINS  
 Aadd(aRetF200[nPosF200],3.0)//18-ALIQ_COFINS  
 Aadd(aRetF200[nPosF200],1500.00)//19-VL_COFINS  
 Aadd(aRetF200[nPosF200],60.00)//20-PERC_REC_RECEB  
 Aadd(aRetF200[nPosF200],"1")//21-IND_NAT_EMP  
 Aadd(aRetF200[nPosF200],"Informações complementares")//22-INF_COMP  
 Aadd(aRetF200[nPosF200],"0")//Informa se o registro eh de regime cumulativo (0) ou nao cumulativo (1)  
 Else   
 Aadd(aRetF200[nPosF200],"F200")//01-REG  
 Aadd(aRetF200[nPosF200],"02")//02-IND_OPER  
 Aadd(aRetF200[nPosF200],"01")//03-UNID_IMOB  
 Aadd(aRetF200[nPosF200],"TOTVS")//04-IDENT_EMP  
 Aadd(aRetF200[nPosF200],"Descricao Resumida Totvs")//05-DESC_UNID_IMOB  
 Aadd(aRetF200[nPosF200],"123456789")//06-NUM_CONT  
 Aadd(aRetF200[nPosF200],"36403560808")//07-CPF_CNPJ_ADQU  
 Aadd(aRetF200[nPosF200],"13062018")//08-DT_OPER  
 Aadd(aRetF200[nPosF200],50000.00)//09-VL_TOT_VEND  
 Aadd(aRetF200[nPosF200],20000.00)//10-VL_REC_ACUM  
 Aadd(aRetF200[nPosF200],10000.00)//11-VL_TOT_REC  
 Aadd(aRetF200[nPosF200],"01")//12-CST_PIS  
 Aadd(aRetF200[nPosF200],50000.00)//13-VL_BC_PIS  
 Aadd(aRetF200[nPosF200],1.65)//14-ALIQ_PIS  
 Aadd(aRetF200[nPosF200],825.00)//15-VL_PIS  
 Aadd(aRetF200[nPosF200],"01")//16-CST_COFINS  
 Aadd(aRetF200[nPosF200],50000.00)//17-VL_BC_COFINS  
 Aadd(aRetF200[nPosF200],7.6)//18-ALIQ_COFINS  
 Aadd(aRetF200[nPosF200],3800.00)//19-VL_COFINS  
 Aadd(aRetF200[nPosF200],60.00)//20-PERC_REC_RECEB  
 Aadd(aRetF200[nPosF200],"1")//21-IND_NAT_EMP  
 Aadd(aRetF200[nPosF200],"Informações complementares")//22-INF_COMP  
 Aadd(aRetF200[nPosF200],"1")//Informa se o registro eh de regime cumulativo (0) ou nao cumulativo (1)  
 EndIf   
 //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ   
 //³REGISTRO F205 - Sera Gerado 1 para cada registro F200³   
 //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ   
 Aadd(aRetF205,{})  
  
nPosF205 := Len(aRetF205)  
  
Aadd(aRetF205[nPosF205],nPosF200)  
  
//Referencia do registro F200 Pai   
 Aadd(aRetF205[nPosF205],"F205")//01-REG  
 Aadd(aRetF205[nPosF205],30000.00)//02-VL_CUS_INC_ACUM_ANT  
 Aadd(aRetF205[nPosF205],10000.00)//03-VL_CUS_INC_PER_ESC  
 Aadd(aRetF205[nPosF205],40000.00)//04-VL_CUS_INC_ACUM  
 Aadd(aRetF205[nPosF205],8000.00)//05-VL_EXC_BC_CUS_INC_ACUM  
 Aadd(aRetF205[nPosF205],32000.00)//06-VL_BC_CUS_INC  
 Aadd(aRetF205[nPosF205],"50")//07-CST_PIS  
 Aadd(aRetF205[nPosF205],1.65)//08-ALIQ_PIS  
 Aadd(aRetF205[nPosF205],528.00)//09-VL_CRED_PIS_ACUM  
 Aadd(aRetF205[nPosF205],40.00)//10-VL_CRED_PIS_DESC_ANT  
 Aadd(aRetF205[nPosF205],60.00)//11-VL_CRED_PIS_DESC  
 Aadd(aRetF205[nPosF205],428.00)//12-VL_CRED_PIS_DESC_FUT  
 Aadd(aRetF205[nPosF205],"50") //13-CST_COFINS  
 Aadd(aRetF205[nPosF205],7.6)//14-ALIQ_COFINS  
 Aadd(aRetF205[nPosF205],2432.00)//15-VL_CRED_COFINS_ACUM  
 Aadd(aRetF205[nPosF205],100.00)//16-VL_CRED_COFINS_DESC_ANT  
 Aadd(aRetF205[nPosF205],200.00)//17-VL_CRED_COFINS_DESC  
 Aadd(aRetF205[nPosF205],2132.00)//18-VL_CRED_COFINS_DESC_FUT  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ  
 //³REGISTRO F210 - Gerados N registros para cada F200 ³  
 //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ  
  
Aadd(aRetF210,{})  
  
nPosF210 := Len(aRetF210)  
  
Aadd(aRetF210[nPosF210],nPosF200)//Referencia do registro F200 Pai   
 Aadd(aRetF210[nPosF210],"F210")//01-REG  
 Aadd(aRetF210[nPosF210],5000.00)//02-VL_CUS_ORC  
 Aadd(aRetF210[nPosF210],0.00)//03-VL_EXC  
 Aadd(aRetF210[nPosF210],5000.00)//04-VL_CUS_ORC_AJU  
 Aadd(aRetF210[nPosF210],10000.00)//05-VL_BC_CRED  
 Aadd(aRetF210[nPosF210],"50")//06-CST_PIS  
 Aadd(aRetF210[nPosF210],1.65)//07-ALIQ_PIS  
 Aadd(aRetF210[nPosF210],165.00)//08-VL_CRED_PIS_UTIL  
 Aadd(aRetF210[nPosF210],"50")//09-CST_COFINS  
 Aadd(aRetF210[nPosF210],7.6)//10-ALIQ_COFINS  
 Aadd(aRetF210[nPosF210],760.00)//11-VL_CRED_COFINS_UTIL  
 Next  
  
EndIf  
   
Return {aRetF200,aRetF205,aRetF210}
```
