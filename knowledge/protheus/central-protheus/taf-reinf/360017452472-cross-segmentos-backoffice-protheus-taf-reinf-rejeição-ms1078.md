---
article_id: 360017452472
category: TAF - REINF
content_hash: 2947a85d3944b63615c403afbca9d547f661663e33b1e8f38ab7a290e543ecee
fetched_at: '2026-06-28T22:41:34.835551+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1078
type: support-article
updated_at: '2023-04-04T12:03:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017452472-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1078
---

**Ocorrência**

Ao transmitir um evento da Reinf, é rejeitado com a seguinte mensagem:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047530773/mceclip0.png)**

**Ambiente**TAF -  A partir de 12.1.17  
  
**Solução**Esse erro ocorre, pois a Receita ainda não processou ou ainda não enviou o protocolo de fechamento.

Quando ocorrer o erro MS1078, a recomendação é que seja feita reabertura do período, e após envio do evento R-2099 (Fechamento).

Acesse **Apuração dos Eventos execute** o botão **Reabertura Período.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047530853/mceclip1.png)

Acesse **Monitor** e transmita o evento do R-2098.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047530973/mceclip2.png)

Após processe o R-2099 e transmita novamente o evento.

**Saiba mais**[Evento R-2098](http://tdn.totvs.com/display/public/TAF/EFD-Reinf#EFD-Reinf-EventoR-2098%E2%86%92ReaberturadosEventosPeri%C3%B3dicos)[Rejeições da Receita - Reinf](http://tdn.totvs.com/pages/releaseview.action?pageId=366646855)
