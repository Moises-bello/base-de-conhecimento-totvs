---
article_id: 18393038165015
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 02db0d23041f10d17ce121da0d340e80a35975e55ed102e032bd731e922b42c5
fetched_at: '2026-06-28T22:38:42.723525+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO MATA410
  (Devolução de Compras)
type: support-article
updated_at: '2023-10-19T13:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18393038165015-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-MATA410-Devolu%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18392994028183) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto MATA410 - Pedidos de Venda de Devolução de Compras.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de Pedidos de Venda de Devolução de Compras via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
//==============================================//  
//            DEVOLUCAO DE COMPRAS              //  
//==============================================//  
  
User Function MyMata410()  
  
    Local cDoc       := ""           //Numero do Pedido de Vendas  
    Local cA2Cod     := "000001"     //Codigo do Fornecedor  
    Local cA2Loja    := "01"         //Loja do Forncedor  
    Local cE4Codigo  := "001"        //Codigo da Condicao de Pagamento  
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
    ConOut(PadC("Inclusao de Pedido de Venda de Devolucao de Compras", 80))  
  
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
  
    //****************************************************************  
    //* VERIFICACAO DO AMBIENTE PARA TESTE  
    //****************************************************************  
  
    ConOut("Verificando o ambiente")  
  
    //VERIFICAR CONDICAO DE PAGAMENTO  
    If SE4->(! MsSeek(cFilSE4 + cE4Codigo))  
        lOk     := .F.  
        ConOut("Cadastrar Condicao de Pagamento: " + cE4Codigo)  
    EndIf  
  
    //VERIFICAR FORNECEDOR  
    If SA2->(! MsSeek(cFilSA2 + cA2Cod + cA2Loja))  
        lOk     := .F.  
        ConOut("Cadastrar Fornecedor: " + cA2Cod + " - " + cA2Loja)  
    EndIf  
  
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
                aadd(aCabec, {"C5_TIPO"   , "D"      , Nil}) //Tipo do Pedido  
                aadd(aCabec, {"C5_CLIENTE", cA2Cod   , Nil})  
                aadd(aCabec, {"C5_LOJACLI", cA2Loja  , Nil})  
                aadd(aCabec, {"C5_LOJAENT", cA2Loja  , Nil})  
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
                aadd(aLinha,{"C6_NFORI"  , "000222"     , Nil}) //NF de Origem  
                aadd(aLinha,{"C6_SERIORI", "1"          , Nil}) //Serie da NF de Origem  
                aadd(aLinha,{"C6_ITEMORI", "0001"       , Nil}) //Item da NF de Origem  
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
  
Return(.T.)
```

  
**Saiba Mais**

**[MATA410 - Geração automática de Pedido de Vendas ExecAuto](https://tdn.totvs.com/x/DIRn)**
