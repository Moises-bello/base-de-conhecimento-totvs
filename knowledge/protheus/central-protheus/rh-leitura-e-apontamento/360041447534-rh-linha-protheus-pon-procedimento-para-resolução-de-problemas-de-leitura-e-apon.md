---
article_id: 360041447534
category: RH - Leitura e Apontamento
content_hash: 7827c832364f3e4d21a417045e2c87f3fb081f9e874bd450b03cfd10fe0c96d4
fetched_at: '2026-06-28T22:44:45.999468+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Procedimento para resolução de problemas de leitura
  e apontamento de marcações em dias compensados ou DSR
type: support-article
updated_at: '2025-10-06T13:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041447534-RH-Linha-Protheus-PON-Procedimento-para-resolu%C3%A7%C3%A3o-de-problemas-de-leitura-e-apontamento-de-marca%C3%A7%C3%B5es-em-dias-compensados-ou-DSR
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35435090049431) Tempo aproximado para leitura: 00:01:30 min**Ocorrência**Quando o cliente realiza a leitura e o apontamento das marcações de um determinado período, o sistema desconsidera as marcações realizadas em dias compensados ou DSRs no módulo SIGAPON.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões

**Causa**A causa para o sistema alocar incorretamente as marcações realizadas em dias não trabalhados, como tipos de dias compensados e DSRs é o fato do cliente não ter os horários cadastrados na tabela de horário padrão para esses dias.  
  
Partindo do princípio de que é necessário que haja um horário estipulado para que o sistema aloque as batidas corretamente e aponte os eventos a serem gerados nos apontamentos (horas extras, DSR, compensadas etc.). Portanto, para que o sistema posicione corretamente as batidas na rotina de marcações e gere as horas devidas, é necessário que exista, na tabela de horário padrão, um horário estipulado para a jornada do colaborador.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o SIGAPON, em **Atualizações > Cadastro do ponto > Tabela de horário padrão**. Conforme descrito acima, o cadastro da tabela de horário padrão precisa conter todos os horários preenchidos, **mesmo para os dias não trabalhados**, como tipo dia Compensado e DSR. Veja como deve ficar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32079858023447)

O lançamento de horários para esses dias não alterará o apontamento dos eventos de horas extras realizados na data.

**Exemplo:**  
Colaborador trabalhou no sábado compensado, realizando o seguinte horário: 08:00 - 12:00. Para esse apontamento, o sistema gerará integralmente as 04:00 horas compensadas trabalhadas pelo colaborador, caso o cliente tenha esse tipo de hora extra cadastrado na rotina de tipos de hora extra:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32079826860055)

Para ordenar as marcações, o cliente deve apontá-las via **Leitura e Apontamento (PONM010)** de marcações, informando a opção de apontamento na pergunta **“Processamento?”**. Dessa forma, as tabelas SP8 e SPJ serão novamente validadas e as marcações serão reordenadas.

****Saiba mais:  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)****[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)
