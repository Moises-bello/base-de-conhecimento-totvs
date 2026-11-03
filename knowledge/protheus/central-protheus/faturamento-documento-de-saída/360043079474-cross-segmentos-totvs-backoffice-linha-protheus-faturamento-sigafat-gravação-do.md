---
article_id: 360043079474
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6ef5f16b0b93e661d4838d3fa80f3a4da33dfe04bcb34d9790c4a93eee03227b
fetched_at: '2026-06-28T22:38:44.183139+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Gravação do número da nota no título '
type: support-article
updated_at: '2022-09-20T17:28:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043079474-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Grava%C3%A7%C3%A3o-do-n%C3%BAmero-da-nota-no-t%C3%ADtulo
---

**Dúvida**

Onde é gravado a numeração da nota no titulo contas a receber?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões  
  
**Solução**

O sistema grava o campo **E1\_NUM** (Número do Título)  de acordo com a numeração da nota gerada no documento de saída, o sistema utiliza a numeração do campo **F2\_DOC** (Número do documento de saída). A série da nota é gravado no campo **E1\_SERIE**.

**OBS:** O campo **E1\_NUMNOTA** (Número da nota fiscal) é gravado quando o faturamento é gerado através dos módulo Loja, Veículos, Oficina.
