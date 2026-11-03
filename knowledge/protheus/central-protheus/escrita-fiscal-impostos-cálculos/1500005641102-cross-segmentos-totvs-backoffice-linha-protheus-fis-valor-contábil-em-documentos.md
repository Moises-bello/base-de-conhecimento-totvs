---
article_id: 1500005641102
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 158800c69c7029eb2cd2ccae07ce21d31b4121b322827763b6b5c37f8ab22640
fetched_at: '2026-06-28T22:39:30.629153+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Valor Contábil em
  documentos com valores zerados
type: support-article
updated_at: '2021-07-29T13:24:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005641102-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-Cont%C3%A1bil-em-documentos-com-valores-zerados
---

**Dúvida**Como escriturar valor Contábil em documentos que não possuem valor total, escriturados com campo **" Agrega Valor" (F4\_AGREG) = N**.  
  
**Ambiente**  
Microsiga Protheus – A partir da versão 11.80  
  
**Solução**O parâmetro **MV\_LFAGREG = .T. (*True/* Verdadeiro)** indica se deve ser feita a escrituração, mesmo não agregando valor ao total da nota. Ao habilitá-lo como =**.T. (*True/* Verdadeiro)** as informações são geradas.
