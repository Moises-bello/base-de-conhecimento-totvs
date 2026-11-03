---
article_id: 360015852071
category: RH - Cadastros
content_hash: ff6d8759dac5ffd70d769872f9ad2f30881adc498f3b163c51a0b6b29e7a61f1
fetched_at: '2026-06-28T22:44:52.689518+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Como utilizar a funcionalidade de Contador de
  Faltas no Ponto Eletrônico
type: support-article
updated_at: '2026-02-04T18:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015852071-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-de-Contador-de-Faltas-no-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31777514758167)** **Tempo aproximado para leitura:****00:01:00 min**  
  
**Dúvida**  
Como utilizar a funcionalidade de Contador de Faltas no Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para gerar uma verba de desconto de **Falta** **em Dias** nos Resultados, pode ser utilizado um **Evento Contador.**  
No cadastro de Eventos, existe um campo chamado **Contador (P9\_EVECONT)**, e ele é responsável por contar dentro do período de apontamento a quantidade de ocorrências de Falta.  
  
Será necessário cadastrar um novo Evento que será o **Contador**, e nele, deve ser vinculada uma veba de tipo **DIA** e com **ID de cálculo da Folha 0054 - Falta em Dia**. É importante também que este evento **não tenha ID** de ponto atrelado ao seu cadastro.  
No cadastro do Evento de Falta com ID de Ponto **010A ou 009N**, não deve existir verba atrelada, pois ela deverá ser atrelada somente no cadastro do Evento Contador.  
Além disso, é importante que o campo **Desc. DSR** esteja como SIM **somente** no Evento de Falta **com ID de Ponto** 010A ou 009N.  
  
Para realizar todo este processo, segue exemplo abaixo:  
  
**Evento Contador:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530298524695)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530039349655)  
  
**Evento de Falta 010A:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530039361303)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530039380375)  
  
**Verba 466:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530179133719)  
  
**Importante:** A partir do dia 01/06/2024, o mnemônico P\_SEGFALT (antigo MV\_SEGFALT) passa a ter o conteúdo **automaticamente alterado para .T. , impossibilitando assim o uso desativado.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31777519245079)  
  
Importante também informar que quando é utilizado o Evento Contador de Faltas, **não é possível fazer um abono parcial de horas, apenas total.**  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - GPE - Mnemônico P\_SEGFALT (Antigo MV\_SEGFALT)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23373321713431-RH-Linha-Protheus-GPE-Mnem%C3%B4nico-P-SEGFALT-Antigo-MV-SEGFALT)  
[RH - Linha Protheus - GPE - Funcionamento do mnemônico P\_SEGFALT nas faltas no Controle Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050771994-RH-Linha-Protheus-GPE-Funcionamento-do-mnem%C3%B4nico-P-SEGFALT-nas-faltas-no-Controle-Dias-de-Direito)  
[RH - Linha Protheus - PON - Como utilizar a funcionalidade do Contador de DSR no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051693134-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-do-contador-de-DSR-no-Ponto-Eletr%C3%B4nico)
