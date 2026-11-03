---
article_id: 4402430130583
category: RH - FGTS / SEFIP
content_hash: e1c75c22ad988496b942d9fa27b87f444ed1dba727c212e8036410752f9426a3
fetched_at: '2026-06-28T22:43:41.306798+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Por que FGTS não é recolhido na Sefip quando rescisão
  é calculada com FGTS mês anterior
type: support-article
updated_at: '2025-09-05T12:09:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402430130583-RH-Linha-Protheus-GPE-Por-que-FGTS-n%C3%A3o-%C3%A9-recolhido-na-Sefip-quando-rescis%C3%A3o-%C3%A9-calculada-com-FGTS-m%C3%AAs-anterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34708445416471) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Por que FGTS não é recolhido na Sefip quando rescisão é calculada com FGTS mês anterior?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Conforme *layout* da GRRF, quando há cálculo de FGTS mês anterior na rescisão, esse FGTS é recolhido na GRRF, dessa forma, ao gerar a Sefip do mês anterior ao da rescisão, esse valor não será recolhido, caso contrário, seria recolhido em dobro.  
  
Abaixo exemplo de rescisão com cálculo de FGTS mês anterior onde o valor é recolhido na GRRF:  
  
Folha mês anterior a rescisão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402430114839)  
Rescisão com FGTS mês anterior:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402435540247)  
GRRF grada:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402435549207)

**Saiba mais**  
[RH - Linha Protheus - GPE - Como apurar FGTS mês anterior no cálculo da rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038796313)
