---
article_id: 27606833750423
category: ADVPL - Classe e Função
content_hash: 26636f2f218c66f9347d8aa0e042961fed81d7c094a3987a251005d4b865ecef
fetched_at: '2026-06-28T22:40:21.596781+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível criar
  uma rotina em MVC utilizando TLPP?
type: support-article
updated_at: '2024-11-06T18:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27606833750423-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-criar-uma-rotina-em-MVC-utilizando-TLPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27606861523479) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

É possível criar uma rotina em MVC utilizando TLPP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da 12.1.2410  
  
**Solução**

A partir da release 12.1.2410 é possível criar uma rotina em MVC em TLPP.

Com o TLPP, obrigatoriamente uma namespace precisa ser declarada no fonte e todas essas funções passam a ser function ou user function para customizações.

Como as funções estáticas não serão mais utilizadas, tudo é feito com base no namespace, portanto agora o valor enviado sempre será o namespace completo mais o nome da função principal.

![teste2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/27607090825751)

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'FWMVCDEF.CH'  
#include "tlpp-core.th"  
#include "tlpp-rest.th"  
  
User Function COMP011_MVC()  
Local oBrowse  
  
oBrowse := FWMBrowse():New()  
oBrowse:SetAlias('SA1')  
oBrowse:SetDescription('Clientes')  
oBrowse:Activate()  
  
Return NIL  
  
//-------------------------------------------------------------------  
  
namespace custom.mvc.ttllpp  
   
user function menudef() as array  
local aRotina := {} as array  
  
Add Option aRotina Title "Incluir" Action "ViewDef.custom.mvc.ttllpp.COMP011_MVC" Operation OP_INCLUIR Access 0 //Aqui, a função principal da rotina é a MinhaFuncaoDeMenu e o namespace é custom.meunamespace.minharotina  
  
Return aRotina  
  
//-------------------------------------------------------------------  
user function ModelDef()  
// Cria a estrutura a ser usada no Modelo de Dados  
Local oStruZA0 := FWFormStruct( 1, 'SA1', /*bAvalCampo*/,/*lViewUsado*/ )  
Local oModel  
  
// Cria o objeto do Modelo de Dados  
oModel := MPFormModel():New('COMP011MODEL', /*bPreValidacao*/, /*bPreValidacao*/ , /*bCommit*/, /*bCancel*/ )  
  
// Adiciona ao modelo uma estrutura de formulário de edição por campo  
oModel:AddFields( 'ZA0MASTER', /*cOwner*/, oStruZA0)  
  
// Adiciona a descricao do Modelo de Dados  
oModel:SetDescription( 'Modelo de Dados de Autor/Interprete' )  
  
// Adiciona a descricao do Componente do Modelo de Dados  
oModel:GetModel( 'ZA0MASTER' ):SetDescription( 'Dados de Autor/Interprete' )  
  
oModel:SetPrimaryKey({"A1_FILIAL","A1_COD"})  
  
// Liga a validação da ativacao do Modelo de Dados  
//oModel:SetVldActivate( { |oModel| COMP011ACT( oModel ) } )  
  
Return oModel  
  
//-------------------------------------------------------------------  
user function ViewDef()  
// Cria um objeto de Modelo de Dados baseado no ModelDef do fonte informado  
Local oModel   := FWLoadModel( 'custom.mvc.ttllpp.COMP011_MVC' )  
// Cria a estrutura a ser usada na View  
Local oStruZA0 := FWFormStruct( 2, 'SA1' )  
Local oView  
  
// Cria o objeto de View  
oView := FWFormView():New()  
  
// Define qual o Modelo de dados será utilizado  
oView:SetModel( oModel )  
  
//Adiciona no nosso View um controle do tipo FormFields(antiga enchoice)  
oView:AddField( 'VIEW_ZA0', oStruZA0, 'ZA0MASTER' )  
  
// Criar um "box" horizontal para receber algum elemento da view  
oView:CreateHorizontalBox( 'TELA' , 100 )  
  
// Relaciona o ID da View com o "box" para exibicao  
oView:SetOwnerView( 'VIEW_ZA0', 'TELA' )  
  
Return oView
```

**Saiba mais:**

[TLPP no Protheus](https://tdn.totvs.com/display/public/framework/Suporte+a+TLPP+no+Protheus)
