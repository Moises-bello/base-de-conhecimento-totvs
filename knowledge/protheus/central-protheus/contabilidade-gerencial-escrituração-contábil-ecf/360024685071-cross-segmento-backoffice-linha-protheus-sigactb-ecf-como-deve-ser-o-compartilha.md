---
article_id: 360024685071
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 2dfbf0c65b93abf2dc0c04b49437c9677bc7cd05eec7e7ece6f9750137865198
fetched_at: '2026-06-28T22:40:47.714475+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF  COMO DEVE SER O
  COMPARTILHAMENTO DO PLANO DE CONTAS NO TAF ?
type: support-article
updated_at: '2022-04-22T12:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024685071-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-COMO-DEVE-SER-O-COMPARTILHAMENTO-DO-PLANO-DE-CONTAS-NO-TAF
---

**Dúvida**

COMO DEVE SER O COMPARTILHAMENTO DO PLANO DE CONTAS NO TAF PARA ATENDER O ECF?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12  
  
  
**Solução**

É necessário que as tabelas do TAF:

C1O – Plano de conta

CH5 – Plano de contas referencial

Tenham o mesmo compartilhamento das respectivas tabelas do SIGACTB:

CT1 Plano de contas

CVD – Amarração Plano de contas com o Referencial

CVN Plano referencial

Veja mais :[Como devo utilizar o compartilhamento de tabelas do TAF? (Tabelas autocontidas não devem ter seucompartilhamento alterado)](http://tdn.totvs.com/pages/releaseview.action?pageId=342301375)

Exemplo tabela abaixo não devem ter o seu compartilhamento alterado  pois são autocontidas

C2R - Natureza das contas

CHA - Código de Conta Referencial
