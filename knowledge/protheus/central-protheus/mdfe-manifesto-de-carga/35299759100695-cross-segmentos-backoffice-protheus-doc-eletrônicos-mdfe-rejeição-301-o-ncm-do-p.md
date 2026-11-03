---
article_id: 35299759100695
category: MDFe - Manifesto de Carga
content_hash: 98e3b75d6d2cba7f1e11b7dfa985e7f580f8e4b85adbf5707b6188313845df93
fetched_at: '2026-06-28T22:40:08.213108+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Rejeição
  301: O NCM do produto predominante da  carga lotação deve ser informado'
type: support-article
updated_at: '2025-09-30T14:46:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35299759100695-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-301-O-NCM-do-produto-predominante-da-carga-lota%C3%A7%C3%A3o-deve-ser-informado
---

**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões

**Dúvida**

Como solucionar a Rejeição 301: O NCM do produto predominante da  carga lotação deve ser informado?

**Causa**

Se modal rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou transportador que emitirá CTe globalizado (tpEmit=3) ou Transportador Próprio que informou o Tipo de Transportador (tpEmi=2 com tag tpTransp informada) e MDFe possuir apenas um DF-e transportado no grupo infDoc: O campo NCM do grupo produto predominante deverá ser informado

**Solução**

Para correção da rejeição 301 é necessario informar o NCM na Aba Produto predominante.

Na tela principal da rotina **SPEDMDFE** clique sobre o MDFe e depois em alterar, após isso vá ate a aba **Produto Predominante** e informe o **NCM** e salve, após isso retransmita o MDFe e monitore.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35299759084823)

Referencia NT 2025.001.
