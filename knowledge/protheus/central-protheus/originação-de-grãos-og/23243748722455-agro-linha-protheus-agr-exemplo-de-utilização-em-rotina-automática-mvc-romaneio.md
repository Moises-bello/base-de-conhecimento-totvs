---
article_id: 23243748722455
category: Originação de Grãos (OG)
content_hash: a2ea46d47d6b53946f8a194ef37c85b5e2920241fd05743e295f8dff68446125
fetched_at: '2026-06-28T22:45:39.468418+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Exemplo de Utilização em Rotina Automática MVC
  - Romaneio OGA250/OGA251
type: support-article
updated_at: '2025-06-24T11:37:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23243748722455-Agro-Linha-Protheus-AGR-Exemplo-de-Utiliza%C3%A7%C3%A3o-em-Rotina-Autom%C3%A1tica-MVC-Romaneio-OGA250-OGA251
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23243748698263) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como procedimento num **Exemplo de Utilização em Rotina Automática MVC - Romaneio OGA250/OGA251**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, siga o seguinte procedimento:

**Exemplo de código - Inclusão Romaneio com Pesagem**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | `User Function zIncRomP()`  `Local lRet := .F.`  `Local oModel := Nil`    `oModel  := FWLoadModel('OGA250')`  `oModel:SetOperation(MODEL_OPERATION_INSERT) //INCLUSÃO`  `oModel:Activate()`    `//### Modelos de dados: NJJUNICO, NJKUNICO, NK4UNICO, NJMUNICO ###`  `//Setando valores nos campos`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_TIPENT', '0') //COM PESAGEM`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_TIPO', '4') //SAIDA POR VENDA`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_CODCTR', '000116') //NUMERO DO CONTRATO`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_TPFORM', '1')`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_LOCAL', '01')`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_TABELA', '000001')`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_PESO1', 1000)`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_PESO2', 2000)`  `oModel:GetModel('NJJUNICO'):SetValue('NJJ_PSSUBT', 1000)`    `//modelo de dados da aba Classificação(Grid)`  `oModel:GetModel('NJKUNICO'):GoLine( 1 ) //posicionando na linha`  `oModel:GetModel('NJKUNICO'):SetValue('NJK_PERDES', 1)`  `oModel:GetModel('NJKUNICO'):GoLine( 2 ) //posicionando na linha`  `oModel:GetModel('NJKUNICO'):SetValue('NJK_PERDES', 0.8)`    `//modelo de dados da aba Comercialização(Grid)`  `oModel:GetModel( "NJMUNICO" ):GoLine( 1 ) //posicionando na linha`  `oModel:GetModel('NJMUNICO'):SetValue('NJM_ITEROM', '01')`    `If oModel:VldData() //valida os dados`  `oModel:CommitData() //realiza a gravação do registro`  `MsgInfo("Registro incluído com sucesso")`  `lRet := .T.`  `Else`  `VarInfo("",oModel:GetErrorMessage())`  `MsgAlert("Erro ao incluir o registro")`  `EndIf`    `return lRet` |
