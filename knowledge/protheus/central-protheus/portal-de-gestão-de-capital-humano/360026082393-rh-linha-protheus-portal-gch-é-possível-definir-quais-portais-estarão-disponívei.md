---
article_id: 360026082393
category: Portal de Gestão de Capital Humano
content_hash: 9b7e424ab3b7a81c06b7ce4582d38e56818bd84e23e0d047b1d034f3e9dcccc6
fetched_at: '2026-06-28T22:42:58.973638+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - É possível definir quais portais estarão
  disponíveis na tela de login
type: support-article
updated_at: '2022-08-18T11:17:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082393-RH-Linha-Protheus-PORTAL-GCH-%C3%89-poss%C3%ADvel-definir-quais-portais-estar%C3%A3o-dispon%C3%ADveis-na-tela-de-login
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como configurar quais portais estarão disponíveis no campo Tipo (combo) da tela de login?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101003233/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano - Todas as versões  
  
**Solução**Existe sim a possibilidade de utilizar um Ponto de Entrada para fixar qual opção do portal será apresentada. Para isto Utilize a função **User Function PORTSEL().**  
Este ponto de entrada foi criado para configurar quais portais deverão aparecer no campo Tipo (combo) da tela de Login dos Portais.  
  
**Exemplo :** Nesse exemplo deverá aparecer no campo Tipo apenas o Portal RH.

User Function PORTSEL()

Return "1"  
  
**Retorno  
Tipo -** Caracter  
**Descrição** - O retorno deste P.E. deve ter um dos seguintes valores (em caracter):

**0** - Para exibir todos os portais

**1** - Para exibir somente o primeiro Portal (RH)

**2**- Para exibir somente o segundo Portal (PMS)

**3** - Para exibir somente o terceiro Portal (PLS)

**4** - Para exibir somente o quarto Portal (Portal Protheus)  
  
Para mais informações sobre o uso do Ponto de Entrada clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=6804837)  
 **Importante:** O suporte não auxilia em customização, caso precise de auxílio para utilizar o P.E, orientamos o agendamento de um analista in loco.  
  
**Saiba Mais  
[RH - Linha Protheus - PORTAL GCH - Customizar o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045425034)**  
[Artigos Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0)
