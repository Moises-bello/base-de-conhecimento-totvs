---
article_id: 1500004323282
category: NFe - Nota Fiscal Eletrônica
content_hash: e9d0c9a0033a7e6a5e41019cbc106c9783cb87fe8f39d475ed4cc21b5094342d
fetched_at: '2026-06-28T22:40:01.414974+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 442 Rejeição :
  Descrição do pagamento não permitida. '
type: support-article
updated_at: '2021-08-27T17:31:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004323282--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-442-Rejei%C3%A7%C3%A3o-Descri%C3%A7%C3%A3o-do-pagamento-n%C3%A3o-permitida
---

**Dúvida**

Como solucionar a rejeição abaixo.

442 Rejeição : Descrição do pagamento não permitida

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Caso a forma de pagamento **seja diferente de 99-Outros**, **não** pode ser gerada a **TAG XPAG.**

* O ajuste para que não ocorra este erro, **está no fonte do NFESEFAZ:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403746612375/mceclip0.png)

* Conforme a nota técnica **2020.006\_v\_1.20 página 8 :**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407259018903/mceclip0.png)

1 - Para a correção realizar atualização do fonte do **NFESEFAZ, do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

2- Exclua a nota e **gere novamente.**

* **Saiba mais:**

O NFESEFAZ, deve ter **data igual ou superior 28/06/2021**

* **Validação da Sefaz:**

![442_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005276862/442_rejeicao.JPG)
