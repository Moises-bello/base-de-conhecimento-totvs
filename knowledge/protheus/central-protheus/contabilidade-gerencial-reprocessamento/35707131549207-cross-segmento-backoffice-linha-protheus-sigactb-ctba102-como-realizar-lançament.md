---
article_id: 35707131549207
category: Contabilidade Gerencial - Reprocessamento
content_hash: 64d831062a3a54f1c4c27a0c3d848eab4f5c375947ef368d3bc57314386192ad
fetched_at: '2026-06-28T22:40:41.975410+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como realizar
  lançamento de transferência de saldos das entidades contábeis.
type: support-article
updated_at: '2026-06-26T01:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707131549207-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-realizar-lan%C3%A7amento-de-transfer%C3%AAncia-de-saldos-das-entidades-cont%C3%A1beis
---

**Dúvida**  
Como realizar a transferência de saldos de uma entidade contábil para outra.

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - Todas Versões

**Solução:**

Não existe uma rotina ou processo automático para realizar a transferência de saldos diretamente entre as entidades contábeis no sistema.

Para a transferência manual de saldos entre entidades contábeis, siga o procedimento de inclusão de lançamentos manuais na rotina **CTBA102 - Lançamentos Contábeis Automáticos**:

* Acesse a rotina **CTBA102**.
* Realize o lançamento manual de transferência (débito em uma entidade/crédito em outra, ou vice-versa).

Documentações referente a inclusão de lançamentos manuais:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como efetuar um Lançamento de Partida dobrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053273953-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-efetuar-um-Lan%C3%A7amento-de-Partida-dobrada)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como efetuar um Lançamento de Partida Simples](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020712551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-efetuar-um-Lan%C3%A7amento-de-Partida-Simples)

**Observação Importante**: Por ser um conceito contábil, a empresa deve verificar junto ao seu contador se este procedimento atende às suas necessidades.

**Procedimento Específico para ECD (Bloco I157)**

Para lançamentos de transferência que visam a geração do **Bloco I157** (Transferência de Saldos de Planos de Contas Anterior) na ECD, é necessário seguir o processo específico para vinculação na rotina CTBA102, conforme documentação dedicada, que detalha o relacionamento da "transferência de saldos" no lançamento.

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102 - Como gerar o registro I157 da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD)

**Saiba mais:**  
[**Lançamento Contábil Automático (CTBA102 - SIGACTB)**](https://tdn.totvs.com/pages/viewpage.action?pageId=342313859)
