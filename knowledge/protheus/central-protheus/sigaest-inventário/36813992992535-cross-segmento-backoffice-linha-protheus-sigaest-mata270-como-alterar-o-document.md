---
article_id: 36813992992535
category: SIGAEST - INVENTÁRIO
content_hash: d2e49fe098670be07a0562e3822767d1cedeedd71ac2da10b92155ad4408415d
fetched_at: '2026-06-28T22:38:50.287027+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 Como alterar
  o Documento gerado pelo inventário, para que o mesmo não gere = "INVENT"
type: support-article
updated_at: '2025-12-05T19:50:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36813992992535-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-Como-alterar-o-Documento-gerado-pelo-invent%C3%A1rio-para-que-o-mesmo-n%C3%A3o-gere-INVENT
---

O sistema Protheus padrão grava o campo "Documento" como "INVENT" no processo de Inventário para facilitar a identificação no Kardex. Para alterar essa gravação, é necessário utilizar pontos de entrada específicos com apoio do time de desenvolvimento. Links com documentações e orientações estão disponíveis para ajustes no MATA340 e controle do D3\_DOC.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36813992977175) Tempo aproximado para leitura: **00:03:00 min**  
  
  
**Dúvida**  
Há algo que possa ser feito para que o sistema realmente assuma o conteúdo digitado no campo "Documento" ao invés de "INVENT" no processo de Inventário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
Realmente no padrão todo Acerto de Inventário (MATA340) que gere um movimento interno (MATA241) entre a diferença contada no Sistema para o saldo que tinha anteriormente.   
  
O sistema gera o movimento é gravado com D3\_DOC = INVENT, pois isso serve para que, no Kardex, seja possível informar de maneira mais clara e ser melhor a identificação de que aquele movimento de produto foi ocasionado por um Inventário.  
  
Para casos em que seja necessária a alteração do modo de gravação do campo D3\_DOC, possuimos as documentações de apoio, para que junto ao seu time de desenvolvimento seja possível analisar um ponto de entrada que mais se adeque a sua necessidade  
  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Pontos de Entrada disponíveis na rotina Acerto de Inventário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16928358150167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Acerto-de-Invent%C3%A1rio)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 - Pontos de Entrada disponíveis na rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11629519812887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina)  
  
**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Controle de numeração D3\_DOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34841866033175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Controle-de-numera%C3%A7%C3%A3o-D3-DOC)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)

[Clique aqui e veja mais artigos sobre INVENTÁRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
