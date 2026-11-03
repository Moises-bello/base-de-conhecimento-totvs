---
article_id: 8083792151575
category: ADVPL - Classe e Função
content_hash: 06d4d700ca9148243a09b28808304ec3f049e23aee022c62e2e5de28b82b422b
fetched_at: '2026-06-28T22:40:16.731147+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - FilBrowse permite
  a utilização de filtros na MBrowse
type: support-article
updated_at: '2022-10-04T12:30:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8083792151575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-FilBrowse-permite-a-utiliza%C3%A7%C3%A3o-de-filtros-na-MBrowse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**FilBrowse permite a utilização de filtros na MBrowse?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL –  Todas as versões  
  
**Solução**A **FilBrowse**() é uma funcionalidade que permite a utilização de filtros na função **MBrowse**().  
**Sintaxe:** FilBrowse(cAlias, aQuery, cFiltro, lShowProc)  
  
**Parâmetros:**

|  |  |
| --- | --- |
| cAlias | Alias ativo definido para a Mbrowse() |
| aQuery | Este parâmetro deverá ser inicializado sempre vazio e sua passagem obrigatoriamente por referência, pois, seu retorno será enviado para a função EndFilBrw(). [1]=>Nome do Arquivo Físico [2]=>Ordem correspondente ao Sindex |
| cFiltro | Condição de filtro para a MBrowse() |
| lShowProc | Habilita (.T.) ou desabilita (.F.) a apresentação da mensagem “Selecionando registros ...”, no processamento. |

**PoC AdvPL**Mbrowse() utilizando as funções acessórias

```
#Include "Protheus.ch"  
  
User Function MBrwSA2()  
    Local cAlias := "SA2"  
    Local aCores := {}  
    Local cFiltra := "A2_FILIAL == '"+xFilial('SA2')+"' .And. A2_EST == 'SP'"  
    Private cCadastro := "Cadastro de Fornecedores"  
    Private aRotina := {}  
    Private aIndexSA2 := {}  
    Private bFiltraBrw:= { || FilBrowse(cAlias,@aIndexSA2,@cFiltra) }  
    AADD(aRotina,{"Pesquisar" ,"PesqBrw" ,0,1})  
    AADD(aRotina,{"Visualizar" ,"AxVisual" ,0,2})  
    AADD(aRotina,{"Incluir" ,"U_BInclui" ,0,3})  
/*  
-- CORES DISPONIVEIS PARA LEGENDA --  
BR_AMARELO  
BR_AZUL  
BR_BRANCO  
BR_CINZA  
BR_LARANJA  
BR_MARRON  
BR_VERDE  
BR_VERMELHO  
BR_PINK  
BR_PRETO  
*/  
    AADD(aCores,{"A2_TIPO == 'F'" ,"BR_VERDE" })  
    AADD(aCores,{"A2_TIPO == 'J'" ,"BR_AMARELO" })  
    AADD(aCores,{"A2_TIPO == 'X'" ,"BR_LARANJA" })  
    AADD(aCores,{"A2_TIPO == 'R'" ,"BR_MARRON" })  
    AADD(aCores,{"Empty(A2_TIPO)" ,"BR_PRETO" })  
    dbSelectArea(cAlias)  
    dbSetOrder(1)  
//+------------------------------------------------------------  
//| Cria o filtro na MBrowse utilizando a função FilBrowse  
//+------------------------------------------------------------  
    Eval(bFiltraBrw)  
    dbSelectArea(cAlias)  
    dbGoTop()  
    mBrowse(6,1,22,75,cAlias,,,,,,aCores)  
//+------------------------------------------------  
//| Deleta o filtro utilizado na função FilBrowse  
//+------------------------------------------------  
    EndFilBrw(cAlias,aIndexSA2)  
Return Nil  
//+---------------------------------------  
//|Função: BInclui - Rotina de Inclusão  
//+---------------------------------------  
User Function BInclui(cAlias,nReg,nOpc)  
    Local nOpcao := 0  
    nOpcao := AxInclui(cAlias,nReg,nOpc)  
    If nOpcao == 1  
        MsgInfo("Inclusão efetuada com sucesso!")  
    Else  
        MsgInfo("Inclusão cancelada!")  
    Endif  
Return Nil
```

**Saiba mais**  
[**MBrowse**](https://tdn.totvs.com/pages/releaseview.action?pageId=24346981)
