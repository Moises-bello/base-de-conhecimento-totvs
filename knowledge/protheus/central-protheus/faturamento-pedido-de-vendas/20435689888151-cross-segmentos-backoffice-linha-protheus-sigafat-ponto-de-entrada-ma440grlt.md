---
article_id: 20435689888151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0a343308d3b8947390e8aa1e9641a1f3a47a316abf980c898b9eb87523239f10
fetched_at: '2026-06-28T22:38:42.512211+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Ponto de entrada
  MA440GRLT
type: support-article
updated_at: '2024-01-09T18:31:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435689888151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-entrada-MA440GRLT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20435689817239) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual é o exemplo de uso do Ponto de entrada MA440GRLT?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**O ponto de entrada MA440GRLT serve para otimizar/modificar a escolha do lote/endereço/série do produto antes da gravação da liberação na tabela SC9 - Liberação de pedidos de venda, de acordo com a regra do usuário.

**OBS:** A verificação se o lote realmente existe nas tabelas deve ser realizada pelo Analista In Loco programador.

**Exemplo de uso do ponto de entrada MA440GRLT:**

```
#INCLUDE 'PROTHEUS.CH'

User Function MA440GRLT()
    Alert("Ponto de entrada MA440GRLT ativado!")
    
    Local aArea := SC6->(GetArea())
    Local cLote := "EA" //C6_LOTECTL, colocar o lote desejado.

    DBSELECTAREA('SC6')
  
    // Se for o produto L (Tem esse tratamento particular)
    If (SC6-C6_PRODUTO = 'L')
        SC6-C6_LOTECTL := cLote
    EndIf
    
    RestArea(aArea) 
Return()
```
