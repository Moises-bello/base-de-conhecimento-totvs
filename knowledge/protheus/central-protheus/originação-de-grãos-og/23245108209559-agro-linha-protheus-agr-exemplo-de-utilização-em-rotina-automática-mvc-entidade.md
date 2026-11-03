---
article_id: 23245108209559
category: Originação de Grãos (OG)
content_hash: eda0a7f368b8d6c67bf1a8acd42a509189fd37fb215f208eae3707205e26fe9a
fetched_at: '2026-06-28T22:45:39.454466+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Exemplo de Utilização em Rotina Automática MVC
  - Entidade OGA010
type: support-article
updated_at: '2025-06-24T11:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23245108209559-Agro-Linha-Protheus-AGR-Exemplo-de-Utiliza%C3%A7%C3%A3o-em-Rotina-Autom%C3%A1tica-MVC-Entidade-OGA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23245108187671) Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como é realizado um procedimento para **Exemplo de Utilização em Rotina Automática MVC - Entidade OGA010**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize o seguinte procedimento:

* [Inclusão](https://tdn.totvs.com/pages/releaseview.action?pageId=648427786#tabs-passo1)

|  |
| --- |
| `User Function zDelReg()<``font``></``font``>`  `Local lRet := .F.<``font``></``font``>`  `Local oModel := Nil<``font``></``font``>`  `<``font``></``font``>`  `dbSelectArea("NJ0")<``font``></``font``>`  `NJ0->(DbSetOrder(1))<``font``></``font``>`  `If NJ0->(DbSeek(xFilial("NJ0") + '990001'))<``font``></``font``>`  `oModel  := FWLoadModel('OGA010')   <``font``></``font``>`  `oModel:SetOperation(MODEL_OPERATION_DELETE) //EXCLUSÃO<``font``></``font``>`  `oModel:Activate()<``font``></``font``>`  `<``font``></``font``>`  `If oModel:VldData() //valida os dados<``font``></``font``>`  `oModel:CommitData() //realiza a gravação do registro<``font``></``font``>`  `MsgInfo("Registro excluido com sucesso")   <``font``></``font``>`  `lRet := .T.<``font``></``font``>`  `Else   <``font``></``font``>`  `VarInfo("",oModel:GetErrorMessage())<``font``></``font``>`  `MsgAlert("Erro ao excluir o registro")<``font``></``font``>`  `EndIf <``font``></``font``>`  `Else<``font``></``font``>`  `MsgInfo("Registro não localizado!")<``font``></``font``>`  `EndIf<``font``></``font``>`  `<``font``></``font``>`  `return lRet` |
