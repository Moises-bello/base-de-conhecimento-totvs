---
article_id: 25829282922903
category: Originação de Grãos (OG)
content_hash: 8ca9905aa97221b47dfc105eb8f3e6cf79f61daebbeb1d31be3ef1123770d380
fetched_at: '2026-06-28T22:45:44.881035+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem
  - Exclusão da Rotina
type: support-article
updated_at: '2025-06-21T15:39:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25829282922903-Agro-Linha-Protheus-AGR-Rotina-Autom%C3%A1tica-MVC-Servi%C3%A7o-de-armazenagem-Exclus%C3%A3o-da-Rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25829282898327) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Como efetuar a exclusão da **Rotina Automática MVC Serviço de armazenagem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

* [Exclusão](https://tdn.totvs.com/pages/releaseview.action?pageId=861559739#tabs-passo3)

**Exemplo de código - Exclusão do registro**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26 | `User Function zDMVC261()`  `Local lRet := .F.`  `Local oModel := Nil`  `//Exemplo de exclusão`  `dbSelectArea("NKG")`  `NKG->(DbSetOrder(1))`  `If NKG->(DbSeek(xFilial("NKG") + '000178' + '00000003'))`    `oModel  := FWLoadModel('OGA261')`  `oModel:SetOperation(MODEL_OPERATION_DELETE) //EXCLUSÃO`  `oModel:Activate()`    `If oModel:VldData() //valida os dados`  `oModel:CommitData() //realiza a gravação do registro`  `MsgInfo("Registro excluido com sucesso!")`  `lRet := .T.`  `Else`  `VarInfo("Erro ao excluir o registro!",oModel:GetErrorMessage())`  `MsgAlert("Erro ao excluir o registro!")`  `EndIf`    `Else`  `MsgAlert("Registro não localizado!")`  `EndIf`    `return lRet` |

**Saiba mais:**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Incluir](https://totvssuporte.zendesk.com/knowledge/editor/01J5WZYB0QDVDT49AZN348KNT3/pt-br?brand_id=1509248&template_id=115015907348)**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Alterar](https://totvssuporte.zendesk.com/knowledge/editor/new/pt-br?brand_id=1509248&template_id=115015907348)**
