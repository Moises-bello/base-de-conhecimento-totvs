---
article_id: 4410709308183
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 7ea40c5219458e3176b944fe01a39c57afaa887658d9e36541577536b14b0906
fetched_at: '2026-06-28T22:36:59.047119+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada  para
  limpar alguns campos dos itens da cópia do Pedido de Exportação
type: support-article
updated_at: '2021-10-14T14:18:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410709308183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-limpar-alguns-campos-dos-itens-da-c%C3%B3pia-do-Pedido-de-Exporta%C3%A7%C3%A3o
---

**Dúvida**Temos um ponto de entrada para limpar alguns campos dos itens quando realizamos a cópia de um processo no Pedido de Exportação (EECAP100)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**

Na rotina está disponível o ponto de entrada **PE\_COPYPED**:

```
ExecBlock("EECAP100",.f.,.f{"PE_COPYPED",lCapa,lItens})
```

Este ponto de entrada é executado quando é confirmada a cópia do pedido. Além do parâmetro **"PE\_COPYPED"**, que indica a execução do ponto de entrada, são passadas as posições 2 com **lCapa** e 3 com **lItens**, indicando que a execução da cópia processou estas opções.  
Para limpar informações adicionais dos itens do processo, deve ser verificada se lItens é .T. (True) e executar um looping nos itens.   
  
Exemplo:

```
#include "protheus.ch"  
  
User Function EECAP100()  
Local cParamIXB  
  
Begin Sequence  
  
If ValType(ParamIXB) == "A"  
cParamIXB:= ParamIXB[1]  
Else  
cParamIXB:= ParamIXB  
EndIf  
  
Do Case  
  
Case cParamIXB == "PE_COPYPED"  
/*  
Exemplo quando acessada a ação de cópia do processo  
If ParamIXB[3] //se foi selecionada a cópia dos itens  
WorkIt->(DBgoTop())  
While WorkIt->(!Eof())  
WorkIt->EE8_ZZZZZ:= ""  
WorkIt->(DBSkip())  
EndDo  
WorkIt->(DBgoTop())  
EndIf  
*/  
  
EndCase  
  
End Sequence  
  
Return
```

**Saiba mais****[EECAP100 Pedido de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=397378412)**
