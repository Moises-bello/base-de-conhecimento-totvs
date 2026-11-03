---
article_id: 360055613574
category: NFe - Nota Fiscal Eletrônica
content_hash: d8e416c486f328a347fa025789100e03a5369e244c4591d0eea3b01e85360343
fetched_at: '2026-06-28T22:40:00.470665+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 228 Rejeição:
  Data de Emissão muito atrasada'
type: support-article
updated_at: '2021-10-11T17:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055613574--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-228-Rejei%C3%A7%C3%A3o-Data-de-Emiss%C3%A3o-muito-atrasada
---

**Dúvida**

Como solucionar a rejeição abaixo:

228 Rejeição: Data de Emissão muito atrasada ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para notas de emissão **Normal, SVC -AN e SVC-RS a emissão da nota não pode ser de mais de 30 dias, ou outro** limite determinado pela Sefaz.

1 - Para a correção da rejeição é necessário **excluir a nota e gerar novamente** para a gravação dos campos **F2\_EMISSAO ou F1\_EMISSAO** dentro do prazo da Sefaz.

* **Exemplo das TAGS:**

![tag_228.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360096344453/tag_228.PNG)

* **Saiba mais:**

Caso tenha gerado o documento no mesmo dia, verifique ao logar no Protheus a data base, se está correta.

* **Validação da Sefaz:**

![Rejei__o_228_valida__o_da_Sefaz.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360096342553/Rejei__o_228_valida__o_da_Sefaz.PNG)
