---
article_id: 34334822288535
category: Contabilidade Gerencial - Reprocessamento
content_hash: c559b6ae62743f1f744d542a80ea2e73124d85df9f708c9f1e773a63c7fa7363
fetched_at: '2026-06-28T22:40:41.959508+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Agendamento simultâneo
  das rotinas CTBA980 e CTBA193 no schedule
type: support-article
updated_at: '2025-08-21T13:11:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334822288535-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Agendamento-simult%C3%A2neo-das-rotinas-CTBA980-e-CTBA193-no-schedule
---

**Dúvida**  
Posso manter as rotinas CTBA980 e CTBA193 cadastradas simultaneamente no Schedule?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 12.1.2310

**VISÃO GERAL**

Sim, poderá manter o agendamento da **CTBA193** mesmo com a **CTBA980**configurada, pois as rotinas possuem propósitos distintos e complementares:

* A **CTBA193**é essencial para a **geração inicial** dos saldos, enquanto a **CTBA980**atua para ajustes pontuais.
* Desativar a **CTBA193**poderia levar a atrasos ou inconsistências, já que a **CTBA980**só intervém quando uma divergência é detectada.

**Rotina** [**CTBA193**](https://tdn.totvs.com/display/PROT/CTBA193+Gerenciador+de+Saldos+On-Line+-+P12)  
Destina-se ao processo de gravação de saldos contábeis. Esta rotina é acionada automaticamente após a geração de um lançamento, executando a fila de saldos por meio de um *job*e atualizando as tabelas de saldos correspondentes.  
   
**Rotina** [**CTBA980**](https://tdn.totvs.com/pages/releaseview.action?pageId=851295422)  
Utilizada exclusivamente para correção de saldos quando são identificadas divergências entre os valores registrados nos saldos e no movimento contábil.  
**Documentação relacionada:**

**Documentações Relacionadas:**

[Framework - Linha Protheus - Schedule: agendando a execução de rotinas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028340252-Framework-Linha-Protheus-Schedule-agendando-a-execu%C3%A7%C3%A3o-de-rotinas)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Fechamento Contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839/live_preview/01K354KXDG4JH69RJ8BM899K2D)  
[CTBA193 Gerenciador de Saldos On-Line - P12](https://tdn.totvs.com/display/PROT/CTBA193+Gerenciador+de+Saldos+On-Line+-+P12)  
[Monitor de Saldos On-line (SIGACTB)](https://tdn.totvs.com/pages/releaseview.action?pageId=852898157)
