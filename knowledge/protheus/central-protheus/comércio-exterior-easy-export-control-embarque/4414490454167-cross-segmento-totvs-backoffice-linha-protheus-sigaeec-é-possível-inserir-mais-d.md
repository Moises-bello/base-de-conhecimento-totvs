---
article_id: 4414490454167
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 2dbb8a95dd5545f1f0b12df0cc3c06ba1b5bb9f039520f581f63645557a816a6
fetched_at: '2026-06-28T22:36:39.167213+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - É possível inserir
  mais de um LPCO na tabela EE9 (campo EE9_LPCO)
type: support-article
updated_at: '2021-11-30T18:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414490454167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-%C3%89-poss%C3%ADvel-inserir-mais-de-um-LPCO-na-tabela-EE9-campo-EE9-LPCO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível inserir mais de um **LPCO** na tabela EE9 (campo **EE9\_LPCO**)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Alterado a rotina EECAE100 para considerar mais de um **LPCO** digitado no campo EE9\_LPCO sendo que separado por vírgula e dessa forma levar a informação para o XML da DUE a ser enviado de forma que para cada LPCO será gerado uma informação de documentação diferente.

Foram alterados nos campos referentes a **LPCO** na tabela **EE9** e na **EK2** os tamanhos padrão para 23 e liberado a alteração de tamanho para que seja possível informar um maior número de **LPCO** por item do embarque de exportação.  
  
**Saiba mais**[Múltiplos LPCO por item do Embarque de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=545635055)
