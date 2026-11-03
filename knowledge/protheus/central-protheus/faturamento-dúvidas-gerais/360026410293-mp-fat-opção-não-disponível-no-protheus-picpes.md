---
article_id: 360026410293
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c885a4dd8c29251789244d0671bac969d68fb1cd2e45be9d97bceb55c40372b2
fetched_at: '2026-06-28T22:38:31.318848+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Opção não disponível no Protheus - PicPES
type: support-article
updated_at: '2021-04-28T15:54:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026410293-MP-FAT-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-PicPES
---

**Ocorrência**Ao acessar cadastro do cliente (**MATA030**) > outras ações > posição do cliente (**FINC010**) apresenta o seguinte erro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041735253/mceclip0.png)  
 **Ambiente**

Microsiga Protheus - versão 12.  
   
 **Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **sigavld.prx****: <https://suporte.totvs.com/portal/p/10098/download?e=724337>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
