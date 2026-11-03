---
article_id: 360054849114
category: Manutenção de Ativos (SIGAMNT)
content_hash: 71aacb9dbdae2abacf864d2cd470f4c9e5c41a5ddbd6ac321d32d472a1c7bf2f
fetched_at: '2026-06-28T22:42:33.111407+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Datas utilizadas no Mapa de Manutenção
type: support-article
updated_at: '2021-06-29T16:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054849114-Manufatura-Linha-Protheus-MNT-Datas-utilizadas-no-Mapa-de-Manuten%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Por que quando a **O.S - Ordem de Serviço** do **Plano de Manutenção** não está realizada é utilizada a data prevista e ao finalizar a **O.S** a data é alterada?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Foi identificado que, quando é finalizada uma **O.S** de **Plano de Manutenção**, a data de previsão é alterada para uma data diferente da inicialmente registrada, como se estivesse sendo mudado o histórico da data de previsão do **Plano de Manutenção**.  
  
**Exemplo**  
**Plano de Manutenção** de 12 meses com intervalo de 2 meses.   
Última manutenção realizada em 05/11 do ano anterior com as duas primeiras **O.S** finalizadas.  
**Previsto.....:** 05/01 - 05/03 - 03/06 - 03/08 - 03/10 - 03/12  
**Realizado..:** 03/02 - 03/04 -   
  
Ao finalizar a terceira **O.S** prevista, as datas previstas são reprogramadas para:  
**Previsto.....:** 05/01 - 05/03 - 05/05 - 30/08 - 30/10 - 30/12  
**Realizado..:** 03/02 - 03/04 - 30/06  
  
**Conceito**Enquanto o **Plano de Manutenção** não possuir ordens de serviço finalizadas ele segue as datas de manutenção prevista início **TJ\_DTMPINI - Data Inicio Manut. Prev.**   
Quando a **O.S** for finalizada, ou seja, quando se buscar o histórico, o **Mapa de Manutenção** observará a data original **TJ\_DTORIGI - Data Original Ordem Serv.** da **O.S**. A data original da **O.S** somente é utilizada após a **O.S** ser encerrada.  
A data prevista pode ser alterada manualmente, contudo, para que se mantenha o histórico de datas e com os dados íntegros é utilizada a **Data original** que não pode ser alterada.
