---
article_id: 115011093448
category: ADVPL - Ponto de Entrada
content_hash: ca6b3b5766e5ba6e1b73195e55c5fcd73c64b28f114884839abfe8a875fb2f27
fetched_at: '2026-06-28T22:40:11.860046+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MA410LEG
type: support-article
updated_at: '2022-06-21T17:53:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011093448-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA410LEG
---

**Dúvida**Houve mudança com ponto de entrada MA410LEG na versão P12 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Na Versão P12 o ponto de entrada MA410LEG traz por PARAMIXB 5 itens no array, sendo assim é necessário verificar o conteúdo da legenda, para pode adicionar um novo item.

Exemplo:

```
#include 'protheus.ch'  
  
user function MA410LEG()  
  
Local aLeg := PARAMIXB  
  
Alert("MA410LEG")  
  
aLeg := { {'ENABLE' ,"Pedido de Venda em aberto"},;  
{'DISABLE' ,"Pedido de Venda encerrado"},;  
{'BR_AMARELO',"Pedido de Venda liberado" },;  
{'BR_AZUL' ,"Pedido de Venda com Bloqueio de Regra"},;  
{'BR_LARANJA',"Pedido de Venda com Bloqueio de Verba" },;  
{'BR_PRETO',"Teste" } }//Customização  
  
Return aLeg
```

**Saiba mais**  
[ADV0027 ponto de entrada MA410LEG na p12](http://tdn.totvs.com/display/PROT/ADV0027_PE_MA410LEG_NA_P12)
