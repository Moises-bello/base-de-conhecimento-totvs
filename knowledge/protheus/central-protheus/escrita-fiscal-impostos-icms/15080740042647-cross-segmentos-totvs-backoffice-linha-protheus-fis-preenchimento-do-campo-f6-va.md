---
article_id: 15080740042647
category: Escrita Fiscal - Impostos - ICMS
content_hash: 841b21ee318fa57c12cb09277a6b665a0f6885d3ed9fa22412d83520e06ca228
fetched_at: '2026-06-28T22:39:24.239410+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Preenchimento do
  campo F6_VALFUND
type: support-article
updated_at: '2023-06-05T19:23:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15080740042647-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Preenchimento-do-campo-F6-VALFUND
---

**Dúvida**Em qual momento é preenchido o campo F6\_VALFUND

**Ambiente**A partir da versão Protheus 12.1.33

**Solução**O campo F6\_VALFUND será preenchido quando tiver FECP para o estado de destino onde:

MV\_SOMAGNR estiver com a UF de destino

Exemplo: MV\_SOMAGNR=RJ/MG/

MV\_GNRENF = .T. 

MV\_SUBTRIB e ou FISA097 não pode estar com Inscrição estadual de substituto tributário do estado de destino, onde devera ser tratado por operação a geração da SF6, ou seja por nota emitida.
