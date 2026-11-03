---
article_id: 1500002362442
category: RH - Cadastros
content_hash: 3e352f761ca2f8e164787220e521ba45455ac264a1fce1405ce549fad1439787
fetched_at: '2026-06-28T22:44:52.967650+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Diferença entre Adicional Noturno e Adicional Noturno
  sobre Hora Extra
type: support-article
updated_at: '2026-02-04T18:56:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002362442-RH-Linha-Protheus-PON-Diferen%C3%A7a-entre-Adicional-Noturno-e-Adicional-Noturno-sobre-Hora-Extra
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34313903081751) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual é a diferença entre os Identificadores de ponto **004A - Adicional Noturno** e o **028A - Adicional Noturno sobre Hora Extra?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A finalidade de ambos os identificadores é a mesma, **apurar a quantidade de adicional noturno a pagar para o Funcionário**, porém são demonstrados em situações diferentes.  
  
**Situação 1:**  
Quando a tabela de horário padrão do Funcionário **termina em horário Diurno** e o funcionário faz alguma **hora extra em horário noturno**, normalmente após as 22h00min, o sistema fará a apuração das Horas Extras e consequentemente, o Adicional Noturno sobre as horas extras, ou seja, **vai demonstrar o adicional noturno através do identificador de ponto 028A.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914154087575)**  
  
Evento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914154090647)  
  
**Situação 2:**  
Quando a tabela de horário padrão do Funcionário **termina em horário Noturno,** normalmente após as 22h00min, o sistema fará a apuração das **Horas normais trabalhadas** e consequentemente, o Adicional Noturno sobre as horas normais, ou seja, **vai demonstrar o adicional noturno através do identificador de ponto 004A.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914154092951)**  
  
Evento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914154094743)  
  
**Situação 3:**  
Quando a tabela de horário padrão do funcionário **termina em horário Noturno,** normalmente após as 22h00min, **porém ele também faz alguma hora extra noturna** o sistema fará a apuração das **Horas normais trabalhadas,** do **Adicional Noturno sobre as horas normais** bem como a apuração das **Horas Extras** e do **Adicional Noturno sobre as horas extras**, ou seja, vai demonstrar o **adicional noturno sobre as horas normais** através do identificador de ponto **004A** e o **adicional noturno sobre as horas extras** através do identificador de ponto **028A.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31914154095895)**  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
