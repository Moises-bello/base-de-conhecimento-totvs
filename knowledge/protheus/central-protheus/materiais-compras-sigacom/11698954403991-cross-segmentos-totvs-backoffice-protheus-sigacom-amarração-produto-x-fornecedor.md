---
article_id: 11698954403991
category: Materiais - Compras (SIGACOM)
content_hash: a1b50123e6970c46ce9eb601e60da49de7fb572aa63d0bedd19ab3a7016b6d7a
fetched_at: '2026-06-28T22:41:13.150292+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Amarração Produto x
  Fornecedor (Rotina Automática MATA061 - EXECAUTO)
type: support-article
updated_at: '2023-01-16T11:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11698954403991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Amarra%C3%A7%C3%A3o-Produto-x-Fornecedor-Rotina-Autom%C3%A1tica-MATA061-EXECAUTO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04 min** **Dúvida**

Como configurar a rotina automática que permite a inclusão de amarração produto x fornecedor?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Protheus 12  
  
**Solução**

Para realizar a opção de alteração e/ou exclusão é necessário que deixe posicionado no registro a ser alterado ou excluído.

Exemplo de Incusão :

#Include "Protheus.ch"  
#Include "RwMake.ch"  
#Include "TbiConn.ch"  
  
User Function EXEC061()  
  
Local nOpc := 3  
Local oModel := Nil  
Local cProd061 := "0002"  
Local cForn1 := "001"  
Local cLoja1 := "01"  
Local cForn2 := "002"  
Local cLoja2 := "01"  
  
PREPARE ENVIRONMENT EMPRESA "32" FILIAL "6597" MODULO "COM"  
  
oModel := FWLoadModel('MATA061')  
  
oModel:SetOperation(nOpc)  
oModel:Activate()  
  
//Cabeçalho  
oModel:SetValue('MdFieldSA5','A5\_PRODUTO',cProd061)  
oModel:SetValue('MdFieldSA5','A5\_NOMPROD','PRODUTO 061 CT001')  
  
//Grid  
oModel:SetValue('MdGridSA5','A5\_FORNECE',cForn1)  
oModel:SetValue('MdGridSA5','A5\_LOJA' ,cLoja1)  
//oModel:SetValue('MdGridSA5','A5\_NOMEFOR', 'FOR. P/ ROTINA MATA061 - CT001')  
  
//Nova linha na Grid  
oModel:GetModel("MdGridSA5"):AddLine()  
  
oModel:SetValue('MdGridSA5','A5\_FORNECE',cForn2)  
oModel:SetValue('MdGridSA5','A5\_LOJA' ,cLoja2)  
//oModel:SetValue('MdGridSA5','A5\_NOMEFOR', 'FOR. P/ ROTINA MATA061 - CT001')  
  
If oModel:VldData()  
oModel:CommitData()  
Endif  
  
oModel:DeActivate()  
  
oModel:Destroy()  
  
RESET ENVIRONMENT  
  
Return

**Saiba mais em :**

[Rotina Automatica Mata061 - Execauto](https://tdn.totvs.com/x/pGGlGw)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
