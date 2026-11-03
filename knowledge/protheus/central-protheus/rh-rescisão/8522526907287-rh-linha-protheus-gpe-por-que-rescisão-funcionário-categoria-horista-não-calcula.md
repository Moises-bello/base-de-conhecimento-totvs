---
article_id: 8522526907287
category: RH - Rescisão
content_hash: 827d354dada57a97dd562e507079da046078f4b9d7be8620dbc38e402a2413cd
fetched_at: '2026-06-28T22:43:50.790316+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Por que rescisão funcionário categoria horista
  não calcula verbas indenizatórias por base 31 dias '
type: support-article
updated_at: '2025-06-13T11:52:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8522526907287-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-funcion%C3%A1rio-categoria-horista-n%C3%A3o-calcula-verbas-indenizat%C3%B3rias-por-base-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Por que rescisão funcionário categoria horista não calcula verbas indenizatórias por base 31 dias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**No cálculo da rescisão, mesmo que o mnemônico P\_DIASRES esteja parametrizado para calcular sobre os dias do mês (28, 29, 30 ou 31), as verbas indenizatórias de férias e 13º sempre serão calculadas sobre 30 dias, pois para esses cálculos é sempre considerado 30 dias, mesmo que seja funcionário horista.  
   
No calculo normal de férias e de 13º o sistema segue essa mesma regra, sempre 30 dias.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Qual o impacto de calcular rescisão original com o mnemônico P\_DIASRES = 2 e calcular rescisão complementar por dissídio com o P\_DIASRES = 1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7431764289559-RH-Linha-Protheus-GPE-Qual-o-impacto-de-calcular-rescis%C3%A3o-original-com-o-mnem%C3%B4nico-P-DIASRES-2-e-calcular-rescis%C3%A3o-complementar-por-diss%C3%ADdio-com-o-P-DIASRES-1?source=search)
