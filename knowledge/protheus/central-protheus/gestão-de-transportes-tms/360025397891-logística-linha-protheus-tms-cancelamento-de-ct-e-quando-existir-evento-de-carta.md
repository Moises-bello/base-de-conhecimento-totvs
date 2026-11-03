---
article_id: 360025397891
category: Gestão de Transportes (TMS)
content_hash: 7dc7bf6234e7f1993adb3b9185125710ad6ba8af5e0215ae9caa76d2b45a4e38
fetched_at: '2026-06-28T22:45:27.389662+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cancelamento de CT-e quando existir evento
  de Carta de Correção
type: support-article
updated_at: '2025-03-28T18:42:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025397891-Log%C3%ADstica-Linha-Protheus-TMS-Cancelamento-de-CT-e-quando-existir-evento-de-Carta-de-Corre%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31003281161879)** Tempo aproximado para leitura: **00:00:50 min****Dúvida**É possível cancelar um **CT-e - Conhecimento de Transporte eletrônico** com evento de **Carta de Correção** vinculado?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Não é possível cancelar um **CTe** que possua evento de **Carta de Correção** vinculado. Ao estornar o cálculo do documento, o Sistema possui a validação **TMSA20053** **- CTe possui carta de correção, não será possível estornar o calculo** caso o **CTe** possua evento de **Carta de Correção** vinculado a ele.   
  
Essa validação no Sistema existe para impedir que o cancelamento seja rejeitado pela **SEFAZ** **- Secretaria da Fazenda** com a **Rejeição 523 - Vedado cancelamento quando existir evento Carta de Correção.**
