---
article_id: 360039771093
category: NFe - Nota Fiscal Eletrônica
content_hash: 6ee4db9c0d97e39230b95fe94b9eb3a0c630c42636e17c6865ec6146d256f3bb
fetched_at: '2026-06-28T22:40:01.858564+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - ICMS Recolhido
  anteriormente e ICMS Efetivo para RS '
type: support-article
updated_at: '2021-10-11T17:03:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039771093--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-ICMS-Recolhido-anteriormente-e-ICMS-Efetivo-para-RS
---

**Dúvida**Quando é gerado o grupo do ICMS recolhido anteriormente e do ICMS efetivo no XML para o RS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Para consumidor final:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052597933/mceclip0.png)

* **Gera apenas o grupo do ICMS efetivo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052598033/mceclip1.png)

* **Para não consumidor final:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052598173/mceclip2.png)

* **Gera apenas o grupo do ICMS recolhido anteriormente:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052596453/mceclip1.png)**

* O fonte do MATXFIS e do  NFESEFAZ faz esse tratamento para atender o **Decreto nº 54308 NF-e UF RS**

* Conforme o **parecer da consultoria de segmentos** da TOTVS no link abaixo:

[Parecer da consultoria](http://tdn.totvs.com/pages/viewpage.action?pageId=444598643)

Quando for para operações **não destinadas ao consumidor final** geramos apenas o grupo:

**a)** vBCSTRet, pST e vICMSSTRet, na hipótese de operações não destinadas a   
consumidor final; = (ICMS Presumido, “Crédito”)

Quando for para operações  **destinadas ao consumidor final** geramos apenas o grupo:

**b)** pRedBCEfet, vBCEfet, pICMSEfet e vICMSEfet, na hipótese de operações destinadas a   
consumidor final. = (ICMS Efetivo, “Débito”)

**Saiba mais:**

Para calcular os impostos de acordo com consumidor final e não consumidor final há os artigos abaixo de apoio:

[MP - NFE - NT 2018.005 ICMS60 e ICMS500 TAGS vBCSTRet, pST e vICMSSTRet](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025598751)

[MP - NFE - NT 2018.005 ICMS60 e ICMS500 TAG vICMSSubstituto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025305012)

[MP - FIS - Como gerar as tags do ICMS efetivo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680071)
