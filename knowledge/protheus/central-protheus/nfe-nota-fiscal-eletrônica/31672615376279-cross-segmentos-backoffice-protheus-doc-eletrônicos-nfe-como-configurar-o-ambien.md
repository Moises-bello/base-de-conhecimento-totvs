---
article_id: 31672615376279
category: NFe - Nota Fiscal Eletrônica
content_hash: 5a1a38714873149bf64a9280aa0f3ea2e236b2a4aed8a40f6bb813e9ad950c3b
fetched_at: '2026-06-28T22:40:06.902506+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Como configurar
  o ambiente para emissão em contingência?
type: support-article
updated_at: '2025-04-28T11:41:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31672615376279-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Como-configurar-o-ambiente-para-emiss%C3%A3o-em-conting%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31672675755927) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como configurar o ambiente para emissão em contingência?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

A emissão em contingência é efetuada quando há interrupção da internet na empresa ou quando a SEFAZ autoriza a emissão em contingência por indisponibilidade dos seus serviços.

No caso de falta de internet, a emissão a ser utilizada deve ser a off-line. Já nas demais contingências, a SEFAZ informará qual contingência deve ser utilizada.

A configuração deve ser efetuada no modulo Faturamento>NFESEFAZ>Outras ações>Paramêtros>NFE

![svcan modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31672675757847)

**\*Importante\*\***

Uma nota emitida em contingência **não deve ser retransmitida em outra modalidade**.  
A modalidade da nota compõe a chave, se houver retransmissão em modalidades diferentes, será gerada uma nova chave e o processo entrará em duplicidade.

**Lembrando que a modalidade de contingência 5 – Contingência DPEC/EPEC deve ser utilizada apenas se for orientado pela SEFAZ**, pois, ao utilizar essa opção indevidamente, o evento fica registrado, mas não vinculado, ou seja, a nota não é autorizada.

A disponibilidade dos serviços pode ser verificada no endereço:

<https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx>
