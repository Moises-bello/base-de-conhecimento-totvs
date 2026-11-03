---
article_id: 360041898933
category: Materiais - Compras (SIGACOM)
content_hash: 613f831fbec714d3e6f0ac7183533b158f7a3ab0857ec4b7b398bf8876e9dca4
fetched_at: '2026-06-28T22:41:24.172578+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são as opções
  do campo CR_STATUS ?
type: support-article
updated_at: '2024-02-16T14:33:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041898933-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-as-op%C3%A7%C3%B5es-do-campo-CR-STATUS
---

**Dúvida**Quais são as opções do campo CR\_STATUS ?

**Ambiente**Protheus - Compras - Todas as versões  
  
**Solução**

CR\_STATUS='01' - Pendente em níveis anteriores

CR\_STATUS='02' - Pendente

CR\_STATUS='03' - Aprovado

CR\_STATUS='04' - Bloqueado

CR\_STATUS='05' - Aprovado/rejeitado pelo nível

CR\_STATUS='06' - Rejeitado

CR\_STATUS='07' - Documento Rejeitado ou Bloqueado por outro usuário.

Obs: Em paralelo temos a tabela DBM, que controla os saldos dos aprovadores. Quando um aprovador libera o documento de alçada, na tabela DBM o campo DBM\_APROV é preenchido com o valor 1 e o saldo do aprovador é descontado.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
