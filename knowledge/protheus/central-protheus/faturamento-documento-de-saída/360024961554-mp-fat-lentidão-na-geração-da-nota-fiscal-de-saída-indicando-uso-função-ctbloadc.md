---
article_id: 360024961554
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c24c0b031ca452318128571f0381acdbc750d2252a01534eb0d6a47cf10c6246
fetched_at: '2026-06-28T22:38:45.185846+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Lentidão na geração da Nota Fiscal de Saída indicando uso função
  CTBLOADCQD (CTBXVLD)
type: support-article
updated_at: '2021-04-28T15:13:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024961554-MP-FAT-Lentid%C3%A3o-na-gera%C3%A7%C3%A3o-da-Nota-Fiscal-de-Sa%C3%ADda-indicando-uso-fun%C3%A7%C3%A3o-CTBLOADCQD-CTBXVLD
---

**Dúvida**

Lentidão na geração da Nota Fiscal de Saída indicando uso função CTBLOADCQD (CTBXVLD).

**Ambiente**

Microsiga Protheus -  a partir da versão 12.  
  
**Solução**

A lentidão na geração da Nota Fiscal no faturamento pode ocorrer em casos onde as tabelas **CT1** e **CVD** estiverem com o modo de compartilhamento diferentes. 

O compartilhamento incorreto dessas tabelas também pode causar lentidão nas rotinas do financeiro e do próprio contábil.

A maneira de validar essa baixa performance é via leitura de logprofiler . Se no momento da leitura do log indicar o uso da função **CTBLOADCQD** (**CTBXVLD**), mesmo sem estar gerando contabilização  da nota, é um forte indicio de que as tabelas **CT1** e **CVD** estejam o modo de compartilhamento diferentes. 

Para avaliação e tratamento das tabelas contábeis, consulte link a seguir, com a orientação do Módulo CTB:**<http://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>**  
  
Veja também o Documento " Como habilitar e gerar o LogProfiler para avaliação de desempenho: **<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021553991-MP-SIGAFIN-Como-habilitar-e-gerar-o-LogProfiler-para-avalia%C3%A7%C3%A3o-de-desempenho->**
