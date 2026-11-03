---
article_id: 36320697108631
category: Financeiro - Análise de Crédito Financeiro
content_hash: 331d665adfcc96b1454d320918854e820e3d638c38a9bc769a68910a4aac9cdb
fetched_at: '2026-06-28T22:37:25.525972+00:00'
product: protheus
section_id: 36607745462423
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Cálculo
  de Inadimplência
type: support-article
updated_at: '2025-12-23T23:17:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36320697108631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-C%C3%A1lculo-de-Inadimpl%C3%AAncia
---

**Dúvida:**  
Como o sistema realiza o cálculo de inadimplência do cliente?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - A partir da release 12.1.33.  
  
  
**Solução:**  
O **cálculo de inadimplência** é realizado com base nos **valores dos títulos em aberto**, utilizando a seguinte fórmula:

**(Valores Vencidos / (Valores Pendentes + Valores Vencidos)) × 100**

Dessa forma, o resultado representa o **percentual de inadimplência** em relação ao total de valores ainda não quitados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36320674981911)

**Exemplo:**

* **Valores Vencidos = R$10.000,00 / (R$2.500,00 + R$10.000,00)) × 100**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36320697099031)

**Saiba mais**

[Análise de Crédito Financeiro - FINAPP001 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=733953052)
