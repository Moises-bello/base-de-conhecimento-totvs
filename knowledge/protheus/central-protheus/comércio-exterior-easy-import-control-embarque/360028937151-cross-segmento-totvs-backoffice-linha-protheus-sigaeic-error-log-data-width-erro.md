---
article_id: 360028937151
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 67b875c70ed4b1b8399314d5a2cc00058559219b5fac84b1bd95a905953f2077
fetched_at: '2026-06-28T22:39:48.718980+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - ERROR LOG: Data
  width error - Field: WKVLPAGTO2'
type: support-article
updated_at: '2021-08-30T18:46:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028937151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-ERROR-LOG-Data-width-error-Field-WKVLPAGTO2
---

**Ocorrência**Ao realizar a gravação dos títulos do embarque/desembaraço apresenta error log: Data width error - Field: WKVLPAGTO2 Value: 539999999999.945920 on TPC252GRAVA(EICTP252.PRW)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o conteúdo do(s) campo(s): Até (YR\_KILO1) e Valor(YR\_VALOR1), encontra-se incorretos.   
  
**Solução**Neste caso, verifique o valor informado para o frete no cadastro da via de transporte, altere o mesmo para um valor aproximado para o cálculo do PR e PRE, desta forma, não apresentará o error log:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029700651/mceclip1.png)
