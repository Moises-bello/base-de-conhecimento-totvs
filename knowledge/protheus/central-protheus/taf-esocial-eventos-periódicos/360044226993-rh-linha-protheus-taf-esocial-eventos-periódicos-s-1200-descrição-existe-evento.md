---
article_id: 360044226993
category: TAF - eSocial - Eventos Periódicos
content_hash: dcde9366e456e102197d6988f3564938a910621f0f319ff091b82700ec9d2acc
fetched_at: '2026-06-28T22:45:18.998253+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - Descrição:
  Existe evento de pagamento associado que será impactado pelo evento retificador.'
type: support-article
updated_at: '2026-06-23T21:01:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044226993-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-Descri%C3%A7%C3%A3o-Existe-evento-de-pagamento-associado-que-ser%C3%A1-impactado-pelo-evento-retificador
---

**Dúvida**O que fazer quando acontecer a inconsistência 989 ao enviar o evento S-1200 ?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23701178357527)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1200 - Todas as versões

**Solução**

Ao retificar um S-1200 existindo um S-1210 enviado ao RET no período para o funcionário, é necessário que seja transmitido o evento S-3000 (exclusão) do S-1210 antes que seja enviado a retificação do S-1200.

O RET não aceitará o S-1200 pois existe uma ordem cronológica de envio, primeiro o S-1200 e depois o S-1210.

Após enviar o S-3000 do S-1210, você poderá retificar o S-1200 que o RET aceitará o mesmo.
