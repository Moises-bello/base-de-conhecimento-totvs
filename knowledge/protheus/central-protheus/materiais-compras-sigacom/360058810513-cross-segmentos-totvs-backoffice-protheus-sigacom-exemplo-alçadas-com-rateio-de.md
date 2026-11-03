---
article_id: 360058810513
category: Materiais - Compras (SIGACOM)
content_hash: bdc2a633192ca50608f966818c49ff456354a14f2813e51914174c34147f018f
fetched_at: '2026-06-28T22:41:17.689221+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo alçadas com
  rateio de entidade contábil para dois Grupos na Solicitação de Compras
type: support-article
updated_at: '2022-05-18T20:50:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058810513-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-al%C3%A7adas-com-rateio-de-entidade-cont%C3%A1bil-para-dois-Grupos-na-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Exemplo alçadas com rateio de entidade contábil na Solicitação de Compras.

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

**SIGACOM > Atualizações > Solicitações > Solicitação de Compras**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098957973/mceclip1.png)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096636394/mceclip0.png)

Exemplo do SIGACOM > Atualizações > Administração de Compras > Grupo de Aprovação:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098959153/mceclip6.png)

**Grupo F:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096637094/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098958373/mceclip3.png)

**Grupo G:**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096637174/mceclip4.png)**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098958433/mceclip5.png)**

Ao criar a Solicitação de Compras o sistema apresenta o log de aprovação conforme abaixo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098960493/mceclip8.png)

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098960373/mceclip7.png)**

O registro foi direcionado para dois aprovadores de Grupos diferentes conforme configuração.

Neste processo é possível consultar/liberar/rejeitar na rotina **SIGACOM > Atualizações > Liberações > Liberar Documentos (MATA094)**

**Aprovador: AP1**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096639454/mceclip10.png)**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098960753/mceclip9.png)**

Após essa liberação o log de aprovação é atualizado conforme exemplo:

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096639494/mceclip11.png)**

Nessa situação após liberação do aprovador a **solicitação de compras** permanece bloqueada, pois ainda consta pendente para outro aprovador:

**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098961033/mceclip12.png)**

Após o outro aprovador liberar o registro fica disponível para uso:

**Aprovador: AP2**

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098961133/mceclip13.png)**

**![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098961633/mceclip14.png)**
