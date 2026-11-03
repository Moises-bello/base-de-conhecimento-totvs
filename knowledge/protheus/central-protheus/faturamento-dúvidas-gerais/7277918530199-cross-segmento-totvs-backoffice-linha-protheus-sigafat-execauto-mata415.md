---
article_id: 7277918530199
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c69ecbe43694399547cba4b39c0c04e54be138ab5cc8dca647fbffadde5fb7e2
fetched_at: '2026-06-28T22:38:32.786052+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO MATA415
type: support-article
updated_at: '2022-07-25T12:28:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7277918530199-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-MATA415
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto MATA415 - Orçamentos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de orçamentos via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE'TOTVS.CH'  
#INCLUDE'PROTHEUS.CH'  
#INCLUDE'TBICONN.CH'  
  
User Function MyMata415()  
  
    Local aCabec        := {}  
    Local aItens        := {}  
    Local aLinha        := {}  
    Local nX            := 0  
    Local nY            := 0  
    Local cDoc          := "000032"   //Codigo do Orcamento  
    Local lOk           := .T.  
    Local cOpc          := "4"  //Seleciona a operacao (3-Inclusao / 4-Alteracao / 5-Exclusao)  
  
    PRIVATE lMsErroAuto := .F.  
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //| ABERTURA DO AMBIENTE                                         |  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
    ConOut(Repl("-",80))  
    ConOut(PadC("Teste de Inclusao / Alteracao / Exclusao de orcamentos de venda",80))  
  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FAT" TABLES "SC5","SC6","SA1","SA2","SB1","SB2","SF4","SCJ","SCK","SCL"  
  
        //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
        //| VERIFICACAO DO AMBIENTE PARA TESTE                           |  
        //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
        ConOut("Conectado")  
  
        //VERIFICAR PRODUTO  
        dbSelectArea("SB1")  
        dbSetOrder(1)  
        If !SB1->(MsSeek(xFilial("SB1") + "000001"))  
            lOk := .F.  
            ConOut("Cadastrar produto: 000001")  
        EndIf  
  
        //VERIFICAR TES  
        dbSelectArea("SF4")  
        dbSetOrder(1)  
        If !SF4->(MsSeek(xFilial("SF4") + "501"))  
            lOk := .F.  
            ConOut("Cadastrar TES: 501")  
        EndIf  
  
        //VERIFICAR CONDICAO DE PAGAMENTO  
        dbSelectArea("SE4")  
        dbSetOrder(1)  
        If !SE4->(MsSeek(xFilial("SE4") + "001"))  
            lOk := .F.  
            ConOut("Cadastrar condicao de pagamento: 001")  
        EndIf  
  
        //VERIFICAR CLIENTE  
        dbSelectArea("SA1")  
        dbSetOrder(1)  
        If !SA1->(MsSeek(xFilial("SA1") + "000001"))  
            lOk := .F.  
            ConOut("Cadastrar cliente: 000001")  
        EndIf  
  
        If lOk  
  
            //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
            //| TESTE DE INCLUSAO                                            |  
            //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
            IF cOpc $ "3" //Inclusao              
                ConOut("Teste de inclusao")  
                ConOut("Inicio: " + Time())              
  
                For nY := 1 To 1 //Quantidade de Orcamentos  
                    cDoc := GetSxeNum("SCJ","CJ_NUM")  
                    RollBAckSx8()  
                    aCabec := {}  
                    aItens := {}  
                    aadd(aCabec,{"CJ_NUM"    ,cDoc            ,Nil})  
                    aadd(aCabec,{"CJ_CLIENTE",SA1->A1_COD     ,Nil})  
                    aadd(aCabec,{"CJ_LOJACLI",SA1->A1_LOJA    ,Nil})  
                    aadd(aCabec,{"CJ_LOJAENT",SA1->A1_LOJA    ,Nil})  
                    aadd(aCabec,{"CJ_CONDPAG",SE4->E4_CODIGO  ,Nil})  
                    CONOUT("Passou pelo Array do Cabecalho")  
  
                    For nX := 1 To 1 //Quantidade de itens  
                        aLinha := {}  
                        aadd(aLinha,{"CK_ITEM",StrZero(nX,2)        ,Nil})  
                        aadd(aLinha,{"CK_PRODUTO"   ,SB1->B1_COD    ,Nil})  
                        aadd(aLinha,{"CK_QTDVEN"    ,1              ,Nil})  
                        aadd(aLinha,{"CK_PRCVEN"    ,100            ,Nil})   
                        aadd(aLinha,{"CK_PRUNIT"    ,100            ,Nil})   
                        aadd(aLinha,{"CK_VALOR"     ,100            ,Nil})   
                        aadd(aLinha,{"CK_TES"       ,"501"          ,Nil})  
                        aadd(aItens,aLinha)  
                        CONOUT("Passou pelo Array dos itens")  
                    Next nX  
  
                    CONOUT("Iniciar a gravacao")  
                    MATA415(aCabec,aItens,3)                      
  
                    If !lMsErroAuto  
                        ConOut("Incluido com sucesso! Orcamento: " + cDoc)  
                        cOpc:= "3"  
                    Else  
                        ConOut("Erro na inclusao!")  
                        MOSTRAERRO()  
                    EndIf  
                Next nY  
  
                ConOut("Fim: " + Time())  
  
             //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
             //| TESTE DE ALTERACAO                                           |  
             //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
            ELSEIF cOpc $ "4" //Alteracao  
                aCabec := {}  
                aItens := {}  
                aLinha := {}                  
  
                //Pesquisa  
                aadd(aCabec,{"CJ_NUM"    ,cDoc     ,Nil })  //Numero do Orcamento  
                aadd(aCabec,{"CJ_CLIENTE","000001" ,Nil })  //CJ_CLIENTE antes da alteracao  
                aadd(aLinha,{"LINPOS"    ,"CK_ITEM","01"})  
                aadd(aLinha,{"AUTDELETA" ,"S"      ,Nil })  
                aadd(aItens,aLinha)  
  
                //Alteracao no Cabecalho  
                aadd(aCabec,{"CJ_CLIENTE","000002",Nil})  //CJ_CLIENTE apos a alteracao  
  
                //Alteracao no Item  
                For nX := 1 To 1  
                    aLinha := {}  
                    aadd(aLinha,{"CK_ITEM"   ,"01"     ,Nil })  
                    aadd(aLinha,{"CK_PRODUTO","000002" ,Nil })  
                    aadd(aLinha,{"CK_QTDVEN" ,2        ,Nil })  
                    aadd(aLinha,{"CK_PRCVEN" ,1000     ,Nil })  
                    aadd(aLinha,{"CK_PRUNIT" ,1000     ,Nil })  
                    aadd(aLinha,{"CK_VALOR"  ,2000     ,Nil })  
                    aadd(aLinha,{"CK_TES"    ,"501"    ,Nil })  
                    aadd(aLinha,{"LINPOS"    ,"CK_ITEM","01"})  
                    aadd(aItens,aLinha)  
                Next nX  
  
                ConOut(PadC("Teste de alteracao",80))  
                ConOut("Inicio: " + Time())  
                MATA415(aCabec,aItens,4)                  
  
                If !lMsErroAuto  
                    ConOut("Alterado com sucesso! Orcamento: " + cDoc)  
                Else  
                    ConOut("Erro na alteracao!")  
                    MOSTRAERRO()  
                EndIf  
  
                ConOut("Fim: " + Time())  
                ConOut(Repl("-",80))  
  
             //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
             //| TESTE DE EXCLUSAO                                            |  
             //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
            ELSEIF cOpc $ "5" //Exclusao  
                aCabec := {}  
  
                //Pesquisa  
                aadd(aCabec,{"CJ_NUM"    ,cDoc    ,Nil})  
                ConOut(PadC("Teste de exclusao",80))  
                ConOut("Inicio: " + Time())  
  
                MATA415(aCabec,aItens,5)  
  
                If !lMsErroAuto  
                    ConOut("Excluido com sucesso! Orcamento: " + cDoc)  
                Else  
                    ConOut("Erro na exclusao!")  
                    MOSTRAERRO()  
                EndIf  
  
                ConOut("Fim: " + Time())  
                ConOut(Repl("-",80))  
            ENDIF  
         EndIf  
  
    RESET ENVIRONMENT  
  
Return
```

**Saiba Mais**

**[MATA415 - Orçamentos (ExecAuto)](https://tdn.totvs.com/x/3QCAAw)**
