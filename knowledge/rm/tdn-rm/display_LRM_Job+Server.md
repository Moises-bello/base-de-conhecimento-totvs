---
content_hash: e9912da79593a6f6eb43a7c3d66423a38209ca18dac39d95a37864a68a48ef6b
fetched_at: '2026-06-29T00:11:02.523436+00:00'
page_id: '61931720'
product: rm
source: tdn-rm
title: Job Server
type: documentation
url: https://tdn.totvs.com/display/LRM/Job+Server
version: 4
---

**Introdução**

A execução de processos na linha RM foi modificada estruturalmente para trazer benefícios e possibilidades ao processamento das tarefas e processos. Isso foi possível graças à mudança da arquitetura de Win32 para .Net.

Conceitualmente, os Jobs são os processos na linha RM, e cada um possui informações únicas que vão desde a data da execução do Job, até a estação e o usuário que o executou. O Job é criado no momento da execução de um processo, e é registrado no Gerenciador de Jobs, que será detalhado adiante.

As informações sobre os processos estão mais ricas de informação e detalhamento, além de se tornar mais prático e confiável o gerenciamento das tarefas no sistema.

Além disso, os Jobs são executados pelo JobServer, que é o mecanismo de execução dos processos. O avanço no uso do JobServer vem da possibilidade de utilizar a Arquitetura 3 Camadas, onde funcionalidades da linha RM, bancos de dados e estações de trabalho cliente trabalham fisicamente em separado, uma estação diferente para cada camada.

Você pode executar os Jobs de duas formas diferentes: **Execução Assíncrona**e **Agendamento de Processos**.

Para mais informações consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.JobServer.aspx).
