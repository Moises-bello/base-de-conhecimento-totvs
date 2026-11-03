---
article_id: 360028079392
category: Escrita Fiscal - Error.log
content_hash: 237bbdb036b08eb82b102ff97233d1746b50ec1f6b48bc60820058bf071990ab
fetched_at: '2026-06-28T22:39:32.784202+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - array out of bounds
  ( 1 of 0 )  on MAFISRET(MATXFIS.PRX)
type: support-article
updated_at: '2021-07-08T12:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028079392-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-array-out-of-bounds-1-of-0-on-MAFISRET-MATXFIS-PRX
---

**Ocorrência**

Ao gerar o relatório MATR940 ocorre o error log:

"array out of bounds ( 1 of 0 ) on MAFISRET(MATXFIS.PRX) 25/10/2018 15:23:00 line : 2030"  
  
**Ambiente**

Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Causa**

Normalmente este erro ocorre quando o sistema encontra divergências nas tabelas

(Banco de Dados).

Um documento lançado, é composto por 04 tabelas, sendo elas:

\* NF Entrada:

SD1 (Itens Docto Entrada)

SF1 (Cabeçalho Docto Entrada)

SFT (Itens do Livro Fiscal)

SF3 (Cabeçalho do Livro Fiscal)

ou

\*  NF Saída:

SD2 (Itens Docto Saída)

SF2(Cabeçalho Docto Saída)

SFT (Itens do Livro Fiscal)

SF3 (Cabeçalho do Livro Fiscal)

No Errorlog é identificado que somente é encontrado na SD1 o campo D1\_DOC(C) :"Ex" 000095479). Sendo assim, é necessário verificar se a SF1 deste documento existe, caso não encontre, esta é a divergência que ocorre o erro, é possível que ocorra a inversão dessas tabelas.

**Solução**

Para correção, a linha na SF1 deve ser recuperada (Caso ainda existente) ou a linha deste documento deve ser deletada da SD1, poderá ocorrer a inversão dessas tabelas.
