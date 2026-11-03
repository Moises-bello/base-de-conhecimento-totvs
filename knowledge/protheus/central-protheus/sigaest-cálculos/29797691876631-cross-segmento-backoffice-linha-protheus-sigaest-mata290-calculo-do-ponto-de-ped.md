---
article_id: 29797691876631
category: SIGAEST - CÁLCULOS
content_hash: fe95415ff099d74b3607181b231aebdab94f4d69e3481753b25d5d60291e336c
fetched_at: '2026-06-28T22:39:04.050763+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA290 - Calculo
  do Ponto de Pedido
type: support-article
updated_at: '2025-03-12T12:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29797691876631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Calculo-do-Ponto-de-Pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29797691861143) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Como é calculado o Ponto de Pedido no Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O ponto de pedido é a quantidade em estoque que uma vez atingida, inicia o processo de compra ou produção, considerando o consumo médio mensal, **[o tempo de reposição](https://tdn.totvs.com/pages/viewpage.action?pageId=433252473)** e **[o estoque de segurança.](https://tdn.totvs.com/pages/viewpage.action?pageId=433252482)**

Dessa forma, a fórmula para cálculo do ponto de pedido é PP = (CM\*TR) + ES.

em que:

CM = consumo médio

TR = tempo de reposição, que é o prazo de entrega do cadastro do produto

ES = estoque de segurança

PP = ponto de pedido

**Exemplo:**

CM = 30

TR = 02 meses

ES = 20

PP = (CM\*TR) + ES

PP = (30\*2) + 20 = 80

**Saiba mais:**

*[Lote Econômico - MATA290 - Tudo sobre a rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=347442943)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)*
