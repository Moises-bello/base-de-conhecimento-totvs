---
article_id: 19572431175447
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 318f7ec5e34bad3115b33414d25eeec061ff39067c126ac57ad0b22a0e274db1
fetched_at: '2026-06-28T22:38:42.688888+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - ExecAuto MATA410
  (Com Poder DE/EM Terceiros)
type: support-article
updated_at: '2023-12-05T13:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19572431175447-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ExecAuto-MATA410-Com-Poder-DE-EM-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19572434763543) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Exemplo de utilização do Execauto MATA410 - Pedidos de Venda com Poder DE/EM Terceiros.  
  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de Pedidos de Venda com Poder DE/EM Terceiros via rotina automática (ExecAuto).

**OBS:** Quando for utilizar o pedido de venda "Tipo B (Beneficiamento)", comentar as variáveis que seriam usadas no tipo do pedido de venda "Tipo N (Normal)" e vice-versa.

**Exemplo:**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
//===================================================================//  
//            PEDIDO DE VENDAS COM PODER DE/EM TERCEIRO              //  
//===================================================================//  
  
User Function MyMata410()  
    // Se tipo B  
    //Local cA2Cod     := "000001"     //Código do Fornecedor  
    //Local cA2Loja    := "01"         //Loja do Fornecedor  
  
    // Se tipo N  
    Local cA1Cod     := "000001"     //Código do cliente  
    Local cA1Loja    := "01"         //Loja do cliente  
  
    Local cDoc       := ""           //Numero do Pedido de Vendas  
    Local cE4Codigo  := "001"        //Código da Condição de Pagamento  
    Local cFilSA2    := ""  
    Local cFilSB1    := ""  
    Local cFilSE4    := ""  
    Local cFilSF4    := ""  
    Local aCabec     := {}  
    Local aItens     := {}  
    Local aLinha     := {}  
    Local lOk        := .T.  
  
    Private lMsErroAuto    := .F.  
    Private lAutoErrNoFile := .F.  
  
    //****************************************************************  
    //* ABERTURA DO AMBIENTE  
    //****************************************************************  
  
    ConOut(Repl("-",80))  
    ConOut(PadC("Inclusao de Pedido de Venda com Poder DE/EM Terceiros", 80))  
  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FAT" TABLES "SC5","SC6","SA1","SA2","SB1","SB2","SF4"  
  
    SA2->(dbSetOrder(1))  
    SB1->(dbSetOrder(1))  
    SE4->(dbSetOrder(1))  
    SF4->(dbSetOrder(1))  
  
    cFilAGG := xFilial("AGG")  
    cFilSA2 := xFilial("SA2")  
    cFilSB1 := xFilial("SB1")  
    cFilSE4 := xFilial("SE4")  
    cFilSF4 := xFilial("SF4")  
  
    If lOk  
  
        //****************************************************************  
        //* INCLUSAO - INICIO  
        //****************************************************************  
  
            ConOut("Teste de Inclusao")  
            ConOut("Inicio: " + Time())  
  
                //CABEÇALHO  
                cDoc := GetSxeNum("SC5", "C5_NUM")  
                RollBAckSx8()  
                aCabec   := {}  
                aItens   := {}  
                aLinha   := {}  
                aadd(aCabec, {"C5_NUM"    , cDoc     , Nil})  
                  
                // Se tipo N  
                aadd(aCabec, {"C5_TIPO"   , "N"      , Nil}) //Tipo do Pedido 'N - Normal'  
                aadd(aCabec, {"C5_CLIENTE", cA1Cod   , Nil})  
                aadd(aCabec, {"C5_LOJACLI", cA1Loja  , Nil})  
                aadd(aCabec, {"C5_LOJAENT", cA1Loja  , Nil})   
                 
                // Se tipo B  
                //aadd(aCabec, {"C5_TIPO"   , "B"      , Nil}) //Tipo do Pedido 'B - Beneficiamento'  
                //aadd(aCabec, {"C5_CLIENTE", cA2Cod   , Nil})  
                //aadd(aCabec, {"C5_LOJACLI", cA2Loja  , Nil})  
                //aadd(aCabec, {"C5_LOJAENT", cA2Loja  , Nil})  
                  
                aadd(aCabec, {"C5_CONDPAG", cE4Codigo, Nil})  
                CONOUT("Passou pelo Array do Cabecalho")  
  
                //ITENS  
                aLinha := {}  
                aadd(aLinha,{"C6_ITEM"   , "01"         , Nil}) //Item do pedido  
                aadd(aLinha,{"C6_PRODUTO", "000001"     , Nil})  
                aadd(aLinha,{"C6_QTDVEN" , 1            , Nil})  
                aadd(aLinha,{"C6_PRCVEN" , 100          , Nil})  
                aadd(aLinha,{"C6_PRUNIT" , 100          , Nil})  
                aadd(aLinha,{"C6_VALOR"  , 100          , Nil})  
                aadd(aLinha,{"C6_TES"    , "501"        , Nil})  
                aadd(aLinha,{"C6_IDENTB6", "000077"     , Nil}) //*Código identificador do Poder/EM Terceiro se a TES for de devolução (F4_PODER3 = 'D - Devolução')            
                aadd(aLinha,{"C6_NFORI"  , "000222"     , Nil}) //*NF de Origem se a TES deve ser preenchido se for de devolução (F4_PODER3 = 'D - Devolução')  
                aadd(aLinha,{"C6_SERIORI", "1"          , Nil}) //*Serie da NF de Origem deve ser preenchido se a TES for de devolução (F4_PODER3 = 'D - Devolução')  
                aadd(aLinha,{"C6_ITEMORI", "0001"       , Nil}) //*Item da NF de Origem deve ser preenchido se a TES for de devolução (F4_PODER3 = 'D - Devolução')  
                // *Se a TES não for de devolução, passar em branco no lugar do conteúdo, assim: ""  
                 
                aadd(aItens, aLinha)  
                CONOUT("Passou pelo Array dos itens")  
  
                CONOUT("Iniciando a gravacao")  
                MSExecAuto({|a, b, c, d| MATA410(a, b, c, d)}, aCabec, aItens, 3, .F.)  
  
                If !lMsErroAuto  
                    ConOut("Incluido com sucesso! Pedido: " + cDoc)  
                Else  
                    ConOut("Erro na inclusao!")  
                    MOSTRAERRO()  
                EndIf  
  
            ConOut("Fim: " + Time())  
            ConOut(Repl("-",80))  
  
    EndIf  
  
    RESET ENVIRONMENT
```
