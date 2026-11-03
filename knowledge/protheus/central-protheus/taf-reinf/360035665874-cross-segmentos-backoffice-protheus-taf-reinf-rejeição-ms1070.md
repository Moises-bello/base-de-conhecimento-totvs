---
article_id: 360035665874
category: TAF - REINF
content_hash: ce36c3ef7264b1435d91e86cec928d2cf358acac7415e6b448ff4718457254d4
fetched_at: '2026-06-28T22:41:34.832066+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1070
type: support-article
updated_at: '2023-04-04T12:02:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035665874-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1070
---

**Ocorrência**

Ao Transmitir o fechamento do período R-2099, o evento é retornado com a seguinte rejeição:

![ms1070.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046518934/ms1070.png)

**Ambiente**

TAF - SIGATAF - A partir do 12.1.33  
  
**Causa**Ao processar o evento R-2099, ele é gerado com ou sem movimento de acordo com os eventos transmitidos e monitorados no TAF.

Ou seja, se no período for enviado o R-2050, para que o R-2099 considere esse evento, ele precisa estar monitorado no TAF, caso contrário o R-2099 é gerado como sem movimento para o R-2020, causando a rejeição acima.

No caso do R-2050, o problema ocorre quando o evento foi transmitido mas está com a seguinte legenda:

![Aguardando_retorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606330108183)

**Solução**

Para solucionar essa ocorrência, realizar o seguinte procedimento:

1. O Evento R-2050 precisa estar com status "AUTORIZADO", clique em aguardando governo e consulte o retorno do evento.

![consulta_retorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606370305815)

2. Após consultar o retorno do evento e o status atualizar para "AUTORIZADO" , realize a exclusão inconsistente do evento R-2099 apure e transmita novamente. 

![Autorizado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606426141975)

**Importante: Nos casos em que a transmissão do evento foi feita diretamente pela Receita Federal (e-Cac), mas o fechamento ocorrer pelo TAF, será necessário a intervenção de um Analista In Loco para o ajuste dos recibos, pois a Receita Federal não disponibiliza uma URL para que o TAF consulte eventos que foram transmitidos pelo e-Cac.**
