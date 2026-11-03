---
article_id: 360021385431
category: ADVPL - Ponto de Entrada
content_hash: 54853c438935d0fd19c0eb11297181fbf00ed47bacbccb53a99dd7c609448809
fetched_at: '2026-06-28T22:40:11.573370+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada MA410COR:
  Alterar cores do cadastro do status do pedido'
type: support-article
updated_at: '2021-12-21T20:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021385431-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA410COR-Alterar-cores-do-cadastro-do-status-do-pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como pode ser alterado cores do cadastro de pedido de vendas. Houve mudança com ponto de entrada **MA410COR** para a versão 12?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Na versão 12 o ponto de entrada **MA410COR** traz por **paramixb** 5 itens no *array*, sendo assim é necessário verificar o conteúdo da legenda para pode adicionar um novo item.

Segue exemplo de customização na versão 12:

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
```

Exemplo do MA410LEG que é utilizado em conjunto:

```
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

Observação:  
- Caso persista é necessário o debug do ponto de entrada, a nova condição deverá está na primeira posição.  
- Sugiro a compilação seja utilizado o VsCode.  
- Lembrando que para inserir as legendas além das cores existe o PE **MA410LEG  
  
Saiba mais**[MA410LEG - Alterar textos da legenda de status do pedido](https://tdn.totvs.com/display/public/PROT/MA410LEG+-+Alterar+textos+da+legenda+de+status+do+pedido)
