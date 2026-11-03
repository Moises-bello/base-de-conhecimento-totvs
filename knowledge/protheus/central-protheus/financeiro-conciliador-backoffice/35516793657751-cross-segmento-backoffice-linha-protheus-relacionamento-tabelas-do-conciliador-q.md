---
article_id: 35516793657751
category: Financeiro - Conciliador Backoffice
content_hash: 1efe64ceaa8662cd77e796d03085930e2cb83e8a1077a266f35a8a63bb85870d
fetched_at: '2026-06-28T22:37:47.034340+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Relacionamento tabelas do Conciliador
  QLD e QLC
type: support-article
updated_at: '2025-10-09T13:29:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35516793657751-Cross-Segmento-Backoffice-Linha-Protheus-Relacionamento-tabelas-do-Conciliador-QLD-e-QLC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35516808901911) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual o relacionamento das tabelas QLC e QLD com as tabelas do financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
**Solução**  
As tabelas **QLC** e **QLD** são utilizadas como tabelas de controle internas do processo de conciliação. Essas tabelas se relacionam com as tabelas **SIG** e **FK5** apenas por meio de campos específicos.

A tabela **QLC** mantém associação exclusivamente com a tabela **QLD**, vinculando-se por meio do **código da conciliação**.  
A tabela **QLD**, por sua vez, possui dois registros para cada conciliação — um correspondente à tabela **FK5** e outro à **SIG** —, sendo que cada um desses registros referencia o campo **\_MUIDT** no campo **FK5\_IDMOV**.

A tabela **SE5** não possui associação padrão com as novas tabelas; nela, apenas o campo **E5\_RECONC** é atualizado, de forma a indicar a relação com o movimento bancário correspondente.

**Saiba mais**

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Backoffice Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Financeiro)
