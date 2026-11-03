---
article_id: 8680380385175
category: Faturamento - Cadastros
content_hash: cad615704096c9fcea566fa5039a0d93696039dc38f7b0406733991f48fd01d2
fetched_at: '2026-06-28T22:38:36.550407+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO MATA030
type: support-article
updated_at: '2022-09-06T13:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8680380385175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-MATA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto MATA030 - Cadastro de Clientes.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para Cadastro de Clientes via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE"PROTHEUS.CH"  
#INCLUDE"TBICONN.CH"  
  
UserFunctionMyMATA030()  
  
    LocalaVetor        := {} //Array com as informacoes do Cadastro de Clientes  
    LocalnOpc          := 3  //Tipo de operacao  
    PRIVATElMsErroAuto := .F.  
  
    IfnOpc==3  
  
        DbSelectArea("SA1")  
        DbSetOrder(1)  
  
        ConOut("Teste de Inclusao de Cliente")  
        ConOut("Inicio: " + Time())  
  
        IfDBSeek(xFilial("SA1")+"000001"+"01")  
            aVetor  := {{"A1_COD"     ,"XBX141"            ,Nil},;// Codigo  
                        {"A1_LOJA"    ,"01"                ,Nil},;// Loja  
                        {"A1_NOME"    ,"ROTINA AUTOMATICA" ,Nil},;// Nome  
                        {"A1_END"     ,"BRAZ LEME"         ,Nil},;// Endereco  
                        {"A1_NREDUZ"  ,"ROTAUTO"           ,Nil},;// Nome Fantasia  
                        {"A1_TIPO"    ,"F"                 ,Nil},;// Tipo  
                        {"A1_EST"     ,"SP"                ,Nil},;// Estado  
                        {"A1_MUN"     ,"SAO PAULO"         ,Nil}; // Municipio  
                    }  
  
            //3-Inclusão, 4-Alteração, 5-Exclusão  
            CONOUT("Iniciando a gravacao")  
            MSExecAuto({|x,y| Mata030(x,y)},aVetor,3)  
  
            IflMsErroAuto  
                Conout("Erro na inclusao!")   
                lRet := lMsErroAuto  
                MostraErro()  // Nao funciona na execucao via JOB  
            Else  
                Conout("Cliente incluido com sucesso!")  
            EndIf  
  
            ConOut("Fim: " + Time())      
        Else  
            Conout ("Cliente nao cadastrado!")  
        EndIf  
    EndIf  
Return
```

 **Saiba Mais:**

**[Cross Segmento - Backoffice Linha Protheus - ADVPL - Execauto Cadastro de Cliente (MATA030)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019904352-MP-ADVPL-Execauto-Cadastro-de-Cliente-MATA030-?)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Execauto Rotina Automática Cadastro de Clientes - CRMA980](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029074312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Execauto-Rotina-Autom%C3%A1tica-Cadastro-de-Clientes-CRMA980)**
