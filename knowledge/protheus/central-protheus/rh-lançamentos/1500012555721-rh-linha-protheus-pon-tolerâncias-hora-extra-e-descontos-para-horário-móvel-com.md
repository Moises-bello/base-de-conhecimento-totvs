---
article_id: 1500012555721
category: RH - Lançamentos
content_hash: 4a99df21b2ef79214466c129e1b766998af35d8d9cb503bca7e9040cd7bb5b8b
fetched_at: '2026-06-28T22:44:46.896769+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Tolerâncias Hora Extra e Descontos, para horário
  móvel com mobilidade ou horário fixo
type: support-article
updated_at: '2026-06-19T14:39:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012555721-RH-Linha-Protheus-PON-Toler%C3%A2ncias-Hora-Extra-e-Descontos-para-hor%C3%A1rio-m%C3%B3vel-com-mobilidade-ou-hor%C3%A1rio-fixo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34261851457815) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Tolerâncias Hora Extra e Descontos, para horário móvel limitado ou horário fixo  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Essa documentação vale para quando temos, uma regra de apontamento com **horário móvel com mobilidade de horas** e para **horários fixos**.  
  
Vamos abordar o funcionamento das tolerâncias, tenho como exemplo horário padrão das:   
**08:00 - 12:00 - 13:12 - 18:00**  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019851761)**  
  
Vamos usar uma tolerância da seguinte maneira:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019851301)  
No horário móvel que vou utilizar nesse teste, temos:  
**Tolerância Hora Extra Período 10 minutos**  
**Tolerância Hora Extra 05-05-05-05**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019577122)  
  
Ou podemos também utilizar, com esse mesmo conceito, uma regra de apontamento, **com horário e intervalo fixos**.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019855261)  
  
Assim, como disse, teremos uma tabela de horário padrão das **08:00 - 12:00 - 13:12 - 18:00**  
  
Marcações do funcionário:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019577222)  
  
Explicação por dia de todos os apontamentos gerados:  
- **Dia 05/04/2021** 08:00 12:00 13:12 18:00 não tem hora extra período não tem hora extra diária  
- **Dia 06/04/2021** 07:54 (6 min) 12:01 (1 min) 13:10 (2 min) 18:02 (2 min) = Total período 6+1+2+2=11 ultrapassou o período **PAGA HE**  
Neste exemplo a entrada foi superior a tolerância de 5 minutos, como quebrou e a soma dos outros horários ultrapassa 10 minutos  irá gerar a hora extra.  
- **Dia 07/04/2021** 07:58 (2 min) 12:02 (2 min) 13:10 (2 min) 18:02 (2 min) = Total período 2+2+2+2=8 minutos não ultrapassou o período **não paga HE**  
Neste exemplo a entrada não foi superior a tolerância de 5 minutos, como não quebrou e a soma dos outros horários não ultrapassou 10 minutos não irá gerar a hora extra.  
- **Dia 08/04/2021** 07:55 (5 min) 12:01 (1 min) 13:10 (2 min) 18:02 (2 min) = Total período 5+1+2+2=10 minutos não ultrapassou o período **não paga HE**  
Neste exemplo a entrada não foi superior a tolerância de 5 minutos, como não quebrou e a soma dos outros horários não ultrapassou 10 minutos não irá gerar a hora extra.  
- **Dia 09/04/2021** 07:55 (5 min) 12:02 (2 min) 13:10 (2 min) 18:02 (2 min) = Total período 5+2+2+2=11 minutos ultrapassou o período **PAGA HE**  
Neste exemplo a entrada foi está igual a tolerância de 5 minutos, como quebrou e a soma dos outros horários ultrapassa 10 minutos irá gerar a hora extra.  
- **Dia 10/04/2021** 07:55 (5 min) 12:00 13:12 18:02 (2 min) = Total período 5+2=7 minutos não ultrapassou o período **não paga HE**  
Neste exemplo a entrada foi está igual a tolerância de 5 minutos, não quebrou, a saída está inferior não quebrou e o total não ultrapassou os 10 minutos.  
  
**IMPORTANTE**:  
Como abordei mais acima, esse mesmo conceito vale tanto para cálculo de tolerância em Horas Extras, quanto para os descontos, no caso, Atraso e Saída Antecipada e, é utilizada para Horário Móvel com limitações de horas antes e depois ou então para horários fixos.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Conceito e funcionamento de horário móvel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004195191-RH-Linha-Protheus-PON-Conceito-e-funcionamento-de-hor%C3%A1rio-m%C3%B3vel)  
[RH - Linha Protheus - PON - Como funciona o Horário Móvel Livre](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016803271-RH-Linha-Protheus-PON-Como-funciona-o-Hor%C3%A1rio-M%C3%B3vel-Livre)
