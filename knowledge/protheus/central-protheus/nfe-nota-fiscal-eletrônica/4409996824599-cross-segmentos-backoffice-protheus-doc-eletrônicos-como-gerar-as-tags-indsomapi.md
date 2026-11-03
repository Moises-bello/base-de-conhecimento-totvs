---
article_id: 4409996824599
category: NFe - Nota Fiscal Eletrônica
content_hash: a084775993aa65b7ae4efbc016686e525c210c2453b0984cf80b835c8e5ff38b
fetched_at: '2026-06-28T22:40:06.716599+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as TAGS
  IndSomaPISST e IndSomaCOFINSST
type: support-article
updated_at: '2025-07-28T18:59:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409996824599-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-IndSomaPISST-e-IndSomaCOFINSST
---

**Dúvida**Qual o procedimento para gerar as gerar as TAGS IndSomaPISST e IndSomaCOFINSST  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**As TAGS IndSomaPISST e IndSomaCOFINSST**só são apresentadas no XML, caso tenha sido realizada as atualizações, as configurações para o calculo do imposto e a situação tributária do PIS e Cofins 05.

1. O **Protheus e o TSS** devem estar com as atualizações abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

2. Para realizar o **calculo realizar o procedimento abaixo:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular PIS/COFINS ST no total da NF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408510846871)

3. No TES preencher os campo **SIT. trib. PIS "F4\_CSTPIS" e SIT. trib. Cof "F4\_CSTCOF" = 05**

**![20211004_100253.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410002196247)**

4. Para agregar ao total da nota o **PIS/COF ST (F4\_APSCFST)** igual a 1= Sim no TES.

* **Exemplo do XML:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409997257879)**
