---
article_id: 360040979094
category: TAF - REINF
content_hash: fcdb01514237b93bf21d66a5cb5adcfe7e68039f70ff3ca72ec0884a5f8cc0dd
fetched_at: '2026-06-28T22:41:33.441151+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Financeiro -  Como gerar título avulso
  para o Evento R-2030
type: support-article
updated_at: '2023-03-30T13:39:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040979094-Cross-Segmentos-Backoffice-Protheus-Financeiro-Como-gerar-t%C3%ADtulo-avulso-para-o-Evento-R-2030
---

**Dúvida**

Como gerar um título avulso para o evento R-2030 da Reinf?

**Ambiente**

TAF - REINF - 12.1.17 ou superior

**Solução:**

Lançamento no Contas a Receber (título avulso) para gerar evento R-2030 no EFD-Reinf:

* Preencher os campos obrigatórios:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055240833/mceclip5.png)

* Preencher o Complemento do Título:

<https://tdn.totvs.com/pages/releaseview.action?pageId=281128084>

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241033/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241153/mceclip7.png)

Observação: A Integração/Processamento no TAF é feita pela data de emissão e integra com o valor bruto do título, mesmo que baixado parcialmente, conforme imagem abaixo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241233/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054376294/mceclip9.png)

* O Extrator Fiscal faz a integração no TAF, pela data de emissão e pela data de contabilização (data da baixa/pagamento)
* **Primeiro teste, informando Data de Contabilização:**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054376414/mceclip10.png)

* Layout T0154 - Cadastro de Recibos/Faturas

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054376514/mceclip11.png)

Arquivo TXT:

|T154|001515-3|1|C999   99|**20191218**|1|TESTE 2|||||3000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241533/mceclip12.png)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241613/mceclip13.png)

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055241773/mceclip14.png)

* **Segundo teste, informando Data de Emissão:**

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054377754/mceclip18.png)

Arquivo TXT:

|T154|001515-3|1|C999   99|**20191201**|1|TESTE 2|||||3000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055242873/mceclip19.png)

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054377794/mceclip20.png)
