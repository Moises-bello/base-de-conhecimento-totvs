---
article_id: 15111556505239
category: Faturamento - Cadastros
content_hash: d15013250e54fc6eb6fcffafc9b812b20725eb5226f037b78e8b05273068263c
fetched_at: '2026-06-28T22:38:36.585251+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO MATA360
type: support-article
updated_at: '2023-06-06T19:36:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15111556505239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-MATA360
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto MATA360 - Condições de Pagamento.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de Condição de Pagamento via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function MyMata360()  
  
    //DEFININDO variáveis  
    Local nOpcX         := 5   //Seleciona o tipo da operacao (3-Inclusao / 4-Alteracao / 5-Exclusao)  
    Local aItemAux      := {}  //Array auxiliar para inserção dos itens  
    Local aCabec        := {}  //Array do cabeçalho (SE4)  
    Local aItens        := {}  //Array que irá conter os itens (SEC)  
    Private lMsErroAuto := .F. //Indicador do status pós chamada  
  
    ConOut(Repl("-",80))  
    ConOut(PadC("Teste de Inclusao / Alteracao / Exclusao de Condicao de Pagamento", 80))  
  
    //Abertura do ambiente  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FAT" TABLES "SE4","SEC"  
  
        SE4->(dbSetOrder(1))  
        SEC->(dbSetOrder(1))  
  
        cFilAGG := xFilial("SE4")  
        cFilSA1 := xFilial("SEC")  
  
        //Inclusão - Início  
        If nOpcX = 3 //Inclusao  
  
            ConOut("Teste de Inclusao")  
            ConOut("Inicio: " + Time())  
  
            //Populando Cabeçalho  
            aAdd(aCabec, {"E4_CODIGO", "800"         , Nil})  
            aAdd(aCabec, {"E4_TIPO"  , "1"           , Nil})  
            aAdd(aCabec, {"E4_COND"  , "00"          , Nil})  
            aAdd(aCabec, {"E4_DESCRI", "TESTE ROTAUT", Nil})  
            CONOUT("Passou pelo Array do Cabecalho")  
  
            //Populando Item auxiliar  
            aAdd(aItemAux, {"EC_ITEM"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_TIPO"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_COND"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_IPI"   , ""  , Nil})  
            aAdd(aItemAux, {"EC_DDD"   , ""  , Nil})  
            aAdd(aItemAux, {"EC_SOLID" , ""  , Nil})  
            aAdd(aItemAux, {"EC_RATEIO", 0.00, Nil})  
            aAdd(aItens, aItemAux)  
            CONOUT("Passou pelo Array dos itens")  
  
            //Chamando rotina automática de inclusão  
            CONOUT("Iniciando a gravacao")  
            MSExecAuto({|x,y,z|mata360(x,y,z)},aCabec,aItens, nOpcX)  
  
            //Verificando status da rotina executada  
            If !lMsErroAuto  
                ConOut("Incluido com sucesso")  
            Else  
                ConOut("Erro na inclusao")  
            EndIf  
  
            ConOut("Fim: " + Time())  
            ConOut(Repl("-",80))  
  
        //Alteração - Início  
        ElseIf nOpcX = 4 //Alteracao  
  
            ConOut("Teste de Alteracao")  
            ConOut("Inicio: " + Time())  
  
            aAdd(aCabec, {"E4_CODIGO", "800"         , Nil})  
            aAdd(aCabec, {"E4_TIPO"  , "1"           , Nil})  
            aAdd(aCabec, {"E4_COND"  , "00,30"       , Nil})  
            aAdd(aCabec, {"E4_DESCRI", "TESTE ROTAUT", Nil})  
  
            aAdd(aItemAux, {"EC_ITEM"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_TIPO"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_COND"  , ""  , Nil})  
            aAdd(aItemAux, {"EC_IPI"   , ""  , Nil})  
            aAdd(aItemAux, {"EC_DDD"   , ""  , Nil})  
            aAdd(aItemAux, {"EC_SOLID" , ""  , Nil})  
            aAdd(aItemAux, {"EC_RATEIO", 0.00, Nil})  
            aAdd(aItens, aItemAux)  
  
            MSExecAuto({|x,y,z|mata360(x,y,z)},aCabec,aItens, nOpcX)  
  
            If !lMsErroAuto  
                ConOut("Alterado com sucesso")  
            Else  
                ConOut("Erro na alteracao")  
            EndIf  
  
            ConOut("Fim: " + Time())  
            ConOut(Repl("-",80))  
  
        //Exclusão - Início  
        ElseIf nOpcX = 5 //Exclusao  
  
            ConOut("Teste de Exclusao")  
            ConOut("Inicio: " + Time())  
  
            aAdd(aCabec, {"E4_CODIGO", "800"         , Nil})  
  
            MSExecAuto({|x,y,z|mata360(x,y,z)},aCabec,aItens, nOpcX)  
  
            If !lMsErroAuto  
                ConOut("Excluido com sucesso")  
            Else  
                ConOut("Erro na exclusao")  
            EndIf  
  
            ConOut("Fim: " + Time())  
            ConOut(Repl("-",80))  
  
        EndIf  
  
    RESET ENVIRONMENT  
  
Return
```

**Saiba Mais**

**[MATA360 - Condição de Pagamento (ExecAuto)](https://tdn.totvs.com/x/4gZvBg)**
