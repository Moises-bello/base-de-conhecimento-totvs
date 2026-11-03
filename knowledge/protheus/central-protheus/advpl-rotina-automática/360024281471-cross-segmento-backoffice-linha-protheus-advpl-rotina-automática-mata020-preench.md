---
article_id: 360024281471
category: ADVPL - Rotina Automática
content_hash: 413f2a8fa89f81f202827716a341c83289b60cc564ae367e1bce8eedfd02769b
fetched_at: '2026-06-28T22:40:24.200401+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina automática mata020
  preenchimento da tabela FIL
type: support-article
updated_at: '2022-04-07T19:53:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024281471-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-mata020-preenchimento-da-tabela-FIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**É possível por meio darotina automática de cadastro de fornecedores (MATA020) realizar o preenchimento da tabela FIL (Outras Ações/Bancos [A020BANCOS])?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Sim, utilizando a estrutura MVC, onde deve ser informado o Sub modelo "BANCOS", abaixo PoC:

```
#Include "Protheus.ch"  
#Include "RwMake.ch"  
#Include "TbiConn.ch"  
  
User Function EXEC020()  
  
Local nOpc := 3 // ----> Inclusão  
Local oModel := Nil  
Local cCod := "008"  
Local cLoja := "01"  
Local cNome := "Fornecedor 008"  
Local cNReduz := "Forn 008"  
Local cEnd := "Av Braz Leme, 1000"  
Local cBairro := "Casa Verde"  
Local cEst := "SP"  
Local cCodMun := "50308"  
Local cMun := "São Paulo"  
Local cTipo := "F"  
Local cCGC := "88888888888"  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM"  
  
oModel := FWLoadModel('MATA020')  
  
oModel:SetOperation(nOpc)  
oModel:Activate()  
  
//Cabeçalho  
oModel:SetValue('SA2MASTER','A2_COD' ,cCod)  
oModel:SetValue('SA2MASTER','A2_LOJA' ,cLoja)  
oModel:SetValue('SA2MASTER','A2_NOME' ,cNome)  
oModel:SetValue('SA2MASTER','A2_NREDUZ' ,cNReduz)  
oModel:SetValue('SA2MASTER','A2_END' ,cEnd)  
oModel:SetValue('SA2MASTER','A2_BAIRRO' ,cBairro)  
oModel:SetValue('SA2MASTER','A2_EST' ,cEst)  
oModel:SetValue('SA2MASTER','A2_COD_MUN',cCodMun)  
oModel:SetValue('SA2MASTER','A2_MUN' ,cMun)  
oModel:SetValue('SA2MASTER','A2_TIPO' ,cTipo)  
oModel:SetValue('SA2MASTER','A2_CGC' ,cCGC)  
  
oModel:SetValue('BANCOS','FIL_BANCO' ,"01")  
oModel:SetValue('BANCOS','FIL_AGENCI' ,"0101")  
oModel:SetValue('BANCOS','FIL_CONTA' ,"010101")  
  
If oModel:VldData()  
oModel:CommitData()  
Endif  
  
oModel:DeActivate()  
  
oModel:Destroy()  
  
RESET ENVIRONMENT  
  
Return
```

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5304004068247/mceclip3.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5303948941847/mceclip0.png)

**Saiba mais**[MATA020 MVC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=463824753)
