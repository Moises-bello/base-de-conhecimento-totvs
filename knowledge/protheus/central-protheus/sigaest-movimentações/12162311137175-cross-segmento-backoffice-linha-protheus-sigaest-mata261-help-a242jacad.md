---
article_id: 12162311137175
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b7e31cf57953026051a8012ef4609bb88ff7d779d7b558406759d9f97584c6c4
fetched_at: '2026-06-28T22:38:57.029220+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - HELP A242JACAD
type: support-article
updated_at: '2026-03-10T15:01:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12162311137175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-HELP-A242JACAD
---

O erro HELP A242JACAD na rotina Transferências Múltiplas (MATA261) ocorre porque há mais de uma linha do mesmo produto, o sistema não aceita linhas duplicadas. O usuário deve somar as quantidades e usar uma única linha para realizar a transferência do material em estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37636824195991) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual a o motivo que apresenta o ***HELP A242JACAD*** na rotina Transferências Múltiplas (MATA261)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
O HELP A242JACAD é apresentado devido constar mais de uma linha do mesmo produto, a mensagem indica que a rotina não está preparada para trabalhar com duas linhas exatamente iguais, nesse cenário, o usuário deve utilizar uma única linha e informar a quantidade total que deseja transferir, atendendo dessa forma sua necessidade de realizar a transferência do material em estoque.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12162318715159)

**Nesse caso, como no exemplo acima, deve-se somar as quantidades e manter apenas uma linha no documento.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12162533138967)

**Pode deletar uma das linhas e acrescentar a diferença no outro registro.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12162635276183)

**OBS:** Hoje no padrão, não dispõe de um Ponto de Entrada para mudar esse comportamento.

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
