---
article_id: 10715824859031
category: RH - Rescisão
content_hash: 38100a65b0dc6e2c2d2a63127e5f79f2b6f6bbd9deb077a437f4e2d0189506b6
fetched_at: '2026-06-28T22:43:50.835382+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os Pontos de Entradas existente na rotina
  Cálculo de rescisão GPEM040
type: support-article
updated_at: '2025-09-08T18:45:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10715824859031-RH-Linha-Protheus-GPE-Quais-os-Pontos-de-Entradas-existente-na-rotina-C%C3%A1lculo-de-rescis%C3%A3o-GPEM040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34788845658007) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais os Pontos de Entradas existente na rotina **Cálculo de rescisão** (GPEM040*)?*  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A rotina GPEM040-Rescisão na versão 12 foi desenvolvida em MVC, então os pontos de entrada GPESALAR, GPM040RA, GPM040AR e VLDTPRESP não são mais chamados na rotina.  
  
Como a rotina esta em MVC, deve ser usado o ponto de entrada GPEM040, abaixo segue documentação com modelo de utilização do PE GPEM040:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=680971161>  
  
  
**Saiba Mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como realizar o cálculo simulado da rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034654694-MP-GPE-Como-realizar-o-c%C3%A1lculo-simulado-da-rescis%C3%A3o)  
[Pontos de Entrada para fontes Advpl desenvolvidos utilizando o conceito MVC](https://tdn.totvs.com/display/public/framework/Pontos+de+Entrada+para+fontes+Advpl+desenvolvidos+utilizando+o+conceito+MVC)
