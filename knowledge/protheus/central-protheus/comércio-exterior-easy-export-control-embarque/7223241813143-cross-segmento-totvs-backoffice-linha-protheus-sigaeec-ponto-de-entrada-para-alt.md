---
article_id: 7223241813143
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 76764bbd5c497fded3493e43935be105ca66c7e74639766f530e54c51b1d3102
fetched_at: '2026-06-28T22:36:39.214830+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  para alteração dos campos no rodapé do Embarque de exportação
type: support-article
updated_at: '2022-07-04T19:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7223241813143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-altera%C3%A7%C3%A3o-dos-campos-no-rodap%C3%A9-do-Embarque-de-exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Temos algum de um ponto de Entrada com a opção de alterar os campos do rodapé no Embarque de Exportação **(EECAE100)**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Temos o ponto de entrada **ANTES\_REFRESH\_RODAPE**  que permite a alteração dos campos do rodapé do embarque de exportação.

```
#include "protheus.ch"  
  
User Function EECAE100()  
Local cParamIXB := ""  
   If ValType(ParamIXB) == "A"  
      cParamIXB:= ParamIXB[1]  
   Else  
      cParamIXB:= ParamIXB  
   EndIf  
   Do Case  
      Case cPARAMIXB == "ANTES_REFRESH_RODAPE"      
           M->EEC_TOTPED := 101 //Total Embarque   
           nTotEmbBr := 102 // Total Emb.(Bruto)  
           M->EEC_TOTFOB := 103 //Total Fob  
           M->EEC_VLFOB := 103 //Total Fob Interno, deixar este valor igual ao EEC_TOTFOB  
           M->EEC_TOTLIQ := 104 // Total Liquido   
           M->EEC_PESLIQ :=105 // Peso Líquido      
           M->EEC_PESBRU := 106 //Peso Bruto  
   EndCase  
Return NIL
```

**Saiba mais**

[PE EECAE100 Embarque](https://tdn.totvs.com/display/public/PROT/DT+PE+EECAE100+Embarque)
