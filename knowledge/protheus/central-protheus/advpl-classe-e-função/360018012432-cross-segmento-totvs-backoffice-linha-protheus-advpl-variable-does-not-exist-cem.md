---
article_id: 360018012432
category: ADVPL - Classe e Função
content_hash: 1533fdeec011189f1da7d1146222ecc2b0c4d19aa14389f433f34bda98101df7
fetched_at: '2026-06-28T22:40:18.216298+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Variable does not
  exist CEMPANT on FWCODEMP
type: support-article
updated_at: '2022-01-06T19:43:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018012432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Variable-does-not-exist-CEMPANT-on-FWCODEMP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Estou usando uma customização via *schedule* e gerou esse erroTHREAD ERROR ([XXXXX], XXXXXXX, THIS)  xx/xx/xxxx    
variable does not exist CEMPANT on FWCODEMP(FWFILIAL.PRW)   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**Esse erro ocorre pois foi utilizada uma função **FWCodEmp**sem preparar o ambiente.  
  
**Solução**

Neste caso é necessário preparar o ambiente com a**Prepare Environment** pois o *schedule* só agenda a execução.

Exemplo para o agendamento.

```
#Include 'Protheus.ch'  
#Include "tbiconn.ch"  
  
User Function tstfilial()  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'  
local cfili:= ""  
conout("OK")  
cfili:= FWCodEmp()  
conout("FILIAL " + cfili)  
  
RESET ENVIRONMENT  
  
Return
```

**Saiba mais**[FWCodEmp](http://tdn.totvs.com/pages/releaseview.action?pageId=6815128)[Prepare Environment](http://tdn.totvs.com/pages/releaseview.action?pageId=6814708)
