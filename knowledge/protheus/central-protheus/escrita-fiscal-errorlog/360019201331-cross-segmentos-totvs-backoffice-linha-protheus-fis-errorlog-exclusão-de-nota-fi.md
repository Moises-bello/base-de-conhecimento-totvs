---
article_id: 360019201331
category: Escrita Fiscal - Error.log
content_hash: 8561a6bd36d18424418ff1f7b4ff516957ae7cbf19216baa8b8ed725df0dbb9c
fetched_at: '2026-06-28T22:39:32.839080+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Error.log - exclusão
  de nota fiscal manual  " variable does not exist NHLDPRV on A920GRAVA(MATA920.PRW)
  ".
type: support-article
updated_at: '2021-07-08T13:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019201331-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Error-log-exclus%C3%A3o-de-nota-fiscal-manual-variable-does-not-exist-NHLDPRV-on-A920GRAVA-MATA920-PRW
---

**Ocorrência**Ao tentar excluir uma nota fiscal manual gerar error.log " variable does not exist NHLDPRV on A920GRAVA(MATA920.PRW) ".  
  
**Ambiente**  
Protheus – Livro fiscal – A partir da versão 12.1.17  
  
**Causa**Rotina desatualizada.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
Aplicar patch : P12117: <https://suporte.totvs.com/portal/p/10098/download?e=697953>

PS : Aplicar primeiramente em base de HOMOLOGAÇÃO.
