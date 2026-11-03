---
article_id: 13969047906583
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 525758e5cc0d3bd6b637331a64efa15a854841a3eb29994b55ee64e5689e88c4
fetched_at: '2026-06-28T22:39:09.593509+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA019 - Indicador
  de Produtos - Exemplo de Rotina Automática MATA019
type: support-article
updated_at: '2023-04-18T21:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13969047906583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA019-Indicador-de-Produtos-Exemplo-de-Rotina-Autom%C3%A1tica-MATA019
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:31 min** **Dúvida**Possui exemplo para rotina automática da rotina MATA019 em MVC?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões  
  
**Solução**

Deve ser avaliada se a rotina pretendida esta preparada para execução automática, caso sim, o modelo de construção é o mesmo para todas a rotinas, exemplo a rotina **MATA019** (Indicadores de Produtos), desta forma basta seguir o exemplo documentado.

Importante: Por se tratar de um exemplo deve-se realizar o ajuste de acordo com a demanda/necessidade da empresa.

Exemplo:

```
/*------------------------------------------------------------------------  
  
EXEMPLO DE INCLUSÃO NA TABELA SBZ UTILIZANDO MVC  
  
------------------------------------------------------------------------*/  
  
#INCLUDE "RWMAKE.CH"  
  
#INCLUDE "TBICONN.CH"  
  
#INCLUDE 'Protheus.ch'  
  
#INCLUDE 'FWMVCDef.ch'  
  
  
User Function m019Inc1Ra()  
  
    Local oModel As Object  
  
    Local nCont := 1   
  
    Local nRec := 2  
  
    Local cLocalPad := ''  
  
    RPCSetEnv("99", "01",/*cUser*/, /*cPass*/, "EST", "MATA019", {"SB1", "SBZ"})  
  
    CONOUT("Iniciar execução rotina Automatica MVC - MATA019")  
  
//O registro deve estar posicionado   
  
    DBSelectArea("SB1")  
  
    DBSetorder(1)  
  
    dbGotop()  
  
    while !EOF() .AND. xFilial("SB1") == SB1->B1_FILIAL .AND. SB1->B1_COD <= "CANETA"  
  
    cLocalPad := SB1->B1_LOCPAD          
   
  
        oModel := FwLoadModel ("MATA019")  
  
        oModel:SetOperation(MODEL_OPERATION_UPDATE)  
  
        oModel:Activate()  
  
        oModel:LoadValue("SBZDETAIL", "BZ_FILIAL", "01")  
  
        oModel:LoadValue("SBZDETAIL", "BZ_LOCPAD", cLocalPad)  
  
        If (oModel:VldData())  
  
            oModel:CommitData()  
  
            CONOUT("Inclusao Numero" + cValToChar(nCont) + "")  
  
            nCont := nCont++  
  
        Else  
  
            aErro := oModel:GetErrorMessage()  
  
            AutoGrLog( "Id do formulário de origem:" + ' [' + AllToChar( aErro[1] ) +']' )  
  
            AutoGrLog( "Id do campo de origem: " + ' [' + AllToChar( aErro[2] ) +']' )  
  
            AutoGrLog( "Id do formulário de erro: " + ' [' + AllToChar( aErro[3] ) +']' )  
  
            AutoGrLog( "Id do campo de erro: " + ' [' + AllToChar( aErro[4] ) +']' )  
  
            AutoGrLog( "Id do erro: " + ' [' + AllToChar( aErro[5] ) + ']' )  
  
            AutoGrLog( "Mensagem do erro: " + ' [' + AllToChar( aErro[6] ) +']' )  
  
            AutoGrLog( "Mensagem da solução: " + ' [' + AllToChar( aErro[7] ) +']' )  
  
            AutoGrLog( "Valor atribuído: " + ' [' + AllToChar( aErro[8] ) +']' )  
  
            AutoGrLog( "Valor anterior: " + ' [' + AllToChar( aErro[9] ) +']' )  
  
            MostraErro()  
  
            EndIf  
  
            nRec := nRec++  
  
            oModel:Destroy()  
  
            oModel:DeActivate()  
  
              
  
            SB1->(dbSkip())  
  
            ENDDO  
  
        RPCClearEnv()  
  
RETURN
```

Abaixo documentação do exemplo utilizado:  
[https://tdn.totvs.com/pages/viewpage.action?pageId=358453385](https://tdn.totvs.com/pages/releaseview.action?pageId=6814842)

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA019 - Indicador de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021908151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA019-Indicador-de-Produtos)*
