---
article_id: 360027506172
category: ADVPL - Classe e Função
content_hash: 9abf98711acad9527a7be20c308991818700d103346fcd6238f4fed88b5fa06d
fetched_at: '2026-06-28T22:40:15.661289+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consulta especifica
  com retorno em variável
type: support-article
updated_at: '2024-06-03T12:12:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027506172-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consulta-especifica-com-retorno-em-vari%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23602428860823)Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**Ao executar uma Consulta específica é gerado o erro abaixo:

```
invalid typecast in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-buildv2appsrv-tec11win32rpo32\advtec9_tt11\advpl\instrvar.inl at line 781  
 on FWPOSSHOW(PROTHEUSLOOKUP.PRW)
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Este erro é reproduzido quando a função contida no campo Expressão retorna um valor diferente de lógico.  
  
**Solução**Retornar um valor lógico na função contida no campo Expressão e atribuir o conteúdo desejado em uma variável estática que será resgatada por uma função (contida no mesmo fonte da variável estática).  
  
FonteNo exemplo abaixo atribuímos o valor desejado em MP\_CONPAD e recuperamos o conteúdo utilizando a função T200GET():

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027449911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027449931)

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// VARIÁVEL DE RETORNO  
Static MP_CONPAD As Character  
  
//-------------------------------------------------------  
// CONSULTA PADRÃO COM CAIXA DE MARCAÇÃO (MARKBROWSE)  
//-------------------------------------------------------  
User Function T200CONPAD()  
    Local aArea   As Array   // ÁREA DE TRABALHO CORRENTE  
    Local lFind   As Logical // CONTROLE DE VARIÁVEL ENCONTRADA  
    Local oDialog As Object  // CAIXA DE DIÁLOGO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    lFind   := .F.  
    aArea   := GetArea()  
    oDialog := GenDialog(50)  
  
    // INCORPORA A GRID  
    GenMarkBrw(@oDialog)  
  
    // EXIBE A CAIXA DE DIÁLOGO  
    ACTIVATE MSDIALOG oDialog CENTERED  
  
    // RESTAURA A ÁREA DE TRABALHO ANTERIOR  
    RestArea(aArea)  
  
    // VALIDA SE ALGO FOI SELECIONADO  
    IIf (MP_CONPAD != NIL .And. Len(MP_CONPAD) > 0, lFind := .T., lFind := .F.)  
Return (lFind)  
  
//--------------------------------------------------------  
// EFETUA A MONTAGEM DA CAIXA DE DIÁLOGO DE FUNDO  
//--------------------------------------------------------  
Static Function GenDialog(nPercent As Numeric)  
    Local oSize   As Object // TAMANHO DOS COMPONENTES  
    Local oDialog As Object // CAIXA DE DIÁLOGO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    oSize := FwDefSize():New(.F.)  
  
    // DEFINIÇÃO DA CAIXA DE DIÁLOGO  
    DEFINE MSDIALOG oDialog TITLE "Consulta Padrão - Tipos" FROM 000,000 TO Round(oSize:aWindSize[3] * (nPercent/100), 0), Round(oSize:aWindSize[4] * (nPercent/100), 0) PIXEL  
Return (oDialog)  
  
//--------------------------------------------------------  
// INCORPORA A GRID EM UMA CAIXA DE DIÁLOGO  
//--------------------------------------------------------  
Static Function GenMarkBrw(oDialog As Object)  
    Local oMark   As Object // GRID DE SELEÇÃO  
    Local aFields As Array  // CAMPOS DO NAVEGADOR  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cAlias  := GetNextAlias()  
    aFields := {}  
  
    // MONTA A ESTRUTURA E O CONTEÚDO DOS CAMPOS  
    GenTable(cAlias)  
  
    // CAMPOS DO NAVEGADOR  
    AAdd(aFields, {"Código",    "TRB_COD",  "C", 04, 00})  
    AAdd(aFields, {"Descrição", "TRB_DESC", "C", 30, 00})  
  
    // DEFINIÇÕES DO NAVEGADOR  
    oMark := FwMarkBrowse():New()  
        oMark:SetIgnoreARotina(.T.)  
        oMark:SetMenuDef("T200CONPAD")  
        oMark:SetAlias(cAlias)  
        oMark:SetTemporary(.T.)  
        oMark:SetFields(aFields)  
        oMark:SetFieldMark("TRB_OK")  
        oMark:SetOwner(oDialog)  
        oMark:IsInvert(.T.)  
        oMark:SetDescription("Tipos")  
        oMark:SetOnlyFields({"TRB_OK", "TRB_COD", "TRB_DESC"})  
  
        // BOTÕES DA ROTINA  
        oMark:AddButton("Confirmar", {|| CheckSelected(@oMark)})  
    oMark:Activate()  
Return (NIL)  
  
//--------------------------------------------------------  
// GERA O ARQUIVO DE TRABALHO  
//--------------------------------------------------------  
Static Function GenTable(cAlias As Character)  
    Local oTable  As Object  // OBJETO DA TABELA TEMPORÁRIA  
    Local aFields As Array   // VETOR DE CAMPOS  
    Local aData   As Array   // CONTEÚDO DOS CAMPOS  
    Local nX      As Numeric // CONTROLADOR DE LAÇO  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    nX      := 0  
    aData   := {}  
    aFields := {}  
    oTable  := FwTemporaryTable():New(cAlias)  
  
    // DEFINE A ESTRUTURA DE CAMPOS  
    AAdd(aFields, {"TRB_OK",   "C", 02, 00})  
    AAdd(aFields, {"TRB_COD",  "C", 04, 00})  
    AAdd(aFields, {"TRB_DESC", "C", 30, 00})  
  
    // INSERE OS CAMPOS NA TABELA TEMPORÁRIA  
    oTable:SetFields(aFields)  
  
    // ÍNDICE DA TABELA TEMPORÁRIA  
    oTable:AddIndex("01", {"TRB_COD"})  
  
    // CRIA A TABELA  
    oTable:Create()  
  
    // SELECIONA A ÁREA PARA NÃO PRECISAR APONTAR  
    DbSelectArea(cAlias)  
  
    // DADOS QUE SERÃO INSERIDOS NA TABELA  
    AAdd(aData, {"PC",  "Produto ao Consumidor"})  
    AAdd(aData, {"PI",  "Produto de Origem Industrial"})  
    AAdd(aData, {"BC",  "Bem de Conveniência"})  
    AAdd(aData, {"BI",  "Bem de Impulso"})  
    AAdd(aData, {"BE",  "Bem de Emergência"})  
    AAdd(aData, {"BCC", "Bem de Compra Comprada"})  
  
    // INSERE OS DADOS NA TABELA TEMPORÁRIA  
    For nX := 1 To Len(aData)  
        RecLock(cAlias, .T.)  
            TRB_COD  := aData[nX][1]  
            TRB_DESC := aData[nX][2]  
        MsUnlock()  
    Next nX  
  
    // POSICIONA NO INÍCIO DO ARQUIVO  
    DbGoTop()  
Return (NIL)  
  
//--------------------------------------------------------  
// PREPARA O RETORNO PARA O CAMPO  
//--------------------------------------------------------  
Static Function CheckSelected(oMark As Object)  
    Local cSelected As Character // RETORNO DA CONSULTA  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    cSelected := Space(0)  
  
    // PERCORRE A TABELA CORRENTE E CONCATENA CAMPOS MARCADOS  
    DbGoTop()  
    DbEval({|| IIf(oMark:IsMark(oMark:Mark()), cSelected += "+" + AllTrim(TRB_COD), cSelected += Space(0))})  
  
    // REMOVE O PRIMEIRO CARACTERE E ATRIBUI A VARIÁVEL DE RETORNO  
    MP_CONPAD := IIf(Len(cSelected) > 0, SubStr(cSelected, 2), cSelected)  
  
    // FECHA A CAIXA DE DIÁLOGO  
    oMark:oBrowse:oOwner:End()  
Return (NIL)  
  
//--------------------------------------------------------  
// SOBRESCRIÇÃO DAS OPERAÇÕES DA ROTINA PADRÃO  
//--------------------------------------------------------  
Static Function MenuDef()  
    Local aRotina As Array // OPERAÇÕES DA ROTINA  
  
    // INICIALIZAÇÃO DE VARIÁVEIS  
    aRotina := {}  
Return (aRotina)  
  
//--------------------------------------------------------  
// RETORNA A VARIÁVEL ESTÁTICA PARA O CAMPO  
//--------------------------------------------------------  
User Function T200GET()  
Return (MP_CONPAD)
```
