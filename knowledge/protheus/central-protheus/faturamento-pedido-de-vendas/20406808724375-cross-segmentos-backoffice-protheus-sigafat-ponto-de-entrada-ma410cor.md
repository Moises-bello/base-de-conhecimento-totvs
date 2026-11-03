---
article_id: 20406808724375
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4b3220daef04f51d6aeaa1c6954bb6ae39d4c8aa23de0b32966f4c1ad1437f81
fetched_at: '2026-06-28T22:38:42.586621+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus – SIGAFAT – Ponto de entrada MA410COR
type: support-article
updated_at: '2025-03-05T16:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20406808724375-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-MA410COR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20406780161431) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual é o exemplo do Ponto de entrada MA410COR?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus – Faturamento (SIGAFAT) – Todas as versões.

**Solução**

Esse ponto de entrada serve para customizar as cores das legendas conforme o valor/expressão dos campos desejados.

**OBS:** Os campos utilizados para formulação das expressões, devem existir no banco de dados, ou seja, não podem ser virtuais.

**Exemplo:**

User Function MA410COR()

  

Local aCores := {}

  

Alert("Entrando no ponto de entrada MA410COR")

  

aAdd(aCores, {"C5\_BLQ == '3'", "BR\_PRETO", "Teste 01"})

aAdd(aCores, {"Empty(C5\_LIBEROK).And.Empty(C5\_NOTA) .And. Empty(C5\_BLQ)", "ENABLE", "Pedido em Aberto"})

aAdd(aCores, {"!Empty(C5\_NOTA).Or.C5\_LIBEROK=='E' .And. Empty(C5\_BLQ)", "DISABLE", "Pedido Encerrado"})

aAdd(aCores, {"!Empty(C5\_LIBEROK).And.Empty(C5\_NOTA).And. Empty(C5\_BLQ)", "BR\_AMARELO", "Pedido Liberado"})

aAdd(aCores, {"C5\_BLQ == '1'", "BR\_AZUL", "Pedido de venda com bloqueio de regra"})

aAdd(aCores, {"C5\_BLQ == '2'", "BR\_LARANJA", "Pedido de venda com bloqueio de verba"})

  

Return aCores

**Saiba mais:**

[**MA410COR - Alterar cores do cadastro do status do pedido**](https://tdn.totvs.com/x/C4Vn)
