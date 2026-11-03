---
article_id: 360021507611
category: ADVPL - Classe e Função
content_hash: 6206faadd019bdbc83f9171f73b58f047d74ac46c869d1cf98150c82fc939d58
fetched_at: '2026-06-28T22:40:18.190091+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização do MsDocument
  no ponto MTA094RO.
type: support-article
updated_at: '2023-05-26T16:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021507611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-do-MsDocument-no-ponto-MTA094RO
---

**Dúvida**Como devo declarar a função MsDocument para que funcione corretamente na rotina MATA094?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 11.80  
  
  
**Solução**Para a utilização deve seguir o exemplo abaixo.

```
#Include 'Protheus.ch'  
  
User Function MTA094RO()  
  
Private aRotina:= PARAMIXB[1]  
  
Aadd(aRotina,{'MsDocument_',"U_MSdoc()", 0, 4,0,NIL})  
  
//Validações do usuário  
  
Return (aRotina)  
  
  
User Function MSdoc()  
  
Private aRotina := FWloadmenudef('MATA094')  
  
MsDocument('SC7',SC7->(RecNo()), 4)  
  
return .t.
```

**Saiba Mais**

**[MTA094RO](http://tdn.totvs.com/display/public/PROT/TTPVOU_COM_DT_Ponto_de_Entrada_MTA094RO)**

**[MsDocument](http://tdn.totvs.com/display/public/PROT/MsDocument)**
