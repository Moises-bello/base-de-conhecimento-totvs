---
article_id: 360026037973
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 99c17c36cd8af67e2fbc682ca6aa713f7bd9be1aeb2ddd0a9437bb9a6b2be52d
fetched_at: '2026-06-28T22:38:30.074061+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos -TOTVS Backoffice (Linha Protheus)-SIGAFAT-Processo de Cancelamento
  via Totvs Colaboração 2.0
type: support-article
updated_at: '2022-08-16T15:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026037973-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Processo-de-Cancelamento-via-Totvs-Colabora%C3%A7%C3%A3o-2-0
---

**Dúvida**

Como efetuar a configuração do Fatjobnfe com Totvs colaboração no cancelamento da Nota fiscal de saída (**MATA521**)?  
  
**Ambiente**

Cross Segmentos -TOTVS Backoffice (Linha Protheus)-SIGAFAT- a partir da release 12.1.17.

**Solução**

Implementado o processo de exclusão de documento de saída onde é utilizado a ferramenta NeoGrid (Totvs Colaboração 2.0) no momento que a NFe - Nota Fiscal Eletrônica retornar com autorização de cancelamento por parte da SEFAZ.  
Quanto ao processo de exclusão, após o retorno do cancelamento da nota fiscal eletrônica que não utiliza a ferramenta da NeoGrid, o processo permanece inalterado.

Para implementação, siga os passos do documento técnico  do desenvolvimento de produto:**[Processo de cancelamento de NFe (Nota Fiscal Eletrônica) via Totvs Colaboração 2.0](http://tdn.totvs.com/pages/releaseview.action?pageId=329032026)**
