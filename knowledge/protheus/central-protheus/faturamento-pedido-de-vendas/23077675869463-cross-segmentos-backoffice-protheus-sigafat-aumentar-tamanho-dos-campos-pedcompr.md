---
article_id: 23077675869463
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a3f3b4471b41d683b18adac7df38940f9ad616c1b0ddfaefb308364cac9613d4
fetched_at: '2026-06-28T22:38:39.647736+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Aumentar tamanho dos campos
  "Ped.Compra (C6_PEDCOM)" e "Item PC (C6_ITEMPC)"
type: support-article
updated_at: '2024-05-16T13:54:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23077675869463-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Aumentar-tamanho-dos-campos-Ped-Compra-C6-PEDCOM-e-Item-PC-C6-ITEMPC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23077689898007) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Pode aumentar o tamanho dos campos "Ped.Compra (C6\_PEDCOM)" e "Item PC (C6\_ITEMPC)"  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O tamanho desses campo são travados, não permitindo alteração do usuário nativamente.  
  
Não recomendamos alteração "forçada" dos campos nas tabelas para prevenção de muitos erros que não são nem mapeáveis.  
  
**OBSERVAÇÃO:** Ambos os campos são alfanuméricos permitindo milhares de combinações

* O campo C6\_PEDCOM recebe o valor dos pedidos de compra, que também possuem 6 espaços.
* O campo C6\_ITEMPC recebe a posição nos itens (aCols), não é o código do Item.  
  ![](https://totvssuporte.zendesk.com/attachments/token/4K8wFueHdynxyiMrxi96UjbXm/?name=image.png)

Ambos são alfanuméricos, podendo alcançar milhões de combinações.  
  
A documentação dos campos a seguir se aplica para os campos da documentação o saiba mais.

**Saiba mais:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tamanho dos campos C5\_NUM e C6\_NUM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046826433-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tamanho-dos-campos-C5-NUM-e-C6-NUM?source=search)
