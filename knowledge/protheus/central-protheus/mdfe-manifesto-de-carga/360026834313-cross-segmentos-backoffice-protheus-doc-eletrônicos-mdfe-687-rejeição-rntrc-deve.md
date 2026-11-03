---
article_id: 360026834313
category: MDFe - Manifesto de Carga
content_hash: a409ebc76b103cd3395ac4f7b99fa0ca61548c881c5366c494730f95904696e8
fetched_at: '2026-06-28T22:40:08.242100+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 687 Rejeição
  RNTRC deve estar associado ao transportador indicado
type: support-article
updated_at: '2025-06-17T18:21:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026834313-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-687-Rejei%C3%A7%C3%A3o-RNTRC-deve-estar-associado-ao-transportador-indicado
---

**Dúvida**Como corrigir a rejeição 687: Rejeição RNTRC deve estar associado ao transportador indicado  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

O **RNTRC** que a Sefaz está exigindo é um registro obrigatório com **ANTT:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041739574)**

* **Conforme o XML de exemplo no grupo <prop>:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499112/mceclip2.png)**

É necessário consultar o **CFP ou CNPJ** do transportador e verificar se o **RNTRC** informado é mesmo que consta na **ANTT.**

* Há um link de Consulta do **RNTRC** no site:

<https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/>  
  
Sendo possível a consulta através do CPF ou CNPJ 

* **O proprietário  fica no cadastro de veiculo DA3\_CODFOR**

Sendo assim, deve preencher no cadastro de **fornecedor** vinculado a **DA3\_CODFOR** o campo **A2\_RNTRC**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042581793)
