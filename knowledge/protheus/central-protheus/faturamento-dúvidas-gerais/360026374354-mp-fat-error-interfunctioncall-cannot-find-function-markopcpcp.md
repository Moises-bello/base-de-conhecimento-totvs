---
article_id: 360026374354
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3249a4b86c7e24d4e2fd052e8d0c6ac42165f2e62e5013ee0533372a4733a3cd
fetched_at: '2026-06-28T22:38:31.205081+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Error: InterFunctionCall: cannot find function MARKOPCPCP'
type: support-article
updated_at: '2021-04-28T15:54:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026374354-MP-FAT-Error-InterFunctionCall-cannot-find-function-MARKOPCPCP
---

**Ocorrência**

Ao inserir um pedido (**MATA410**) com opcionais está gerando o erro :

**InterFunctionCall: cannot find function MARKOPCPCP in AppMap on MARKOPC(SIGACUSB.PRX) 17/01/2019 16:29:23 line : 588**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **pcpxfun,** conforme a sua versão de ambiente:

**12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=762138> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=762137> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=762136> ;**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
