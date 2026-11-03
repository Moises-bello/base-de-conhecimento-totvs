---
article_id: 4405944751895
category: RH - Cadastros
content_hash: ca542eb2f80a79221d8a16862952afb07e66a733a407a97ab0e93b69baca1397
fetched_at: '2026-06-28T22:44:52.777483+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como ajustar os apontamentos quando o funcionário
  possuí horário móvel e saída expediente antes do horário de intervalo
type: support-article
updated_at: '2025-11-10T12:16:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405944751895-RH-Linha-Protheus-PON-Como-ajustar-os-apontamentos-quando-o-funcion%C3%A1rio-possu%C3%AD-hor%C3%A1rio-m%C3%B3vel-e-sa%C3%ADda-expediente-antes-do-hor%C3%A1rio-de-intervalo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29374007625751) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como ajustar os apontamentos quando o funcionário tem uma saída expediente antes do horário de intervalo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**Quando o funcionário está vinculado em uma Regra de Apontamento que possui um horário de **intervalo móvel**, e ocorre uma **saída expediente antes do intervalo**, o sistema entende que a **primeira saída se refere ao intervalo**, e a **segunda, uma saída expediente**, quando **o correto, seria o contrário**.  
  
Para fazer esse ajuste, será necessário criar uma **Exceção** para esse dia, e vincular uma **outra Regra de Apontamento** que tenha um horário de **intervalo fixo**, desta forma, conseguimos determinar exatamente qual foi o **horário de saída do intervalo**. Segue exemplo abaixo:  
Utilizaremos para este exemplo, um funcionário que está vinculando a um turno das **08h - 12h - 13h - 17h**, e o **intervalo é móvel:**  
  
Num determinado dia, o funcionário teve uma saída expediente das 09h às 09h30 e saiu para o intervalo das 12h30 às 13h30, o sistema gerou os apontamentos abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405939339927)  
  
O cadastro da **Exceção** pode ser por **Funcionário** ou **Período**. Neste caso, será utilizada a **Exceção por Funcionário,** que deve ser criada desta forma:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405939453975)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405939404311)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405944616727)  
  
A **Regra de Apontamento 05**, que foi vinculada ao cadastro de **Exceção**, possui o **intervalo fixo**:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405939470231)  
  
Após o cadastro, é necessário fazer um **reapontamento** das marcações do funcionário, com isso, o sistema atualizará os apontamentos de maneira correta:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405939491223)

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Utilização de exceção por funcionário para escalas de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043030894-RH-Linha-Protheus-PON-Utiliza%C3%A7%C3%A3o-de-exce%C3%A7%C3%A3o-por-funcion%C3%A1rio-para-escalas-de-trabalho)  
[RH - Linha Protheus - PON - Como cadastrar uma exceção por período para trocar o horário e regra de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053939854-RH-Linha-Protheus-PON-Como-cadastrar-uma-exce%C3%A7%C3%A3o-por-per%C3%ADodo-para-trocar-o-hor%C3%A1rio-e-regra-de-apontamento)
