---
article_id: 360020438892
category: MDFe - Manifesto de Carga
content_hash: 217fb67745b203b8d5f9df46c007ff94e65ead483331be29c78fe515d2ea21e3
fetched_at: '2026-06-28T22:40:08.238269+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 681 - Veiculo
  de terceiro (Próprio) sem RNTRC
type: support-article
updated_at: '2025-06-17T18:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020438892-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-681-Veiculo-de-terceiro-Pr%C3%B3prio-sem-RNTRC
---

**Dúvida**Como corrigir a 681 Rejeição- Veiculo de terceiro (Próprio) sem RNTRC.  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução**

* **Conforme o site da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013517071/mceclip0.png)

* **Será validada a rejeição:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013517211/mceclip1.png)**

* **Se gerado o grupo de****Proprietário do Veículo a TAG é obrigatória:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499192/mceclip3.png)**

* **Conforme o XML de exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013499112/mceclip2.png)**

Para que não ocorra a rejeição se o Veiculo seja de terceiro ou Próprio sem RNTRC

O campo DA3\_CODFOR deve ficar em branco.

**Faça um novo teste gerando o mdfe do zero após alterar a tabela DA3**
