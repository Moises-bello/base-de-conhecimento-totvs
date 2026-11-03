---
article_id: 4406011766423
category: RH - Cadastros
content_hash: 01c3e230ec97f6155071408078e5cd8c1a8134872cc8af38a796c9315f29ae25
fetched_at: '2026-06-28T22:44:53.097953+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Qual a funcionalidade do campo Considera Marcação
  da Regra de Apontamento
type: support-article
updated_at: '2025-12-29T11:59:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406011766423-RH-Linha-Protheus-PON-Qual-a-funcionalidade-do-campo-Considera-Marca%C3%A7%C3%A3o-da-Regra-de-Apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29374065156247) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Qual a funcionalidade do campo **Considera Marcação** da Regra de Apontamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**  
No cadastro de **Regra de Apontamento**, **aba Outros**, existe o campo **Considera Marcação** que possui duas opções: **Entrada e Saída**.   
A **finalidade dele** é determinar **qual dia** será utilizado para o **Apontamento dos Eventos**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406010657943)

Para um **turno Diurno** não há diferença se este campo estiver como Entrada ou Saída, mas para turnos Noturnos sim, visto que a jornada inicia em um dia e finaliza no outro.

A primeira diferença visível pode ser observada nas rotinas de manutenção, como por exemplo, a rotina de Marcações. É possível verificar que existem duas colunas de data: a coluna de **Data Referência**, que mostra o dia em que o funcionário finalizou a jornada, e a coluna de **Data 1ª Entrada**, que mostra o dia em que o funcionário iniciou a jornada.![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406011291671)  
  
Os **apontamentos**, como explicado anteriormente, serão **gerados** com base na data de **saída do expediente**. Para termos um exemplo, vamos utilizar um turno que os dias trabalhados são de **Segunda à Sexta-feira** com horário das **22h às 05h**, **Sábado** é um dia **Compensado** e **Domingo DSR.**  
  
Veja que o **apontamento** do dia **02.07**, corresponde a jornada **iniciada no dia 01** e **finalizada no dia 02:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406011504791)  
  
  
Neste caso, a jornada iniciou na **Sexta**, dia **02**, e finalizou no **Sábado**, dia **03**, portanto, os **apontamentos** foram gerados com base no dia **03**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406011623959)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como alterar a Regra de Apontamento de um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18869900945687-RH-Linha-Protheus-PON-Como-alterar-a-Regra-de-Apontamento-de-um-Funcion%C3%A1rio)
