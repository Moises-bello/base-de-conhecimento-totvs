---
article_id: 25831118696471
category: Originação de Grãos (OG)
content_hash: 465465c2ce7691420b57f8fce2b6dd85b8ff7713571835c16cb3294b5beff468
fetched_at: '2026-06-28T22:45:44.870091+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem
  - Alterar
type: support-article
updated_at: '2024-08-22T20:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25831118696471-Agro-Linha-Protheus-AGR-Rotina-Autom%C3%A1tica-MVC-Servi%C3%A7o-de-armazenagem-Alterar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25831126056087) Tempo aproximado para leitura: **00:00:50 min** **Dúvida****Rotina Automática MVC Serviço de armazenagem.** Como alterar?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

* [Alteração](https://tdn.totvs.com/pages/releaseview.action?pageId=861559739#tabs-passo2)

**Exemplo de código - Alteração do registro**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | `User Function zUMVC261()`  `Local lRet := .F.`  `Local oModel := Nil`    `//Exemplo de alteração`  `dbSelectArea("NKG")`  `NKG->(DbSetOrder(1))`  `If NKG->(DbSeek(xFilial("NKG") + '000178' + '00000003'))`    `oModel  := FWLoadModel('OGA261')`  `oModel:SetOperation(MODEL_OPERATION_UPDATE) //Alteração`  `oModel:Activate()`    `//Setando valores nos campos`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VALTAR', 26)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VLTARC', 520)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VALSER', 520)`    `If oModel:VldData() //valida os dados`  `oModel:CommitData() //realiza a gravação do registro`  `MsgInfo("Registro incluído com sucesso")`  `lRet := .T.`  `Else`  `VarInfo("",oModel:GetErrorMessage())`  `MsgAlert("Erro ao incluir o registro")`  `EndIf`  `Else`  `MsgAlert("Registro não localizado!")`  `EndIf`    `return lRet` |

**Saiba mais**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Incluir](https://totvssuporte.zendesk.com/knowledge/editor/01J5WZYB0QDVDT49AZN348KNT3/pt-br?brand_id=1509248&template_id=115015907348)**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Excluir](https://totvssuporte.zendesk.com/knowledge/editor/01J5X4X099K2AFQH7AA8KC2PVD/pt-br?brand_id=1509248&template_id=115015907348)**
