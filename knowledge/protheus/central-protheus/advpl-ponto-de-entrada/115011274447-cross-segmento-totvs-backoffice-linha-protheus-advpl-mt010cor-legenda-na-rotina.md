---
article_id: 115011274447
category: ADVPL - Ponto de Entrada
content_hash: 310193e94e99e3d0bd1446024e52c6e52c436923922f9fe48dcae71419dd6429
fetched_at: '2026-06-28T22:40:11.759271+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MT010COR Legenda
  na rotina cadastro de produtos  '
type: support-article
updated_at: '2022-06-21T17:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011274447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MT010COR-Legenda-na-rotina-cadastro-de-produtos
---

**Dúvida**Houve mudança com ponto de entrada MT010COR?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Na Versão protheus 12, o ponto de entrada MT010COR o array, deverá se montado com 3 itens

```
Unknown macro: {Condição, Cor, Descrição}
```

Exemplo

```
#Include 'Protheus.ch'  
  
 User Function MT010COR()  
 Local aCores:={}  
  
 Alert ("Passou pelo aCores")  
 aAdd(aCores,{'B1_TIPO == "AI"','BR_VERMELHO', 'Produto teste'})  
  
 Return aCores
```

**Saiba mais**  
[ADV0030 Ponto de entrada MT010COR](http://tdn.totvs.com/display/PROT/ADV0030_PE_MT010COR_NA_P12)
