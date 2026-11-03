---
article_id: 360057817213
category: NFe - Nota Fiscal Eletrônica
content_hash: d8e3b3fd373db19367ea5a3154075122bb2ae82e1732827bba0955b32a68e745
fetched_at: '2026-06-28T22:40:01.846454+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Error log variable
  does not exist CENTATIV on CHECKACTIVEENT(TSSCONFIG.PRW)'
type: support-article
updated_at: '2021-12-02T17:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057817213--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Error-log-variable-does-not-exist-CENTATIV-on-CHECKACTIVEENT-TSSCONFIG-PRW
---

**Dúvida**Como corrigir o error log abaixo?

variable does not exist CENTATIV on CHECKACTIVEENT(TSSCONFIG.PRW) 20/08/2020 12:07:30 line : 1119

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para correção do erro informado, será necessário que atualize o fonte SPEDNFE.  
  
Pois possui o fonte TSSCONFIG atualizado e utilizando uma variável inexistente no SPEDNFE desatualizado (no exemplo utilizado, data do SPEDNFE.PRX 12/03/2020).

THREAD ERROR ([28016], francisco, LAPTOP-1O0IFKLF) 02/10/2020 10:21:52  
variable does not exist CENTATIV on CHECKACTIVEENT(TSSCONFIG.PRW) 20/08/2020 12:07:30 line : 1119

[TOTVS build: 7.00.191205P-20200220]  
Called from SPEDENTATIV(SPEDNFE.PRX) 12/03/2020 12:27:42 line : 5565  
Called from SPEDNFE2(SPEDNFE.PRX) 12/03/2020 12:27:42 line : 171  
Called from SPEDNFE(SPEDNFE.PRX) 12/03/2020 12:27:42 line : 61  
Called from \_\_EXECUTE(APLIB090.PRW) 18/05/2020 17:21:57 line : 680  
Called from MDIEXECUTE(APLIB260.PRW) 18/05/2020 17:21:57 line : 896

Segue pacote para atualização do ambiente Protheus:  
P12.1.23: <https://suporte.totvs.com/portal/p/10098/download?e=785322>   
P12.1.25: <https://suporte.totvs.com/portal/p/10098/download?e=785367>   
P12.1.27: <https://suporte.totvs.com/portal/p/10098/download?e=956647>

**\*Importante:** Faça um backup do rpo do Protheus antes da atualização. Se possível, validar primeiramente em ambiente de testes.  
\*\*Ao aplicar "aceitar somente fontes mais atualizados".  
  
Caso o incidente persista mesmo após a atualização, abra um ticket em nosso suporte NFe, para análise.
