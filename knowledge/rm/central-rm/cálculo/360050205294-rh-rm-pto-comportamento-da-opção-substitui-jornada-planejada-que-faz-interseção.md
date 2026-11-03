---
article_id: 360050205294
category: Cálculo
content_hash: 9738986440340c8e46a8bd4f0fca1e777ddf154c05ae3feb565da8fa50b200fb
fetched_at: '2026-06-28T22:46:29.202200+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Comportamento da opção "Substitui jornada planejada que faz
  interseção com o feriado" na etapa Feriados do sindicato
type: support-article
updated_at: '2025-02-19T01:12:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050205294-RH-RM-PTO-Comportamento-da-op%C3%A7%C3%A3o-Substitui-jornada-planejada-que-faz-interse%C3%A7%C3%A3o-com-o-feriado-na-etapa-Feriados-do-sindicato
---

**Dúvida**Qual o comportamento da opção "***Substitui jornada planejada que faz interseção com o feriado"*** *na etapa Feriados**do parâmetro do sindicato?*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) – Automação de Ponto – A partir da versão 12.1.27  
  
**Solução**Quando o parâmetro estiver marcado o sistema irá calcular extra de feriado para todas as jornadas de trabalho que intercedem com o feriado. 

**Exemplo:**  
Parâmetro marcado e horário noturno

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077636393)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077635593)

Feriado cadastrado no dia 23/05/2020.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076484254)

Após aplicar o recalculo o sistema irá calcular o feriado para  a jornada do dia 22/05  das 21:00 +06:00 e para a jornada do dia 23/05  21:00 +06:00.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077635773)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076484474)

**Mais** [Comportamento de feriado no sindicato](https://tdn.totvs.com/display/public/LRM/Feriados)
