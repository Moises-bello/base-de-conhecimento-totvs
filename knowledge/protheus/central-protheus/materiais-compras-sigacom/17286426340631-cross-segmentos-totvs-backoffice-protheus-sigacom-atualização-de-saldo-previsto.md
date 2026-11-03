---
article_id: 17286426340631
category: Materiais - Compras (SIGACOM)
content_hash: 7fc02919013c04df1eb30fd8b1740b3bc8347bfbadb89f2bd66a84557fa503ed
fetched_at: '2026-06-28T22:41:14.242216+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Atualização de saldo
  previsto de um pedido originado via cotação
type: support-article
updated_at: '2023-09-05T15:13:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17286426340631-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Atualiza%C3%A7%C3%A3o-de-saldo-previsto-de-um-pedido-originado-via-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17286438468503) Tempo aproximado para leitura:  **00:02:00 min** **Dúvida**

Como é realizado a atualização do Saldo do Pedido Previsto Originado via Cotação?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da VERSÃO 12  
  
**Solução**

Ao vincular uma solicitação de compras em uma cotação, essa solicitação de compras será vinculada a cotação, ou seja, todo processo de saldo previsto/produto atendido será através da cotação.

Passo a Passo :

Onde temos uma **Solicitação de Compras, Processo de cotação e geração de Pedido de Compras** temos o seguinte cenário:

* Inclusão de uma **Solicitação de Compras (MATA110):**

Solicitação de Compras (SC1)

![SC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17286430027927)

Nesse momento o **saldo previsto (B2\_SALPEDI)**do produto PRD001 é atualizado para 50

* **Gerar cotação (MATA131)**, e **Atualiza Cotação (MATA150)**, vinculando a Solicitação de Compras:

Cotação (SC8)

![sc2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17286430034711)

**Importante**

Obs: Ao vincular uma Solicitação de Compras e uma cotação, a quantidade atendida (C1\_QUJE) da Solicitação de Compras será vinculada a quantidade da cotação (C8\_QUANT)

**Solicitação de Compras (MATA110)** terá sua **quantidade atendida (C1\_QUJE)**

Solicitação de Compras (SC1)

![sc3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17286419119767)

***Saiba Mais:***

[Atualização de saldo previsto de um pedido originado via cotação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=777268724)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
