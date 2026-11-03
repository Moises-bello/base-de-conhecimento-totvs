---
article_id: 20709789002007
category: Escrita Fiscal - Impostos - ICMS
content_hash: 7b1eb05684c467b95cdadc62ff55a53d97244533f2eef49af65fb7a067f14b9f
fetched_at: '2026-06-28T22:39:24.050731+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o credito outorgado para gerar C197?
type: support-article
updated_at: '2024-01-19T18:21:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20709789002007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-credito-outorgado-para-gerar-C197
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20709788969495) Tempo aproximado para leitura: 03:00**min** **Dúvida**Como configurar o credito outorgado para gerar C197 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Segue um exemplo para gerar o C197  
 

MV\_ESTADO = SP  
   
Código

|  |  |  |
| --- | --- | --- |
| SP10090757 | Feijão - Crédito Presumido -  Artigo 25 do Anexo III do RICMS/00 | 01/2016 |

   
   
1a) Credito Outorgado  
produto importado , origem = 1  

Calculo do credito outorgado = 3%

TES  
Calcula icms = sim  
L fiscal icms = tributado  
Sit trib icm = 00

Crd Out Sp = 3%  
   
![](https://totvssuporte.zendesk.com/attachments/token/l7UjOzme6NkuaF2cpjpOHNXdL/?name=image.png)  
   
Reflexo  
![](https://totvssuporte.zendesk.com/attachments/token/PHlSdjRiSL122u9oygdTxPyiL/?name=image.png)  
   
Produto importado  
Origem = 1  
   
![](https://totvssuporte.zendesk.com/attachments/token/aC5LcTutApCnk16GSQafvRABN/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/6FEMUWFHsKq16Bp9Il3VFMGxU/?name=image.png)
