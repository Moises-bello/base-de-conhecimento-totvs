---
article_id: 360059945873
category: NFe - Nota Fiscal Eletrônica
content_hash: 0ace6ee1a7b9b1b1beb3abfe94fb72a3f001b5cf641c825ed775a8812d54f476
fetched_at: '2026-06-28T22:40:01.503663+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 625 Rejeição:
  Inscrição SUFRAMA deve ser informada na venda com isenção para ZFM '
type: support-article
updated_at: '2021-10-11T17:53:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059945873--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-625-Rejei%C3%A7%C3%A3o-Inscri%C3%A7%C3%A3o-SUFRAMA-deve-ser-informada-na-venda-com-isen%C3%A7%C3%A3o-para-ZFM
---

**Dúvida**Como corrigir a rejeição abaixo:

625 Rejeição: Inscrição SUFRAMA deve ser informada na venda com isenção para ZFM ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Se informado no TES o campo ***F4\_MOTICMS  "Mot. Desone." = 7***

**![F4_MOTICM__7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100720313/F4_MOTICM__7.png)**

2- Será necessário preencher no cadastro de cliente o campo ***Suframa A1\_SUFRAMA***com a inscrição:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048809114/mceclip1.png)

* Será gerado a TAG ***ISUF*** conforme o exemplo abaixo:

![isuf_xml.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098471234/isuf_xml.JPG)

3 - Após isso, exclua a nota e gere novamente.

4- Caso não possa ser informada a ***inscrição do suframa,*** deve ser alterado o motivo de desoneração no TES ***F4\_MOTICMS  "Mot. Desone =*** **diferente de 7 - Suframa.**

5- Após isso, exclua a nota e gere novamente.

* **Validação da Sefaz:**

**![rejeicao_625.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360100720193/rejeicao_625.JPG)**
