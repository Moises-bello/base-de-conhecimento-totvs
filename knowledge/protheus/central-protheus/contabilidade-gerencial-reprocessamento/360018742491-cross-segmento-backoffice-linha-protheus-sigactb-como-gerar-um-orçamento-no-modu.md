---
article_id: 360018742491
category: Contabilidade Gerencial - Reprocessamento
content_hash: e036639d96e1007ffb64a7abc59d8b783a588123a681b054dbc6fa2004912793
fetched_at: '2026-06-28T22:40:41.955762+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  COMO GERAR UM ORÇAMENTO
  NO MODULO CONTABIL
type: support-article
updated_at: '2024-04-17T11:54:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018742491-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-COMO-GERAR-UM-OR%C3%87AMENTO-NO-MODULO-CONTABIL
---

**Dúvida**COMO GERAR UM ORÇAMENTO NO MODULO CONTÁBIL?  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – A partir da versão 11.80.

**Solução**Rotina CTBA390 + Incluir

É criado uma revisão conforme pré cadastro de datas, contas e entidades.

Que alimenta a tabela CV1.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014198431/mceclip0.png)

Ainda na rotina CTBA390, Ações relacionadas + gerar saldo.

Os saldos alimentam as tabelas de saldos CQ0, CQ1..etc

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014197992/mceclip2.png)

Após a gerar os saldos, o saldo orçado ficará disponível para consultas nos relatórios.

Por exemplo: Comparativo Conta X Saldos CTBR350

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014198272/mceclip3.png)
