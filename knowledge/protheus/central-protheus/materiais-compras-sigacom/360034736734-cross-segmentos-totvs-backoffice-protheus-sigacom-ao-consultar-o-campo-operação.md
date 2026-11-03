---
article_id: 360034736734
category: Materiais - Compras (SIGACOM)
content_hash: f82a8ecf1cd948e55c675c1f789d6de7583f1bbc75cb2119ba4dd141fa607f19
fetched_at: '2026-06-28T22:41:14.127841+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao consultar o campo
  Operação (D1_OPER) no documento de entrada, o mesmo é apresentado vazio
type: support-article
updated_at: '2024-04-19T20:16:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034736734-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-consultar-o-campo-Opera%C3%A7%C3%A3o-D1-OPER-no-documento-de-entrada-o-mesmo-%C3%A9-apresentado-vazio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:01:28 min****Dúvida**

Ao consultar o campo Operação (D1\_OPER) no documento de entrada, o mesmo é apresentado vazio

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 11.80

**Solução**Esta situação ocorre devido ao campo ser Virtual.

Campos com contexto virtual não são persistidos no banco de dados. Seu contexto é apenas durante a execução das rotinas onde eles são apresentados. Por este motivo, ao visualizar um registro, o campo não apresenta valor. Esta é uma característica de campos virtuais.

***Saíba Mais :***

[Mais Artigos sobre Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
