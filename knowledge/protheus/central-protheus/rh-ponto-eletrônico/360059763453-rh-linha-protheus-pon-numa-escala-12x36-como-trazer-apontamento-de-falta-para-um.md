---
article_id: 360059763453
category: RH - Ponto Eletrônico
content_hash: 8e29b81e95d15c8554acfd3dcf382df603f71b9b2f9848efcba47f5ff46a7e05
fetched_at: '2026-06-28T22:44:58.244684+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Numa escala 12x36, como trazer apontamento de falta
  para um feriado em dia trabalhado da escala desse turno
type: support-article
updated_at: '2026-02-09T21:02:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059763453-RH-Linha-Protheus-PON-Numa-escala-12x36-como-trazer-apontamento-de-falta-para-um-feriado-em-dia-trabalhado-da-escala-desse-turno
---

**Dúvida**Numa escala 12x36, como trazer apontamento de falta para um feriado em dia trabalhado da escala desse turno  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Este dia sendo um feriado e, para a jornada 12x36 se for um dia trabalhado e, o funcionário efetivamente trabalhar, **será gerado como Hora Extra**.  
  
Da mesma forma se, o funcionário não trabalhar este dia de feriado, mesmo sendo na escala dele 12x36, **por ser o feriado não será falta**.  
  
Duas opções para solucionar, além de incluir o apontamento manualmente de falta para os funcionários:  
1ª) ter estes funcionários em uma **regra de apontamento específica** e, o **campo Trabalha Feriado na primeira aba da Regra estar como SIM**, com isso, irá gerar falta se o funcionário não trabalhar porém não irá gerar Hora Extra para quem trabalhou este dia.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411027499159/mceclip0.png)  
  
2ª) incluir uma exceção por período ou por funcionário, **transformando este dia de feriado em um dia normal.**  
  
Por exemplo dessa forma:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098161334/mceclip0.png)​  
  
Assim, como no exemplo acima, apenas a matrícula **000014 terá o dia 15/11/2020 como dia normal**, com isso, mesmo ela estando em um turno 12x36 irá gerar a falta neste dia.
