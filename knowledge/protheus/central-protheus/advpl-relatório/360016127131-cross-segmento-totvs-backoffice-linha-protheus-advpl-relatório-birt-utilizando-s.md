---
article_id: 360016127131
category: ADVPL - Relatório
content_hash: f17c7a87ee36a67012a82e952389025a9cebcbfaf812f3b56d401f9d14dff6b7
fetched_at: '2026-06-28T22:40:22.888096+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Relatório Birt utilizando
  SX1
type: support-article
updated_at: '2021-05-21T17:22:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016127131-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Relat%C3%B3rio-Birt-utilizando-SX1
---

**Dúvida**Auxilio na documentação Relatório BIRT para criação do DATA SET ADVPL - SX1

<http://tdn.totvs.com/display/framework/02.3.2+BIRT+%7C+Data+Set+-+ADVPL>

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**1- USER Dataset é um rdmake para um relatório pre definido, que é compilado no RPO para ser vinculado ao DATASET do Relatório

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011616791/mceclip0.png)

Abaixo os ponto de orientação do USER DATASET, este modelo é especifico para Tabela SX1, mas serve de base para qualquer tabela.

1-Definição de Pergunte

2-Definição de campos da tabela temporária

3-Definição da Query no caso SX1

4-Definição dos campos que irá receber os dados da SX1

5-Gravação da Tabela temporaria

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011616871/mceclip1.png)
