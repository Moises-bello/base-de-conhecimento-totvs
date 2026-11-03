---
article_id: 1500004512542
category: Materiais - Compras (SIGACOM)
content_hash: 05879c54cc2d0f3ebdc5ec78e5e2417407edcb1a04eafa39ccc3f1965272c392
fetched_at: '2026-06-28T22:41:24.268181+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual campo de valor
  o sistama considera para gravar o campo DE_CUSTO1 quando, na Nota de Entrada há
  Rateio por Centro de Custo ?
type: support-article
updated_at: '2025-10-07T12:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004512542-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-campo-de-valor-o-sistama-considera-para-gravar-o-campo-DE-CUSTO1-quando-na-Nota-de-Entrada-h%C3%A1-Rateio-por-Centro-de-Custo
---

**Dúvida**

Qual campo de valor o sistama considera para gravar o campo DE\_CUSTO1 quando, na Nota de Entrada há Rateio por Centro de Custo ?

**Ambiente**

Protheus - Compras - A partir da versão 12

**Solução**

Cada vez que em uma nota de entrada há a informação de um rateio por centro de custo, o sistema por padrão, grava as informações dentro da tabela SDE.

Para gravar o campo DE\_CUSTO1, o sistema usa o valor calculado no campo D1\_CUSTO e, baseado nele, é feito o cálculo de acordo com os  percentuais informados no rateio.

**Veja exemplo abaixo :**

*Rateio informado na nota de entrada. Usados 4 centros de custo com 25% por em cada um.*

*![rateio1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005658782)*

*Ao salvar a nota, o sistema gravará esse rateio na tabela SDE.*

*![rateio2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005766021)*

*O campo DE\_CUSTO1, de cada centro de custo foi calculado com o valor de R$ 375,00, porque o D1\_CUSTO dessa nota foi calculado com o valor de R$ 1.500,00. Nesse exemplo o mesmo valor do total da nota, porém o valor do custo do produto pode variar, de acordo com impostos e/ou outros valores, como despesas, descontos, impostos, etc.*

*![RATEIO3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005766101)*

*Logo, 25% de R$ 1.500,00 corresponde a R$ 375,00. valor gravado no campo DE\_CUSTO1.*

***Caso tenha alguma dúvida sobre como é efetuado o cálculo do campo D1\_CUSTO, solicitamos entrar em contato com a equipe de suporte do módulo Estoque/Custos.***

***Saiba Mais :***

*[PCOM12084 - Custo de rateio por Centro de Custo da nota fiscal ficando negativo (DE\_CUSTO1)](https://tdn.totvs.com/display/PROT/PCOM12084+-+Custo+de+rateio+por+Centro+de+Custo+da+nota+fiscal+ficando+negativo)*

[PÁGINA CENTRALIZADORA DE COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
