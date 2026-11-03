---
article_id: 18946817111831
category: RH - Cadastros
content_hash: a0694841bceedf9eb2a76228a75679d18015fcc22d4b214417eaa8fce2b936d8
fetched_at: '2026-06-28T22:44:53.045151+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Nos Tipos de Horas Extras, é gerada mensagem "Este
  evento não foi classificado como Hora Extra"
type: support-article
updated_at: '2025-12-16T13:10:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18946817111831-RH-Linha-Protheus-PON-Nos-Tipos-de-Horas-Extras-%C3%A9-gerada-mensagem-Este-evento-n%C3%A3o-foi-classificado-como-Hora-Extra
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18946807056279)****Tempo aproximado para leitura: 00:01:00 min***  
  
**Dúvida**  
No módulo **Ponto Eletrônico**, ao informar um código de evento na rotina de **Tipos Horas Extras** é apresentado o ***help*** "Atenção! Este evento não foi classificado como Hora Extra."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18946794379159)   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Esse incidente pode ocorrer quando na rotina de **Tipos Horas Extras** é informado um **Código de** **Evento** que não está classificado como **Hora Extra.**  
  
**Solução**  
Para solucionar essa ocorrência, na rotina **Atualizações > Cadastro do Ponto > Tipos Horas Extras**, deve ser informado um **Código de Evento** de **Hora Extra** que esteja com a classificação **1- Hora Extra**, no Cadastro de Eventos.

No exemplo abaixo, foi selecionado o tipo Normal, e quando posicionado nos campos **Cod. Não Aut**. e **Cod. Autoriz**., deve ser informado um código de evento de hora extra. O sistema já carrega os eventos de hora extra que constam cadastrados em seu sistema:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18950454018583)

Lembrando que o **cadastro de Tipos Horas Extras determina** quais serão os eventos gerados de forma automática quando o funcionário realizar horas extras, e que o cadastro dos 08 primeiros tipos é obrigatório, sempre lembrando de **não repetir código de evento** entre os diferentes tipos.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Regras importantes para o cadastro dos Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras?source=search)  
[RH - Linha Protheus - PON - Como gerar eventos Autorizados ou Não Autorizados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406010444567-RH-Linha-Protheus-PON-Como-gerar-eventos-Autorizados-ou-N%C3%A3o-Autorizados)
