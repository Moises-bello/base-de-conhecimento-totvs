---
article_id: 360022895891
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e3a7e8c7f1d9b75fd7eeb4edd97e3b88f738f0946acb5cd8cc86a8891154c80a
fetched_at: '2026-06-28T22:38:31.245356+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-InterFunctionCall cannot find function A410CDBAR
type: support-article
updated_at: '2021-04-28T15:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022895891-MP-FAT-InterFunctionCall-cannot-find-function-A410CDBAR
---

**Ocorrência**

Ao incluir um pedido de venda (**mata410**), ocorre a mensagem: InterFunctionCall: cannot find function A410CDBAR in AppMap on {|| a410CdBar(lM410Bar, oGetD, nOpc)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020378512/mceclip0.png)

**Ambiente**

Microsiga Protheus - a partir da versão 12.

**Causa**

O erro ocorre, devido a função **A410CDBAR**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Efetue o download do **MATN410C** , rotina pai da função A410CDBAR, mais atual, conforme a release de sistema:

12.1.25: correção dentro do pacote de acumulados do módulo:[https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/**faturamento**\_expedicao\_continua](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/faturamento_expedicao_continua)

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=755343> ;

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=755342> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
