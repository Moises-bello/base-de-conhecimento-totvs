---
article_id: 360029076391
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 99a3534dcd8fc4b02069174c403bb9005b5701260d5fe640d2bfba1460968f1d
fetched_at: '2026-06-28T22:38:33.152875+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function GFEXINTCOD'
type: support-article
updated_at: '2021-04-28T15:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029076391-MP-FAT-InterFunctionCall-cannot-find-function-GFEXINTCOD
---

**Ocorrência**

Ao alterar a transportadora pela rotina **A512MANUT** (**MATA512**) temos o seguinte erro:

THREAD ERROR ([16956], noliveira, SOROCABA-IP095) 03/06/2019 10:09:20   
**InterFunctionCall: cannot find function GFEXINTCOD in AppMap on OMSM011COD(OMSM011.PRW) 09/03/2019 10:41:07 line : 2027**

**Ambiente**

Microsiga Protheus -  a partir da versão 12.

**Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado ou não existe no RPO.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **GFEXINTA:**

**<https://suporte.totvs.com/portal/p/10098/download?e=728490>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
