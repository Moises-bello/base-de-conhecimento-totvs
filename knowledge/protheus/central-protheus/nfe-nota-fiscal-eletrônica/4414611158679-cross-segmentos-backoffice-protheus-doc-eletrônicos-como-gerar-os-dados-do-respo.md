---
article_id: 4414611158679
category: NFe - Nota Fiscal Eletrônica
content_hash: d2c84f9a8adadda5fd6b6a323d45ad3e2b253e26979a5ac1a4df4aed24b69fc9
fetched_at: '2026-06-28T22:40:06.758418+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar os dados
  do Responsável Técnico
type: support-article
updated_at: '2025-07-28T19:05:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414611158679-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-os-dados-do-Respons%C3%A1vel-T%C3%A9cnico
---

**Dúvida**Como gerar os dados do Responsável Técnico ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Os dados do Responsável Técnico são informações do **SOFTWARE** ou seja, da **TOTVS** . Essas informações estão em um fonte fechado não sendo possível alteração.

* **Será gerado no XML as informações do Responsável técnico conforme o exemplo abaixo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33773947355031)

2- Será necessário **criar o parâmetro manualmente** caso não tenha no configurador o parâmetro como**Caractere** conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773957689367)

* **Parâmetro no Configurador:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773947360407)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773957691927)

3- Escolha uma das **opções abaixo 0, 1 ou 2:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773957697431)

* ***Saiba mais:***

Na ***release 12.1.33*** o parâmetro  pode ser Lógico ou caractere conforme a documentação do link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=318604074)*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415251562135)

 5 - Após isso, **exclua a nota e gere** novamente.
