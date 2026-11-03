---
article_id: 17890348211607
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5e6be41060b94b186b764b7699d4e9054d8e056b1f87b0be1bd7492a09b3c3b8
fetched_at: '2026-06-28T22:38:55.763364+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - Execauto
  da rotina
type: support-article
updated_at: '2025-07-10T19:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17890348211607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-Execauto-da-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17890332262935) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Para a rotina Baixas do CQ (MATA175)  é possível utilizar EXECAUTO?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Sim, é possível no link abaixo seguem as instruções e exemplos disponíveis. Verificar com seu Analista Desenvolvedor para criar conforme sua necessidade específica.

Documentação desenvolvimento: **[ExecAuto MATA175](https://tdn.totvs.com/display/public/PROT/MATA175+-+Programa+de+Baixas+do+Controle+de+Qualidade+CQ)**

```
#Include "protheus.ch"  
#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function EXECMATA175()  
Local dDataL:=DATE()  
Local aLibera   := {}  
Local cNumCQ    := "SK000C" // Numero do movimento criado anteriormente  
Local cProd     := "PATESTEEND        "//+Space(14)  
Local cLocal    := "98"  
PRIVATE lMsErroAuto := .F.  
//------------------------//| Abertura do ambiente |//------------------------  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "01" USER 'ADMIN' PASSWORD '' MODULO "EST" TABLES "SB1","SD7"                  
  
dDataL:= dDataBase  
ConOut(Repl("-",80))  
ConOut(PadC("Teste -  Baixas do Controle de Qualidade (CQ)",80))  
ConOut("Inicio: "+Time())  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿//| Teste de Inclusao   |//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
DbSelectArea("SD7")                                
DbGoTop()  
DbSetOrder(1)  
dbSeek(xFilial("SD7")+cNumCq+cProd+cLocal)  
  
//If !Found() .Or. SD7->D7_TIPO != 0  
//    conOut("Não encontrado")  
//    Return  
//Endif  
  
aAdd(aLibera,{  {"D7_TIPO"      ,1                  ,Nil},;  // 1=Libera o item do CQ / 2=Rejeita o item do CQ                
                {"D7_DATA"      ,dDataL             ,Nil},;  //              
                {"D7_QTDE"      ,50                 ,Nil},;  
                {"D7_QTSEGUM"   ,10                 ,Nil},;  //              
                {"D7_OBS"       ,""                 ,Nil},;  //                                                
                {"D7_MOTREJE"   ,""                 ,Nil},;  //              
                {"D7_LOCDEST"   ,"01"               ,Nil},;  //              
                {"D7_SALDO"     ,NIL                ,Nil},;  //              
                {"D7_SALDO2"    ,NIL                ,Nil},;//  
                {"D7_LOCALIZ"   ,"END01"            ,Nil},; //                                                                                        
                {"D7_ESTORNO"   ,NIL                ,Nil}})  //  
  
MSExecAuto({|x,y,z| MATA175(x,y)},aLibera,4)  
  
If !lMsErroAuto  
    ConOut("Incluido com sucesso! ")      
Else  
    MostraErro()      
    ConOut("Erro na inclusao!")  
EndIf  
    ConOut("Fim  : "+Time())  
  
    //RESET ENVIRONMENT  
Return Nil
```

**Veja o *exemplo* abaixo e também um *vídeo anexo*:**

***Saiba Mais:***

[SIGAEST - Rotina MATA175 - Instruções padrões sobre Controle de Qualidade no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
