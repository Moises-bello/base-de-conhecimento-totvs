---
article_id: 1500002754861
category: RH - Cadastros
content_hash: 55726d7c0457ad73489438ac6d4898c06437eb4cd70b96286c1130c73892ff5a
fetched_at: '2026-06-28T22:44:53.012783+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidades dos campos de Limite inferior e
  Limite superior na Tabela de Horário Padrão
type: support-article
updated_at: '2026-02-04T14:22:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35191081032215) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual é a funcionalidade dos campos Limite Inferior e Limite Superior na Tabela de Horário Padrão?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Na Tabela de Horário Padrão, acessando o módulo SIGAPON, em **Atualizações - Cadastro do Ponto - Tabela de Horário Padrão**, temos dois campos que, por vezes, geram dúvidas quanto aos seus preenchimentos, que são **PJ\_HORMENO** e **PJ\_HORMAIS**, respectivamente, **Limite Inferior e Limite Superior:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31998647816983)  
  
A funcionalidade dos campos é para determinar ao Sistema, quantas horas **antes do início** e, quantas horas **após o fim da jornada** do trabalho, o funcionário registrará a marcação e esse dado será utilizado para o mesmo dia da leitura para montagem do calendário e posicionamento das batidas.  
  
Em tese, faremos **a soma do total do Limite Inferior + Horas Trabalhadas + Intervalo + Limite Superior** e, essa precisa ser de até **23:59**, respeitando sempre, o horário de entrada e o de saída da jornada diária.  
  
Levando em consideração o exemplo acima:  
**- Entrada do funcionário:** 07:00  
**- Limite Inferior (PJ\_HORMENO):** 07:00 horas antes da entrada (00:00 às 07:00)  
**- Limite Superior (PJ\_HORMAIS):** 06:59 após o término da jornada (17:00 às 23:59)  
**- Horas Trabalhadas:** 09:00  
**- Intervalo:** 01:00

**Cálculo total das 24 horas diárias:**  
07:00 (Limite Inferior) + 09:00 (Horas Trabalhadas) + 01:00 (Intervalo) + 06:59 (Limite Superior) = 23:59  
  
Quando temos uma **tabela de horário padrão que, envolva horário noturno**, é importante verificarmos os campos abaixo para totalizar corretamente os **limites inferior e superior**, tendo sempre como base o horário noturno do funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31998647818135)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)  
[RH - Linha Protheus - PON - Como incluir uma Sequência na Tabela de Horário Padrão já cadastrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18327885648151-RH-Linha-Protheus-PON-Como-incluir-uma-Sequ%C3%AAncia-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-j%C3%A1-cadastrada)  
[RH - Linha Protheus - PON - Help: TPADNCAD - Tabela de Horário Padrão não cadastrada para o turno corrente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055399773-RH-Linha-Protheus-PON-Help-TPADNCAD-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-n%C3%A3o-cadastrada-para-o-turno-corrente)
