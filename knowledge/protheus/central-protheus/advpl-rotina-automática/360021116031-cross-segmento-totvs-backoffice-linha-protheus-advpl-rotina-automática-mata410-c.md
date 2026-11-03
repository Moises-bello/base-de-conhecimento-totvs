---
article_id: 360021116031
category: ADVPL - Rotina Automática
content_hash: ebdc17972bb3ea58bf0483220968c7c715c7c5f89909c98b6802933481d3a9ab
fetched_at: '2026-06-28T22:40:25.037528+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - AdvPL - Rotina automática
  mata410 com getsxenum
type: support-article
updated_at: '2021-11-24T13:33:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021116031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-AdvPL-Rotina-autom%C3%A1tica-mata410-com-getsxenum
---

**Ocorrência**Ao utilizar as funções GetSXENum(), ConfirmSX8() ou RollbackSX8() na rotina MATA410, o número registrado no campo C5\_NUM não está retornando de um em um.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - AdvPL - A partir da versão 11.8  
  
**Causa**  
A rotina MATA410 já possuí o controle de numeração para o campo de numero do pedido (C5\_NUM) pois o campo já possui a função GetSXENum() no inicializador padrão.  
  
**Solução**Remover o uso das funções GetSXENum(), ConfirmSX8() e RollbackSX8(), assim como o campo C5\_NUM no vetor que será enviado para a rotina automática caso no inicializador padrão do mesmo já tenha a função GetSXENum().  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function TMATA410()  
    Local nOpr    := 3  // NÚMERO DA OPERAÇÃO (INCLUSÃO)  
    Local aHeader := {} // INFORMAÇÕES DO CABEÇALHO  
    Local aLine   := {} // INFORMAÇÕES DA LINHA  
    Local aItems  := {} // CONJUNTO DE LINHAS  
    Local aArea   := {} // ARMAZENA ÁREA CORRENTE  
  
    Private lMsErroAuto := .F.  
    Private lMsHelpAuto := .T.  
  
    RPCSetEnv("99", "01", NIL, NIL, "FAT", NIL, {"SC5", "SC6"}) // ABERTURA DE AMBIENTE (REMOVER SE EXECUTADO VIA SMARTCLIENT)  
        aArea := GetArea() // CAPTURA DA ÁREA PARA FUTURA RESTAURAÇÃO  
  
        // cNum := GetSXENum("SC5", "C5_NUM") // REMOVER PARA GERAÇÃO DE NUMERAÇÃO AUTOMÁTICA PELA ROTINA  
  
        // DADOS DO CABEÇALHO  
        // AAdd(aHeader, {"C5_NUM", cNum, NIL}) // REMOVER PARA GERAÇÃO DE NUMERAÇÃO AUTOMÁTICA PELA ROTINA  
        AAdd(aHeader, {"C5_TIPO", "N", NIL})  
        AAdd(aHeader, {"C5_CLIENTE", "CLT006", NIL})  
        AAdd(aHeader, {"C5_LOJACLI", "10", NIL})  
        AAdd(aHeader, {"C5_LOJAENT", "10", NIL})  
        AAdd(aHeader, {"C5_CONDPAG", "001", NIL})  
        AAdd(aHeader, {"C5_TRANSP", "TRP001", NIL})  
        AAdd(aHeader, {"C5_TPFRETE", "R", NIL})  
  
        // DADOS DOS ITENS  
        AAdd(aLine, {"C6_PRODUTO", "PRDT0027", NIL})  
        AAdd(aLine, {"C6_QTDVEN", 1, NIL})  
        AAdd(aLine, {"C6_PRUNIT", 1116.13, NIL})  
        AAdd(aLine, {"C6_PRCVEN", 1116.13, NIL})  
        AAdd(aLine, {"C6_VALOR", 1116.13, NIL})  
        AAdd(aLine, {"C6_TES", "501", NIL})  
  
        AAdd(aItems, aLine)  
  
        MsExecAuto({|x, y, z| MATA410(x, y, z)}, aHeader, aItems, nOpr)  
  
        // VALIDAÇÃO DE ERRO  
        If (lMsErroAuto)  
            MostraErro()  
            // RollbackSX8() // REMOVER PARA GERAÇÃO DE NUMERAÇÃO AUTOMÁTICA PELA ROTINA  
  
            ConOut(Repl("-", 80))  
            ConOut(PadC("MATA410 automatic routine ended with error", 80))  
            ConOut(PadC("Ended at: " + Time(), 80))  
            ConOut(Repl("-", 80))  
        Else  
            // ConfirmSX8() // REMOVER PARA GERAÇÃO DE NUMERAÇÃO AUTOMÁTICA PELA ROTINA  
  
            ConOut(Repl("-", 80))  
            ConOut(PadC("MATA410 automatic routine successfully ended", 80))  
            ConOut(PadC("Ended at: " + Time(), 80))  
            ConOut(Repl("-", 80))  
        EndIf  
  
        RestArea(aArea) // RESTAURAÇÃO DA ÁREA ANTERIOR  
    RPCClearEnv() // FECHAMENTO DE AMBIENTE (REMOVER SE EXECUTADO VIA SMARTCLIENT)  
Return (NIL)
```

**Saiba mais**  
[MATA410 - Geração automática de Pedido de Vendas ExecAuto](http://tdn.totvs.com/pages/releaseview.action?pageId=6784012)
