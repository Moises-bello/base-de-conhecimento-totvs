---
article_id: 1500003690482
category: RH - Lançamentos
content_hash: 2ca436345ae4b61067e119835d4a188f0214ce589e7b224b05901c001a42924c
fetched_at: '2026-06-28T22:44:46.905337+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Apontamento de Absenteísmo em jornadas noturnas
  - horário móvel livre
type: support-article
updated_at: '2025-06-05T13:40:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003690482-RH-Linha-Protheus-PON-Apontamento-de-Absente%C3%ADsmo-em-jornadas-noturnas-hor%C3%A1rio-m%C3%B3vel-livre
---

**Dúvida**Apontamento de Absenteísmo em jornadas noturnas - horário móvel livre  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**É de conhecimento que, a **hora noturna por CLT inicia-se as 22:00 e finda as 05:00**, com isso, temos casos onde o funcionário possui uma **Tabela de Horário Padrão** comercial diurna e um horário móvel livre pela Regra de Apontamento.  
  
Nesse caso, o funcionário, pode iniciar sua jornada o momento mais conveniente, porém quando temos um absenteísmo, ou seja, menos horas realizadas e essas, são na parte pós 22:00, o absenteísmo apontado leva em conta a valorização da hora noturna.  
  
Vejamos um **exemplo** bem clássico. Na [Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) conforme configurada à seguir:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102558154)  
  
**Regra de Apontamento** como horário móvel livre(dia inteiro):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102559074)  
  
Nesse **exemplo**, utilizando tolerância de 10 minutos no período.  
Para configurar as tolerâncias na regra:[Tolerâncias Hora Extra e Descontos, para horário móvel limitado ou horário fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012555721-RH-Linha-Protheus-PON-Toler%C3%A2ncias-Hora-Extra-e-Descontos-para-hor%C3%A1rio-m%C3%B3vel-limitado-ou-hor%C3%A1rio-fixo)  
  
Acessando em **Atualizações-Lançamentos-Integrados**, filtre o funcionário e entre como alterar:  
Um apontamento normal de desconto seria, por exemplo, funcionário iniciando as 08:00 e findando a jornada as 17:30, ou seja, 30 minutos de saída antecipada (por conta do horário móvel - nunca atraso nesse caso).  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003681322)  
  
Com isso, o funcionário realizou 30 minutos a menos de jornada padrão, por isso, um apontamento de 0,30 minutos nesse dia.  
  
Porém, e se este funcionário um dia, entrar as 13:00 e com isso, findar 10 horas depois (total da jornada padrão) as 23:00, porém nesse dia ele foi embora as 22:30. O Sistema estaria correto em apontar 30 minutos nesse caso? Vamos ver no exemplo abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003783981)  
  
O entendimento que temos é que mesmo a tabela de horário padrão sendo diurna, o funcionário neste dia, por causa da mobilidade de horário, fez 30 minutos dessa jornada em horário noturno.  
  
Se valorizarmos os 30 minutos, temos 34 minutos de trabalho, por isso o apontamento de um Adicional Noturno de 34 minutos e uma Saída Antecipada de 0,26 minutos e não de 0,30 minutos, pois conforme valorização, o funcionário trabalhou 4 minutos a mais.   
  
Mas e se a Empresa não entender dessa forma? Temos como alterar?  
Sim, temos! No cadastro do [Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho), o campo abaixo que friso em amarelo, é responsável por valorizar ou não o desconto, sendo para mais ou menos.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003733102)  
  
No nosso exemplo, vou cadastrar o campo de Considera Adicional Noturno na Saída Antecipada como Não e, acessar novamente o Integrados e reapontar.  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003734062)  
  
Integrados após campo alterado:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003785401)  
  
Veja que, continuamos com os 0,34 minutos de hora noturna mas agora, a saída antecipada apontou como hora corrida 0,30 minutos.  
  
**Saiba Mais**  
Acesse o *link* a seguir par mais informações sobre Adicional Noturno no módulo de Ponto:   
[Como gerar o Adicional Noturno e Adicional Noturno sobre Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711-RH-Linha-Protheus-PON-Como-gerar-o-Adicional-Noturno-e-Adicional-Noturno-sobre-Horas-Extras)  
[Percentuais diferentes de adicional noturno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001771862-RH-Linha-Protheus-PON-Percentuais-diferentes-de-adicional-noturno)
