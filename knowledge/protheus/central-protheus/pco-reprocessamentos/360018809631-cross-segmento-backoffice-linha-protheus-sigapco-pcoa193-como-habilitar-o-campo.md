---
article_id: 360018809631
category: PCO - Reprocessamentos
content_hash: b43a250631e947d5f352b1a1153b040aa1636aeb4cde287ff17573ae56f4328e
fetched_at: '2026-06-28T22:37:07.010834+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA193 Como Habilitar
  o campo AL1_TPATU para funcionar via JOB?
type: support-article
updated_at: '2023-11-21T14:13:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018809631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA193-Como-Habilitar-o-campo-AL1-TPATU-para-funcionar-via-JOB
---

**Dúvida**Como Habilitar o campo AL1\_TPATU para funcionar via JOB?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Criar os parâmetros abaixo

Nome da Var: MV\_PCOJOB1  
Tipo: Numérico  
Descrição: intervalos em segundos para processar a fila

Nome da Var: MV\_PCOJOB2  
Tipo: Numérico  
Descrição: numero de dias para processar a fila
