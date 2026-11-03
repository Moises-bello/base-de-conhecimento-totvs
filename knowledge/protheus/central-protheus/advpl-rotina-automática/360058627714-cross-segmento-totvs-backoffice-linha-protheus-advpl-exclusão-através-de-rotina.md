---
article_id: 360058627714
category: ADVPL - Rotina Automática
content_hash: 26875b6328f7fe7d2e6be9ee23367a686bc7297a572d84fd6fbc61b362b52ca9
fetched_at: '2026-06-28T22:40:24.251681+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Exclusão através
  de rotina automática TECA040 '
type: support-article
updated_at: '2022-06-21T17:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058627714-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exclus%C3%A3o-atrav%C3%A9s-de-rotina-autom%C3%A1tica-TECA040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível realizar a exclusão via ExecAuto rotina TECA040?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.25.  
  
**Solução**

O ponto de entrada TECA040 será utilizado para **exclusão** da base instalada utilizado rotina automática. Disponibilização de exemplo - MsExecAuto.  
Sintaxe  
TECA040 - Exclusão da base instalada através de rotina automática ( ) --> lRet  
  
Retorno

```
lRet(logico)
```

Exemplo:

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TOPCONN.CH"  
#INCLUDE "XMLXFUN.CH"  
#INCLUDE "TBICONN.CH"  
  
/*/  
ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ  
±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±  
±±ÚÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄ¿±±  
±±³Funcao    ³ Ex040Aut ³ Autor ³ Vendas Clientes       ³ Data ³ 04/12/2020 ³±±  
±±ÃÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄ´±±  
±±³Descricao ³ Exclui registro da base instalada atraves de rotina automatica³±±  
±±ÃÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´±±  
±±³ Uso      ³ Field Service                                                 ³±±  
±±ÀÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ±±  
±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±  
ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß  
/*/  
User Function Ex040Aut()  
Local aCab040   := {}    // Cabecalho do AA3  
Local aItens040 := {}    // Itens AA4  
Local lRet      := .T.    
Local nI  
Local aNrsSerie := {} // Array com o numero de serie para exclusao da base instalada  
Local nRegs     := 0  
Local dData     := "04/12/2020"  
  
PRIVATE lMsErroAuto := .F.  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ  
//| Abertura do ambiente                                          
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Exclusao da Base Instalada",80))  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "TEC" TABLES "AA3","AA4","SXB"  
  
Aadd(aNrsSerie,"00000000002000000157")  
  
nRegs     := Len(aNrsSerie)   
  
For nI := 1 to nRegs                                          
    Aadd(aCab040, { "AA3_FILIAL"    , ""                , NIL } )                 
    Aadd(aCab040, { "AA3_CODCLI"    , "000001"          , NIL } )                 
    Aadd(aCab040, { "AA3_LOJA"      , "01"              , NIL } )                 
    Aadd(aCab040, { "AA3_CODPRO"    , "000000000000001" , NIL } )                 
    Aadd(aCab040, { "AA3_NUMSER"    , aNrsSerie[nI]     , NIL } )                  
    Aadd(aCab040, { "AA3_DTVEN"     , dData             , NIL } )                 
    TECA040(,aCab040,aItens040,5)     
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿                 
    //³VerIfica se houveram erros durante a geracao da base   ³                 
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ                 
  
    If lMsErroAuto                                
        lRet := !lMsErroAuto                 
    Endif  
                                                                                
    aCab040 := {}  
Next  
  
Return lRet
```

**Saiba mais**[TECA040 - Criação da base instalada através de rotina automática](https://tdn.totvs.com/pages/releaseview.action?pageId=6785778)
