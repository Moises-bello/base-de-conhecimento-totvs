---
article_id: 9248641498135
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: be81584dfdf7b3e260795bdd7905423e0d10c9f6be1c9b6d60548b98d359b752
fetched_at: '2026-06-28T22:38:42.446338+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MTA455VL
type: support-article
updated_at: '2024-01-05T17:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9248641498135-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MTA455VL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MTA455VL - Valida a seleção de Lotes/Endereçamento.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **MTA455VL** permite **validar a seleção de Lotes/Endereçamento** na Nova Liberação na opção Liberação de Estoque (SIGAFAT).  
  
**Exemplo**

```
User Function MTA455VL(cAlias)  
  
Local aArea := GetArea()  
Local lRet  
  
dbSelectArea(ParamIxb[1]) // Alias TRB do MarkBrowse  
  
// Validacao - lRet := .T. (confirma a selecao)  
// Validacao - lRet := .F. (nao confirma)  
  
Alert("Entrou no Ponto de Entrada MTA455VL")  
  
If SC9->C9_BLEST = "02" // Condicao  
lRet := .T.  
Alert("Selecao do Lote/Enderecamento confirmada")  
Else  
lRet := .F.  
Alert("Selecao do Lote/Enderecamento nao confirmada")  
EndIf  
  
RestArea(aArea)  
  
Return (lRet)
```

**Saiba Mais**

**[MTA455VL - Valida a seleção de Lotes/Endereçamento](https://tdn.totvs.com/x/MoZn)**
