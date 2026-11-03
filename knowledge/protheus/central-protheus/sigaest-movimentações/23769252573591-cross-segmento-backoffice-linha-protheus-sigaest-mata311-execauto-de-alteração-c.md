---
article_id: 23769252573591
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 3c580fd1cdc3588b8760ddfce0fc4131232d36dfef9f779c8c66ec665a05e8f4
fetched_at: '2026-06-28T22:38:54.247971+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATA311 - ExecAuto
  de alteração com mais de uma linha
type: support-article
updated_at: '2024-05-27T21:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23769252573591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA311-ExecAuto-de-altera%C3%A7%C3%A3o-com-mais-de-uma-linha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23769261281687) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como executar a alteração na rotina MATA311 - Solicitação de Transferência entre Filiais em um registro com mais de uma linha?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Abaixo demonstramos um exemplo de ExecAuto da rotina MATA311 - Solicitação de Transferência entre Filiais, com a alteração de mais de uma linha. 

Atenção: Este é apenas um exemplo, entre em contato com seu analista programador ou com seu Gerente de Atendimento para adaptar à sua necessidade:

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
#INCLUDE "TBICONN.CH"  
  
/*  
Exemplo de alteracao de uma solicitacao de transferência via rotina automatica com mais de uma linha  
*/  
  
User Function m311Alt()  
Local oModel  
Local nX  
Local cCodDoc  
Local nTotLin  
local nLin  
Private cOpId311        := "004" // DECLARACAO PARA O REALIZAR A ALTERACAO DA SOLICITACAO  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01' USER 'admin' PASSWORD '' MODULO "EST"  
  
cCodDoc := "0000000001" // codigo do documento de solicitação de transferência a ser alterado  
  
//Posiciona registro  
dbSelectArea("NNS")  
NNS->(DbSetOrder(1))  
If NNS->(DbSeek(xFilial("NNS") + cCodDoc))  
  
   //carrega o model  
   oModel   := FWLoadModel( "MATA311" )  
  
   //Define operação do modelo  
   oModel:SetOperation( MODEL_OPERATION_UPDATE )  
  
   //Ativaзгo do modelo  
   oModel:Activate()  
  
   //-- Preenchimento dos campos da NNT da 1a linha  
  
   oModel:SetValue( "NNTDETAIL","NNT_QUANT",4)  
   oModelGrid := oModel:GetModel( "NNTDETAIL" )  
  
// Retorna o total de linhas, incluindo as deletadas.*  
nTotLin := oModelGrid:Length( .F. )  
  
For nLin := 1 To nTotLin    
oModelGrid:SetLine(nLin)  
  
If !oModelGrid:IsDeleted( nLin )  
oModelGrid:SetValue("NNT_QUANT", nLin) // Atribui as quantidades por linha     
EndIf   
  
Next  
  
   If oModel:VldData() //Validação do modelo  
      oModel:CommitData() // Gravaзгo do Modelo  
  
   Else  
      aLog := oModel:GetErrorMessage() //Recupera o erro do model quando nao passou no VldData  
      cMensLog := ''  
  
      //laco para gravar em string cLog conteudo do array aLog  
      For nX := 1 to Len(aLog)  
         If !Empty(aLog[nX])  
            cMensLog += Alltrim(aLog[nX]) + CHR(13)+CHR(10)  
         EndIf  
      Next nX  
  
      lMsErroAuto := .T. //seta variavel private como erro  
      AutoGRLog(cMensLog) //grava log para exibir com funcao mostraerro  
      MostraErro()  
  
   EndIf  
  
Else  
   conout("Documento de Solicitação de transferência não encontrado")  
ENDIF  
  
Return NIL
```

***Saiba Mais:***

*[Solicitação de Transferencia de Materiais - MATA311 - Estoque - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=554642567)*

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
