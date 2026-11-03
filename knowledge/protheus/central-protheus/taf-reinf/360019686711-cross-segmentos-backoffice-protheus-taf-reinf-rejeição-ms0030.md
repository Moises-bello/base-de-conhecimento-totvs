---
article_id: 360019686711
category: TAF - REINF
content_hash: 1692a529732224c3c33175b05b52667acb445561f8076e2e75f115c720289ada
fetched_at: '2026-06-28T22:41:34.813921+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS0030
type: support-article
updated_at: '2023-10-18T16:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019686711-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS0030
---

**Ocorrência**

Ao transmitir um evento da REINF, é rejeitado com a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17300856356887)

**Ambiente** TAF - Release 12.1.33 e superior

**Causa**

**PRODUÇÂO LAYOUT 2\_01\_02**

Esse erro está ocorrendo devido a alteração do layout**2\_01\_02 em base de produção,**  o mesmo entrou em em vigor na  Produção no dia 21/09/2023

**Solução PRODUÇÃO**

Alterar o conteúdo do parâmetro MV\_TAFVLRE, deixando-o com o seguinte valor:

2\_01\_02

* [TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

E somente após realizar a transmissão do evento em questão.

Caso aconteça a mesma inconsistência faça o procedimento abaixo:

 Vá em Eventos REINF:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015248472)

Selecione o evento que está com o problema e realize a exclusão do evento:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015248632)

Após, faça um nova apuração e o transmita.
