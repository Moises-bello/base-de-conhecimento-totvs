---
article_id: 360022784291
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: cd7e90cfaaf173a5cf593ac55d6a79c9abd9b470329101bdd758e100be8b4798
fetched_at: '2026-06-28T22:40:32.404262+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - CTBA105 Como é composta a chave
  de rastreamento na tabela CV3.
type: support-article
updated_at: '2023-02-04T12:15:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022784291-Cross-Segmento-Backoffice-Linha-Protheus-CTBA105-Como-%C3%A9-composta-a-chave-de-rastreamento-na-tabela-CV3
---

**Dúvida**Como é composta a chave de rastreamento na contabilidade gerencial (CV3)?  
  
**Ambiente**Protheus – Contabilidade gerencial – A partir da versão 11.80  
  
  
**Solução:**

A tabela CV3- Rastreamento Contábil, tem sua funcionalidade e conceito focados somente para geração de registros de contabilizações realizadas via integração, ou seja, contabilizações provenientes de outros módulos/processos (Contas a Pagar, Faturamento, Compras, etc) e somente gera o rastreio contábil referente a moeda origem(01).

Exemplo: Lançamento contábil (rotina CTBA102) integração lançamento padrão 801, origem  módulo SIGAATF.

Na CV3 campo CV3\_RECDES é gravado o recno da CT2 e no campo CV3\_RECORI é gravado o recno da SN4.

No campo CV3\_SEQUEN o mesmo conteúdo é replicado para o CT2\_SEQUEN.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020125452/mceclip0.png)

Importante! O append,das tabelas envolvidas, via APSDU perderá a rastreabilidade do recno.

Todo procedimento de backup e restauração deve ser feito via banco, caso necessário.

Saiba mais:

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
