---
article_id: 360058345433
category: ADVPL - Classe e Função
content_hash: 0074934e1266a6e5891402e1cf9ff183a3684c86847a4f48ced934df0c17f18c
fetched_at: '2026-06-28T22:40:19.560708+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Grid MVC
type: support-article
updated_at: '2023-05-11T17:23:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058345433-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Grid-MVC
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe alguma classe que permite criarmos uma grid com as linhas editáveis e com uma coluna checkBox?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL -a partir da versão 12.1.17  
  
**Solução**Segue abaixo um modelo de exemplo apenas com grid e uma coluna ***checkBox*** em ***MVC***.

```
#Include 'protheus.ch'  
#Include 'fwmvcdef.ch'  
   
#define cNomeArq "zProjetoMvc"  
#define cTab    "SB1"  
   
//-------------------------------------------------------------------  
/*/{Protheus.doc} Eduardo Paro de Simoni  
    Função principal da rotina MVC.   
-------------------------------------------------------------------*/  
Function u_zGridMvc()  
    FWExecView( 'GRID Sem Cabeçalho', "VIEWDEF."+cNomeArq+"", MODEL_OPERATION_INSERT, , { || .T. }, , 30 )  
Return  
  
//-------------------------------------------------------------------  
/*/{Protheus.doc} ModelDef  
//-------------------------------------------------------------------/*/  
Static Function ModelDef()  
    local oModel    as object  
    local oStrCampo as object  
    local oStrGrid  as object  
   
    // Estrutura Fake de Field  
    oStrCampo := FWFormModelStruct():New()  
  
    //Adiciona uma estrutura que represente uma tabela, essa tabela  
    oStrCampo:AddTable( '' , { 'X_ZMVC' } , "Grid_Eduardo" , {|| ''} )   
  
    //Adiciona um campo a estrutura.  
    oStrCampo:AddField( 'X_ZMVC' , 'X_ZMVC' , 'X_ZMVC' , 'C' , 15 )   
  
    //Estrutura de Grid  
    oStrGrid := FWFormStruct( 1, cTab )  
  
    oModel   := MPFormModel():New( 'MIDMAIN' )  
  
    //Atribuindo formulários para o modelo  
    oModel:AddFields('CABEC', , oStrCampo )  
    oModel:AddGrid( 'GRID', 'CABEC', oStrGrid )  
      
    //Setando a chave primária da rotina  
    oModel:SetRelation( 'GRID', { { 'X_ZMVC', 'X_ZMVC' } } )  
      
    //Adicionando descrição ao modelo  
    oModel:SetDescription( "Grid_Eduardo" )  
  
    oModel:SetPrimaryKey( { 'X_ZMVC' } )  
    oStrGrid:AddField('SELECT', ' ', 'SELECT', 'L', 1, 0, , , {}, .F.,FWBuildFeature( STRUCT_FEATURE_INIPAD, ".F."))  
  
    // Necessário que haja alguma alteração na estrutura   
    oModel:SetActivate( { | oModel | FwFldPut( "X_ZMVC", "FAKE" ) } )  
  
Return oModel  
  
//-------------------------------------------------------------------  
/*/{Protheus.doc} ViewDef  
Função estática do ViewDef  
//-------------------------------------------------------------------/*/  
Static Function ViewDef()  
    local oView    as object  
    local oModel   as object  
    local oStrCabec  as object  
    local oStrGrid as object  
      
    // Instancia a Estrutura  
    oStrCabec := FWFormViewStruct():New()  
    oStrCabec:AddField( 'X_ZMVC' , '01' , 'X_ZMVC' , 'X_ZMVC',{},'@!'  )  
      
    // Instancia a Estrutura  
    oStrGrid := FWFormStruct( 2, cTab )  
    oStrGrid:AddField( 'SELECT','01','SELECT','SELECT',, 'Check')  
      
    // Carrega o Modelo  
    oModel  := FWLoadModel( cNomeArq )  
  
    // Instancia a VIEW  
    oView   := FwFormView():New()  
  
    // Seta o Modelo da View  
    oView:SetModel( oModel )  
      
    // Estrutura visual dos campos  
    oView:AddField('CAB', oStrCabec, 'CABEC')  
      
    // Estrutura visual das grids  
    oView:AddGrid('GRID', oStrGrid, 'GRID')  
      
    //Criando um container com nome tela com 100%  
    oView:CreateHorizontalBox( 'CABEC', 0 )  
    oView:CreateHorizontalBox( 'GRID', 100 )  
      
    oView:SetOwnerView('CAB' , 'CABEC' )  
    oView:SetOwnerView('GRID', 'GRID')  
  
    oView:SetDescription( "Grid_Eduardo" )  
      
Return oView
```

**Saiba mais**

[PDF:](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC) [ADVPL UTILIZANDO MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)
