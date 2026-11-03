---
article_id: 28154701303703
category: Financeiro - Contas a Receber
content_hash: 2d576a8170db8268f8b31eccb304e952090d646850c2c6b7f20b1f06456a43c3
fetched_at: '2026-06-28T22:38:12.538830+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Variação cambial com
  o título e banco com a mesma moeda
type: support-article
updated_at: '2024-11-29T17:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28154701303703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Varia%C3%A7%C3%A3o-cambial-com-o-t%C3%ADtulo-e-banco-com-a-mesma-moeda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28154701287447) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível realizar variação cambial utilizando a mesma moeda do título e do banco?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Baixa variação cambial - Todas as versões  
  
**Solução**

A variação cambial ocorre quando há uma conversão entre moedas diferentes devido à flutuação da taxa de câmbio, sendo o valor relativo entre duas moedas. Se ambas as operações estão na mesma moeda, não há taxa de câmbio envolvida, e, portanto, não há variação cambial.

**Por exemplo:**

* Se você compra algo em reais (R$) e paga em reais (R$), não existe necessidade de calcular um câmbio, pois não há troca de moeda.
* Agora, se você compra em dólares (USD) e paga em reais (R$), o sistema precisa calcular a variação com base na taxa de câmbio entre USD e BRL, o que pode gerar uma diferença ao longo do tempo, dependendo das flutuações do mercado.

**Resumindo:** A variação cambial só existe quando ocorre uma operação entre **moedas diferentes**, pois o câmbio mede a relação entre elas.
