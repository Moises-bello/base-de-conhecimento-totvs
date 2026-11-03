---
article_id: 4406010444567
category: RH - Cadastros
content_hash: 8e28f27c4ef2ef89bec13898e26ba16e165695b0a65f98a119493a8b96a5a3ec
fetched_at: '2026-06-28T22:44:52.890552+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar eventos Autorizados ou Não Autorizados
type: support-article
updated_at: '2026-02-24T20:45:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406010444567-RH-Linha-Protheus-PON-Como-gerar-eventos-Autorizados-ou-N%C3%A3o-Autorizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19222852296087) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como gerar eventos Autorizados ou Não Autorizados nos apontamentos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O que determina se os eventos serão apontados como **Autorizados** ou **Não Autorizados** é o cadastro da Regra de Apontamento. Se nos campos relatados abaixo deixarmos como **SIM**, serão gerados eventos **Autorizados**, se deixarmos como **NÃO**, serão gerados eventos **Não Autorizados**.  
  
Para os eventos de provento**,** em **Atualizações - Cadastro do Ponto - Regra de Apontamento - Apontamentos** existem os campos abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222860241431)  
  
- **Pg. Ad. Not** (PA\_ADNOT) = este campo serve para determinar em qual **ID** **de Ponto** será gerado o **Adicional Noturno.** Se estiver como **SIM**, será apontado o **ID 004A**, se estiver como **NÃO**, será apontado o **ID 003N**;  
  
- **Pg. Ad. Not. Ex**. (PA\_ADNOTEX) = este campo serve para determinar em qual **ID de Ponto** será gerado o **Adicional Noturno sobre Horas Extras.** Se estiver como **SIM**, será apontado o **ID 028A**, se estiver como **NÃO**, será apontado o **ID 027N**;  
  
- **Pg. Hora. Ext.** (PA\_PAGHEXT) = este campo serve para determinar em **quais batidas de dias Trabalhados**, a **Hora Extra** deve ser apontada como evento **Autorizado** ou **Não Autorizado**. Utilizando o print desta documentação como exemplo, e levando em consideração um turno que tenha 4 batidas no dia, o sistema entenderá que: para as marcações do **intervalo** (1ª saída e 2ª entrada) , caso o funcionário realize **Hora Extra**, será apontado em evento **Não Autorizado**, mas se ocorrer **Hora Extra** em **qualquer outra batida do dia**, serão apontados eventos **Autorizados**;  
  
- **Pg. He. Dia Nt.** (PA\_PAGHEDNT) = este campo serve para determinar em quais dias **Não Trabalhados**, as **Horas Extras** serão apontadas com eventos **Autorizados** ou **Não Autorizados**. Utilizando o print desta documentação como exemplo, todos os dias Não Trabalhados estão assinalados (**Compensado, DSR, Feriado e Não Trabalhado**), ou seja, se o funcionário trabalhar em qualquer um desses dias, os eventos de Horas Extras serão apontados como **Autorizados**. Caso as opções estejam **desmarcadas**, as Horas Extras nestes dias serão apontadas como **Não Autorizadas**.  
  
Lembrando que para as **Horas Extras**, é de **extrema importância** que o cadastro dos **Tipos de Horas Extras** esteja feito de maneira correta, ou seja: os oito primeiros tipos cadastrados e sem repetição de eventos, [conforme orientações desta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras)  
  
Para os eventos de **desconto**, existem os campos abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222852316439)  
  
- **Desc. DSR** (PA\_DESCDSR) = este campo serve para determinar em qual **ID** **de Ponto** será gerado o **desconto de DSR**. Se estiver como **SIM**, será apontado o **ID 018A**, se estiver como **NÃO**, será apontado o **ID 017N**;  
  
- **Desc. Faltas** (PA\_FALTAS) = este campo serve pra determinar em quais **IDs de Ponto** serão gerados os **descontos de** **Falta Integral** e **Falta 1/2 Período**.   
Para a **Falta Integral**: Se estiver como **SIM**, será apontado o **ID 010A**, se estiver como **NÃO**, será apontado o **ID 009N**.   
  
Para a **Falta 1/2 Período**: Se estiver como **SIM**, será apontado o **ID 008A**, se estiver como **NÃO**, será apontado o **ID 007N.**  
  
- **Desc. Atrasos (**PA\_ATRASOS) = este campo serve para determinar em qual **ID de Ponto** será gerado o **desconto de Atraso**. Se estiver como **SIM**, será apontado o **ID 012A**, se estiver como **NÃO**, será apontado o **ID 011N**;  
  
- **Desc. S. Antec.** (PA\_SAIANT) = este campo serve para determinar em qual **ID de Ponto** será gerado o **desconto de Saída Antecipada**. Se estiver como **SIM**, será apontado o **ID 014A**, se estiver como **NÃO**, será apontado o **ID 013N**;  
  
- **Desc. S. Exped.** (PA\_SAIEXPE) = este campo serve para determinar em qual **ID de Ponto** será gerado o **desconto de Saída Expediente**. Se estiver como **SIM**, será apontado o **ID 020A**, se estiver como **NÃO**, será apontado o **ID 019N**.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
