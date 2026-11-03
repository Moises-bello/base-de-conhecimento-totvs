---
article_id: 10451999560343
category: ERRORLOG
content_hash: ae1901634041fd07f54762a130dc928a13b4cfb004aa57eccf723f17388de8d1
fetched_at: '2026-06-28T22:44:39.441444+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - Meu RH - Error log ao aprovar uma solicitação (TCFA040)
  - variable is not array - Type [U] on WFLOADVALFILE(WFPROCESS.PRW)
type: support-article
updated_at: '2026-06-19T18:59:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10451999560343-RH-Linha-Protheus-Meu-RH-Error-log-ao-aprovar-uma-solicita%C3%A7%C3%A3o-TCFA040-variable-is-not-array-Type-U-on-WFLOADVALFILE-WFPROCESS-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24973890115095) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Errorlog ao aprovar uma solicitação na rotina "Efetivar solicitações" (TCFA040)   
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**  
Inconsistência no registro de processamento dentro da pasta process do workflow  
  
**Solução**  
Localizar no arquivo do Errorlog o código do "processo" com problema, conforme o exemplo abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/eUPfBJdRtgyWCifMUMjPh00eT/?name=image.png)   
  
No caminho onde esta a pasta workflow, abaixo da sua pasta Protheus\_data, exemplo:  
**C:\Protheus\_12.2210\Protheus\_Data\workflow**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451547599255)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451721837335)

Localize o registro de acordo com o que foi apresentado no error log:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451795236503)

Exclua o arquivo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451798658967)  
  
Realize a efetivação da solicitação que apresentava o error log:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451860061847)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10451912618007)
