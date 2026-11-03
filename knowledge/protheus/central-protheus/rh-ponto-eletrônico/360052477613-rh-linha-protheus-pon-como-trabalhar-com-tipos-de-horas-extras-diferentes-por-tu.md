---
article_id: 360052477613
category: RH - Ponto Eletrônico
content_hash: cce617d177b4435998d277baa7d42b7706d3ae8ac578a8dea83494cc5a697abb
fetched_at: '2026-06-28T22:44:58.302602+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como trabalhar com Tipos de Horas Extras diferentes
  por turnos
type: support-article
updated_at: '2021-09-13T19:23:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052477613-RH-Linha-Protheus-PON-Como-trabalhar-com-Tipos-de-Horas-Extras-diferentes-por-turnos
---

**Dúvida**Como trabalhar com apuração de Horas Extras dando tratamento diferente para cada turno?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No cadastro dos Tipos de Horas Extras, é possível inserir registros com Turno associado ou não.  
No exemplo abaixo, quero ter um tratamento diferente apenas para o turno 01, para os demais turnos da empresa, o tratamento será o mesmo.  
É importante saber que nesta rotina, é necessário minimamente cadastrar os 08 primeiros tipos de horas extras, sendo: Normal, DSR, Compensado, Feriado, Noturna Normal, Noturna DSR, Noturna Compensada e Noturna Feriado, e também que não pode ocorrer repetição de eventos:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083210133/mceclip0.png)  
  
Veja que fiz o cadastro dos 08 primeiros tipos para o turno 01 para que estes eventos específicos sejam calculados para funcionários atrelados a este turno, para os demais funcionários/turno, temos o cadastro também dos 08 primeiros tipos de horas extras mas com o campo de turno em branco e outros códigos de evento.
