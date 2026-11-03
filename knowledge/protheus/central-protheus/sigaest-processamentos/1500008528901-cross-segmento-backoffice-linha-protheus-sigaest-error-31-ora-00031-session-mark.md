---
article_id: 1500008528901
category: SIGAEST - PROCESSAMENTOS
content_hash: ec0e829ef8fad7b0723364fa8649ff5e3a623bb8fa0af7960b0bd26380e4a86a
fetched_at: '2026-06-28T22:39:04.846806+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'Cross Segmento  - Backoffice (Linha Protheus) - SIGAEST - Error : 31 - ORA-00031:
  session marked for kill em rotinas de Processamento'
type: support-article
updated_at: '2021-11-15T13:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008528901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Error-31-ORA-00031-session-marked-for-kill-em-rotinas-de-Processamento
---

**Ocorrência**Ao executar rotinas de Processamento no Protheus, como Fechamento de Estoque (Virada de Saldos) - MATA280 - ocorre o seguinte erro no banco de dados Oracle:

"*Error : 31 - ORA-00031: session marked for kill: ORA-00028: your session has been killed*".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Causa**

Este erro ocorre no banco de dados Oracle, normalmente com as seguintes causas:

* Sessão eliminada manualmente por usuário de banco de dados privilegiado;
* Tempo limite do banco de dados (timed out);
* Deadlock no banco de dados (quando o mesmo, por segurança, bloqueia para não haver duas ou mais transações simultaneamente).
* Bug específico do Oracle no banco de dados;
* Firewall ou outro problema de rede.

**Solução**Para um melhor diagnóstico do que está causando este problema, a TOTVS recomenda que o usuário que esteja enfrentando este problema solicite o apoio da equipe de TI ou Administração do Banco de Dados (DBA) da empresa. Pois, se tratando de uma não conformidade do banco Oracle, basicamente por perder comunicação com os serviços do Protheus automaticamente o processamento não é concluído.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Roteiro para Fechamento de Estoque (virada de saldos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Roteiro-para-Fechamento-de-Estoque-virada-de-saldos-)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)*

[*Clique aqui e veja mais artigos sobre Fechamento de Estoque/Virada de Saldos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
