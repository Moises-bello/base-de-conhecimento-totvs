---
article_id: 1500001332202
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: aeccbe4eb5a360a9ae492f72e85157206501e2a6eea01cb79c9d3041fbbdf443
fetched_at: '2026-06-28T22:38:33.067584+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Inclusão de Campos no Cabeçalho da rotina Controle de Reservas (MATA430)
type: support-article
updated_at: '2022-12-30T18:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001332202-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Inclus%C3%A3o-de-Campos-no-Cabe%C3%A7alho-da-rotina-Controle-de-Reservas-MATA430
---

**Dúvida**Como incluir campos no cabeçalho da rotina **Controle de Reservas** (**MATA430**)?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12

**Solução**

É possível visualizar que a rotina **Controle de Reservas** (**MATA430**) possui o Cabeçalho e as linhas de Itens, porém possui apenas uma tabela (**SC0**).

Caso necessite inserir campos de usuário, eles serão sempre inseridos nas linhas de itens, pois os campos de cabeçalho estão pré-definidos no código fonte.

Para inserir campos de usuário no cabeçalho da Reserva, será necessário utilizar um ponto de entrada, como a rotina está em MVC é possível o uso dos pontos de entrada em MVC: <https://tdn.totvs.com/x/cBtrD>

**Saiba mais**: <https://tdn.totvs.com/x/P5AjDw>
