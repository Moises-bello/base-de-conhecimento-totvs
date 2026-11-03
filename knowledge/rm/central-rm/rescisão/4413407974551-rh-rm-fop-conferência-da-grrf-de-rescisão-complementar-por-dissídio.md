---
article_id: 4413407974551
category: Rescisão
content_hash: ee2e179bfcfdcc49f11e9dc6389255696b875ae559e8cf08d532abd880eca74f
fetched_at: '2026-06-28T22:46:54.451478+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP -  Conferência da GRRF de rescisão complementar por dissídio
type: support-article
updated_at: '2025-01-21T18:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413407974551-RH-RM-FOP-Confer%C3%AAncia-da-GRRF-de-rescis%C3%A3o-complementar-por-diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como conferir a GRRF da rescisão complementar por dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A Guia de Recolhimento Rescisório do FGTS da rescisão complementar tem por objetivo o recolhimento referente aos valores de Aviso Prévio, 13º Salário Indenizado e a Multa Rescisória das verbas não indenizatórias. Uma vez que a GRRF de rescisão complementar não permite recolhimento do FGTS do sobre a remuneração do mês e remuneração de 13º salário, será feito o recolhimento na SEFIP com código 650.  
Para conferência da GRRF de rescisão complementar, separamos do cálculo efetuado as verbas com Identificadores referente as verbas indenizatórias, das demais verbas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413417592343/mceclip0.png)  
  
Será levado para a GRRF os valores referente aos códigos de cálculos:

* [Código de Cálculo 99 - Diferença Aviso Prévio](https://tdn.totvs.com/pages/releaseview.action?pageId=452718356#:~:text=Provento%20do%20tipo%20valor.,tenha%20sido%20lan%C3%A7ada%20na%20rescis%C3%A3o.)
* [Código de Cálculo 98 - Diferença 13º Salário Indenizado Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=452718367)  
    
  As demais verbas com incidência em FGTS serão levadas apenas a multa de 40% sobre o percentual de 8%.

**Memória de cálculo**  
**VALOR FGTS** - verbas 0084 + 1187 + 1822 = 359,34 =  359,34 X 8% = **28,74** - base para recolhimento da multa dos 40%  
**Verbas Indenizatórias:** (verbas 0086) = 6,16    
**Sobre Verbas Indenizatórias:** Este campo é composto pelos eventos Diferença Aviso Indenizado, Diferença 13 salario indenizado, diferença de medias de aviso indenizado, diferença media 13 salario indenizado.

**Log de Calculo GRRF**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413407928983/mceclip1.png)****Memoria Calculo GRRF****Aviso Prévio Indenizado**Valor aviso indenizado =  6,16  
Depósito = 6,16 \* 8% = 0,49  
  
**Multa Rescisória**  
Valor 8% verbas não indenizatória = 28,74  
Saldo Rescisório = 0,49 + 28,74 = 29,23  
Depósito = 29,23 \* 40% = 11,69 + 0,49 = 12,18  
  
Total a recolher = 12,18  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413407968407/mceclip2.png)  
  
**SEFIP 650**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413407925527/mceclip0.png)

**Importante**  
  
**Glossário**  
**FGTS-** Fundo de Garantia do Tempo de Serviço (FGTS)  
**SEFIP-**  Sistema Empresa de Recolhimento do FGTS  
**GRRF-** Guia de Recolhimento Rescisório do FGTS
