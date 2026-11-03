---
article_id: 360035748813
category: Materiais - Compras (SIGACOM)
content_hash: 28ee591c7fe9e3bb7bd349cf8a49f2d5841c4b897fa4155ea74ba5330087ad19
fetched_at: '2026-06-28T22:41:24.136634+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais Espécies de Documento
  de Entrada geram integração com a Folha?
type: support-article
updated_at: '2022-05-18T21:16:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035748813-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-Esp%C3%A9cies-de-Documento-de-Entrada-geram-integra%C3%A7%C3%A3o-com-a-Folha
---

**Dúvida**

Quais Espécies de Documento de Entrada geram integração com a Folha?  
  
**Ambiente**

Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

A integração do Documento de Entrada com Folha sempre irá ocorrer quando o campo A2\_NUMRA estiver preenchido com a matricula cadastrada na Folha, independente da espécie do documento de entrada.

Conforme a função A103AtuSRK responsável pela integração e em nenhum momento a espécie do documento é validada.

Caso este formato de Integração não atenda às necessidades, poderá ser utilizado o ponto de entrada abaixo:

M103GERT - Define geração do Lançamento Futuro:

<https://tdn.totvs.com/pages/viewpage.action?pageId=6085304>

**Artigos relacionados:**

* [MP - SIGACOM - Gerar registro na SRK a partir do Documento de Entrada com Autônomo - NFA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026158432-MP-SIGACOM-Gerar-registro-na-SRK-a-partir-do-Documento-de-Entrada-com-Aut%C3%B4nomo-NFA)
* [MP - SIGACOM - RPA através de Entrada de NF de Prestação de Serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012650891-MP-SIGACOM-RPA-atrav%C3%A9s-de-Entrada-de-NF-de-Presta%C3%A7%C3%A3o-de-Servi%C3%A7o)
