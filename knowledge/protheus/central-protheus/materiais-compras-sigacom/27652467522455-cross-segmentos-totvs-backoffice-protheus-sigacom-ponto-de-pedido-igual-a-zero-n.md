---
article_id: 27652467522455
category: Materiais - Compras (SIGACOM)
content_hash: ef281b068d0da4417ca746698e066ba5f10409b43515e82cb9a1059d0354c169
fetched_at: '2026-06-28T22:41:13.043918+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  PONTO DE PEDIDO -
  Igual a Zero não gerar Solicitação de Compras
type: support-article
updated_at: '2024-11-08T13:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27652467522455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-PONTO-DE-PEDIDO-Igual-a-Zero-n%C3%A3o-gerar-Solicita%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27652467497879) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Como não gerar solicitação quando o Ponto de Pedido for igual a zero?  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gesão de Compras- Versão 12  
  
**Solução**

Quando o campo "Ponto de Pedido" é igual a zero, a rotina **MATA170** só gerará Solicitação/Pedido de Compras caso o saldo do produto seja inferior a zero (ou seja, saldo negativo).

Exemplo:

* **Ponto de Pedido** = 0
* **Saldo Atual** = -1

Ao executar a rotina do ponto de pedido, será gerada uma solicitação de compras com quantidade 2, para tornar o saldo do produto positivo novamente.

A única forma de evitar que o ponto de pedido gere demanda para produtos configurados com valor 0 é configurar o parâmetro **Cons. Necess. Bruta (MV\_PAR09)** como "Não".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27652478801943)

***Saiba Mais***

[Como configurar Ponto de Pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414843367319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-configurar-Ponto-de-Pedido)

[SIGACOM - Pontos de Entrada Solicitação por Ponto de Pedido - MATA170](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408775373207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-Solicita%C3%A7%C3%A3o-por-Ponto-de-Pedido-MATA170)

[Como é realizado o cálculo de necessidade na rotina Ponto de Pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27256450694935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-necessidade-na-rotina-Ponto-de-Pedido)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
