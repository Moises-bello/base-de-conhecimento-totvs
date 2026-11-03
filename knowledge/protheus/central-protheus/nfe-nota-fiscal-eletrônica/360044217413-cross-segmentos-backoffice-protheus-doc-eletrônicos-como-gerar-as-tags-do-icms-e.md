---
article_id: 360044217413
category: NFe - Nota Fiscal Eletrônica
content_hash: 87d7dd127f6d019af694d1406c49acb4b76f7eea47ac2cb5b0aff31b4c8dfd56
fetched_at: '2026-06-28T22:40:06.703615+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as tags
  do ICMS efetivo
type: support-article
updated_at: '2025-06-23T12:12:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044217413-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-tags-do-ICMS-efetivo
---

**Dúvida**

Como gerar as tags do ICMS efetivo ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para gerar as tags do ICMS efetivo configure conforme abaixo:

**1- Configurar no cadastro de cliente:**

Tipo (A1\_TIPO) = **Consumidor Final**

![A1_TIPO_CONSUMIDOR_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043390997655)

**2- Configurar no TES:**

Calcula ICMS (F4\_ICM) = **Sim ou não**

**![calcula_icms_S_ou_N.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043032994199)**

Livro Fiscal de ICMS (F4\_LFICM) = **Outros**

**![LIVRO_OUTROS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043108194967)**

Sit Trib ICM (F4\_SITTRIB) = **60**

![Sit_trib_icm_60.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043195593751)

* **Exemplo do XML :**

![](https://lh3.googleusercontent.com/-8M82ap9oNNg/XHfhZpNVDoI/AAAAAAAAAH0/0GGXCY2UEM0Cyd38dRTZlAhglApimcXVwCK8BGAs/s493/2019-02-28.png)

* **Saiba mais:**

Para **UF de RS é gerada as TAGS do ICMS efetivo para Produtor rural,**para isso realizar os procedimentos abaixo:

1- Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_ESTADO = RS.**

![MV_ESTADO_RS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043655482903)

2- No cadastro de cliente configure o campo **Tipo (A1\_TIPO)** = **L** **(Produtor Rural)**

![A1_TIPO_PRODUTOR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043451266199)

3-  Configure o TES  conforme abaixo:

**Calcula ICMS (F4\_ICM)** = Sim ou não

![calcula_icms_S_ou_N.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043032994199)

**Livro Fiscal de ICMS (F4\_LFICM)** = Outros

![LIVRO_OUTROS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043108194967)

**Sit Trib ICM (F4\_SITTRIB)** = 60

![Sit_trib_icm_60.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12043195593751)

* Esse tratamento foi realizado para atender o **parecer do link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=490661819>

* Referente ao destaque do **ICMS Efetivo destacar no Danfe segue o parecer** da consultoria **no link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=552104177>

* **Saiba mais:**

Será considerada a regra de preenchimento das Tags abaixo:

**pRedBCEfet**:  segundo a regra de validação deverá ser preenchido com percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (vBCEfet).

**vBCEfet:**segundo a regra de validação deverá ser preenchido com Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do vProd por (1- pRedBCEfet).

 **pICMSEfet**: segundo a regra de validação deverá ser preenchido com a Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação.

**vICMSEfet**: segundo a regra de validação deverá ser preenchido Obtido pelo produto do valor do campo pICMSEfet pelo valor do campo vBCEfet, caso estivesse submetida ao regime comum de tributação.
