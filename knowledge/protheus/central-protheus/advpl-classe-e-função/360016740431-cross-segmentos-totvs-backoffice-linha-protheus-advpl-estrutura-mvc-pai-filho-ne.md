---
article_id: 360016740431
category: ADVPL - Classe e Função
content_hash: b641a866bd1a10b728e89172234ca2c8badec3d491fea7040654465f0d21a9fb
fetched_at: '2026-06-28T22:40:19.283802+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Estrutura MVC:
  Pai + Filho + Neto'
type: support-article
updated_at: '2022-01-10T15:28:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016740431-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Estrutura-MVC-Pai-Filho-Neto
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como criar uma rotina no modelo "pai x filho x neto" com base na arquitetura ADVPL em MVC?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Segue abaixo três exemplo de código ADVPL em MVC demostrando os tipos de relacionamento (pai, pai + filho e pai + filho + neto).

**Exemplo relacionamento PAI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012759791/mceclip0.png)

```
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function COMP011_MVC()  
    Local oBrowse := FwLoadBrw("COMP011_MVC")  
  
    oBrowse:Activate()  
Return (NIL)  
  
// BROWSEDEF() SERÁ ÚTIL PARA FUTURAS HERANÇAS: FWLOADBRW()  
Static Function BrowseDef()  
    Local oBrowse := FwMBrowse():New()  
  
    oBrowse:SetAlias("ZA0")  
    oBrowse:SetDescription("Cadastro de Autor/Interprete")  
  
    oBrowse:AddLegend("ZA0_TIPO=='1'", "YELLOW", "Autor")  
    oBrowse:AddLegend("ZA0_TIPO=='2'", "BLUE" , "Interprete")  
  
   // DEFINE DE ONDE SERÁ RETIRADO O MENUDEF  
   oBrowse:SetMenuDef("COMP011_MVC")  
Return (oBrowse)  
  
// OPERAÇÕES DA ROTINA  
Static Function MenuDef()  
    // FUNÇÃO PARA CRIAR MENUDEF  
    Local aRotina := FWMVCMenu("COMP011_MVC")  
Return (aRotina)  
  
// REGRAS DE NEGÓCIO  
Static Function ModelDef()  
    // INSTANCIA O MODELO  
    Local oModel := MPFormModel():New("COMP011M")  
  
    // INSTANCIA O SUBMODELO  
    Local oStruZA0 := FwFormStruct(1, "ZA0")  
  
    // DEFINE O SUBMODELO COMO FIELD  
    oModel:AddFields("ZA0MASTER", NIL, oStruZA0)  
  
    // DESCRIÇÃO DO MODELO  
    oModel:SetDescription("Modelo de Dados de Autor/Interprete")  
  
    // DESCRIÇÃO DO SUBMODELO  
    oModel:GetModel("ZA0MASTER"):SetDescription("Dados de Autor/Interprete")  
Return (oModel)  
  
// INTERFACE GRÁFICA  
Static Function ViewDef()  
    // INSTANCIA A VIEW  
    Local oView := FwFormView():New()  
  
    // INSTANCIA AS SUBVIEWS  
    Local oStruZA0 := FwFormStruct(2, "ZA0")  
  
    // RECEBE O MODELO DE DADOS  
    Local oModel := FwLoadModel("COMP011_MVC")  
  
    // INDICA O MODELO DA VIEW  
    oView:SetModel(oModel)  
  
    // CRIA ESTRUTURA VISUAL DE CAMPOS  
    oView:AddField("VIEW_ZA0", oStruZA0, "ZA0MASTER")  
  
    // CRIA BOX HORIZONTAL  
    oView:CreateHorizontalBox("TELA" , 100)  
  
    // RELACIONA OS BOX COM A ESTRUTURA VISUAL  
    oView:SetOwnerView("VIEW_ZA0", "TELA")  
Return (oView)
```

**Exemplo relacionamento PAI + FILHO  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012760011/mceclip1.png)**

```
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function COMP021_MVC()  
    Local oBrowse := FwLoadBrw("COMP021_MVC")  
  
    oBrowse:Activate()  
Return (NIL)  
  
// BROWSEDEF() SERÁ ÚTIL PARA FUTURAS HERANÇAS: FWLOADBRW()  
Static Function BrowseDef()  
    Local oBrowse := FwMBrowse():New()  
  
    oBrowse:SetAlias("ZA1")  
    oBrowse:SetDescription("Musicas")  
  
   // DEFINE DE ONDE SERÁ RETIRADO O MENUDEF  
   oBrowse:SetMenuDef("COMP021_MVC")  
Return (oBrowse)  
  
// OPERAÇÕES DA ROTINA  
Static Function MenuDef()  
    // FUNÇÃO PARA CRIAR MENUDEF  
    Local aRotina := FwMVCMenu("COMP021_MVC")  
Return (aRotina)  
  
// REGRAS DE NEGÓCIO  
Static Function ModelD+ef()  
    // INSTANCIA O MODELO  
    Local oModel := MPFormModel():New("COMP021M")  
  
    // INSTANCIA OS SUBMODELOS  
    Local oStruZA1 := FwFormStruct(1, "ZA1")  
    Local oStruZA2 := FwFormStruct(1, "ZA2")  
  
    // DEFINE SE OS SUBMODELOS SERÃO FIELD OU GRID  
    oModel:AddFields("ZA1MASTER", NIL, oStruZA1)  
    oModel:AddGrid("ZA2DETAIL", "ZA1MASTER", oStruZA2)  
  
    // DEFINE A RELAÇÃO ENTRE OS SUBMODELOS  
    oModel:SetRelation("ZA2DETAIL", {{"ZA2_FILIAL", "FwXFilial('ZA2')"}, {"ZA2_MUSICA", "ZA1_MUSICA"}}, ZA2->(IndexKey( 1 )))  
  
    // DESCRIÇÃO DO MODELO  
    oModel:SetDescription("Modelo de Musicas" )  
  
    // DESCRIÇÃO DOS SUBMODELOS  
    oModel:GetModel("ZA1MASTER"):SetDescription("Dados da Musica")  
    oModel:GetModel("ZA2DETAIL"):SetDescription("Dados do Autor da Musica")  
Return (oModel)  
  
// INTERFACE GRÁFICA  
Static Function ViewDef()  
    // INSTANCIA A VIEW  
    Local oView := FwFormView():New()  
  
    // INSTANCIA AS SUBVIEWS  
    Local oStruZA1 := FwFormStruct(2, "ZA1")  
    Local oStruZA2 := FwFormStruct(2, "ZA2")  
  
    // RECEBE O MODELO DE DADOS  
    Local oModel := FwLoadModel("COMP021_MVC")  
  
    // INDICA O MODELO DA VIEW  
    oView:SetModel(oModel)  
  
    // CRIA ESTRUTURA VISUAL DE CAMPOS  
    oView:AddField("VIEW_ZA1", oStruZA1, "ZA1MASTER")  
    oView:AddGrid("VIEW_ZA2", oStruZA2, "ZA2DETAIL")  
  
    // CRIA BOXES HORIZONTAIS  
    oView:CreateHorizontalBox("SUPERIOR", 30)  
    oView:CreateHorizontalBox("INFERIOR", 70)  
  
    // RELACIONA OS BOXES COM AS ESTRUTURAS VISUAIS  
    oView:SetOwnerView("VIEW_ZA1", "SUPERIOR")  
    oView:SetOwnerView("VIEW_ZA2", "INFERIOR")  
  
    // DEFINE AUTO-INCREMENTO AO CAMPO  
    oView:AddIncrementField("VIEW_ZA2", "ZA2_ITEM")  
  
    // DEFINE OS TÍTULOS DAS SUBVIEWS  
    oView:EnableTitleView("VIEW_ZA2","MUSICAS")  
Return (oView)
```

**Exemplo relacionamento PAI + FILHO + NETO**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012760951/mceclip2.png)

```
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function COMP023_MVC()  
    Local oBrowse := FwLoadBrw("COMP023_MVC")  
  
    oBrowse:Activate()  
Return (NIL)  
  
// BROWSEDEF() SERÁ ÚTIL PARA FUTURAS HERANÇAS: FWLOADBRW()  
Static Function BrowseDef()  
    Local oBrowse := FwMBrowse():New()  
  
    oBrowse:SetAlias("ZA3")  
    oBrowse:SetDescription("Albuns")  
  
   // DEFINE DE ONDE SERÁ RETIRADO O MENUDEF  
   oBrowse:SetMenuDef("COMP023_MVC")  
Return (oBrowse)  
  
// OPERAÇÕES DA ROTINA  
Static Function MenuDef()  
    // FUNÇÃO PARA CRIAR MENUDEF  
    Local aRotina := FWMVCMenu("COMP023_MVC")  
Return (aRotina)  
  
// REGRAS DE NEGÓCIO  
Static Function ModelDef()  
    // INSTANCIA O MODELO  
    Local oModel := MPFormModel():New("COMP023M")  
  
    // INSTANCIA OS SUBMODELOS  
    Local oStruZA3 := FwFormStruct(1, "ZA3")  
    Local oStruZA4 := FwFormStruct(1, "ZA4")  
    Local oStruZA5 := FwFormStruct(1, "ZA5")  
  
    // DEFINE SE OS SUBMODELOS SERÃO FIELD OU GRID  
    oModel:AddFields("ZA3MASTER", NIL, oStruZA3)  
    oModel:AddGrid("ZA4DETAIL", "ZA3MASTER", oStruZA4)  
    oModel:AddGrid("ZA5DETAIL", "ZA4DETAIL", oStruZA5)  
  
    // DEFINE A RELAÇÃO ENTRE OS SUBMODELOS  
    oModel:SetRelation("ZA4DETAIL", {{"ZA4_FILIAL", "FwXFilial('ZA4')"}, {"ZA4_ALBUM", "ZA3_ALBUM"}}, ZA4->(IndexKey(1)))  
    oModel:SetRelation("ZA5DETAIL", {{"ZA5_FILIAL", "FwXFilial('ZA5')"}, {"ZA5_ALBUM", "ZA3_ALBUM"}, {"ZA5_MUSICA", "ZA4_MUSICA"}}, ZA5->(IndexKey(1)))  
  
    // DESCRIÇÃO DO MODELO  
    oModel:SetDescription("Modelo de Albuns")  
  
    // DESCRIÇÃO DOS SUBMODELOS  
    oModel:GetModel("ZA3MASTER"):SetDescription("Dados do Album")  
    oModel:GetModel("ZA4DETAIL"):SetDescription("Dados das Musicas do Album")  
    oModel:GetModel("ZA5DETAIL"):SetDescription("Interpretes das Musicas do Album")  
Return (oModel)  
  
// INTERFACE GRÁFICA  
Static Function ViewDef()  
    // INSTANCIA A VIEW  
    Local oView := FwFormView():New()  
  
    // INSTANCIA AS SUBVIEWS  
    Local oStruZA3 := FwFormStruct(2, "ZA3")  
    Local oStruZA4 := FwFormStruct(2, "ZA4")  
    Local oStruZA5 := FwFormStruct(2, "ZA5")  
  
    // RECEBE O MODELO DE DADOS  
    Local oModel := FwLoadModel("COMP023_MVC")  
  
    // REMOVE CAMPOS DA EXIBIÇÃO  
    oStruZA4:RemoveField("ZA4_ALBUM")  
    oStruZA5:RemoveField("ZA5_ALBUM")  
    oStruZA5:RemoveField("ZA5_MUSICA")  
  
    // INDICA O MODELO DA VIEW  
    oView:SetModel(oModel)  
  
    // CRIA ESTRUTURA VISUAL DE CAMPOS  
    oView:AddField("VIEW_ZA3", oStruZA3, "ZA3MASTER")  
  
    // CRIA A ESTRUTURA VISUAL DAS GRIDS  
    oView:AddGrid("VIEW_ZA4", oStruZA4, "ZA4DETAIL")  
    oView:AddGrid("VIEW_ZA5", oStruZA5, "ZA5DETAIL")  
  
    // CRIA BOXES HORIZONTAIS  
    oView:CreateHorizontalBox("EMCIMA", 20)  
    oView:CreateHorizontalBox("MEIO", 40)  
    oView:CreateHorizontalBox("EMBAIXO", 40)  
  
    // RELACIONA OS BOXES COM AS ESTRUTURAS VISUAIS  
    oView:SetOwnerView("VIEW_ZA3", "EMCIMA")  
    oView:SetOwnerView("VIEW_ZA4", "MEIO")  
    oView:SetOwnerView("VIEW_ZA5", "EMBAIXO")  
  
    // DEFINE OS TÍTULOS DAS SUBVIEWS  
    oView:EnableTitleView("VIEW_ZA3")  
    oView:EnableTitleView("VIEW_ZA4", "MÚSICAS DO ÁLBUM", RGB(224, 30, 43))  
    oView:EnableTitleView("VIEW_ZA5", "INTERPRETES DAS MÚSICAS", 0)  
Return (oView)
```

  
**Saiba mais**[PDF:](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC) [ADVPL UTILIZANDO](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC) [MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)
