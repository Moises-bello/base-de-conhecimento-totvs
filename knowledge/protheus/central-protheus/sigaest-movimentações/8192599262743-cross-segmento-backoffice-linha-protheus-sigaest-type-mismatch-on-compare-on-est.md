---
article_id: 8192599262743
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 233d266d613338488d3aab9397d2ffa5ff41d1da0ec6033c81f4eb5f2fff0406
fetched_at: '2026-06-28T22:38:58.413999+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - type mismatch on compare  on
  ESTMETRICS(ESTXFUN.PRW)
type: support-article
updated_at: '2022-08-16T11:08:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8192599262743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-type-mismatch-on-compare-on-ESTMETRICS-ESTXFUN-PRW
---

**Ocorrência**Ao acessar o Protheus apresenta o error.log

***type mismatch on compare on ESTMETRICS(ESTXFUN.PRW)*** 31/05/2021 21:58:04 line : 135

[TOTVS build: 7.00.210324P-20220608]  
Called from ESTLOAD(SIGACUSB.PRX) 13/05/2022 09:21:19 line : 16190  
Called from \_\_EXECUTE(APLIB090.PRW) 08/06/2022 16:53:22 line : 721  
Called from {|| \_\_Execute('ESTLoad()','xxxxxxxxxx','Estoque/Custos',' 4',,,.T.)}(APLIB090.PRW) 08/06/2022 16:53:22 line : 2517  
Called from ONLOADEXECUTE(APLIB090.PRW) 08/06/2022 16:53:22 line : 3444  
Called from FWSETENVIRONMENT(FWAPP.PRW) 08/06/2022 16:53:24 line : 2266  
Called from APPSETENVCHILD(FWAPP.PRW) 08/06/2022 16:53:24 line : 2364  
Called from MDIEXECUTE(APLIB260.PRW) 08/06/2022 16:53:22 line : 852

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Causa**Esse incidente ocorre, *devido o parâmetro MV\_CUSFIL no ambiente **estar diferente** do tipo CARACTERE que é o padrão.*  
  
**Solução**Para solucionar essa ocorrência, é necessário revisar como foi incluído o parâmetro no ambiente e ajusta-lo para tipo CARACTERE.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8193095758103/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8192815416087/mceclip0.png)

Saiba Mais:  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
