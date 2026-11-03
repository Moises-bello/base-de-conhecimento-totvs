---
article_id: 360025491913
category: NFe - Nota Fiscal Eletrônica
content_hash: 89b63181371c3ddb4aca4dfb430d3dd3152280d52c63afe73674f877878143aa
fetched_at: '2026-06-28T22:40:05.676221+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar o
  valor da transferência de crédito de ICMS no XML e no Danfe
type: support-article
updated_at: '2025-07-15T11:50:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025491913-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-o-valor-da-transfer%C3%AAncia-de-cr%C3%A9dito-de-ICMS-no-XML-e-no-Danfe
---

**Dúvida**Como destacar o valor da transferência de crédito de ICMS no XML e no Danfe ?

   
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para destacar o valor da **transferência de crédito de ICMS** no **XML** e no **Danfe** incluir o CFOP da nota conforme o exemplo abaixo:

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar** **MV\_CFOPTRA =** 5601/5602/

* **Exemplo do parâmetro no configurador:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039288334)

* **Para mais informações clique no link abaixo:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=341223557>

2. Após isso, **exclua a nota** e gere novamente.

3. Para gerar as TAGS zeradas, Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar e retire o CFOP do** **MV\_CFOPTRA**

4. Após isso, **exclua a nota e** gere novamente.
