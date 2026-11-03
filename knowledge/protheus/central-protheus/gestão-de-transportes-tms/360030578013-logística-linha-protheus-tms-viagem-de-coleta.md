---
article_id: 360030578013
category: Gestão de Transportes (TMS)
content_hash: 81643eb07e25b667e746658a9427953b7c41f87d4e042b7ff44fcb447471171c
fetched_at: '2026-06-28T22:45:33.480490+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Viagem de coleta
type: support-article
updated_at: '2026-05-04T18:03:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030578013-Log%C3%ADstica-Linha-Protheus-TMS-Viagem-de-coleta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086762519)*** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar uma **viagem de coleta?**  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**  
Para gerar uma **viagem de coleta** é necessário:

* Cadastrar um **Solicitante - TMSA440;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086764439)

* Gerar a **Solicitação de Coleta - TMSA460**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048075785111)

* Vincular a **Solicitação de Coleta** à uma **Viagem de Coleta - TMSA144A**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048075785751)

* Informar o veículo no complemento da viagem em **Outras Ações > Comp. Via**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086766231)

* Fechar a viagem;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086766999)

* Realizar os apontamentos das **Operações - TMSA350;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086767511)

Durante o percurso da **Viagem de Coleta**, se surgirem novas **Solicitações de Coleta**, basta acessar a viagem que está com o status **Em Trânsito - legenda amarela** e adicionar as novas **Solicitações de Coleta**.  
No exemplo abaixo, adicionamos duas novas solicitações com status Em Aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40218937748631)

* Incluir o **Registro de Ocorrência - TMSA360;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048075788183)

* Encerrar a viagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27048086768279)

​Com isso, a solicitação de coleta passará para o *status* **Encerrada**, o que permite, se necessário, vincular a solicitação de coleta na digitação da **Nota Fiscal do cliente.**

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042905073)

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042057274)

**Saiba mais**  
Informações sobre parâmetros da viagem de coleta poderão ser acessadas no *link*: [Logística - Linha Protheus - TMS - Principais parâmetros Viagem Coleta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050303174)  
Informações sobre a rotina Solicitantes: [Solicitantes (TMSA440 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=516214135)  
Informações sobre a digitação da nota fiscal: [Entrada de Documentos de Clientes (TMSA050 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=485881053)  
Informações sobre Registro de ocorrências: [Registro de Ocorrências (TMSA360 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=505767665)  
Informações sobre a rotina de Viagem de coleta: [Viagem - Modelo 2 - Rodoviário Coleta (TMSA144A - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=550329042)
