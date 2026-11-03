---
article_id: 16145221806103
category: Materiais - Compras (SIGACOM)
content_hash: 7b8b3304d3c1efd64d7f2d5dfa39a510f781d47828a25c1d3986f7b11ed74cd2
fetched_at: '2026-06-28T22:41:18.820954+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Help A103DHROBRIG ao
  incluir documento de entrada
type: support-article
updated_at: '2023-07-19T18:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16145221806103-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Help-A103DHROBRIG-ao-incluir-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16145191738135) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao salvar a inclusão de um documento de entrada, o sistema gera o help A103DHROBRIG - O(s) item(ns) 0001 não tiveram a natureza de rendimento preenchida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16144608760087)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33.

**Solução**  
1. Acessar módulo Configurador SIGACFG;

2. Base de dados > Dicionário > Base de dados;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145211441047)

3. Empresa teste > Dicionário de dados > Pesquisar > Digitar a tabela **DHR**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145013506199)

2. Selecionar a tabela DHR > Editar;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145007166359)  
3. Clica no nome da tabela > Campos > Pesquisar > Digitar o campo **DHR\_NATREN;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145064790551)

4. Selecionar o campo **DHR\_NATREN** > Editar;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145098464407)

5. Ir na aba Uso > Desmarcar a opção Obrigatório Usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16145130362903)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
