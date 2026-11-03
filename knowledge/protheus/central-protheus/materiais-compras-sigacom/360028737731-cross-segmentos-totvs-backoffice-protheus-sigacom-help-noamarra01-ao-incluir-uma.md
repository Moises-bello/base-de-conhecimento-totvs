---
article_id: 360028737731
category: Materiais - Compras (SIGACOM)
content_hash: 4a47f3df43b0de8c71a959520d72121d7dccc3ceefe775f7999c3ead4ba15f2d
fetched_at: '2026-06-28T22:41:18.945994+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help NOAMARRA01 ao
  incluir uma Solicitação de Compras
type: support-article
updated_at: '2022-05-18T21:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028737731-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-NOAMARRA01-ao-incluir-uma-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Help **NOAMARRA01** ao incluir uma Solicitação de Compras

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029212171/mceclip5.png)

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

A mensagem é apresentada quando há amarração na tabela **CTA- Amarrações (CTBA250)** com o parâmetro ***MV\_CTBAMAR =2***.

Com essa configuração o sistema não permite incluir amarrações diferentes nos processos de Solicitação de Compras, Pedido de Compras e Documento de Entrada.

Exemplo de cadastro abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029208112/mceclip0.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029212091/mceclip3.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029209492/mceclip2.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029211351/mceclip1.png)

**Parâmetros:**

* MV\_CTBAMAR
* MV\_VLDHEAD

**Obs.:** *Verificar se os campos envolvidos na entidade contábil constam como usados no configurador.*

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
