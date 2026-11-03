---
article_id: 360044384474
category: Materiais - Compras (SIGACOM)
content_hash: ce68be35bd1d2423c9289a1cd6efb02cb394556caa164eec0b632b0aa9b63560
fetched_at: '2026-06-28T22:41:18.827747+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103PCNSLD ao
  Incluir Documento de Entrada - MV_PCTOLER
type: support-article
updated_at: '2021-09-16T20:31:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044384474-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A103PCNSLD-ao-Incluir-Documento-de-Entrada-MV-PCTOLER
---

**Dúvida**

O que pode causar a ocorrência do Help A103PCNSLD ao realizar a inclusão de um Documento de Entrada ?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060478974/mceclip1.png)

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

O Help A103PCNSLD na inclusão da NF de Entrada, pode ocorrer ao se tentar alterar a quantidade de um Item que foi trazido automaticamente ao vincular um Pedido de Compras na situação abaixo:

Após ser trazido automaticamente o item da NF de Entrada ao vincular um Pedido de Compras, e se tentar alterar a quantidade do item para um valor maior do que a tolerância cadastrada no parâmetro ***MV\_PCTOLER***.

Dessa forma para que o Help não mais ocorre deve-se:

- Diminuir a quantidade alterada do item para um valor menor do que o percentual informado no ***MV\_PCTOLER***

ou

- Aumentar o percentual de tolerância informado no ***MV\_PCTOLER***.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060482874/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061411973/mceclip1.png)

Obs: Ao deixar o parâmetro como "0" ele é considerado desativado, para fazer efeito deve conter alguma informação. Ex: 0,5 - 1 - 2 .

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
