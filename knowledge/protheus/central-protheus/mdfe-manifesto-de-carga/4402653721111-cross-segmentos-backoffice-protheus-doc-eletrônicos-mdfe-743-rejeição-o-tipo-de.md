---
article_id: 4402653721111
category: MDFe - Manifesto de Carga
content_hash: 8e8c68ae5eca4fbe207241b73c6ed5f1aec21a935b3fef1efbc90ea5672d7b5a
fetched_at: '2026-06-28T22:40:08.146764+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  743 Rejeição
  : O tipo de transportador deve ser TAC quando informado CPF do proprietário do veículo
  de tração'
type: support-article
updated_at: '2025-06-17T18:57:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402653721111-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-743-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-deve-ser-TAC-quando-informado-CPF-do-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição 743 Rejeição : O tipo de transportador deve ser TAC quando informado CPF do proprietário do veículo de tração ?

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Se modal rodoviário e informado **CPF do proprietário do veículo de tração:**

A informação do tipo de transportador **(tpTransp) deverá ser preenchida com TAC (2).**

1 - Se preenchido no cadastro de Veículo campo **Tipo Transp.  "DA3\_TIPTRA" = 1 - Rodoviário:**

![tipo_rodov.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402654189207)

2- Verifique se deve ser preenchido  o campo no cadastro **de veículo Proprietário "DA3\_CODFOR" e com CPF:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402654342423)**

![DA3_CODFOR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402648836247)

3 - Se necessário gerar **Proprietário** deve gerar TAC = 2, no cadastro de Fornecedor campo "Tipo" A2\_TIPO precisa ser **F - Fisico**

**![TAC_MANUAL.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402649334039)**

**![20210614_150651.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402654670999)**

4- Após isso, exclua o **MDFe e gere novamente.**

* **Validação da Sefaz:**

**![rejei__o_743.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402653667863)**
