---
article_id: 360000146128
category: ADVPL - Ponto de Entrada
content_hash: a17f9937461d582b4da83659542ef1f2bde53c0df5fa80ab8847adbfd8013b1f
fetched_at: '2026-06-28T22:40:11.616357+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL -  Ponto de entrada
  MVC CRMA980
type: support-article
updated_at: '2026-06-15T12:30:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000146128-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-CRMA980
---

**Dúvida**Ponto de entrada MVC CRMA980  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Para utilizar os pontos de entrada da rotina MATA030 no padrão MVC, altere para .T. o **parâmetro MV\_MVCSA1**.  
O ID do modelo da dados da rotina MATA030 é CRMA980, assim sendo, a assinatura da função de usuário deve ser; **Exemplo**: User Function **MYCRMA980()**.  
**Obs.: O nome do arquivo.prw e user function, não poderá ser o mesmo do fonte padrão CRMA980, pois o MVC não faz a tratativa igual o ADVPL sobre o nome da função.**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Incidente There is a source name conflict ao utilizar Ponto de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7406000650391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Incidente-There-is-a-source-name-conflict-ao-utilizar-Ponto-de-Entrada)**

**Exemplo**

|  |
| --- |
| ``` #include "Protheus.ch" #include "FWMVCDEF.CH"  Static __LogTela    := NIL  //-------------------------------------------------------------------  /*/{Protheus.doc} MyCRMA980  Ponto de Entrada do Cadastro de Clientes (MVC) @param      Nao ha @return     Varios. DependerÃ¡ de qual PE esta sendo executado. @author     Faturamento @version    12.1.17 / Superior @since      Mai/2021 /*/  //-------------------------------------------------------------------  User Function MYCRMA980() ///cXXX1,cXXX2,cXXX3,cXXX4,cXXX5,cXXX6     Local aParam        := PARAMIXB     Local xRet          := .T.     Local lIsGrid       := .F. //  Local nLinha        := 0 //  Local nQtdLinhas    := 0 //  Local cRotMVC       := "CRMA980"     Local cIDPonto      := ''     Local cIDModel      := '' //  Local cIDForm       := '' //  Local cEvento       := '' //  Local cCampo        := '' //  Local cConteudo     := '' //  Local cMsg          := ''     Local oObj          := NIL      If __LogTela == NIL         __LogTela   := ApMsgYesNo("A geracao do 'LOG de processamento' dos PE 'CRMA980' (MVC) sera exibido em TELA?" + CRLF + CRLF +;             'SIM = TELA' + CRLF +;             'NAO = CONSOLE do AppServer')     EndIf      If aParam <> NIL         oObj        := aParam[1]         cIDPonto    := aParam[2]         cIDModel    := aParam[3]         lIsGrid     := (Len(aParam) > 3)         nOperation := oObj:GetOperation()          If cIDPonto == 'MODELCOMMITTTS'             // Mostra o tipo de Operacao             //MsgAlert("Operacao " + CValToChar(nOperation), "Tipo de operacao MODELCOMMITTTS")             // Inclusao              If nOperation == 3                 MsgAlert("Entrou no PE - Operacao de Inclusao", "Tipo de operacao 3 MODELCOMMITTTS")             EndIf              // Alteracao             If nOperation == 4                 MsgAlert("Entrou no PE - Operacao de Alteracao", "Tipo de operacao 4 MODELCOMMITTTS")             EndIf              // Exclusao             If nOperation == 5                 MsgAlert("Entrou no PE - Operacao de Exclusao", "Tipo de operacao 5 MODELCOMMITTTS")             EndIf         EndIf     EndIf Return xRet ``` |

**Saiba mais**Todos os pontos de entrada terão seu legado mantido, salvo os pontos que consideramos como pontos padrões (ex: validação após a gravação e botões que serão substituídos), os pontos que trazem conteúdo do sistema por PARAMIXB, esses serão mantidos com suas particularidades.

* [DT Novo Fonte de Cadastro de Clientes em MVC](http://tdn.totvs.com/display/PROT/DT+Novo+Fonte+de+Cadastro+de+Clientes+em+MVC) (informações mais detalhadas dos pontos)
* [Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/viewpage.action?pageId=208345968) (documentação referente ao desenvolvimento de pontos MVC)
* [Acessar Acols rotina MVC](http://tdn.totvs.com/display/public/PROT/ADV0007_FUN_ACOLS_MVC) (aCols por modelo de dados)
* [Fontes em MVC](http://tdn.totvs.com/display/public/PROT/Fontes+em+MVC) (lista de rotinas que migraram para o MVC)
