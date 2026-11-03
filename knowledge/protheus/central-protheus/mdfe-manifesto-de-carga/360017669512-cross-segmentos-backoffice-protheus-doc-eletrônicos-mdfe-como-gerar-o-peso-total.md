---
article_id: 360017669512
category: MDFe - Manifesto de Carga
content_hash: 0352c3a6f98c35f87093897a8c5c505e18c5523f1cfef6d93ac3f5a7d5b14f3f
fetched_at: '2026-06-28T22:40:08.162450+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Como gerar
  o peso total na DAMDFE
type: support-article
updated_at: '2025-06-17T18:31:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017669512-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Como-gerar-o-peso-total-na-DAMDFE
---

**Dúvida**Como gerar o peso total na DAMDFE  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Essa informação de peso total (Kg) na **DAMDFE** é referente a tag **<qCarga>** peso Bruto Total da Carga / Mercadorias Transportadas, para isso a nota de origem deve ter tido peso bruto. Para a nota de origem gerar peso bruto é gerado o grupo **qvol**:

No padrão do nosso **XML** é necessário que os campos no pedido de venda estejam preenchidos **C5\_VOLUME1, C5\_VOLUME2, C5\_VOLUME\_3, C5\_VOLUME4 e C5\_ESPECI1, C5\_ESPECI2, C5\_ESPECI3, C5\_ESPECI4, C5\_PESOL, C5\_PBRUTO**

**OBS:** Existem quatro volumes e quatro espécies **precisa estar preenchido pelo menos um volume e uma espécie,** além do peso bruto e peso líquido.

**Pode ser levado o peso bruto ou peso líquido dos campos:**

* **C5\_PESOL, C5\_PBRUTO**

Ou

* **B1\_PESO, B1\_PESBRU**

Assim será preenchido automático os campos:

**F2\_VOLUME1, F2\_VOLUME2, F2\_VOLUME\_3, F2\_VOLUME4 e F2\_ESPECI1, F2\_ESPECI2, F2\_ESPECI3, F2\_ESPECI4.F2\_VOLUME1, F2\_VOLUME2, F2\_VOLUME\_3, F2\_VOLUME4 e F2\_ESPECI1, F2\_ESPECI2, F2\_ESPECI3, F2\_ESPECI4, F2\_PLIQUI, F2\_PBRUTO**

Poderá verificar que no padrão do **XML** do fonte do **NFESEFAZ** se os campos estiverem preenchidos na **SF2** a informação será levada para o **XML**.

Se for documento de entrada os quatros campos também precisam estar preenchidos. Os campos são os mesmo, mas ao invés de ser na **SF2** e na **SF1** na aba em informações da **Danfe** tem os campos que precisam ser preenchidos.

Assim quando incluir o **MDFe** será gravada na tabela **CC0\_PESOB**, gerado na TAG **qcarga** e na impressão do **DAMDFE** peso total (Kg).

* **Exemplo do DAMDFE:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013197852)
