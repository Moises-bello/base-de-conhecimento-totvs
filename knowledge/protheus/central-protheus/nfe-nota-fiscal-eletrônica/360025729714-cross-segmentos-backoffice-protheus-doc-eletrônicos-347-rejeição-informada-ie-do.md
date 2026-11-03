---
article_id: 360025729714
category: NFe - Nota Fiscal Eletrônica
content_hash: 04ac8af06a11f1a0c65043eaa650f8df44cafcd48857d988298725c39ae5021f
fetched_at: '2026-06-28T22:40:03.926278+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 347 Rejeição :
  Informada IE do substituto tributário em operação que não é interestadual'
type: support-article
updated_at: '2025-08-12T00:31:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025729714-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-347-Rejei%C3%A7%C3%A3o-Informada-IE-do-substituto-tribut%C3%A1rio-em-opera%C3%A7%C3%A3o-que-n%C3%A3o-%C3%A9-interestadual
---

**Dúvida**Como solucionar a rejeição:

347 Rejeição: Informada IE do substituto tributário em operação que não é interestadual ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A TAG **IEST** não deve ser gerada para operações **internas** e do **exterior** **tag:idDest=1 ou 3**com isso, existe um tratamento no fonte do **NFESEFAZ** para que a TAG não seja gerada nessas operações.

Há apenas uma **exceção** para emitentes da **UF do PR** para **operações internas.**

* Conforme o **parecer da consultoria tributária** da TOTVS no link abaixo:

*[Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=497460058%20)*

1- Se estiver gerando rejeição para um UF ***diferente do PR, realizar atualização do NFESEFAZ:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

2- Após isso, ***exclua a nota e gere novamente.***

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040017854)
