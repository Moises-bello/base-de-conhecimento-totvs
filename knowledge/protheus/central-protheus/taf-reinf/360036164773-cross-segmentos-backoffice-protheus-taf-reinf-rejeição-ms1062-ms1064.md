---
article_id: 360036164773
category: TAF - REINF
content_hash: 242fd9e5ce0c3a0bc7b970d1db5a0f041b559161ef507af3620195f1542e4943
fetched_at: '2026-06-28T22:41:34.828620+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1062/ MS1064
type: support-article
updated_at: '2023-04-04T11:52:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164773-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1062-MS1064
---

**Ocorrência**

Ao Transmitir o fechamento do período R-2099, o evento é retornado com a seguinte rejeição:

\*\* Foram enviados eventos(R-2010, R-2020) - Retenção contribuição previdenciária no período de apuração informado\*\*

**Ambiente**

TAF - SIGATAF - A partir do 12.1.17  
  
**Causa**Ao processar o evento R-2099, ele é gerado com ou sem movimento de acordo com os eventos transmitidos e monitorados no TAF.

Ou seja, se no período for enviado o R-2010, para que o R-2099 considere esse evento, ele precisa estar monitorado no TAF, caso contrário o R-2099 é gerado como sem movimento para o R-2010, causando a rejeição acima.

EX:

No caso do R-2010, o problema ocorre quando o evento foi transmitido mas está com a seguinte legenda:

![Aguardando_retorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606084962199)  
  
**Solução**

Para solucionar essa ocorrência, realizar o seguinte procedimento:

1. O Evento R-2010 precisa estar com status "AUTORIZADO", clique em aguardando governo e consulte o retorno do evento.

![consulta_retorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606128539031)

2. Após consultar o retorno do evento e o status atualizar para "AUTORIZADO" , realize a exclusão inconsistente do evento R-2099 apure e transmita novamente.

![Autorizado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606185552151)

**Importante: Nos casos em que a transmissão do evento foi feita diretamente pela Receita Federal (e-Cac), mas o fechamento ocorrer pelo TAF, será necessário a intervenção de um Analista In Loco para o ajuste dos recibos, pois a Receita Federal não disponibiliza uma URL para que o TAF consulte eventos que foram transmitidos pelo e-Cac.**
