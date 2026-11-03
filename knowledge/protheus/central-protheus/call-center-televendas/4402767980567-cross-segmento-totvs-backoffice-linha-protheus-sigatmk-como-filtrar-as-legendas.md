---
article_id: 4402767980567
category: Call Center - Televendas
content_hash: 7ee827602148f2b444d258c7a0c93a447a5b57323e92999036fc54f9a7fc56ab
fetched_at: '2026-06-28T22:41:30.195234+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como filtrar
  as legendas do atendimento televendas
type: support-article
updated_at: '2021-06-16T22:25:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402767980567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-filtrar-as-legendas-do-atendimento-televendas
---

**Dúvida**Como filtrar as legendas do atendimento televendas (**TMKA273**)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**

As legendas do atendimento televendas são compostas da seguinte forma:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402770043415/mceclip0.png)

Para efetuar um filtro na legenda e apresentar os atendimentos conforme as cores, efetue:

* **Faturamento** - **VERDE** - Filtro -> Cancelado(**UA\_CODCANC**) igual a Vazio e Operação(**UA\_OPER**) igual 1 e Nota Fiscal (**UA\_DOC**) igual a Vazio;
* **Faturado** - **VERMELHO** - Filtro - >Cancelado(**UA\_CODCANC**) igual a Vazio e Operação(**UA\_OPER**) igual 1 e Nota Fiscal (**UA\_DOC**) diferente de Vazio;
* **Orçamento** - **AZUL** - Filtro - >Cancelado(**UA\_CODCANC**) igual a Vazio e Operação(**UA\_OPER**) igual 2;
* **Atendimento** - **MARROM** - Filtro - > Cancelado(**UA\_CODCANC**) igual a Vazio e Operação(**UA\_OPER**) igual 3;
* **Cancelado** - **PRETO** - Filtro - > Cancelado(**UA\_CODCANC**) diferente de vazio.

![filtro_pela_legenda_televendas.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402767909911/filtro_pela_legenda_televendas.gif)

**Saiba mais:**

**[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigatmk-Legendas-do-Televendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402767190167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigatmk-Legendas-do-Televendas)**
