---
article_id: 360025385671
category: ADVPL - Classe e Função
content_hash: f70a97f53773d3fbaa6e81685e8758d55c412d4752bcfb43712af9ce647ee8ab
fetched_at: '2026-06-28T22:40:18.301633+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - É possível criar
  um formulário MVC com duas entidades sem utilizar grid
type: support-article
updated_at: '2022-03-17T20:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025385671-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-criar-um-formul%C3%A1rio-MVC-com-duas-entidades-sem-utilizar-grid
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:04:00 min  
Dúvida**É possível criar um formulário MVC com duas entidades sem utilizar *grid* (relação 1:1 | duas *enchoices*)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Sim, é possível contudo as duas tabelas envolvidas no formulário devem ter relacionamento de chave primária x chave estrangeira:  
  
Exemplo:   
[PK] B1\_COD (entidade forte) x [FK] B5\_COD (entidade fraca)  
  
Fonte

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function MVCFLD()  
    Local oBrowse := FwLoadBrw("MVCFLD") // NAVEGADOR  
  
    // ATIVAÇÃO DA TELA  
    oBrowse:Activate()  
Return (NIL)  
  
// NAVEGADOR (BROWSER)  
Static Function BrowseDef()  
    Local oBrowse := FwMBrowse():New() // OBJETO DO NAVEGADOR  
  
    // DEFINE A TABELA PRINCIPAL E A DESCRIÇÃO  
    oBrowse:SetAlias("SB1")  
    oBrowse:SetDescription("Cadastro de Produtos Customizado")  
  
    // DEFINE DE QUAL FONTE SERÁ UTILIZADO O MENUDEF  
    oBrowse:SetMenuDef("MVCFLD")  
Return (oBrowse)  
  
// OPERAÇÕES DA ROTINA (AROTINA)  
Static Function MenuDef()  
Return (FwMVCMenu("MVCFLD"))  
  
// REGRA DE NEGÓCIOS (MODEL)  
Static Function ModelDef()  
    // INSTANCIA O MODELO  
    Local oModel := MPFormModel():New("XMVCFLD")  
  
    // INSTANCIA OS SUBMODELOS  
    Local oStruSB1 := FwFormStruct(1, "SB1")  
    Local oStruSB5 := FwFormStruct(1, "SB5")  
  
    // DEFINE O CAMPO B5_COD COMO OBRIGATÓRIO  
    oStruSB5:SetProperty("B5_COD", MODEL_FIELD_OBRIGAT, .F.)  
  
    // DEFINE SE OS SUBMODELOS SERÃO FIELD OU GRID  
    oModel:AddFields("MD_MASTERSB1", NIL, oStruSB1)  
    oModel:AddFields("MD_DETAILSB5", "MD_MASTERSB1", oStruSB5)  
  
    // DEFINE A RELAÇÃO ENTRE OS SUBMODELOS (CSUBMODELO, {ARELATION1, ARELATION2}, CINDEX)  
    oModel:SetRelation("MD_DETAILSB5", {{"B5_FILIAL", "FwXFilial('SB5')"}, {"B5_COD", "B1_COD"}}, SB5->(IndexKey(1)))  
  
    // DEIXA O MODELO SB5 COMO OPCIONAL  
    oModel:GetModel("MD_DETAILSB5"):SetOptional(.T.)  
  
    // DESCRIÇÃO DO MODELO  
    oModel:SetDescription("Cadastro de Produtos Customizado")  
  
    // DESCRIÇÃO DOS SUBMODELOS  
    oModel:GetModel("MD_MASTERSB1"):SetDescription("Dados Brutos do Produto")  
    oModel:GetModel("MD_DETAILSB5"):SetDescription("Dados Científicos do Produto")  
Return (oModel)  
  
// INTERFACE GRÁFICA (VIEW)  
Static Function ViewDef()  
    // INSTANCIA A VIEW  
    Local oView := FwFormView():New()  
  
    // RECEBE O MODELO DE DADOS  
    Local oModel := FwLoadModel("MVCFLD")  
  
    // INSTANCIA AS SUBVIEWS  
    Local oStruSB1 := FwFormStruct(2, "SB1")  
    Local oStruSB5 := FwFormStruct(2, "SB5")  
  
    // REMOVE O CAMPO DA VISÃO  
    oStruSB5:RemoveField("B5_COD")  
  
    // INDICA O MODELO DA VIEW  
    oView:SetModel(oModel)  
  
    // CRIA ESTRUTURA VISUAL DE CAMPOS  
    oView:AddField("VW_MASTERSB1", oStruSB1, "MD_MASTERSB1")  
    oView:AddField("VW_DETAILSB5", oStruSB5, "MD_DETAILSB5")  
  
    // CRIA BOXES HORIZONTAIS  
    oView:CreateHorizontalBox("BOX_SUPERIOR", 70)  
    oView:CreateHorizontalBox("BOX_INFERIOR", 30)  
  
    // RELACIONA OS BOXES COM AS ESTRUTURAS VISUAIS  
    oView:SetOwnerView("VW_MASTERSB1", "BOX_SUPERIOR")  
    oView:SetOwnerView("VW_DETAILSB5", "BOX_INFERIOR")  
  
    oView:EnableTitleView("MD_MASTERSB1", "Dados Brutos do Produto")  
    oView:EnableTitleView("MD_DETAILSB5", "Dados Científicos do Produto")  
Return (oView)
```
