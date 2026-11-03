---
article_id: 8243004342935
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 9f91ac94e1edaae5a7626b45eeac7ec183cb86e556f0041a48a27880aff5a168
fetched_at: '2026-06-28T22:38:32.978734+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - EXECAUTO TMKA271
type: support-article
updated_at: '2023-06-26T17:03:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8243004342935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-EXECAUTO-TMKA271
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15584167530007) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto TMKA271 - Rotina automática atendimentos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - A partir da release 12.  
  
**Solução**Rotina automática para geração de atendimentos no módulo de Call Center.  
  
**Exemplo**

```
#INCLUDE 'Protheus.ch'  
#INCLUDE "TBICONN.CH"    
  
User Function MyTMKA271(cRotina)  
  
    Local aCabec    := {}  
    Local aItens    := {}  
    Local aLinha    := {}  
    Local nX        := 0  
    Local nY        := 0  
    Local lOk       := .T.  
    Local cEndc     := ""  
    Local cEnde     := ""  
    Local cBairroc  := ""  
    Local cBairroe  := ""  
    Local cMunc     := ""  
    Local cMune     := ""  
    Local cCepc     := ""  
    Local cCepe     := ""  
    Local cEstc     := ""  
    Local cEste     := ""  
    Local cCod      := ""  
    Local cLoja     := ""  
    Local cAtend    := ""  
    Local nDesconto := 0  
    Local nFrete    := 0  
    Local nDespesa  := 0  
    Local lAlterar  := .F.  
    DEFAULT cRotina     := "3"  //Indica as rotinas de atendimento (1-Telemarketing / 2-Televendas / 3-Telecobrança)  
    PRIVATE lMsErroAuto := .F.                                           
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //| Abertura do ambiente                                         |  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
    ConOut(Repl("-",80))  
    ConOut(PadC("Teste de Inclusao de Atendimento"  ,80))  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" USER "ADMIN" PASSWORD "" MODULO "TMK" TABLES "SUA","SUB","SUC","SUD","SB1","SA1","SUS","SE4","AC8","SA4","SU7"  
   
        //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
        //| Verificacao do ambiente para teste para Televendas           |  
        //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
        ConOut("Verificando ambiente para teste Televendas")  
        If cRotina == "2"  
            DbSelectArea("SB1")  
            DbSetOrder(1)  
            If !DbSeek(xFilial("SB1")+"000001")  
                lOk := .F.  
                ConOut("Cadastrar produto: 000001")  
            Endif              
  
            DbSelectArea("SF4")  
            DbSetOrder(1)  
            If !DbSeek(xFilial("SF4")+"501")  
                lOk := .F.  
                ConOut("Cadastrar TES: 501")  
            Endif              
  
            DbSelectArea("SE4")  
            DbSetOrder(1)  
            If !DbSeek(xFilial("SE4")+"001")  
                lOk := .F.  
                ConOut("Cadastrar condicao de pagamento: 001")  
            Endif  
        Endif              
  
        DbSelectArea("SA1")  
        DbSetOrder(1)  
        If !SA1->(DbSeek(xFilial("SA1")+"000001"))  
            lOk := .F.  
            ConOut("Cadastrar cliente: 000001")  
        Else  
            cCod        :=SA1->A1_COD  
            cLoja       :=SA1->A1_LOJA  
            cEndc       :=SA1->A1_ENDCOB  
            cBairroc    :=SA1->A1_BAIRROC  
            cMunc       :=SA1->A1_MUNC  
            cCepc       :=SA1->A1_CEPC  
            cEstc       :=SA1->A1_ESTC  
            cEnde       :=SA1->A1_ENDENT  
            cBairroe    :=SA1->A1_BAIRROE  
            cMune       :=SA1->A1_MUNE  
            cEste       :=SA1->A1_ESTE  
            nDesconto   :=0  
            nFrete      :=0  
            nDespesa    :=0  
        Endif  
  
        Do Case  
            Case cRotina == "2"  
                //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
                //³Incluir atendimentos do televendas   ³  
                //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
                ConOut("Incluindo atendimentos do televendas")  
                ConOut("Inicio: " +Time())  
                For nY := 1 To 1  
                    aCabec := {}  
                    aItens := {}  
                    AADD(aCabec,{"UA_CLIENTE"   ,cCod           ,Nil})  
                    AADD(aCabec,{"UA_LOJA"      ,cLoja          ,Nil})  
                    AADD(aCabec,{"UA_OPERADO"   ,"000001"       ,Nil})  //Codigo do Operador  
                    AADD(aCabec,{"UA_OPER"      ,"2"            ,Nil})  //1-Faturamento 2-Orcamento 3-Atendimento  
                    AADD(aCabec,{"UA_TMK"       ,"2"            ,Nil})  //2-Ativo 1-Receptivo  
                    AADD(aCabec,{"UA_CONDPG"    ,"001"          ,Nil})  //Condicao de Pagamento  
                  //AADD(aCabec,{"UA_TRANSP"    ,"000001"       ,Nil})  //Transportadora  
                    AADD(aCabec,{"UA_ENDCOB"    ,cEndc          ,Nil})  
                    AADD(aCabec,{"UA_BAIRROC"   ,cBairroc       ,Nil})  
                    AADD(aCabec,{"UA_MUNC"      ,cMunc          ,Nil})  
                    AADD(aCabec,{"UA_CEPC"      ,cCepc          ,Nil})  
                    AADD(aCabec,{"UA_ESTC"      ,cEstc          ,Nil})  
                    AADD(aCabec,{"UA_ENDENT"    ,cEnde          ,Nil})  
                    AADD(aCabec,{"UA_BAIRROE"   ,cBairroe       ,Nil})  
                    AADD(aCabec,{"UA_MUNE"      ,cMune          ,Nil})  
                    AADD(aCabec,{"UA_CEPE"      ,cCepe          ,Nil})  
                    AADD(aCabec,{"UA_ESTE"      ,cEste          ,Nil})  
                    AADD(aCabec,{"UA_PROSPEC"   ,.F.            ,Nil})  
                    AADD(aCabec,{"UA_DESCONT"   ,nDesconto      ,Nil})  
                    AADD(aCabec,{"UA_FRETE"     ,nFrete         ,Nil})  
                    AADD(aCabec,{"UA_DESPESA"   ,nDespesa       ,Nil})                  
  
                    For nX := 1 To 1  
                        aLinha := {}  
                        aadd(aLinha,{"UB_ITEM"      ,StrZero(nX,2)  ,Nil})  
                        aadd(aLinha,{"UB_PRODUTO"   ,SB1->B1_COD    ,Nil})  
                        aadd(aLinha,{"UB_QUANT"     ,2              ,Nil})  
                        aadd(aLinha,{"UB_VRUNIT"    ,50             ,Nil})  
                        aadd(aLinha,{"UB_TES"       ,"501"          ,Nil})  
                        aadd(aItens,aLinha)  
                    Next nX  
                Next nY              
  
            Case cRotina == "3"           
                //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
                //³Incluir atendimentos do telecobranca ³  
                //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
                ConOut("Incluindo atendimentos do telecobranca")  
                ConOut("Inicio: " + Time())  
                For nY := 1 To 1  
                    aCabec := {}  
                    aItens := {}  
                    AADD(aCabec,{"ACF_CLIENT"   ,cCod           ,Nil})  //Codigo do cliente  
                    AADD(aCabec,{"ACF_LOJA"     ,cLoja          ,Nil})  //Codigo da loja  
                    AADD(aCabec,{"ACF_OPERAD"   ,"000001"       ,Nil})  //Codigo do Operador  
                    AADD(aCabec,{"ACF_OPERA"    ,"2"            ,Nil})  //Ligacao - 1-Receptivo 2-Ativo  
                    AADD(aCabec,{"ACF_CODCON"   ,"000001"       ,Nil})  //1-Ativo 2-Receptivo  
                    AADD(aCabec,{"ACF_STATUS"   ,"2"            ,Nil})  //Status do Atendimento 1-Atendimento 2-Cobranca 3-Encerrado  
                    AADD(aCabec,{"ACF_MOTIVO"   ,"000001"       ,Nil})  //Ocorrencia      
                    AADD(aCabec,{"ACF_PENDEN"   ,dDatabase      ,Nil})  //Data de Retorno  
                    AADD(aCabec,{"ACF_HRPEND"   ,"20:00"        ,Nil})  //Hora de Retorno  
                    AADD(aCabec,{"ACF_OBS   "   ,"Testes"       ,Nil})  //Observacao                  
  
                    DbSelectArea("SK1")  
                    DbSetOrder(4)  
                    If DbSeek(xFilial("SK1")+ cCod + cLoja)  
                        While !SK1->(Eof()) .AND. xFilial("SK1") == SK1->K1_FILIAL .AND. ;  
                                        ( cCod + cLoja )    == (SK1->K1_CLIENTE + K1_LOJA)                                                      
  
                            //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
                            //³Inserir o array de Itens obrigatoriamente na sequencia abaixo.    ³  
                            //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
                            aLinha := {}  
                            aadd(aLinha,{"ACG_PREFIX"   ,SK1->K1_PREFIXO ,Nil})  
                            aadd(aLinha,{"ACG_PARCEL"   ,SK1->K1_PARCELA ,Nil})  
                            aadd(aLinha,{"ACG_TIPO  "   ,SK1->K1_TIPO    ,Nil})  
                            aadd(aLinha,{"ACG_FILORI"   ,SK1->K1_FILORIG ,Nil})  
                            aadd(aLinha,{"ACG_TITULO"   ,SK1->K1_NUM     ,Nil})  
                            aadd(aLinha,{"ACG_STATUS"   ,"2"             ,Nil})//Negociado  
                            aadd(aItens,aLinha)  
                            SK1->(Dbskip())                         
                        End  
                    Endif  
                Next nY  
              
        EndCase                  
  
        //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
        //| Executa a chamada da rotina de atendimento CALL CENTER       |  
        //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
        ConOut("Iniciando a gravacao")  
        TMKA271(aCabec,aItens,3,cRotina)  
  
        //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
        //³Exibe se foi feita a inclusao ou se retornou erro³  
        //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
        If !lMsErroAuto  
            ConOut("Atendimento incluido com sucesso!")  
        Else  
            ConOut("Erro na inclusao!")  
            Mostraerro()  
            DisarmTransaction()  
            Break  
        Endif  
        ConOut("Fim  : "+Time())  
  
        //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
        //³Alteracao de atendimentos          ³  
        //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
        If lAlterar  
            Do Case             
                //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
                //³Alteracao de atendimentos televendas  ³  
                //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ                 
                Case cRotina == "2"  
                    ConOut("Alteracao de atendimentos televendas")  
                    DbSelectArea("SUA")  
                    DbSetOrder(1)  
                    DbSeek(xFilial("SUA")+"000001")                      
  
                    DbSelectArea("SUB")  
                    DbSetOrder(1)  
                    DbSeek(xFilial("SUB")+"000001")                      
  
                    DbSelectArea("SB1")  
                    DbSetOrder(1)  
                    DbSeek(xFilial("SB1")+SUB->UB_PRODUTO)                                      
  
                    aCabec := {}  
                    aItens := {}  
                    AADD(aCabec,{"UA_NUM"       ,SUA->UA_NUM    ,Nil})  
                    AADD(aCabec,{"UA_CLIENTE"   ,SUA->UA_CLIENTE,Nil})  
                    AADD(aCabec,{"UA_LOJA"      ,SUA->UA_LOJA   ,Nil})  
                    AADD(aCabec,{"UA_OPERADO"   ,"000001"       ,Nil})  //Codigo do Operador  
                    AADD(aCabec,{"UA_OPER"      ,"2"            ,Nil})  //1-Faturamento 2-Orcamento 3-Atendimento  
                    AADD(aCabec,{"UA_TMK"       ,"1"            ,Nil})  //1-Ativo 2-Receptivo  
                    AADD(aCabec,{"UA_CONDPG"    ,"001"          ,Nil})  //Condicao de Pagamento  
                    AADD(aCabec,{"UA_TRANSP"    ,"000001"       ,Nil})  //Transportadora  
  
                    For nX := 1 To 1  
                        aLinha := {}  
                        aadd(aLinha,{"LINPOS"    ,"UB_ITEM"      ,"01"})  
                        aadd(aLinha,{"AUTDELETA" ,"N"            ,Nil})  
                        aadd(aLinha,{"UB_PRODUTO",SUB->UB_PRODUTO,Nil})  
                        aadd(aLinha,{"UB_QUANT"  ,3              ,Nil})  
                        aadd(aLinha,{"UB_VRUNIT" ,50             ,Nil})  
                        aadd(aLinha,{"UB_TES"    ,"501"          ,Nil})  
                        aadd(aItens,aLinha)  
                    Next nX                      
  
                //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
                //³Alteracao de atendimentos telecobranca³  
                //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
                ConOut("Alteracao de atendimentos telecobranca")  
                Case cRotina == "3"  
                    cAtend  := "000023"  
                    DbSelectArea("ACF")  
                    DbSetOrder(1)  
                    DbSeek(xFilial("ACF")+cAtend)              
  
                    aCabec := {}  
                    aItens := {}  
                    AADD(aCabec,{"ACF_CODIGO"   ,cAtend         ,Nil})  //Codigo do Atendimento para alteracao  
                    AADD(aCabec,{"ACF_CLIENT"   ,cCod           ,Nil})  //Codigo do cliente  
                    AADD(aCabec,{"ACF_LOJA"     ,cLoja          ,Nil})  //Codigo da loja  
                    AADD(aCabec,{"ACF_OPERAD"   ,"000002"       ,Nil})  //Codigo do Operador  
                    AADD(aCabec,{"ACF_OPERA"    ,"1"            ,Nil})  //Ligacao - 1-Ativo 2-Receptivo  
                    AADD(aCabec,{"ACF_CODCON"   ,"000001"       ,Nil})  //1-Ativo 2-Receptivo  
                    AADD(aCabec,{"ACF_STATUS"   ,"3"            ,Nil})  //Status do Atendimento 1-Atendimento 2-Cobranca 3-Encerrado  
                    AADD(aCabec,{"ACF_MOTIVO"   ,"000001"       ,Nil})  //Ocorrencia      
                    AADD(aCabec,{"ACF_PENDEN"   ,dDatabase      ,Nil})  //Data de Retorno  
                    AADD(aCabec,{"ACF_HRPEND"   ,"20:00"        ,Nil})  //Hora de Retorno  
                    AADD(aCabec,{"ACF_CODENC"   ,"000001"       ,Nil})  //Codigo do Encerramento  
                    AADD(aCabec,{"ACF_OBSMOT"   ,"Observação do Encerramento"   ,Nil})  
                      
                    DbSelectArea("ACG")   
                    DbSetOrder(1)  
                    DbSeek(xFilial("ACG")+cAtend)  
                    While !ACG->(Eof()) .AND.    xFilial("ACG")  == ACG->ACG_FILIAL .AND. ;  
                                                                    ACG->ACG_CODIGO  == cAtend  
                         
                        aLinha := {}  
                        aadd(aLinha,{"AUTDELETA"  ,"N"             ,Nil})  
                        aadd(aLinha,{"ACG_PREFIX" ,ACG->ACG_PREFIX ,Nil})  //Prefixo do titulo  
                        aadd(aLinha,{"ACG_PARCEL" ,ACG->ACG_PARCEL ,Nil})  //Parcela do titulo  
                        aadd(aLinha,{"ACG_TIPO  " ,ACG->ACG_TIPO   ,Nil})  //Tipo do Titulo  
                        aadd(aLinha,{"ACG_FILORI" ,ACG->ACG_FILORI ,Nil})  //Filial de Origem  
                        aadd(aLinha,{"ACG_TITULO" ,ACG->ACG_TITULO ,Nil})  //Numero do Titulo  
                        aadd(aLinha,{"ACG_STATUS" ,"1"             ,Nil})  //Status do Titulo. 1-Pago 2-Negociado  
                        aadd(aItens,aLinha)  
                        
                        ACG->(Dbskip())  
                         
                    End     
            
            EndCase               
  
            //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
            //³Exibe se foi feita a alteracao ou se retornou erro³  
            //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
            ConOut(PadC("Teste de alteracao"    ,80))  
            ConOut("Inicio: " +Time())              
  
            TMKA271(aCabec,aItens,4,cRotina)              
  
            If !lMsErroAuto  
                ConOut("Alterado com sucesso! "+cAtend)  
            Else  
                ConOut("Erro na alteracao!")  
                Mostraerro()  
                DisarmTransaction()  
                Break  
            Endif                         
             
            ConOut("Fim  : "+Time())  
            ConOut(Repl("-",80))        
        Endif  
         
    RESET ENVIRONMENT  
Return(.T.)
```

**Saiba Mais: [TMKA271 - Rotina automática atendimentos](https://tdn.totvs.com/x/f5Jn)**
