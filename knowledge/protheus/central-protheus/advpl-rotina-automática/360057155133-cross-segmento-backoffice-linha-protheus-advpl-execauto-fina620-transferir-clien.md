---
article_id: 360057155133
category: ADVPL - Rotina Automática
content_hash: 46030b930bf0f4ebaf0130fa4e8fd5dd2ce405e4175e69a09b580c96ce792d6f
fetched_at: '2026-06-28T22:40:24.049720+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - ExecAuto() FINA620: Transferir
  Cliente'
type: support-article
updated_at: '2021-12-29T14:56:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057155133-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-ExecAuto-FINA620-Transferir-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Teria um exemplo de rotina automática do FINA620, de transferência de cliente?

**Ambiente**Protheus – ADVPL– A partir da versão P12

**Solução**A rotina possui duas formas de utilização da rotina automática, uma chamando a função **Fa620Auto**, outra via **execauto**.

Chamando a função **Fa620Auto**, é possível solicitar penas transferência entre filiais, já via **execauto** é possível a alteração de cliente também. 

Exemplo de utilização da rotina automática pela função **ExecAuto()**:

```
User function ExFin620()  
  
Local cE1_Pref := " "  
Local cE1_Num := "00102031 "  
Local cE1_Cliente := "000001"  
Local cE1_Loja := "01"  
Local cFilSE1 := "D MG 01 "  
Local cFilDest := "D MG 01 "  
Local aCab := {}  
  
Private lMsErroAuto := .F.  
  
RPCSETENV("T1", "D MG 01", "teste", "123", "FIN", "FINA620")  
  
If SE1->( dbSeek( cFilSE1+cE1_Pref+cE1_Num+" "+"NF"))  
  
aadd(aCab, {"E6_FILDEB",cFilDest})  
aadd(aCab, {"E6_CLIENTE",cE1_Cliente})  
aadd(aCab, {"E6_LOJA",cE1_Loja})  
aadd(aCab, {"AUTHISTDEB","Teste"})  
  
//Inclusao de Solicitação de transferencia  
MSExecAuto({|a, b| FINA620(a,b)}, aCab,3)  
  
If lMsErroAuto  
mostraerro()  
Else  
MsgStop("Processo realizado com sucesso.")  
EndIf  
Else  
MsgStop("Titulo não encontrado.")  
EndIf  
  
Return
```

**Saiba Mais:  
[Solicitação de Transferência (FINA620 - SIGAFIN)](User%20function%20ExFin620()%20%20%20Local%20cE1_Pref%20:=%20"%20"%20Local%20cE1_Num%20:=%20"00102031%20"%20Local%20cE1_Cliente%20:=%20"000001"%20Local%20cE1_Loja%20:=%20"01"%20Local%20cFilSE1%20:=%20"D%20MG%2001%20"%20Local%20cFilDest%20:=%20"D%20MG%2001%20"%20Local%20aCab%20:=%20{}%20%20%20Private%20lMsErroAuto%20:=%20.F.%20%20%20RPCSETENV("T1",%20"D%20MG%2001",%20"teste",%20"123",%20"FIN",%20"FINA620")%20%20%20If%20SE1->(%20dbSeek(%20cFilSE1+cE1_Pref+cE1_Num+"%20"+"NF"))%20%20%20%20%20%20%20aadd(aCab,%20{"E6_FILDEB",cFilDest})%20%20%20%20%20aadd(aCab,%20{"E6_CLIENTE",cE1_Cliente})%20%20%20%20%20aadd(aCab,%20{"E6_LOJA",cE1_Loja})%20%20%20%20%20aadd(aCab,%20{"AUTHISTDEB","Teste"})%20%20%20%20%20%20%20//Inclusao%20de%20Solicita%C3%A7%C3%A3o%20de%20transferencia%20%20%20%20%20MSExecAuto({|a,%20b|%20FINA620(a,b)},%20aCab,3)%20%20%20%20%20%20%20If%20lMsErroAuto%20%20%20%20%20%20%20%20%20mostraerro()%20%20%20%20%20Else%20%20%20%20%20%20%20%20%20MsgStop("Processo%20realizado%20com%20sucesso.")%20%20%20%20%20EndIf%20Else%20%20%20%20%20MsgStop("Titulo%20n%C3%A3o%20encontrado.")%20EndIf%20%20%20Return)**
