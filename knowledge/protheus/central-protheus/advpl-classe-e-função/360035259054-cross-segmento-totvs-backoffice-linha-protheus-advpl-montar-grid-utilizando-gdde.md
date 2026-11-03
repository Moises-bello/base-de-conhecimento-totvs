---
article_id: 360035259054
category: ADVPL - Classe e Função
content_hash: e3e8a496dc0d101855d35656ab28690fac49c122107f0776672eee4247c0101a
fetched_at: '2026-06-28T22:40:17.036628+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Montar grid utilizando
  GDDeleted
type: support-article
updated_at: '2022-04-29T12:27:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035259054-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Montar-grid-utilizando-GDDeleted
---

**Dúvida**Como utilizar montar uma grid utilizando a função `GDDeleted()`?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
//------------------------------------------------------  
// EXIBE GRID PARA VALIDAÇÃO DE GDDELETED()  
//------------------------------------------------------  
User Function T230GDDEL()  
    Local nX        As Numeric  
    Private aHeader As Array  
    Private aCols   As Array  
    Private oGet    As Object  
    Private n       As Numeric  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    nX      := 0  
    n       := 0  
    aHeader := {}  
    aCols   := {}  
    oGet    := NIL  
  
    // POSICIONAR NO REGISTRO  
    DbSelectArea("SA1")  
    DbSetOrder(1)  
    DbSeek(FwxFilial("SA1"))  
  
    // MONTAGEM DO CABEÇALHO  
    Aadd(aHeader, {"Codigo",        "A1_COD",    "@!", 6,  0, "AllWaysTrue()", "û", "C", "SA1",;  
        NIL, NIL, NIL, NIL, NIL, NIL, NIL})  
    Aadd(aHeader, {"Loja",          "A1_LOJA",   "@!", 2,  0, "AllWaysTrue()", "û", "C", "SA1",;  
        NIL, NIL, NIL, NIL, NIL, NIL, NIL})  
    Aadd(aHeader, {"Nome",          "A1_NOME",   "@!", 15, 0, "AllWaysTrue()", "û", "C", "SA1",;  
        NIL, NIL, NIL, NIL, NIL, NIL, NIL})  
    Aadd(aHeader, {"Nome Reduzido", "A1_NREDUZ", "@!", 10, 0, "AllWaysTrue()", "û", "C", "SA1",;  
        NIL, NIL, NIL, NIL, NIL, NIL, NIL})  
  
    // INSERE OS DADOS NA TABELA  
    While (!EOF())  
        // DEFINE O TAMANHO DO GRID  
        AAdd(aCols, Array(Len(aHeader) + 1))  
        aCols[Len(aCols)][1] := SA1->A1_COD  
        aCols[Len(aCols)][2] := SA1->A1_LOJA  
        aCols[Len(aCols)][3] := SA1->A1_NOME  
        aCols[Len(aCols)][4] := SA1->A1_NREDUZ  
  
        // MARCA UMA LINHA COMO DELETADA  
        If (Mod(Len(aCols), 2) == 1)  
            aCols[Len(aCols)][5] := .F.  
        Else  
            aCols[Len(aCols)][5] := .T.  
        EndIf  
  
        // ADICIONA UMA LINHA NO VETOR  
        DbSkip()  
    End  
  
    // EFETUA A MONTAGEM DA CAIXA DE DIÁLOGO  
    DEFINE MSDIALOG oDlg TITLE "MSNEWGETDADOS + GD_DELETE" FROM 000,000 TO 027,093 OF oMainWnd  
        // GERA O OBJETO DE GRID  
        oGet := MsNewGetDados():New(10, 10, 160, 360, GD_INSERT + GD_DELETE + GD_UPDATE,;  
            .T., .T., Space(0), NIL, NIL, NIL, NIL, NIL, .T., oDlg, aHeader, aCols)  
  
        // DEFINIÇÃO DE BOTÕES  
        @017,072 Button "GDDELETED" SIZE 070,020 ACTION TDelecao(@oGet)  
   
        // DEFINE A LINHA POSICIONADA  
        oGet:nAt := Len(aCols)  
        n := oGet:nAt  
    ACTIVATE MSDIALOG oDlg CENTERED // ATIVA A CAIXA DIÁLOGO  
Return (NIL)  
  
//------------------------------------------------------  
// RETORNA SE UMA LINHA ESTÁ DELETADA OU NÃO  
//------------------------------------------------------  
Static Function TDelecao(oGet)  
   Local lRet := GdDeleted(oGet:nAt)  
  
   // EXIBE MENSAGEM SOBRE O ESTADO DA LINHA  
   MsgInfo("Linha " + AllTrim(Str(oGet:nAt)) + IIf(lRet, " está deletada.", " não está deletada."))  
    
   // ATUALIZA O FOCO  
   oGet:oBrowse:SetFocus()  
Return (NIL)
```

**Observações**  
A função `MsNewGetDados()` foi descontinuada.   
  
**Saiba mais**  
[GDDeleted](https://tdn.totvs.com/display/public/PROT/GDDeleted)  
[MsNewGetDados](https://tdn.totvs.com/display/PROT/MsNewGetDados)
