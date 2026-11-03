---
article_id: 115004163268
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 72a698d3855f34cc106b7170764c52a588fc7a40d61b9a8dcdbc188d1be32175
fetched_at: '2026-06-28T22:38:28.578752+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A240VALI
type: support-article
updated_at: '2023-04-20T13:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004163268-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A240VALI
---

**Dúvida**

Ao incluir ou  liberar um pedido de vendas, liberar estoque ou faturar o pedido, o sistema está gerando o **Help: A240VALI.**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Após atualização dos últimos Updates de programas, constatamos que os produtos que possuem controle de rastreabilidade por Lote e/ou Sublotes não estavam respeitando os vencimentos dos lotes e/ou sublotes no processo de inclusão, liberação de pedido, liberação de estoque ou faturamento de pedidos de vendas.

Para corrigir efetue a baixa dos pacotes de expedição contínua dos módulos de Faturamento e Estoque e atualize: o ambiente:

**Expedição contínua Faturamento**: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**

**Expedição contínua Estoque: [SIGAEST](https://tdn.totvs.com/pages/viewpage.action?pageId=522000602)**

***Obs**.Toda atualização deve ser efetuada primeiro em ambiente de homologação para validar e posteriormente, atualize o ambiente de produção.*
