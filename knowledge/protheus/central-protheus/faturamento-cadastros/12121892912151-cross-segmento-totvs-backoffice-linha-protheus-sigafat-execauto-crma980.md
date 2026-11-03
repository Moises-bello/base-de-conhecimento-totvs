---
article_id: 12121892912151
category: Faturamento - Cadastros
content_hash: 41d065fbfa58ba0d6f0f94539d2c580614364a541554f91c5a2509885185619b
fetched_at: '2026-06-28T22:38:36.488070+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO CRMA980'
type: support-article
updated_at: '2023-02-02T14:48:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12121892912151--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto CRMA980 - Cadastro de Clientes**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para **criação, alteração ou exclusão de clientes** via rotina automática (**ExecAuto**).  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function MyCRMA980()   
  
    Local aSA1Auto := {}  
    Local aAI0Auto := {}  
    Local nOpcAuto := 3  //MODEL_OPERATION_INSERT (3-Inclusão, 4-Alteração, 5-Exclusão)  
    Local lRet := .T.      
  
    Private lMsErroAuto := .F.      
  
    lRet := RpcSetEnv("99","01","Admin")  //Empresa "99", Filial "01"  
  
    If lRet  
        //----------------------------------  
        // INCLUSÃO  
        //----------------------------------  
        IF nOpcAuto = 3  //Inclusão  
            ConOut("Teste de Inclusao")  
            ConOut("Inicio: " + Time())  
  
            //----------------------------------  
            // DADOS DO CLIENTE  
            //----------------------------------  
            aAdd(aSA1Auto,{"A1_COD"    ,"XBX141"            ,Nil}) // Codigo  
            aAdd(aSA1Auto,{"A1_LOJA"   ,"01"                ,Nil}) // Loja  
            aAdd(aSA1Auto,{"A1_NOME"   ,"ROTINA AUTOMATICA",Nil}) // Nome  
            aAdd(aSA1Auto,{"A1_END"    ,"BRAZ LEME"         ,Nil}) // Endereco  
            aAdd(aSA1Auto,{"A1_NREDUZ","ROTAUTO"           ,Nil}) // Nome Fantasia  
            aAdd(aSA1Auto,{"A1_TIPO"   ,"F"                 ,Nil}) // Tipo  
            aAdd(aSA1Auto,{"A1_EST"    ,"SP"                ,Nil}) // Estado  
            aAdd(aSA1Auto,{"A1_MUN"    ,"SAO PAULO"         ,Nil}) // Municipio  
            CONOUT("Passou pelo Array da SA1")          
  
            //---------------------------------------  
            // DADOS DO COMPLEMENTO DO CLIENTE  
            //---------------------------------------  
            //aAdd(aAI0Auto,{"AI0_SALDO" ,30 ,Nil})  
            //CONOUT("Passou pelo Array da AI0")          
  
            //------------------------------------  
            // Chamada para cadastrar o cliente  
            //------------------------------------  
            CONOUT("Iniciando a gravacao")  
            MSExecAuto({|a,b,c| CRMA980(a,b,c)},aSA1Auto,nOpcAuto,aAI0Auto)          
  
            If lMsErroAuto  
                lRet := lMsErroAuto  
                MostraErro()  // Nao funciona na execucao via JOB  
            Else  
                Conout("Cliente incluido com sucesso!")  
            EndIf  
  
            ConOut("Fim: " + Time())  
  
        //----------------------------------  
        // ALTERAÇÃO  
        //----------------------------------  
        ElseIf nOpcAuto = 4  //Alteração  
  
            ConOut("Teste de Alteracao")  
            ConOut("Inicio: " + Time())  
  
            //----------------------------------  
            // DADOS DO CLIENTE  
            //----------------------------------  
            aAdd(aSA1Auto,{"A1_COD"    ,"XBX141"            ,Nil}) // Codigo  
            aAdd(aSA1Auto,{"A1_LOJA"   ,"01"                ,Nil}) // Loja  
            aAdd(aSA1Auto,{"A1_NOME"   ,"ROTINA AUTO ALT"   ,Nil}) // Nome  
            aAdd(aSA1Auto,{"A1_END"    ,"BRAZ LEME"         ,Nil}) // Endereco  
            aAdd(aSA1Auto,{"A1_NREDUZ","ROTAUTO"           ,Nil}) // Nome Fantasia  
            aAdd(aSA1Auto,{"A1_TIPO"   ,"F"                 ,Nil}) // Tipo  
            aAdd(aSA1Auto,{"A1_EST"    ,"SP"                ,Nil}) // Estado  
            aAdd(aSA1Auto,{"A1_MUN"    ,"SAO PAULO"         ,Nil}) // Municipio  
            CONOUT("Passou pelo Array da SA1")          
  
            //---------------------------------------  
            // DADOS DO COMPLEMENTO DO CLIENTE  
            //---------------------------------------  
            //aAdd(aAI0Auto,{"AI0_SALDO" ,30 ,Nil})  
            //CONOUT("Passou pelo Array da AI0")          
  
            //------------------------------------  
            // Chamada para alterar o cliente  
            //------------------------------------  
            CONOUT("Iniciando a alteracao")  
            MSExecAuto({|a,b,c| CRMA980(a,b,c)},aSA1Auto,nOpcAuto,aAI0Auto)          
  
            If lMsErroAuto  
                lRet := lMsErroAuto  
                MostraErro()  // Nao funciona na execucao via JOB  
            Else  
                Conout("Cliente alterado com sucesso!")  
            EndIf  
  
            ConOut("Fim: " + Time())  
  
        //----------------------------------  
        // EXCLUSÃO  
        //----------------------------------  
        ElseIf nOpcAuto = 5  //Exclusão  
  
            ConOut("Teste de Exclusao")  
            ConOut("Inicio: " + Time())  
  
            //----------------------------------  
            // DADOS DO CLIENTE  
            //----------------------------------  
            aAdd(aSA1Auto,{"A1_COD"    ,"XBX141"            ,Nil}) // Codigo  
            aAdd(aSA1Auto,{"A1_LOJA"   ,"01"                ,Nil}) // Loja  
            CONOUT("Passou pelo Array da SA1")  
  
            //------------------------------------  
            // Chamada para excluir o cliente  
            //------------------------------------  
            CONOUT("Iniciando a exclusao")  
            MSExecAuto({|a,b,c| CRMA980(a,b,c)},aSA1Auto,nOpcAuto,aAI0Auto)          
  
            If lMsErroAuto  
                lRet := lMsErroAuto  
                MostraErro()  // Nao funciona na execucao via JOB  
            Else  
                Conout("Cliente excluido com sucesso!")  
            EndIf  
  
            ConOut("Fim: " + Time())  
  
        EndIf  
  
    EndIf      
  
    RpcClearEnv()   
  
ReturnlRet
```

**Saiba Mais**

**[Novo Fonte de Cadastro de Clientes em MVC](https://tdn.totvs.com/x/s60GEQ)**
