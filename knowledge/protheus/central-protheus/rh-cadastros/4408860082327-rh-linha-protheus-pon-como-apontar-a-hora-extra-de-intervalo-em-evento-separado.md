---
article_id: 4408860082327
category: RH - Cadastros
content_hash: a8d59e50f6ed2480dd2303aeba30aaf859f80d44cba9b90408b7a08441671ffa
fetched_at: '2026-06-28T22:44:52.789401+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como apontar a Hora Extra de Intervalo em evento
  separado
type: support-article
updated_at: '2026-02-10T18:06:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408860082327-RH-Linha-Protheus-PON-Como-apontar-a-Hora-Extra-de-Intervalo-em-evento-separado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29755383230359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como apontar a Hora Extra do Intervalo em evento separado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**  
Para **Apontar Hora Extra Intervalo** em evento separado, realize os seguintes passos:  
  
**1.** Em **Atualizações > Cadastro do Ponto > Tipos de Horas Extras**, é necessário cadastrar os tipos de horas de Intervalo**.** Para isso é necessário incluir minimamente os cadastros dos tipos de horas de **Intervalo Normal** e **Intervalo Noturna**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755383232279)  
  
2. Os Eventos vinculados não podem ser repetidos nos [Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314) e fica a critério do cliente, da mesma forma se esses eventos devem [computar em Banco de Horas ou ser pago em Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search).   
  
**3.** No exemplo abaixo, utilizamos um turno de trabalho das **07h - 12h - 13h - 18h**.  
Em **Atualizações > Lançamentos > Integrados**, veja que no dia 06.01 o funcionário fez o seguinte horário: **07h - 12h - 12h30 - 18h15**.  
Com o reapontamento, o sistema aponta dois eventos diferentes, sendo um de Hora Extra Intervalo e outro de Horas Extra referente a saída do expediente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755383237527)  
  
**IMPORTANTE**: Essa separação só acontecerá se, na **Regra de Apontamento** o horário do funcionário for todo fixo (para horário móvel não existe a separação de intervalo).  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
