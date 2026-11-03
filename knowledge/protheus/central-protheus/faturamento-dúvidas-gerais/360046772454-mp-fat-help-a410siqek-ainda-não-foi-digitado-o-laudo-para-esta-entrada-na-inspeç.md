---
article_id: 360046772454
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e948074ad52881e02f31cad48de7ed03dab0aa6519f5f59ec5e7561f99bcd6df
fetched_at: '2026-06-28T22:38:33.123272+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - HELP A410SIQEK - Ainda não foi digitado o laudo para esta entrada
  na Inspeção de Entrada.
type: support-article
updated_at: '2021-07-05T17:38:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046772454-MP-FAT-HELP-A410SIQEK-Ainda-n%C3%A3o-foi-digitado-o-laudo-para-esta-entrada-na-Inspe%C3%A7%C3%A3o-de-Entrada
---

**Dúvida**Por que o sistema apresenta o help A410SIQEK no pedido de vendas?  
  
**Ambiente**Microsiga Protheus – Faturamento – A partir da versão 12  
  
**Solução**O help **A410SIQEK** - Ainda **não foi digitado** o **laudo** para esta **entrada** na **Inspeção** de **Entrada** ocorre quando existe **integração** entre os módulos **Faturamento** x **Compras** x **Quality**.

O sistema verifica se, na **devolução** da nota de entrada, a **Nota** **Original** ainda não foi **liberada** do **Controle** de **Qualidade**.

Para isso, verifica a nota de entrada na rotina **Inspeção de Entrada** (Tabela **QEK**) e se a **Situação** da **Entrada** (**QEK\_SITENT**) for igual a "1" (**Laudo Pendente**) ou não tiver preenchimento, o sistema apresenta o Help A410SIQEK na devolução, até que seja informado o **Laudo** na **Inspeção** de **entrada**.
