---
article_id: 4408075288215
category: RH - Rescisão
content_hash: 07a91c96d73162d4e13da4de36d6373b31c481caf55d392d5170df265c6f7c54
fetched_at: '2026-06-28T22:43:53.529734+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que cálculo de rescisão não calcula o domingo
  mesmo com o campo Pg Sab\Dom = Sim
type: support-article
updated_at: '2025-06-16T18:47:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408075288215-RH-Linha-Protheus-GPE-Por-que-c%C3%A1lculo-de-rescis%C3%A3o-n%C3%A3o-calcula-o-domingo-mesmo-com-o-campo-Pg-Sab-Dom-Sim
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que cálculo de rescisão não calcula o domingo mesmo com o campo Pg Sab\Dom = Sim?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O cálculo de rescisão não calcula o domingo, pois não há o cadastro do Id 0430 (DSR indenizado para demissão na sexta-feira). Com o cadastro do Id 0430, em rescisão serão calculados os dias normais de segunda-feira até o sábado no Id 0048 e o domingo no Id 0430.

**ID 0430**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408068596887/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408068606615/mceclip1.png)

**Saiba mais:**Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[MP - GPE - Pagar o sábado e o domingo na demissão quando ocorre em uma Sexta Feira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012452152-MP-GPE-Pagar-o-s%C3%A1bado-e-o-domingo-na-demiss%C3%A3o-quando-ocorre-em-uma-Sexta-Feira?source=search)  
[MP - GPE - Qual a funcionalidade parâmetro MV\_SABDOM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000496202-MP-GPE-Qual-a-funcionalidade-par%C3%A2metro-MV-SABDOM?source=search)
