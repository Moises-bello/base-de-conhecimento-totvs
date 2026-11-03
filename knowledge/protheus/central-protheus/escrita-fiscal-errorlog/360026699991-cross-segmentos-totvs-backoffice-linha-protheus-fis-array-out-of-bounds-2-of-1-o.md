---
article_id: 360026699991
category: Escrita Fiscal - Error.log
content_hash: 92ed1828a6d64490af2cda32cc9ab2b9c18b5b2d1b6a10363e87f8e7f1700733
fetched_at: '2026-06-28T22:39:32.788508+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - array out of bounds
  ( 2 of 1 ) on REPORTPRINT(MATR945.PRX)
type: support-article
updated_at: '2021-07-08T13:23:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026699991-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-array-out-of-bounds-2-of-1-on-REPORTPRINT-MATR945-PRX
---

**Ocorrência**

Ao gerar o relatório da contribuição seguridade social (MATR945) está ocorrendo os seguintes error logs :

"array out of bounds ( 2 of 1 ) on REPORTPRINT(MATR945.PRX) 14/08/2018 17:25:00 line : 400"  
  
**Ambiente**

Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Causa**

No FUNRURAL existe um parâmetro MV\_CONTSOC que precisa ser alimento com três alíquotas (informe o percentual a ser calculado a Contribuição de Seguridade Social "Pessoa Física:=2.2,Seg.Especial 2.3,Juridica:= 2.7"), mas ao preencher com um ou duas alíquotas apenas vai gerar ao error.log ao gerar o relatório da contribuição seguridade social (MATR945).

**Solução**Preencha as três alíquotas no parâmetro MV\_CONTSOC :

  1.1. Pessoa Física.

  1.2. Seg.Especial.

  1.3. Jurídica.

Revise as notas que foram emitidas com a alíquota errada.

Gere o relatório da contribuição seguridade social (MATR945).
