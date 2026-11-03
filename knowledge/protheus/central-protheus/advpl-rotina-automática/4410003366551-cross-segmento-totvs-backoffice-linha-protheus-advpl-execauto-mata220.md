---
article_id: 4410003366551
category: ADVPL - Rotina Automática
content_hash: 148363bb746b3ade0cf7f68a40ceaa08b363c083c03a689c878e51bb2e47a139
fetched_at: '2026-06-28T22:40:24.255858+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execauto MATA220
type: support-article
updated_at: '2021-10-04T14:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410003366551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execauto-MATA220
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Poderiam disponibilizar o exemplo do ExecAuto MATA220?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Segue exemplo do ExecAuto MATA220

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TbIconn.ch"  
#INCLUDE "TopConn.ch"   
#INCLUDE "TbIconn.ch"  
  
User Function MyMata220()  
  
Local PARAMIXB1 := {}  
Local PARAMIXB2 := 3  
Local cProd := "04"  
Local cArmazem := "01"  
Local cQtdIni := 30  
PRIVATE lMsErroAuto := .F.  
  
//------------------------//| Abertura do ambiente |//------------------------  
RpcSetEnv( "99","01", "Administrador", "", "EST")  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Cadastro de Saldos Iniciais",80))  
ConOut("Inicio: "+Time())  
  
//------------------------//| Teste de Inclusao |//------------------------  
  
PARAMIXB1 := {}  
aadd(PARAMIXB1,{"B9_COD",cProd,})  
aadd(PARAMIXB1,{"B9_LOCAL",cArmazem,})  
aadd(PARAMIXB1,{"B9_QINI",cQtdIni,})  
MSExecAuto({|x,y| mata220(x,y)},PARAMIXB1,PARAMIXB2)  
If !lMsErroAuto  
ConOut("Incluido com sucesso! "+cProd)  
Else  
ConOut("Erro na inclusao!")  
EndIf  
ConOut("Fim : "+Time())  
Return Nil
```

**Saiba mais**  
[MATA220 - Controle de Itens do Estoque](https://tdn.totvs.com/display/public/mp/MATA220+-+Controle+de+Itens+do+Estoque)
