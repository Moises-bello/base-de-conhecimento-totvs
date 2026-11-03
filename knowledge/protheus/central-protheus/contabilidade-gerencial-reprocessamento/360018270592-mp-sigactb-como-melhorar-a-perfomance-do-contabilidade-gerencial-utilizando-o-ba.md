---
article_id: 360018270592
category: Contabilidade Gerencial - Reprocessamento
content_hash: 757d16b76e1932771d948acbfb75df1171eacf6f3b40eafe4ffd270365f34644
fetched_at: '2026-06-28T22:40:42.031854+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: 'MP - SIGACTB: Como melhorar a perfomance do Contabilidade Gerencial utilizando
  o banco de dados Oracle?'
type: support-article
updated_at: '2021-04-28T15:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270592-MP-SIGACTB-Como-melhorar-a-perfomance-do-Contabilidade-Gerencial-utilizando-o-banco-de-dados-Oracle
---

**Dúvida**Como melhorar a perfomance do Contabilidade Gerencial utilizando o banco de dados Oracle?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

O processo a seguir realizado por meio do comando **ANALYZE TABLE** deve ser executado por todos os usuários do Protheus que utilizam o banco de dados Oracle, para atualização/otimização das estatísticas de acessos às tabelas envolvidas nos processos do módulo Contabilidade Gerencial.

* A  seqüência **NNN**  no nome da tabela deve ser substituída pelo número que corresponde a Empresa em processo. Por exemplo, se a empresa está identificada pelo número **01**, os nomes de arquivos serão **CT2010**, **CT3010**, e sucessivamente:

* ANALYZE TABLE CT2NNN
* ANALYZE TABLE CT3NNN
* ANALYZE TABLE CT4NNN
* ANALYZE TABLE CT6NNN
* ANALYZE TABLE CT7NNN
* ANALYZE TABLE CTCNNN
* ANALYZE TABLE CTINNN
* ANALYZE TABLE CTUNNN
* ANALYZE TABLE CTWNNN
* ANALYZE TABLE CTXNNN
* ANALYZE TABLE CTYNNN
* ANALYZE TABLE CTZNNN

**Importante**  
  
Este procedimento deve ser executado periodicamente, pois as tabelas de saldos do módulo CTB são constantemente manipuladas em grandes blocos pela rotina de **Reprocessamento (CTBA190)**.
