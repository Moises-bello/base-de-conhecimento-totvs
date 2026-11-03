---
article_id: 4421427574423
category: MDFe - Manifesto de Carga
content_hash: cef1854ee1f8da6df750274882f8a5c0d84c85973803913970fc01392a5873b0
fetched_at: '2026-06-28T22:40:08.225208+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 029 : Falha
  de schema na Tag qcarga'
type: support-article
updated_at: '2025-06-17T17:41:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421427574423-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-029-Falha-de-schema-na-Tag-qcarga
---

**Dúvida**Como solucionar a falha de Schema referente a TAG qcarga ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Ao apresentar falha de Schema no MDFe referente a TAG **<qCarga> peso Bruto Total da Carga / Mercadorias Transportadas.**

 1-  Preencher na nota de origem Volume, espécie, peso bruto e peso líquido nos campos do pedido de venda **C5\_VOLUME1, C5\_VOLUME2, C5\_VOLUME\_3, C5\_VOLUME4 e C5\_ESPECI1, C5\_ESPECI2, C5\_ESPECI3, C5\_ESPECI4, C5\_PESOL, C5\_PBRUTO**

**OBS:** Existem quatro volumes e quatro espécies **precisa estar preenchido pelo menos um volume e uma espécie,** além do peso bruto e peso líquido.

**Pode ser levado o peso bruto ou peso líquido dos campos:**

* **C5\_PESOL, C5\_PBRUTO**

Ou

* **B1\_PESO, B1\_PESBRU**

2 -Ao incluir o **MDFe** será gravada na tabela **CC0\_PESOB**, gerado na TAG **qcarga** e na impressão do **DAMDFE** peso total (Kg).

* **Exemplo do DAMDFE:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32683400913559)
