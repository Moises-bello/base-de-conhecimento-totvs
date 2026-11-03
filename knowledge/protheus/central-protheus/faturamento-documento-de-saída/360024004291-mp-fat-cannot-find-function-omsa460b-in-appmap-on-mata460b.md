---
article_id: 360024004291
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7951109ee6d806a2f3691d93889e90a0e3f0e80b96ceb61da1a2bac470ecf90f
fetched_at: '2026-06-28T22:38:45.213870+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT-Cannot find function OMSA460B in AppMap on MATA460B
type: support-article
updated_at: '2021-04-28T15:13:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024004291-MP-FAT-Cannot-find-function-OMSA460B-in-AppMap-on-MATA460B
---

**Ocorrência**

Cannot find function OMSA460B in AppMap on MATA460B  
  
**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

Ao entrar na rotina de geração de documento de saída, ocorre o erro: **cannot find function OMSA460B in AppMap on MATA460B(MATA461.PRX) 10/01/2019 07:57:05 line : 7983,** o erro ocorre devido a função **OMSA460B** não ter sido encontrada no RPO.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote atualizado da rotina **OMSA460B.PRX, conforme o release:**

**12.1.27:<https://r.totvs.io/p/975886> ; 12.1.25:<https://r.totvs.io/p/975885> ; 12.1.23:<https://r.totvs.io/p/975884> ; 12.1.17:<https://r.totvs.io/p/975883>  (garantia estendida);**

**12.1.17- <https://suporte.totvs.com/portal/p/10098/download?e=724282>****(sem garantia estendida)**

2. Aplique o pacote via TDS ou VS-CODE para atualização do RPO;

3. Reinicie o Smartclient  e refaça o processo de geração do documento de saída.

**Obs: Para aplicação do pacote é necessário que o analista tenha conhecimentos em estrutura Protheus, em caso de dúvidas no processe, acione a equipe de atendimento de Frame Work.**

**Sempre efetue a aplicação do pacote em ambiente de homologação para validar a atualização, e posteriormente aplique em ambiente de produção.**
