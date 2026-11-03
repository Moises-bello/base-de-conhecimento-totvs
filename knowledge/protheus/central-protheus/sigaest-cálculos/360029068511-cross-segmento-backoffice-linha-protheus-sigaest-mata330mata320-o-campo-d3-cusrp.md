---
article_id: 360029068511
category: SIGAEST - CÁLCULOS
content_hash: a82697766949fc8cae4d152d04cf8bbbb7b3511eaaa1ba5dae1d3f2ba2673135
fetched_at: '2026-06-28T22:39:04.151201+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330/MATA320 -
  o campo D3 _CUSRP1 não está sendo gravado
type: support-article
updated_at: '2025-03-12T12:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029068511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-MATA320-o-campo-D3-CUSRP1-n%C3%A3o-est%C3%A1-sendo-gravado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503174769047) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O *Protheus* não está gravando o campo D3 \_CUSRP1. O que fazer?  
  
**Ambiente**Protheus - Estoque e Custos - A partir da versão 12  
  
**Solução**

Uma vez determinado o Custo Standard dos produtos (seja pela rotina MATA320 ou manualmente no cadastro de produtos, ou seja, campo B1\_CUSTD atualizado), é possível valorizar as movimentações pelo Custo Standard. Isto será feito através da rotina de Recálculo do Custo Médio (MATA330), quando estiver com o parâmetro **MV\_CUSREP= T**. Ao executá-la, os movimentos serão valorizados partindo do custo de referência contido no cadastro de produtos (campo B1\_CUSTD).

Obs: o custo de reposição está disponível apenas em modo offline, ou seja, pela execução do Recálculo do Custo Médio.

**Saiba mais:**

*[MP - SIGAEST - Conceito de utilização da rotina MATA320 - Custo Standard - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*

#
