---
article_id: 360022703431
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 157a65e6e75a1560b4136b4737cca8e1e5ed439c1e4b4a8314a1be09b5b6fc88
fetched_at: '2026-06-28T22:38:31.324566+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Opção não disponível no Protheus Função SELEOPCPCP Called By SELEOPC
type: support-article
updated_at: '2021-04-28T15:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022703431-MP-FAT-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-SELEOPCPCP-Called-By-SELEOPC
---

**Ocorrência**

Ao alterar um pedido de venda, obtemos a mensagem em abaixo:

**Help: NOFUNCW**

**Problema: Opção não disponível no Protheus Função: SELEOPCPCP Called By SELEOPC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019982132/mceclip0.png)

**Ambiente**

Microsiga Protheus -  a partir da versão 12.1.17.  
  
**Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **pcpxfun** de acordo com a sua versão**:**

**12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=944923> ;**

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=944922> ;**

**12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=944921> (com garantia estendida);**

**12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=827781> (sem garantia estendida);**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.

Caso o ambiente seja Cloud Protheus, a equipe de suporte atuará com o atendimento de suporte integrado.
