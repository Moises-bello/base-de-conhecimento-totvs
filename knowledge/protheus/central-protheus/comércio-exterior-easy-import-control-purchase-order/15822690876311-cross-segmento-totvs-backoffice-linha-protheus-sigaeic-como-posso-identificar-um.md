---
article_id: 15822690876311
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: ed77a441c10d4b2eeedf38392ffe6adb08fb5ad79a96a13a4b78c9e0bbe5fa2c
fetched_at: '2026-06-28T22:39:41.242272+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como posso identificar
  uma Purchase Order em aberto no sistema?
type: support-article
updated_at: '2023-07-14T20:27:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15822690876311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-posso-identificar-uma-Purchase-Order-em-aberto-no-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15822737287319) Tempo aproximado para leitura: **02:00 min** **Dúvida**Como posso identificar uma Purchase Order em aberto (ainda com saldo) no sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – Todas versões  
  
**Solução**Neste caso, sugerimos verificar a Tabela "**SW5**", campo "**W5\_SALDO\_Q**". Ao incluir a Purchase Order, automaticamente são gravadas as tabelas "**SW4**" e "**SW5**" e quando não existir Embarque para o produto, o campo "**W5\_SALDO\_Q**" ficará  com o saldo disponível.

![Gravar_2023_07_14_17_20_19_815](https://centraldeatendimento.totvs.com/hc/article_attachments/16037391834007)
