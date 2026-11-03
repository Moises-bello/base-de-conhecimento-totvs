---
article_id: 360014625691
category: RH - Lançamentos
content_hash: d1bc2593bafd5816017e18a7f683afa549db9052caada418f7048c958ca735c3
fetched_at: '2026-06-28T22:44:46.798267+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como apontar a Interjornada
type: support-article
updated_at: '2025-10-21T20:50:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014625691-RH-Linha-Protheus-PON-Como-apontar-a-Interjornada
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31941378350999) Tempo aproximado para leitura: 00:02:00 min**  
  
Dúvida**Como apontar a Interjornada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A CLT orienta que o funcionário tenha um descanso de 11h entre o término de uma jornada e o início da próxima em dias trabalhados. Caso não seja possível este descanso por completo, o Ponto Eletrônico deverá gerar **Hora Extra Interjornada** para o funcionário.  
  
No Ponto Eletrônico, o evento de Hora Extra Interjornada pode ser apontado através dos IDs **029A** ou **038N.**  
Para que seja apontado o ID 029A, na Regra de Apontamento os campos **Pg. Hora Ext. e Pg. He. Dia Nt**. devem estar **marcados**, ou seja, indicando que os eventos de Horas Extras serão apontados como **Autorizados.**  
Para que seja apontado o ID 038N, na Regra de Apontamento os campos **Pg. Hora Ext. e Pg. He. Dia Nt.** devem estar **desmarcados**, ou seja, indicando que os eventos de Horas Extras serão apontados como **Não Autorizados.**  
  
Para gerar a **Hora Extra Interjornada**, realize os seguintes passos:  
  
**1 -** Cadastrar os **Eventos** e vincular aos IDs de Ponto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20196007377431)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20196020247831)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20196007402135)  
  
OBS: no campo **Cod. p/ Folha** deve ser vinculada uma Verba de sua escolha  
  
  
**2 -** No cadastro do **Turnos de Trabalho**, em Atualizações-Cadastros-Gerais-Turnos de Trabalho,deve ser definida a quantidade de horas de Interjornada através do campo **Hr. Inter. Jor.**  
O campo **Tp. Dia. In. Jo.** aponta se nos dias não trabalhados deve ser apontada a Hora Extra Interjornada. Recomendamos que todas as opções estejam marcadas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14438974665495)  
Ainda no cadastro de **Turnos de Trabalho** existem mais dois campos que precisam atentar-se nas configurações para aplicação da HE Interjornada entre os dias de DSR's e Feriados. Veja conforme cada documentação abaixo:  
[Cálculo da Interjornada quando temos um dia de DSR entre os dias que tiveram jornada trabalhada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004089441-RH-Linha-Protheus-PON-C%C3%A1lculo-da-Interjornada-quando-temos-um-dia-de-DSR-entre-os-dias-que-tiveram-jornada-trabalhada)Cálculo da Interjornada quando temos um dia de Feriado entre os dias que tiveram jornada trabalhada

**3 -** Na **Tabela de Horário Padrão**, é necessário ter o cadastro de horário em todos os dias, mesmo os não trabalhados:  
![58.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009780752)  
  
Com base nestes cadastros, caso o funcionário não tenha o descanso de 11h de uma jornada para outra, ambas em dias Trabalhados, o sistema apontará o evento com a quantidade de horas faltantes deste descanso.  
  
**Veja um exemplo abaixo de como é feito o cálculo:**  
- no dia 04.12, o funcionário finalizou o expediente às 23h. A partir deste horário, começa a contagem das 11h de descanso da Interjornada;  
- no dia 05.12, o funcionário iniciou o expediente às 08h, porém, com as 11h de descanso iniciando às 23h do dia anterior, ele deveria ter iniciado às 10h, portanto, o sistema aponta estas 02h de diferença como Interjornada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20196020278167)  
  
 **Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Cálculo da interjornada quando temos um dia de DSR entre os dias que tiveram jornada trabalhada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004089441-RH-Linha-Protheus-PON-C%C3%A1lculo-da-interjornada-quando-temos-um-dia-de-DSR-entre-os-dias-que-tiveram-jornada-trabalhada?source=search)
