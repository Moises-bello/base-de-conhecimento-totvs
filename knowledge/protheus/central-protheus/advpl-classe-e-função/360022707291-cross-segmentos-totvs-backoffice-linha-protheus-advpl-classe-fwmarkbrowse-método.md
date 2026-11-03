---
article_id: 360022707291
category: ADVPL - Classe e Função
content_hash: 0a9837f25d1f59c017deefbfab972d330ded702ca9719202cf7e0ab04ab3a559
fetched_at: '2026-06-28T22:40:19.378155+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWMarkBrowse
  método SetSemaphore
type: support-article
updated_at: '2022-01-11T14:23:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022707291-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMarkBrowse-m%C3%A9todo-SetSemaphore
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como utilizar o método **FWMarkBrowse**():**SetSemaphore**()?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Ativação do método ativa o controle do semáforo (LockByName) o que impede que 2 usuários marquem o mesmo registro:

![KCS_SEMAPHORE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019853971/KCS_SEMAPHORE.gif)

**Exemplo**

```
#INCLUDE 'totvs.ch'  
#INCLUDE 'FWMVCDEF.CH'  
  
//-------------------------------------------------------------------  
/*/{Protheus.doc} COMP025_MVC  
Exemplo de montagem da modelo e interface de marcacao para uma  
tabela em MVC  
@author Ernani Forastieri e Rodrigo Antonio Godinho  
@since 05/10/2009  
@version P10  
/*/  
//-------------------------------------------------------------------  
User Function COMP025_MVC()  
  
Private oMark  
Private aRotina := MenuDef()  
  
oMark := FWMarkBrowse():New()  
oMark:SetAlias('ZA0')  
oMark:SetSemaphore(.T.)  
oMark:SetDescription('Seleção do Cadastro de Autor/Interprete')  
oMark:SetFieldMark( 'ZA0_OK' )  
oMark:SetAllMark( { || oMark:AllMark() } )  
oMark:AddLegend( "ZA0_TIPO=='1'", "YELLOW", "Autor" )  
oMark:AddLegend( "ZA0_TIPO=='2'", "BLUE" , "Interprete" )  
oMark:Activate()  
  
Return NIL  
  
//-------------------------------------------------------------------  
Static Function MenuDef()  
  
Local aRotina := {}  
  
ADD OPTION aRotina TITLE 'Visualizar' ACTION 'VIEWDEF.COMP025_MVC' OPERATION 2 ACCESS 0  
ADD OPTION aRotina TITLE 'Processar' ACTION 'U_COMP25PROC()' OPERATION 2 ACCESS 0  
  
Return aRotina  
  
//-------------------------------------------------------------------  
Static Function ModelDef()  
  
// Utilizo um model que ja existe  
  
Return FWLoadModel( 'COMP011_MVC' )  
  
//-------------------------------------------------------------------  
Static Function ViewDef()  
  
// Utilizo uma View que ja existe  
Return FWLoadView( 'COMP011_MVC' )  
  
//-------------------------------------------------------------------  
User Function COMP25PROC()  
  
Local aArea := GetArea()  
Local cMarca := oMark:Mark()  
Local lInverte := oMark:IsInvert()  
  
Local nCt := 0  
  
ZA0->( dbGoTop() )  
While !ZA0->( EOF() )  
    If oMark:IsMark(cMarca)  
        nCt++  
    EndIf  
    ZA0->( dbSkip() )  
End  
  
ApMsgInfo( 'Foram marcados ' + AllTrim( Str( nCt ) ) + ' registros.' )  
RestArea( aArea )  
  
Return NIL
```

 **Saiba mais**[FWMarkBrowse](http://tdn.totvs.com/display/public/PROT/FWMarkBrowse)
