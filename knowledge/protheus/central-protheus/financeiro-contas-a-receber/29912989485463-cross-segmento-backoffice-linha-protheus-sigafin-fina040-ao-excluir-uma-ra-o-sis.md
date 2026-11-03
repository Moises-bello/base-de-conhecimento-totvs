---
article_id: 29912989485463
category: Financeiro - Contas a Receber
content_hash: 43df363d48f6eaec63ad6ad6f123605e5600d3467fd0a31d58964a8ed23df6ae
fetched_at: '2026-06-28T22:38:12.496783+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA040 - Ao excluir
  uma RA, o sistema estorna automaticamente o movimento bancário
type: support-article
updated_at: '2025-02-11T20:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29912989485463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Ao-excluir-uma-RA-o-sistema-estorna-automaticamente-o-movimento-banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29912964117527) Tempo aproximado para leitura: **00:05 min****Dúvida**O sistema gera automaticamente um movimento de saída ao excluir a **RA.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA040 - Todas as versões  
  
**Solução**Quando um **RA** **"Recebimento Antecipado"** é criada, o sistema gera automaticamente um movimento bancário correspondente. Caso essa **RA** seja excluída, um movimento de saída é registrado para estornar o valor recebido.

Como o sistema impacta o extrato bancário em ambas as situações (entrada e saída), a exclusão de uma **RA** gera um lançamento contrário no extrato, garantindo que o valor não permaneça na conta.

Vale destacar que esse comportamento é padrão do sistema, pois é necessário registrar a baixa do valor recebido, mesmo em casos de erro. Dessa forma, sempre que uma **RA** for excluída, o sistema automaticamente gerará um movimento de saída correspondente.

Recomendamos que a exclusão ocorra no mesmo dia da criação para evitar inconsistências ou divergências no extrato bancário.

**Saiba mais**

[Contas a Receber - FINA040 - Financeiro - P12](https://tdn.totvs.com.br/display/public/PROT/Contas+a+Receber+-+FINA040+-+Financeiro+-+P12)
