---
article_id: 360034106793
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cb36a69a20548266a67aac70715b9b0d9a7a7daf565089cdfaa9e3bd1bb40542
fetched_at: '2026-06-28T22:38:31.254018+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function A430AUTO in AppMap on FATLOAD(FATXFUN.PRX)'
type: support-article
updated_at: '2021-04-28T15:54:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034106793-MP-FAT-InterFunctionCall-cannot-find-function-A430AUTO-in-AppMap-on-FATLOAD-FATXFUN-PRX
---

**Ocorrência**

Ao tentar logar no faturamento, gera o erro:

**InterFunctionCall: cannot find function A430AUTO in AppMap on FATLOAD(FATXFUN.PRX) 08/03/2018 16:27:54 line : 8623**  
   
 **Ambiente**

Microsiga Protheus -  a partir da release 12.1.17.

**Causa**

Indica que a função não foi encontrada no RPO, isso ocorre quando o fonte pai onde a função foi criada está desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **sigacusb**de acordo com a sua versão**:**

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=758206> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=758205> ;**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
