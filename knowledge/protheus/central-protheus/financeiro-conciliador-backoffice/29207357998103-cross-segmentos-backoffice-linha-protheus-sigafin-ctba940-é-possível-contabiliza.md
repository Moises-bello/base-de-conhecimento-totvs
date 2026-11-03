---
article_id: 29207357998103
category: Financeiro - Conciliador Backoffice
content_hash: 2650d8b17b2d6f35ca11028e680c0f3d4c2054d7d9bc7d5b7c8bee48d6223f3b
fetched_at: '2026-06-28T22:37:47.196402+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - É possível
  contabilizar os processos 0023 e 0024
type: support-article
updated_at: '2025-03-19T19:14:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29207357998103-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-%C3%89-poss%C3%ADvel-contabilizar-os-processos-0023-e-0024
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29207357990935) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**É possível contabilizar os processos 0023 e 0024?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210  
  
  
**Solução**

Os procedimentos financeiros não contabilizam. A rotina **CTBA940**, nas opções **0023 conciliação automática e 0024 conciliação manual**, não efetua a contabilização. Da mesma forma que as rotinas **FINA380 e FINA473** não realizavam, elas apenas conciliam os movimentos, sendo o propósito da rotina.

As rotinas que geram cada movimentação são responsáveis por contabilizar o movimento, seja através do FINA080 (Baixas a pagar manuais) ou FINA100 (Movimentação bancária), por exemplo.

Conforme a documentação dos registros padrão do Financeiro, nunca tivemos registros padrão para as rotinas herdadas.

**Saiba mais**

[Lançamentos\_padrão\_financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
