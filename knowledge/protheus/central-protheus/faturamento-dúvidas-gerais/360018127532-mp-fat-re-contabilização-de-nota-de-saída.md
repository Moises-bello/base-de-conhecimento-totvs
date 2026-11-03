---
article_id: 360018127532
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 85b18dc0517f1634034336f5f6c7f9b220c59ea835f574e9435248ded7fcc9b1
fetched_at: '2026-06-28T22:38:31.333590+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Re contabilização de nota de saída
type: support-article
updated_at: '2021-04-28T15:55:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018127532-MP-FAT-Re-contabiliza%C3%A7%C3%A3o-de-nota-de-sa%C3%ADda
---

**Ocorrência**Estamos tentando re contabilizar umas Notas fiscais de venda, já retirei o flag ta tabela SE1 e SE2 do E1\_LA e E2\_LA, não tem movimentação SE5, na contabilização off line esta como SIM para mostrar os lançamentos contábeis e mesmo assim não traz as notas.  
   
 **Ambiente**Microsiga Protheus - desde versões anteriores a 12.  
   
 **Causa**Após gerar uma contabilização de nota de saída, mesmo que não seja contabilizado, o sistema marca o campo **F2\_DTLANC** com a data do processamento indicando que passou pela rotina.  
   
 **Solução**

Se a contabilização é relacionada a nota de saída, tabelas SF2 e SD2, avalie o campo F2\_DTLANC se está preenchido, pois é ele o flag da nota para permitir a contabilização.  
Limpe o F2\_DTLANC e tente efetuar a contabilização com  lançamento simples, exemplo para **lp610  SD2->D2\_TOTAL**  ou para **lp620 SF2->F2\_VALMERC**, avaliando se o lote contábil 8820 é gerado na contabilidade gerencial.
