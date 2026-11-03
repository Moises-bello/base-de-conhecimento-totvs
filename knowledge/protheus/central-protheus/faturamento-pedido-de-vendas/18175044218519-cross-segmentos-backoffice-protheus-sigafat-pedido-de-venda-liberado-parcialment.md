---
article_id: 18175044218519
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 93c4a263a06cf31c47f863a48652079a18043bf4b10b1d41b3bd4a19218b7081
fetched_at: '2026-06-28T22:38:39.940151+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de Venda Liberado
  Parcialmente
type: support-article
updated_at: '2025-11-28T19:30:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18175044218519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-Venda-Liberado-Parcialmente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18175028672919) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida:**  
O sistema está liberando o pedido de forma parcial?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
Em situações aonde o faturamento possui quantidade maior que disponível, a parâmetros e perguntes que podem influenciar na decisão do sistema entre faturar e bloquear o pedido de venda.  
  
O pergunte é o **"Libera só c/Estoque"** da rotina MATA440 (Liberação de pedido de vendas), exibido ao apertar F12 na tela da rotina.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18174719869591)  
  
Na liberação de pedidos com saldos parciais é necessário acertar o seguinte parâmetro:

* **MV\_GRVBLQ2** que pode possuir os valores **"T"** ou **"F"**

**Exemplo: de sua utilização:**

Supondo um faturamento onde há quantidade disponível de 50, porém no pedido de venda foi requerido 100.

Pergunte F12 - "Libera só c/Estoque" = **Não**

Parâmetro: **MV\_GRVBLQ2** = **F**

Resultado: Bloqueia tudo (Gera a SC9 com a quantidade 100 bloqueada)

Pergunte F12 -"Libera só c/Estoque" = **Sim**

Parâmetro: **MV\_GRVBLQ2** = **F**

Resultado: Fatura com a quantia disponível  
OBS 1: Só gera a **SC9** com o que realmente tem em estoque, ou seja, não é bloqueado, pois só é gerado com o que realmente é possível liberar.

OBS 2: Caso algum item nas linhas liberadas não possuir absolutamente nada para ser liberado sem bloqueios, irá gerar bloqueado com toda sua quantidade, ele não deixará de gerar a tabela SC9.

Pergunte F12 -"Libera só c/Estoque" = **Não**

Parâmetro**: MV\_GRVBLQ2** = **T**

Resultado: Bloqueia tudo

Pergunte F12 -"Libera só c/Estoque"= **Sim**

Parâmetro: **MV\_GRVBLQ2** = **T**

Resultado: Bloqueia só o que realmente não tem, o resto gera liberado.

OBS 1: Gera na **SC9**  duas linhas, uma bloqueada por estoque C9\_BLEST=02, e outra sem bloqueio em branco.

**Saiba mais:**

[Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Funcionalidade do campo C5\_TIPLIB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055457353-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Funcionalidade-do-campo-C5-TIPLIB)

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Como consultar saldo liberado parcialmente no pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28558861442583-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-consultar-saldo-liberado-parcialmente-no-pedido)
