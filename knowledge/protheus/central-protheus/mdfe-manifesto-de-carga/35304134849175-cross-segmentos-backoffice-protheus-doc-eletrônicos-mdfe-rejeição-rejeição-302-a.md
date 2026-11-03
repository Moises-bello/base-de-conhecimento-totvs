---
article_id: 35304134849175
category: MDFe - Manifesto de Carga
content_hash: 6777cfb75edd85eebc5887975e7c274b1c8c790f35277297d0dd18204e45b750
fetched_at: '2026-06-28T22:40:08.215524+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Rejeição
  Rejeição 302: As informações de pagamento devem  ser informadas para carga lotação'
type: support-article
updated_at: '2026-01-08T14:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35304134849175-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-Rejei%C3%A7%C3%A3o-302-As-informa%C3%A7%C3%B5es-de-pagamento-devem-ser-informadas-para-carga-lota%C3%A7%C3%A3o
---

**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões.

**Dúvida**

Como solucionar a Rejeição 302: As informações de pagamento devem  ser informadas para carga lotação ?

**Causa**

Se modal rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou transportador que emitirá CTe globalizado (tpEmit=3) ou Transportador Próprio que informou o Tipo de Transportador (tpEmi=2 com tag tpTransp informada) e MDFe possuir apenas um DF-e transportado no grupo infDoc: O grupo de informações do pagamento deve ser informado (infPag

**Solução**

**Para correção da rejeição 302 é necessario informar as informações de pagamento na Aba Produto predominante.**

**Na tela principal da rotina SPEDMDFE clique sobre o MDFe e depois em alterar, após isso vá ate a aba Informações de Pagamento e preencha os campos obrigatórios e Confirme, após isso retransmita o MDFe e monitore.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35304134826135)

Referencia NT 2025.001.
