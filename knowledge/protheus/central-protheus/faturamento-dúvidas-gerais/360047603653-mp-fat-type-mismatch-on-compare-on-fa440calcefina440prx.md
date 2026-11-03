---
article_id: 360047603653
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: af3c4d3ea594149f41206eaed3985e8da22ce123f12205aef01098cfd8538396
fetched_at: '2026-06-28T22:38:32.699990+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Type mismatch on compare on FA440CALCE(FINA440.PRX)
type: support-article
updated_at: '2021-04-28T15:53:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047603653-MP-FAT-Type-mismatch-on-compare-on-FA440CALCE-FINA440-PRX
---

**Ocorrência**

Ao gerar um faturamento (**MATA461**) com comissão, onde se tenha um vendedor bloqueado (**MATA040**), gera o erro: **type mismatch on compare on FA440CALCE(FINA440.PRX) 06/02/2020 14:10:38** line : 688  
  
**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
  
**Causa**

A rotina não estava efetuando a validação correta para o registro bloqueado, causando a inconsistência.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote de correçãode acordo com a sua versão**:**

**[12.1.27: https://r.totvs.io/p/961355](https://r.totvs.io/p/961355) ;     
[12.1.25: https://r.totvs.io/p/961354](https://r.totvs.io/p/961354) ;   
[12.1.23: https://r.totvs.io/p/961353](https://r.totvs.io/p/961353) ;   
[12.1.17: https://r.totvs.io/p/961352](https://r.totvs.io/p/961352) ; (com garantia estendida)**

2. Aplique o pacote, via TDS ou Vs-Code em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.

Caso o ambiente seja Cloud Protheus, a equipe de suporte atuará com o atendimento de suporte integrado.
