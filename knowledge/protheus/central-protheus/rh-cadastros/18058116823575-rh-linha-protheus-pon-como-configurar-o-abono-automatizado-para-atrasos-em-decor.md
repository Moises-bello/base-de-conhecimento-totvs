---
article_id: 18058116823575
category: RH - Cadastros
content_hash: 5655dec6b803c4b268e2c6694c904712da7c37ace32aaa3b3f599bdd1474f5fc
fetched_at: '2026-06-28T22:44:52.832659+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar o abono automatizado para atrasos
  em decorrência de hora extra interjornada
type: support-article
updated_at: '2026-02-04T19:18:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18058116823575-RH-Linha-Protheus-PON-Como-configurar-o-abono-automatizado-para-atrasos-em-decorr%C3%AAncia-de-hora-extra-interjornada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18058092003735) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configurar o **abono automatizado para atrasos** em decorrência de **hora extra interjornada**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Solução**  
Com essa funcionalidade, o sistema verificará se restou um saldo de horas para o funcionário (referente ao intervalo entre jornadas). Caso exista um saldo de horas e no dia seguinte ocorra um atraso, o sistema abona o primeiro atraso ocorrido no dia com base neste saldo de horas.

Segue exemplo:  
**Atualizações > Cadastro de ponto > Tabela de horário padrão**, filtre o Turno desejado.  
Horário fixo das 08:00 - 12:00 - 13:00 - 17:00:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18056153473815)  
  
No Turno, em **Atualizações > Cadastros Gerais > Turno de trabalho**, filtre o Turno desejado e configure o campo **Hr. Inter Jor**, que deve constar com o intervalo de descanso interjornada de 11:00.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18056247601687)  
  
Ainda no **Turno** na aba **Outros** e no campo **Mot Abon Int- R6\_ABINTJ** informe um código de abono vinculado para abono interjornada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18056304470807)  
  
Acessando a tela de Integrados, em **Atualizações > Lançamentos > Integrados**, filtre o funcionário e entre em **Outras ações > Alterar**.

Veja o cenário: o funcionário efetuará marcação no dia **04/09/2023**, com a saída às **02hs** do dia **05/09/2023**.  
No dia **05/09/2023**, chegará atrasado, marcando sua entrada às **10hs**.

O sistema efetuará o seguinte cálculo:  
**02hs + 11hs (intervalo) = 13hs.**

Ou seja, no dia **05/09/2023** ele poderia entrar às **13hs**.  
A diferença entre **13hs** e o horário da primeira entrada (**08hs**) resulta em **5hs**.

Ou seja, o funcionário tem **5hs de saldo** para abonar o atraso.  
Desta forma, o sistema abonará as **2hs de atraso** dele e as **3hs restantes** seriam concedidas como **hora extra**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18057157019415)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18057131488279)  
  
**\*\*Importante salientar que esse abono é gerado somente em caso de atrasos, em situações que houver faltas ele não é gerado**  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
