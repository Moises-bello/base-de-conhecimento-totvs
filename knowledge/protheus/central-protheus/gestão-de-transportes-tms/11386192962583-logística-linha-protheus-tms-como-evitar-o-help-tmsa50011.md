---
article_id: 11386192962583
category: Gestão de Transportes (TMS)
content_hash: 63a09a77e64c9514448232423462697921090835beb544ed10fd87e1d15e487c
fetched_at: '2026-06-28T22:45:27.428745+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como evitar o help TMSA50011
type: support-article
updated_at: '2023-01-03T20:06:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11386192962583-Log%C3%ADstica-Linha-Protheus-TMS-Como-evitar-o-help-TMSA50011
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:25 min** **Dúvida**Como evitar o *help* **TMSA50011**, no calculo de CT-e complementar?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para a correta geração do Serviço no documento de transporte gerado através da rotina de fatura automática - **TMSA491**, deve-se por premissa configurar o parâmetro **MV\_SRVFAT**. Onde deve ser informado o código do **DOCTMS** de Apoio e o tipo de transporte **1 - Rodoviário** igual ao código do serviço de negociação.   
  
Exemplo: C1=SNA.   
Onde C é o tipo de documento de apoio, 1 é o tipo de transporte Rodoviário e o SNA é o serviço a ser informado.  
  
![12.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/11411460801175)  
  
![13.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/11411485282327)  
  
![11.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/11411464761367)  
  
**Saiba mais**Mais informações poderão ser acessadas no link**:** [Help TMSA50011](https://tdn.totvs.com/pages/viewpage.action?pageId=729250004) **Glossário  
CT-e**- Conhecimento de transporte eletrônico
