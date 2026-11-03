---
article_id: 4413548098199
category: RH - Soluções para error.log
content_hash: 305b1f57732507b8c9c9cfe19fa2ae235a392504e2ae68a538cc54d454a9ddfb
fetched_at: '2026-06-28T22:44:09.039272+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao tentar gerar relatório de provisão, gera error
  log: invalid typecast in file d:\bamboo\xml-data\build-dir\tp11-of19310-tecxwin64\advpl\instrvar.inl
  at line 926  on SENDPRTINFO(APLIB080.PRW)'
type: support-article
updated_at: '2025-09-11T20:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413548098199-RH-Linha-Protheus-GPE-Ao-tentar-gerar-relat%C3%B3rio-de-provis%C3%A3o-gera-error-log-invalid-typecast-in-file-d-bamboo-xml-data-build-dir-tp11-of19310-tecxwin64-advpl-instrvar-inl-at-line-926-on-SENDPRTINFO-APLIB080-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34878389720215) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao tentar gerar relatório de provisão, através da rotina GPER070 gera *error log*: *"****invalid typecast in file* d:\bamboo\xml-data\build-dir\tp11-of19310-tecxwin64\advpl\instrvar.inl at line 926**  
***on* SENDPRTINFO(APLIB080.PRW)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre pois o parâmetro **MV\_CANSALT** está com TIPO incorreto.  
  
**Solução**Pra solução do problema, será necessário corrigir o TIPO do parâmetro MV\_CANSALT para LÓGICO, conforme abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/BaiL3jO7WnKvhh5dzOFhoJOwb/?name=inline1908144247.png)

**Saiba Mais:**

[RH - Soluções Error Log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)   
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
