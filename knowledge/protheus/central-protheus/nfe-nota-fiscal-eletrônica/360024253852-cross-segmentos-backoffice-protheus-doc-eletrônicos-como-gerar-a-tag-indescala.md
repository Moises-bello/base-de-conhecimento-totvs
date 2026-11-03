---
article_id: 360024253852
category: NFe - Nota Fiscal Eletrônica
content_hash: b7853425f16338a955186fceee875a32046d77a6995dd213b72b42ed3108cdc8
fetched_at: '2026-06-28T22:40:00.303627+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar a
  TAG indEscala '
type: support-article
updated_at: '2021-08-04T14:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024253852--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-indEscala
---

**Dúvida**Como gerar a TAG indEscala ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme a nota técnica 2016.002\_v\_1.61 a **TAG indEscala** pode ter o conteúdo **S ou N:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022707971/mceclip0.png)

**Para gerar como S será necessário preencher o campo:**

D3E\_INDESC= 1

* **Exemplo do XML:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022708031/mceclip1.png)

* **Link da consultoria de segmentos:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=274856677>

* **Link com os dados dos campos da tabela D3E:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=423934129>

**Saiba mais:**

* **Conforme o print abaixo da nota técnica 2016.002\_v\_1.61:**

![](https://totvssuporte.zendesk.com/attachments/token/IJjsIkSvfManxB5zHvU7NjbcV/?name=inline1565761531.png)​

Se gerada a TAG indescala uma sequencial opcional há uma TAG que é obrigatória que é o **código do CEST.**

O código do CEST deve ser preenchido no cadastro de produto no campo B1\_CEST e após fazer a nota é gravado o conteúdo nos campos **FT\_CEST e CD2\_CEST.**

Caso esse produto não possua CEST será necessário verificar junto a Sefaz qual conteúdo deve ser informado na TAG obrigatória.

Ou será necessário deixar o campo abaixo em branco:

**D3E\_INDESC**
