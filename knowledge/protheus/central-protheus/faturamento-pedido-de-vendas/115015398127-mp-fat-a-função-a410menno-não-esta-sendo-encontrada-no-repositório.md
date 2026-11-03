---
article_id: 115015398127
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 35dc2d1e9e2d3295da65eb3f69cba5e577184ddf30cd983c39c836770a026ad1
fetched_at: '2026-06-28T22:38:41.263030+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'MP- FAT - A função A410MENNO não esta sendo encontrada no repositório '
type: support-article
updated_at: '2021-04-28T15:51:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015398127-MP-FAT-A-fun%C3%A7%C3%A3o-A410MENNO-n%C3%A3o-esta-sendo-encontrada-no-reposit%C3%B3rio
---

**Ocorrência**   
  
A função **A410MENNO** não esta sendo encontrada no repositório .

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

  
**Causa**

O erro **InterFunctionCall: cannot find function A410MENNO in AppMap** ocorre por que a função A410MENNO não se encontra no RPO ou a fonte pai da rotina MATN410A não está atualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **matn410a:**

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=750735> ;

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=750734> ;

2. Aplique o pacote, via TDS ou antigo IDE, em seu ambiente de testes para validação e posteriormente, no ambiente de produção.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
