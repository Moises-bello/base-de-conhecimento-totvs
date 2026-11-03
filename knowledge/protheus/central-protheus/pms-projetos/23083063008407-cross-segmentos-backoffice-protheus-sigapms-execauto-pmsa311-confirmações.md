---
article_id: 23083063008407
category: PMS - Projetos
content_hash: c02212194bf54c978ce15b7d7110746066b848089b4b94f62459dcece920ca2a
fetched_at: '2026-06-28T22:37:14.900202+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - ExecAuto PMSA311 (Confirmações)
type: support-article
updated_at: '2024-04-26T17:38:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23083063008407-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-ExecAuto-PMSA311-Confirma%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23083084360599) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual exemplo do ExecAuto PMSA311 (Confirmações)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**É possível realizar inclusão, alteração e exclusão de confirmações de tarefas de um projeto (PMSA311).

Ao final da execução são criados dados na tabela AFF (Confirmações).

Exemplo (separada por comentários, a inclusão, alteração e exclusão):

```
//INCLUSAO -------------------------------------------------------------
USER FUNCTION PMS311INC()
    LOCAL aGetCPos	:= {}
    
    PRIVATE lMsErroAuto := .F.
    
    aAdd(aGetCPos ,{"AFF_PROJET" ,'TESTE2    '     	,.F.}) // Informar código do projeto que já existe
    aAdd(aGetCPos ,{"AFF_TAREFA" ,'01          '   	,.F.}) // Informar a tarefa desse projeto
    aAdd(aGetCPos ,{"AFF_REVISA" ,'0001'		    ,.F.}) // Informar o código de revisão desse projeto
    aAdd(aGetCPos ,{"AFF_DATA"   ,dDataBase			,.F.}) // Informar a data que será gerado a confirmação
    aAdd(aGetCPos ,{"AFF_QUANT"  ,0.5				,.F.}) // Informar a quantidade da confirmação
    
    MSExecAuto({|a,b,c|PMSA311(a,b,c)},3,{},aGetCpos)
    
    If lMsErroAuto
        MostraErro()
    Else
        Alert("Confirmação inclusa com sucesso!")
    Endif
 
    /*
    Se tiver ExecAuto, usar essa metodologia de mostrar erro e comentar a acima.
    If (!lMsErroAuto) // OPERAÇÃO FOI EXECUTADA COM SUCESSO
        ConOut(PadC("Automatic routine successfully ended", 80))
    Else // OPERAÇÃO EXECUTADA COM ERRO
        If (!IsBlind()) // COM INTERFACE GRÁFICA
            MostraErro()
        Else // EM ESTADO DE JOB, apontar para um caminho correto na base
            cError := MostraErro("C:\protheus\12.1.2210a\protheus\protheus_data\data", "errorws.log") // ARMAZENA A MENSAGEM DE ERRO

            ConOut(PadC("Automatic routine ended with error", 80))
            ConOut("Error: "+ cError)
        EndIf
    EndIf
    */
Return
  

//ALTERAÇÃO -------------------------------------------------------------
USER FUNCTION PMS311ALT()
    
    LOCAL aGetCPos	:= {}
    
    PRIVATE lMsErroAuto := .F.
    
    DbSelectArea("AFF")
    dbSetOrder(1) //AFF_FILIAL+AFF_PROJET+AFF_REVISA+AFF_TAREFA+DTOS(AFF_DATA)
    DbSeek(xFilial("AFF")+'TESTE2    '+'0001'+'01          '+DTOS(dDataBase) )
    
    aAdd(aGetCPos ,{"AFF_QUANT"  ,0.8					,.T.})
    
    MSExecAuto({|a,b,c|PMSA311(a,b,c)},4,{},aGetCpos)
    
        If lMsErroAuto
            MostraErro()
        Else
            Alert("Confirmação inclusa com sucesso!")
        Endif
    
    /*
    Se tiver ExecAuto, usar essa metodologia de mostrar erro e comentar a acima.
    If (!lMsErroAuto) // OPERAÇÃO FOI EXECUTADA COM SUCESSO
        ConOut(PadC("Automatic routine successfully ended", 80))
    Else // OPERAÇÃO EXECUTADA COM ERRO
        If (!IsBlind()) // COM INTERFACE GRÁFICA
            MostraErro()
        Else // EM ESTADO DE JOB, apontar para um caminho correto na base
            cError := MostraErro("C:\protheus\12.1.2210a\protheus\protheus_data\data", "errorws.log") // ARMAZENA A MENSAGEM DE ERRO
            ConOut(PadC("Automatic routine ended with error", 80))
            ConOut("Error: "+ cError)
        EndIf
    EndIf
    */
Return
   

//EXCLUSÃO -------------------------------------------------------------
USER FUNCTION PMS311EXC()
    
    LOCAL aGetCPos	:= {}
    
    PRIVATE lMsErroAuto := .F.
    
    DbSelectArea("AFF")
    dbSetOrder(1) //AFF_FILIAL+AFF_PROJET+AFF_REVISA+AFF_TAREFA+DTOS(AFF_DATA)
    DbSeek(xFilial("AFF")+'TESTE2    '+'0001'+'01          '+DTOS(dDataBase) )
    
    MSExecAuto({|a,b,c|PMSA311(a,b,c)}, 5, {}, aGetCpos )
    
    If lMsErroAuto
        MostraErro()
    Else
        Alert("Confirmação inclusa com sucesso!")
    Endif
    
    /*
    Se tiver ExecAuto, usar essa metodologia de mostrar erro e comentar a acima.
    If (!lMsErroAuto) // OPERAÇÃO FOI EXECUTADA COM SUCESSO
        ConOut(PadC("Automatic routine successfully ended", 80))
    Else // OPERAÇÃO EXECUTADA COM ERRO
        If (!IsBlind()) // COM INTERFACE GRÁFICA
            MostraErro()
        Else // EM ESTADO DE JOB, apontar para um caminho correto na base
            cError := MostraErro("C:\protheus\12.1.2210a\protheus\protheus_data\data", "errorws.log") // ARMAZENA A MENSAGEM DE ERRO
            ConOut(PadC("Automatic routine ended with error", 80))
            ConOut("Error: "+ cError)
        EndIf
    EndIf
    */
Return
```

**Saiba mais:**

**[PMSA311 Confirmações - Rotina automática](https://tdn.totvs.com/x/dK9n)**

**[Estrutura do Projeto (PMSA310 - SIGAPMS)](https://tdn.totvs.com/x/n5IOFQ)**
