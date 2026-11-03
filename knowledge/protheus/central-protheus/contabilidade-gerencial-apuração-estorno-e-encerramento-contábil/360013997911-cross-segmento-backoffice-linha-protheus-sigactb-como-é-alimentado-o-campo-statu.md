---
article_id: 360013997911
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 928763bf6ee87cd98d042f3b4830258e7ac6999f76f39324e557936054bf2548
fetched_at: '2026-06-28T22:41:05.031097+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como é alimentado o
  campo STATUS das tabelas de saldo?
type: support-article
updated_at: '2025-01-22T21:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013997911-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-%C3%A9-alimentado-o-campo-STATUS-das-tabelas-de-saldo
---

**Dúvida**Como é alimentado o campo STATUS das tabelas de saldo?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.8

**Solução**

As tabelas de saldo **"CQ0", "CQ1", "CQ2", "CQ3", "CQ4", "CQ5", "CQ6", "CQ7" e "CTC"** atualizam a flag de seus arquivos de saldos por meio do campo **STATUS**.

**Exemplo:**

* Campo **CQ0\_STATUS**

Este **STATUS** é gerado automaticamente pela rotina **Encerramento do Exercício (CTBA400)**.

Quando o campo **CTG\_STATUS** da tabela **CTG** (Tabela de Calendário Contábil) é alterado de **Aberto** para **Fechado**, essa atualização também é replicada automaticamente nas demais tabelas mencionadas.
