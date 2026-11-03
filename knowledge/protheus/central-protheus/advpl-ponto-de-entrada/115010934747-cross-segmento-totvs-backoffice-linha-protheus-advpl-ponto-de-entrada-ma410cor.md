---
article_id: 115010934747
category: ADVPL - Ponto de Entrada
content_hash: d0554e24f1b470a9b9b73307151253b7e7e2694e66b2706773bd3482d386aff8
fetched_at: '2026-06-28T22:40:11.856567+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de Entrada
  MA410COR
type: support-article
updated_at: '2022-06-21T17:53:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010934747-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-MA410COR
---

**Dúvida**Houve mudança com ponto de entrada MA410COR?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Na Versão P12 o ponto de entrada MA410COR traz por paramixb 5 itens no array, sendo assim é necessário verificar o conteúdo da legenda para pode adicionar um novo item.

Exemplo

```
User Function MA410COR()  
Local aCores := {} // PARAMIXB traz a estrutura do array padrão  
Alert("MA410COR")  
  
aAdd(aCores, {"C5_TESTE == 'C'", "BR_PRETO", "Teste 01"})  
aAdd(aCores, {"Empty(C5_LIBEROK).And.Empty(C5_NOTA) .And. Empty(C5_BLQ)", "ENABLE", "Pedido em Aberto"})  
aAdd(aCores, {"!Empty(C5_NOTA).Or.C5_LIBEROK=='E' .And. Empty(C5_BLQ)", "DISABLE", "Pedido Encerrado"})  
aAdd(aCores, {"!Empty(C5_LIBEROK).And.Empty(C5_NOTA).And. Empty(C5_BLQ)", "BR_AMARELO", "Pedido Liberado"})  
aAdd(aCores, {"C5_BLQ == '1'", "BR_AZUL""})  
aAdd(aCores, {"C5_BLQ == '2'", "BR_LARANJA"})  
  
Return aCores  
  
---------------------------------------------------------------------------------------------------------------------------------------------------------------  
Exemplo do MA410LEG que é utilizado em conjunto .  
  
#INCLUDE 'protheus.ch'  
User Function MA410LEG()  
Local aLegenda := PARAMIXB  
aLegenda := {}  
  
AADD(aLegenda,{"BR_PINK" ,"Pedido Bloqueado (Crédito Cliente)"})  
AADD(aLegenda,{"BR_CANCEL" ,"Pedido Rejeitado (Regras Dipil)"})  
AADD(aLegenda,{"BR_PRETO" ,"Pedido Bloqueado (Regras Dipil)"})  
AADD(aLegenda,{"ENABLE" ,"Pedido de Venda em aberto"})  
AADD(aLegenda,{"DISABLE" ,"Pedido de Venda encerrado"})  
AADD(aLegenda,{"BR_AZUL" ,"Pedido Bloqueado por Regra"})  
AADD(aLegenda,{"BR_LARANJA" ,"Pedido Bloqueado por Verba"})  
AADD(aLegenda,{"BR_AMARELO" ,"Pedido de Venda liberado"})  
  
Return(aLegenda)
```

Observação

* Caso persista é necessário o debug do ponto, a nova condição deverá está na primeira posição.
* Sugiro a compilação seja utilizado o TDS 11.2 ou 11.3
* Lembrando que para inserir as legendas e das cores existe o PE MA410LEG.

**Saiba mais**  
[ADV0026 ponto de entrada MA410COR](http://tdn.totvs.com/display/PROT/ADV0026_PE_MA410COR_NA_P12)
