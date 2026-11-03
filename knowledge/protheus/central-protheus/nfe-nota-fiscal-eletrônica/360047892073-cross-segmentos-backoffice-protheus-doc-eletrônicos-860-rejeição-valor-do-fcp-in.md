---
article_id: 360047892073
category: NFe - Nota Fiscal Eletrônica
content_hash: cc7669c774ea68489e5b2f9bd1e47667bd93ce8efa56ae80b6f32f912888f521
fetched_at: '2026-06-28T22:40:01.553217+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 860 Rejeição:
  Valor do FCP informado difere de base de cálculo * alíquota '
type: support-article
updated_at: '2021-10-19T16:58:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047892073--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-860-Rejei%C3%A7%C3%A3o-Valor-do-FCP-informado-difere-de-base-de-c%C3%A1lculo-al%C3%ADquota
---

**Dúvida**Como solucionar a rejeição abaixo:

860 Rejeição: Valor do FCP informado difere de base de cálculo \* alíquota ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Informado a tag vFCP (id:N17c) e finNFe=1 (id:B25), verificar:

- Se **CST=00 e vFCP (id:N17c) difere da vBC (id:N15)\* pFCP (id:N17b) (\*4)** ou

- Se **CST=10, 20,70, 90 e vFCP (id:N17c) difere da vBCFCP (id:N17a)\* pFCP (id:N17b) (\*4)** (NT 2016.002)

1. Verifique se a situação tributária da nota está correta no TES no campo **F4\_SITTRIB "Sit Trib. ICM" para não validar a rejeição precisa se diferente 00, 10, 20, 70 ou 90.**

![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411030407575/F4_SITTRIB.gif)

2. Se a situação tributária da nota estiver correta verifique se o **sistema está atualizado conforme o link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

3. Configure a nota **conforme o link abaixo:**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=287056662>

4. Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

Os campos de base do FECP, **Percentual do FECP e Valor do FECP estão abaixo:**

* CD2\_BFCP
* CD2\_PFCP
* CD2\_VFCP

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410991136663/mceclip0.png)**

* Saiba mais:

**Exceção : O prazo previsto para a Nota Técnica 2020.005 v1.21**

* Ambiente de Homologação:**20/10/2021**
* **Ambiente de Produção:25/10/2021**
