---
article_id: 360019319832
category: ADVPL - Classe e Função
content_hash: 9ee09fa3c3a5469b8ee6dc413ff6fc70c9ce405155f622bc1a0efe3d737e09b4
fetched_at: '2026-06-28T22:40:14.207705+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Reference counter
  overflow ( over 32700)
type: support-article
updated_at: '2022-02-21T17:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019319832-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Reference-counter-overflow-over-32700
---

**Ocorrência***Reference counter overflow* ( *over* 32700 ) on **CodeBlock**  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Causa**Utilização de programas **AdvPL** que armazenam e referenciam blocos de código.

Caso um determinado bloco de código, durante sua existência, fosse atribuído mais de 32767 vezes a outras variáveis ou elementos de array, a execução da aplicação era encerrada com a ocorrência de erro fatal **"assert failed on codeblock.cpp"**, precedida por uma ocorrência **"Reference counter overflow ( over 32700 ) on tLocalEnv::IncRefs()"**. Após reproduzida tal ocorrência, o servidor de aplicação tornava-se instável, e poderia apresentar Access Violation seguido de queda do serviço.  
  
**Solução**Uma ocorrência desta natureza não pode derrubar o servidor, e deve gerar uma mensagem de erro que aponte com maior clareza a natureza da ocorrência. Foi realizada uma proteção no Application Server, para que a aplicação AdvPL seja encerrada com a ocorrência de erro **"Reference counter overflow ( over 32600 ) on CodeBlock assignment"**caso este limite seja atingido, e não provoque *Access Violation* no Protheus Server após a finalização do processo.

**Saiba mais:  
[Melhoria - Proteções e limites do AdvPL](http://tdn.totvs.com/pages/viewpage.action?pageId=6065231)**
