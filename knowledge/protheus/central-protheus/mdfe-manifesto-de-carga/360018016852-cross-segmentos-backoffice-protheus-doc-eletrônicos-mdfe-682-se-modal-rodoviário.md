---
article_id: 360018016852
category: MDFe - Manifesto de Carga
content_hash: 61a02f47237577ddc3e61b8ff05ebf0a61db182e474e003b4bdf993daa291507
fetched_at: '2026-06-28T22:40:08.143062+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  682 - Se
  modal rodoviário e informado RNTRC Verificar situação do RNTRC
type: support-article
updated_at: '2025-06-17T18:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018016852-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-682-Se-modal-rodovi%C3%A1rio-e-informado-RNTRC-Verificar-situa%C3%A7%C3%A3o-do-RNTRC
---

**Dúvida**Como corrigir a rejeição 682 - Se modal rodoviário e informado RNTRC Verificar situação do RNTRC  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

* **Conforme o site da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013517071/mceclip0.png)

* **Será validada a rejeição:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013501292)

* **Se gerado o grupo de****Proprietário do Veículo a TAG é obrigatória:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499192/mceclip3.png)**

* **Conforme o XML de exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499112/mceclip2.png)**

* **Nesse caso deve ser preenchido no campo A2\_RNTRC um código válido:**

**Nesse grupo abaixo é opcional:**

​![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499492/mceclip4.png)

 Conteúdo é preenchido no Sigamat.emp da empresa.

 SM0->M0\_RNTRC

Esse RNTRC que a Sefaz está exigindo é um registro obrigatório com ANTT:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499672/mceclip6.png)

* Há um link de Consulta do RNTRC no site: <https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/>

Sendo possível a consulta através do CPF ou CNPJ

Nessa consulta é possível verificar o RNTRC  e se o mesmo encontra-se apto para o transporte.
