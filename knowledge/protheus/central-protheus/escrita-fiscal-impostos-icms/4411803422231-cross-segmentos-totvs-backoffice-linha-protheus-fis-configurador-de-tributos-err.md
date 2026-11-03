---
article_id: 4411803422231
category: Escrita Fiscal - Impostos - ICMS
content_hash: 358b07ba0298df36f9dd675dd121de09ac51ecc2f7b7a1ff8743428d9df6993e
fetched_at: '2026-06-28T22:39:25.615039+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configurador de Tributos
  - Error.log F23010: DB error (Insert): -37 File: F23010 - Error : 1 - ORA-00001:
  unique constraint (SIGA.F23010_UNQ) violated'
type: support-article
updated_at: '2021-10-29T21:06:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411803422231-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configurador-de-Tributos-Error-log-F23010-DB-error-Insert-37-File-F23010-Error-1-ORA-00001-unique-constraint-SIGA-F23010-UNQ-violated
---

**Dúvida**Ao acessar a rotina FISA170 - Configurador de Tributos é apresentado o erro abaixo:

F23010: DB error (Insert): -37 File: F23010 - Error : 1 - ORA-00001: unique constraint (SIGA.F23010\_UNQ) violated

Called from GRVCFOP(FISA165.PRW)   
Called from FSA165CARG(FISA165.PRW)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.1.25  
  
**Solução**

Verificar a tabela 13 (Natureza da operação) da SX5

O erro acontece devido na tabela 13 da SX5 conter algum CFOP duplicado.
