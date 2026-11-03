---
article_id: 360046845054
category: Call Center - Telecobrança
content_hash: e13aec1c477c6b3758289dfcf5c8ce007ede01a2edf0b6c39fca29f1a9bcb6bf
fetched_at: '2026-06-28T22:41:28.590667+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGATMK - Help: Este título não pode
  ser excluído pois se encontra em cobrança'
type: support-article
updated_at: '2024-04-25T13:02:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046845054-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Help-Este-t%C3%ADtulo-n%C3%A3o-pode-ser-exclu%C3%ADdo-pois-se-encontra-em-cobran%C3%A7a
---

**Ocorrência**

Ocorre o help ao cancelar título da liquidação.

Help: Este título não pode ser excluído pois se encontra em cobrança  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Causa**

O help ocorre por que o título gerado na liquidação está na rotina Seleção de Título TMKA180 para cobrança.

**Solução**

Passos para cancelar a liquidação:

1 - Acesse a rotina Seleção de Título **TMKA180**em outras ações-> Exceção, selecione título, marque a opção **"Bloqueia e Libera os Títulos**', e confirme.

2 - Acesse a rotina Contas a Receber **FINA740** e posicione no título gerado para liquidação e cancele a liquidação.
