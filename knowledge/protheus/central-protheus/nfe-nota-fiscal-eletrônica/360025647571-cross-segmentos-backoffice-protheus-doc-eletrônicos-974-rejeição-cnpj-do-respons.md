---
article_id: 360025647571
category: NFe - Nota Fiscal Eletrônica
content_hash: a69e2cba3d858c91625f74ba64f710e65d4cdeace9de366493d70d6efa69eed6
fetched_at: '2026-06-28T22:40:05.598005+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 974 Rejeição :
  CNPJ do responsável técnico diverge do cadastrado'
type: support-article
updated_at: '2025-03-31T18:17:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025647571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-974-Rejei%C3%A7%C3%A3o-CNPJ-do-respons%C3%A1vel-t%C3%A9cnico-diverge-do-cadastrado
---

**Dúvida**

Como corrigir a rejeição 974 Rejeição : CNPJ do responsável técnico diverge do cadastrado ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Os dados do Responsável Técnico são informações do **SOFTWARE** ou seja, da **TOTVS** . Essas informações estão em um fonte fechado não sendo possível alteração.

 1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir:**

* **Parâmetro no Configurador:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31004888466711)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31004888474263)

2. Preencher **opções abaixo 0 - Todos, 1 - NFe ou 2 - MDFe:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31004888475543)

* ***Saiba mais:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31004894518295)

 3. Após isso, ***exclua a nota e gere*** novamente.
