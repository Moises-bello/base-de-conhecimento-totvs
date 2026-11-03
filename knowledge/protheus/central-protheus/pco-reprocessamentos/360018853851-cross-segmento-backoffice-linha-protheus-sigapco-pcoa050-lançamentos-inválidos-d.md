---
article_id: 360018853851
category: PCO - Reprocessamentos
content_hash: 2f598f6bf142008d9188f70a0875c503c254e1f10dfb4e0c85b163166ad3253f
fetched_at: '2026-06-28T22:37:06.982461+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA050 Lançamentos
  inválidos do lote no reprocessamento. '
type: support-article
updated_at: '2023-11-21T14:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018853851-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA050-Lan%C3%A7amentos-inv%C3%A1lidos-do-lote-no-reprocessamento
---

**Dúvida**Lançamentos inválidos do lote no reprocessamento.   
   
 **Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

Quando rodar o reprocessamento de lançamentos do PCO e gerar lançamentos inválidos do lote , fazer uma análise preliminar sobre o status dos campos abaixo:

CTT\_BLOQ- CENTRO DE CUSTO; CTD\_BLOQ-ITEM CONTABIL; CTH\_BLOQ-CLASSE DE VALOR; AK5\_MSBLQ-CONTA ORÇAMENTARIA;

Verificando se estes cadastros estão bloqueados.
