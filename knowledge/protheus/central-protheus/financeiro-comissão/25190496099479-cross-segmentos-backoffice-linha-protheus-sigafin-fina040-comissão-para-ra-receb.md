---
article_id: 25190496099479
category: Financeiro - Comissão
content_hash: a6f73fbcea41e4d20b187be9ec5610b90f2e56ddfdf341dd3c6a6a659b001dd4
fetched_at: '2026-06-28T22:37:50.867289+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Comissão
  para RA - Recebimento Antecipado
type: support-article
updated_at: '2024-09-27T11:55:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25190496099479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Comiss%C3%A3o-para-RA-Recebimento-Antecipado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25196767906455) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como gerar comissão para recebimento antecipado (RA)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
Por padrão, não é possível gerar comissão a partir da inclusão de um título de **recebimento antecipado**.

A regra de negócios relacionada ao **título de recebimento antecipado** estabelece que deverá reduzir o saldo devedor do título da **NF** gerada. No entanto, a comissão será calculada exclusivamente com base na **NF**, dependendo da configuração da geração da **comissão**, sendo na **emissão** ou **baixa**.

**Importante**

A regra para a **geração de comissão** é definida com base na venda:

* **100% na emissão:** Sendo gerada a comissão na emissão, será calculada assim que a NF for emitida
* **100% na baixa do título:** Sendo gerada a comissão na baixa, será calculada assim que a NF for baixada.

No entanto, existe um ponto de entrada **PE F040COM** que pode auxiliar na customização necessária.

[F040COM - Gravação dos dados do título](https://tdn.totvs.com/pages/releaseview.action?pageId=6070864)

**Saiba mais**

[Recálculo de Comissões - FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
