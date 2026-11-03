---
article_id: 360021003872
category: ADVPL - Classe e Função
content_hash: 4ff0dc2ba49beb35adc7b76f1fe323939f28d99dc898ee8c455555bbd72bb1e6
fetched_at: '2026-06-28T22:40:15.596782+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar o
  método AddCalc da classe FwFormModel utilizando a operação de média
type: support-article
updated_at: '2022-01-05T14:40:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021003872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-o-m%C3%A9todo-AddCalc-da-classe-FwFormModel-utilizando-a-opera%C3%A7%C3%A3o-de-m%C3%A9dia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como utilizar o método AddCalc() da classe FwFormModel() utilizando a operação de média ("AVG" ou "AVERAGE")?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.8  
  
**Solução**Utilize a operação "AVERAGE".  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function MVC004()  
    Local oBrowse := FwLoadBrw("MVC004")  
    oBrowse:Activate()  
Return (NIL)  
  
// BROWSER  
Static Function BrowseDef()  
    // INSTANCIAÇÃO DO BROWSER  
    Local oBrowse := FwMBrowse():New()  
  
    // DEFINIÇÃO DE TABELA PRINCIPAL E TÍTULO  
    oBrowse:SetAlias("ZB5")  
    oBrowse:SetDescription("Notas por Turma")  
  
    // DEFINE DE QUAL FONTE SERÁ UTILIZADO O MENUDEF  
    oBrowse:SetMenuDef("MVC004")  
Return (oBrowse)  
  
// OPERAÇÕES  
Static Function MenuDef()  
    Local nX      := 0  
    Local aRotina := {}  
    Local aRotAux := FwMVCMenu("MVC004") // OPERAÇÕES DA ROTINA  
  
    // ADICIONA A OPÇÃO PESQUISA  
    ADD OPTION aRotina TITLE "Pesquisar" ACTION "VIEWDEF.MVC004" OPERATION 1 ACCESS 0  
  
    // ADICIONA AS DEMAIS OPERAÇÕES  
    For nX :=1 To Len(aRotAux)  
        AAdd(aRotina, aRotAux[nX])  
    Next nX  
Return (aRotina)  
  
Static Function ModelDef()  
    // INSTANCIA O MODELO  
    Local oModel := MPFormModel():New("XMVC004")  
  
    // INSTANCIA OS SUBMODELOS  
    Local oStruZB5 := FwFormStruct(1, "ZB5") // TURMA  
    Local oStruZB6 := FwFormStruct(1, "ZB6") // ALUNO  
    Local oStruZB7 := FwFormStruct(1, "ZB7") // DISCIPLINA  
  
    // DEFINE SE OS SUBMODELOS SERÃO FIELD OU GRID  
    oModel:AddFields("MD_MASTERZB5", /*cOwner*/, oStruZB5)  
    oModel:AddGrid("MD_DETAILZB6", "MD_MASTERZB5", oStruZB6)  
    oModel:AddGrid("MD_DETAILZB7", "MD_DETAILZB6", oStruZB7)  
    oModel:AddCalc("MD_DETAILAUX", "MD_DETAILZB6", "MD_DETAILZB7", "ZB7_NOTA", "AUX_AVERAGE", "AVERAGE", {|| .T.}, {|| 0}, "% Materia")  
  
    // DEFINE A RELAÇÃO ENTRE OS SUBMODELOS (CSUBMODELO, {ARELATION1, ARELATION2}, CINDEXFILHO)  
    oModel:SetRelation("MD_DETAILZB6", {{"ZB6_FILIAL", "FwXFilial('ZB6')"}, {"ZB6_CODTUR", "ZB5_CODTUR"}}, ZB6->(IndexKey(1)))  
    oModel:SetRelation("MD_DETAILZB7", {{"ZB7_FILIAL", "FwXFilial('ZB7')"}, {"ZB7_CODTUR", "ZB5_CODTUR"}, {"ZB7_RA", "ZB6_RA"}}, ZB7->(IndexKey(1)))  
  
    // CONTROLE DE NÃO REPETIÇÃO DE DADOS  
    oModel:GetModel("MD_DETAILZB6"):SetUniqueLine({"ZB6_RA"})  
    oModel:GetModel("MD_DETAILZB7"):SetUniqueLine({"ZB7_CODDIS", "ZB7_BIM"})  
  
    // DESCRIÇÃO DO MODELO  
    oModel:SetDescription("Cadastro de Turmas")  
  
    // DESCRIÇÃO DOS SUBMODELOS  
    oModel:GetModel("MD_MASTERZB5"):SetDescription("Dados da Turma")  
    oModel:GetModel("MD_DETAILZB6"):SetDescription("Dados do Aluno")  
    oModel:GetModel("MD_DETAILZB7"):SetDescription("Dados da Disciplina")  
Return (oModel)  
  
// INTERFACE GRÁFICA  
Static Function ViewDef()  
    // INSTANCIA A VIEW  
    Local oView := FwFormView():New()  
  
    // RECEBE O MODELO DE DADOS  
    Local oModel := FwLoadModel("MVC004")  
  
    // INSTANCIA AS SUBVIEWS  
    Local oStruZB5 := FwFormStruct(2, "ZB5")  
    Local oStruZB6 := FwFormStruct(2, "ZB6")  
    Local oStruZB7 := FwFormStruct(2, "ZB7")  
    Local oStruAUX := FwCalcStruct(oModel:GetModel("MD_DETAILAUX"))  
  
    // INDICA O MODELO DA VIEW  
    oView:SetModel(oModel)  
  
    // REMOVE CAMPOS  
    oStruZB6:RemoveField("ZB6_CODTUR")  
    oStruZB7:RemoveField("ZB7_CODTUR")  
    oStruZB7:RemoveField("ZB7_RA")  
  
    // CRIA ESTRUTURA VISUAL DE CAMPOS  
    oView:AddField("VW_MASTERZB5", oStruZB5, "MD_MASTERZB5")  
    oView:AddGrid("VW_DETAILZB6", oStruZB6, "MD_DETAILZB6")  
    oView:AddGrid("VW_DETAILZB7", oStruZB7, "MD_DETAILZB7")  
    oView:AddField("VW_DETAILAUX", oStruAUX, "MD_DETAILAUX")  
  
    // CRIA BOXES  
    oView:CreateHorizontalBox("BOX_SUPERIOR", 10)  
    oView:CreateHorizontalBox("BOX_INFERIOR", 80)  
    oView:CreateHorizontalBox("BOX_AUXILIAR", 10)  
    oView:CreateVerticalBox("BOX_INFERIOR_ESQUERDO", 50, "BOX_INFERIOR")  
    oView:CreateVerticalBox("BOX_INFERIOR_DIREITO", 50, "BOX_INFERIOR")  
  
    // RELACIONA OS BOXES COM AS ESTRUTURAS VISUAIS  
    oView:SetOwnerView("VW_MASTERZB5", "BOX_SUPERIOR")  
    oView:SetOwnerView("VW_DETAILZB6", "BOX_INFERIOR_ESQUERDO")  
    oView:SetOwnerView("VW_DETAILZB7", "BOX_INFERIOR_DIREITO")  
    oView:SetOwnerView("VW_DETAILAUX", "BOX_AUXILIAR")  
  
    // DEFINE OS TÍTULOS DAS SUBVIEWS  
    oView:EnableTitleView("VW_DETAILZB6", "Alunos")  
    oView:EnableTitleView("VW_DETAILZB7", "Disciplinas")  
Return (oView)
```
