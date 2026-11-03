---
article_id: 39285787380759
category: Financeiro - Compensação Contas a Pagar
content_hash: 6b921275c2b0f8322eef39cf432051226ea1f2756c89ab7327822b825d86f715
fetched_at: '2026-06-28T22:37:33.672801+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA340 - Como utilizar a função
  FinCmpAut para realizar compensações automáticas no módulo Financeiro (Contas a
  Pagar)?
type: support-article
updated_at: '2026-03-25T16:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39285787380759-Cross-Segmento-Backoffice-Linha-Protheus-FINA340-Como-utilizar-a-fun%C3%A7%C3%A3o-FinCmpAut-para-realizar-compensa%C3%A7%C3%B5es-autom%C3%A1ticas-no-m%C3%B3dulo-Financeiro-Contas-a-Pagar
---

Para utilizar o processo de Compensação Automática Contas a Pagar é necessário chamar a função: **FinCmpAut.**

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39285787355799)***Tempo aproximado para leitura: **00:08:00 min**

**Ocorrência:**  
Qual função deve ser utilizada **MaIntBxCP ou FinCmpAut** para realizar compensações automáticas no módulo Financeiro (Contas a Pagar)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**  
Para realizar o processo de **Compensação Automática no Contas a Pagar** via rotina automática, deve-se utilizar a função **FinCmpAut**. Esta função permite a compensação de múltiplos títulos (N para N), abrangendo adiantamentos ou devoluções (PA ou NDF) contra títulos de débito (NF, DP, etc.).

É importante destacar que o comportamento da compensação, especialmente no que tange à retenção de impostos, é condicionado pela configuração do parâmetro **MV\_IMPCOM**:

* **MV\_IMPCOM = .T. (Verdadeiro):** A compensação seguirá as mesmas regras de negócio e validações da rotina **FINA340** (Compensação CP), incluindo todo o processo de retenção e cálculo de impostos.
* **MV\_IMPCOM = .F. (Falso):** O sistema executará a compensação baseada no modelo legado (fonte apartado), sem as validações específicas de retenção da rotina FINA340.

**Observação sobre Estornos:** O estorno será aplicado integralmente a todas as compensações realizadas entre os títulos informados nos arrays de títulos e de estorno, não sendo permitida a seleção de uma sequência específica para o cancelamento.

Exemplo de utilização, considerando os seguintes títulos em aberto no Contas a Pagar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39285787356311)

```
#INCLUDE "Protheus.ch"
#INCLUDE "RWMAKE.CH"
#INCLUDE "TBICONN.CH"
 
Static __COMPAUT := Nil
 
User Function CMPAUTOMA()
    Local lRet := .F.
    Local cQry := ""
    Local aTipos := {"NF ", "PA ", "NDF"}
    Local cTblTmp := ""
    Local aNF := {}
    Local aPA_NDF := {}
    Local aContabil := {}
    Local bBlock := Nil
    Local aEstorno := {}
    Local nSldComp := 1000
    Local nTaxaPA := 0
    Local nTaxaNF := 0
    Local nHdl := 0
    Local nOperacao := 2
    Local aRecSE5 := {}
    Local aNDFDados := {}
    Local lHelp := .T.

    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"
 
    If __COMPAUT == Nil
        cQry := "SELECT E2_TIPO TIPO, R_E_C_N_O_ R_E_C_N_O FROM " + RetSqlName("SE2") + " "
        cQry += "WHERE E2_SALDO > 0 AND E2_TIPO IN (?) "
        cQry += "AND D_E_L_E_T_ = ' ' "
        cQry += "ORDER BY E2_TIPO"
        cQry := ChangeQuery(cQry)
        __COMPAUT := FWPreparedStatement():New(cQry)
    EndIf
 
    __COMPAUT:SetIn(1, aTipos)
    cQry := __COMPAUT:GetFixQuery()
    cTblTmp := MpSysOpenQuery(cQry)
 
    While (cTblTmp)->(!Eof())
        If (cTblTmp)->TIPO $ MVPAGANT+"|"+MV_CPNEG
            Aadd(aPA_NDF, (cTblTmp)->R_E_C_N_O)
        Else
            Aadd(aNF, (cTblTmp)->R_E_C_N_O)
        EndIf
 
        (cTblTmp)->(DbSkip())
        lRet := .T.
    EndDo
 
    (cTblTmp)->(DbCloseArea())
    cTblTmp := ""
 
    If lRet
        Pergunte("AFI340", .F.)
        lContabiliza := MV_PAR11 == 1
        lAglutina := MV_PAR08 == 1
        lDigita := MV_PAR09 == 1
 
        lRet := FinCmpAut(aNF, aPA_NDF, aContabil, bBlock, aEstorno, nSldComp, dDatabase, nTaxaPA ,nTaxaNF, nHdl, nOperacao, aRecSE5, aNDFDados, lHelp)
 
        If lRet
            Alert("Compensação realizada com sucesso")
        Else
            Alert("Ocorreu um erro no processo de compensação")
        EndIf
    Else
        Alert("Não existem dados a serem compensados")    
    EndIf
 
Return Nil
```

**Importante 📢️:** Certifique-se de que a inclusão do PA seja realizada com movimentação bancária:

Ao incluir o PA (Pagamento Antecipado), verifique se o parâmetro "Gera movimento bancário sem cheque" está configurado para "Sim" e "Gera cheque para adiantamento" para "Não"
