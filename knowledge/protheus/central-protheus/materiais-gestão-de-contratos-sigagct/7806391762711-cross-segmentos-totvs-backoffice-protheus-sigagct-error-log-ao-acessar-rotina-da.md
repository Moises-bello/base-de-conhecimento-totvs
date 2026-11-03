---
article_id: 7806391762711
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 75806c356db2c8acca21ffdf68ac46d45c9ff9d3c3c6ce942e0fe775431f6ef1
fetched_at: '2026-06-28T22:37:22.753162+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Error log  ao Acessar
  rotina Dashboard de Contratos variable does not exist CFILANT on SUPERGETMV
type: support-article
updated_at: '2022-07-29T14:52:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7806391762711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Error-log-ao-Acessar-rotina-Dashboard-de-Contratos-variable-does-not-exist-CFILANT-on-SUPERGETMV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Error log ao Acessar rotina Dashboard de Contratos variable does not exist CFILANT on SUPERGETMV

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7806985829783/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Causa**O sistema não está conseguindo localizar a filial CFILANT para logar no sistema.  
  
**Solução**Na configuração do Rest do Dashboard de Contratos no appserver.ini na Seção  [HTTPUTRI] deve-se adicionar a chave PreparaIn = All ou PrepareIn = Empresa, Filial que está logada para que o sistema valide a filial logada no sistema, conforme exemplos abaixo:

[HTTPURI]  
URL=/rest  
**PrepareIn=All**  
;PrepareIn=T1,D MG 02  
;dasboardInstances=1,2  
;Instances=4,4,1,1  
Instances=2,5,1,1  
;Instances=1,10  
CORSEnable=1  
AllowOrigin=\*

**Saiba mais:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Dashboard de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036517133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Dashboard-de-Contratos?source=search)

[Dashboard de Contratos](https://tdn.totvs.com/display/public/PROT/Dashboard+de+Contratos)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
