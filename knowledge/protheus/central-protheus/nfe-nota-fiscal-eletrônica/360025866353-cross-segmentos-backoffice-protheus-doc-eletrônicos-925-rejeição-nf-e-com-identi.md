---
article_id: 360025866353
category: NFe - Nota Fiscal Eletrônica
content_hash: a2cf3028a02be99c036f1a98345c81f3892f7e85a76477ba5fb3e0d13c7a0498
fetched_at: '2026-06-28T22:40:01.569000+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 925 - Rejeição
  : NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário'
type: support-article
updated_at: '2021-08-02T14:14:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025866353--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-925-Rejei%C3%A7%C3%A3o-NF-e-com-identifica%C3%A7%C3%A3o-de-estrangeiro-e-inscri%C3%A7%C3%A3o-estadual-informada-para-destinat%C3%A1rio
---

**Dúvida**Como solucionar a rejeição abaixo:

925 - Rejeição : NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informada a TAG **idEstrangeiro** a TAG **IE** não deve ser gerada no XML.

Em operações do **exterior** a TAG **idEstrangeiro**é obrigatória dessa forma não deve haver **IE** nessas operações.

Se operação **interna**verificar se realmente deve haver conteúdo no campo **idEstrangeiro.**

Se **sim** não deve haver conteúdo na TAG **IE.**

* Campo de preenchimento da TAG **idEstrangeiro:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040028394/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040028694/mceclip2.png)

* Campo de preenchimento do **IE** do destinatário

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040029794/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040858553/mceclip4.png)

* **Cadastro de Cliente:**  
  ![](https://totvssuporte.zendesk.com/attachments/token/3YxXY9mmKdIiVFzBRUajhpJde/?name=inline-1114485577.png)​  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/nvdpIGaGgGqVGKtJD5Y3AyI5r/?name=inline-770586794.png)​  
  ![](https://totvssuporte.zendesk.com/attachments/token/xDlkWMIfuxMGEWcckNXqDcGNe/?name=inline-292475918.png)​

* **Cadastro de Fornecedor:**

     ![](https://totvssuporte.zendesk.com/attachments/token/vdmTfl5OB3RUjr1rT0c64YNuH/?name=inline1744640135.png)​  
  
     ![](https://totvssuporte.zendesk.com/attachments/token/gCLm5Rzelye7tNYi0CLltK6Is/?name=inline1704168182.png)​  
  
     ![](https://totvssuporte.zendesk.com/attachments/token/qlU80Sd0pYPmGSIucDKavVmvy/?name=inline-365322687.png)

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040026434/mceclip0.png)**
