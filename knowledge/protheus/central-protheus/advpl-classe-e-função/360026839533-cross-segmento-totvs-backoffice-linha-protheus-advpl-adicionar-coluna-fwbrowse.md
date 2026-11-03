---
article_id: 360026839533
category: ADVPL - Classe e Função
content_hash: 0fa6ebe996c2452c3e25003e0b116c0e75b76c2f050e63d2536a26f4b5e160e5
fetched_at: '2026-06-28T22:40:14.352111+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Adicionar coluna
  FwBrowse
type: support-article
updated_at: '2024-07-04T15:04:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026839533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Adicionar-coluna-FwBrowse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24653376691863)Tempo aproximado para leitura:**00:03:00 min****Dúvida**Como adicionar uma coluna de status utilizando **FWBrowse**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**É possível criar mais de uma coluna de status através do método **AddStatusColumns**.  
A classe herda da **FwFormBrowse**, que herda da **[FwBrowse](http://tdn.totvs.com/display/PROT/FwBrowse)**. Porém ela é especializada para trabalhar com o dicionário de dados Protheus.  
Qualquer outro uso deverá ser realizado com as classes pai.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041753354)

**Exemplo**

```
#Include 'Protheus.ch'  
#INCLUDE "TOTVS.CH"  
#INCLUDE "FWMVCDEF.CH"  
  
User Function ExFwMBrw()  
Local xRetFun := Nil  
  
Private cCadastro := "Título"  
Private oBrowse := Nil  
  
Private aRotina := {{"P&esquisar" ,'PesqBrw' ,0,1},;  
 { "A&lTerar" ,'AxAltera' ,0,4},;  
 {"V&isualizar" ,'AxVisual' ,0,2} }  
  
// Monta o mBrowse para exibição dos registros  
oBrowse := FWMBrowse():New() // Inicializa o objeto  
//Adiciona a coluna de Status  
oBrowse:AddStatusColumns( { || BrwStatus() }, { || BrwLegend() } )  
oBrowse:SetAlias("SB1") // Indica a tabela utilizada  
oBrowse:SetDescription(cCadastro) // Titulo  
oBrowse:DisableDetails() // Desabilita os detalhes  
oBrowse:SetSeeAll(.T.) // Permite visualizar registros todas filiais  
oBrowse:SetChgAll(.T.) // Permite alterar reg. de outras filiais  
oBrowse:Activate() // Ativa  
  
Return Nil  
  
  
//----------------------------------------------------------  
Static Function ValidMark()  
Local lRet := .F.  
  
//----------------------------------------------------------  
Static Function BrwStatus()  
Return Iif(ValidMark(),"BR_VERDE","BR_VERMELHO")  
  
//----------------------------------------------------------  
Static Function BrwLegend()  
Local oLegend := FWLegend():New()  
  
oLegend:Add("","BR_VERDE" , "VERDE" )   
 oLegend:Add("","BR_VERMELHO", "VERMELHO" )   
 oLegend:Activate()  
 oLegend:View()  
 oLegend:DeActivate()  
  
Return
```
