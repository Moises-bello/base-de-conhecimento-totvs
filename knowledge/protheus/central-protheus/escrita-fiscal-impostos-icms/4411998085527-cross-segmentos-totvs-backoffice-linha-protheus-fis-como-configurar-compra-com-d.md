---
article_id: 4411998085527
category: Escrita Fiscal - Impostos - ICMS
content_hash: b72244c8d94e6b59b8c463b49d852d0764288c28293dd12ec7ab5ab1959045b4
fetched_at: '2026-06-28T22:39:24.159624+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar compra
  com diferencial de alíquotas com redução de base de cálculo?
type: support-article
updated_at: '2021-11-03T11:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411998085527-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-compra-com-diferencial-de-al%C3%ADquotas-com-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00**min** **Dúvida**MP - FIS - Como configurar compra com diferencial de alíquotas com redução de base de cálculo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução** MV\_estado = SP  
  
MV\_art117 = .F.  
MV\_p9sped = .T.  
MV\_p9auto = T  
  
P9autotext.SP = na pasta system do Protheus  
  
1) CFOP 2556 compra para consumo  
![](https://totvssuporte.zendesk.com/attachments/token/tmAxflnYntW2gUZm18Lrlr6kC/?name=inline828179024.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/k1Q8jnIaZRCIBYjpAuSVwaljR/?name=inline1312785182.png)​  
  
2)CFOP 2551 - compra para ativo com redução de base de calculo,

TES

Calcula icms = sim

L fiscal icms = outros

% red icm = preenchido

Mat consumo = sim ( não pode ser outros dá erro na apuração do icms )

![](https://totvssuporte.zendesk.com/attachments/token/X2kiS3Jo1BL7Q5N5tRa4JvOdI/?name=inline1854344267.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/giuh5dCEgptqU7rgUtNbn9lLM/?name=inline-2119508689.png)​  
  
Apuração de ICMS  
  
![](https://totvssuporte.zendesk.com/attachments/token/VWpUrx2ihVkqp5uBb4KansLX0/?name=inline-413875840.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/Z76iNmQLoTsv8OuFOC3G2caHB/?name=inline-1921163588.png)​  
detalhamento  
![](https://totvssuporte.zendesk.com/attachments/token/vnBR8lOAFTayHHTOH1G5YjDzt/?name=inline1568933759.png)​  
  
​![](https://totvssuporte.zendesk.com/attachments/token/bf4gAjIbwfzprmKpeJXZRcSkB/?name=inline-1597658981.png)​  
  
Para que o sistema traga de forma correta, precisa configurar o campo da TES  
Mat consumo = SIm
