---
article_id: 360037627993
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: d3c954c2acbdfd1b4d482a0fc59c451f6877bbe388102c7fefaa0169a856b0f3
fetched_at: '2026-06-28T22:38:44.016717+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Como o sistema realiza o
  rateio das Despesas Acessórias (Frete/Seguro/Despesa) no Documento de Saída?
type: support-article
updated_at: '2025-12-11T14:49:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037627993-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Como-o-sistema-realiza-o-rateio-das-Despesas-Acess%C3%B3rias-Frete-Seguro-Despesa-no-Documento-de-Sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30570490093079) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**

Como o sistema realiza o rateio das Despesas Acessórias (Frete/Seguro/Despesa) no Documento de Saída?

**Ambiente**

Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões

**Solução**

O rateio dos valores de **Frete, Seguro** e **Despesas** nos itens do pedido de venda é controlado pelo parâmetro **MV\_RATDESP**, podendo ser feito **por valor** ou **por peso**. Essa distribuição impacta o cálculo de impostos no documento de saída, pois cada item pode possuir regras fiscais diferentes.

**Campos do Pedido de Venda:**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| C5\_FRETE | Valor do frete cobrado, somado ao total da nota fiscal. |
| C5\_SEGURO | Valor do seguro da mercadoria, destacado na nota fiscal. |
| C5\_DESPESA | Outras despesas acessórias, destacadas na nota fiscal. |

**Configuração do Rateio (MV\_RATDESP)**

- Rateio por **Valor** → MV\_RATDESP = FR=1;SEG=1;DESP=1

O frete é distribuído proporcionalmente ao valor de cada item.

- Rateio por **Peso** → MV\_RATDESP = FR=2;SEG=2;DESP=2

O frete é distribuído proporcionalmente ao peso de cada item.

O parâmetro **MV\_TPRTDSP** define o momento do cálculo. Pode ser configurado como:

**MV\_TPRTDSP = 1** - Indica que o valor informado para as despesas acessórias refere-se à Liberação do Pedido de Venda, ou seja, a cada liberação haverá um novo valor de frete, seguro e despesa.

**MV\_TPRTDSP = 2** - Indica que o valor informado para as despesas acessórias refere-se ao Total do Pedido de Venda, independente da liberação do pedido.

**Observações:**

O rateio afeta o cálculo de impostos conforme a tributação dos itens.

Caso o frete, seguro ou despesa devam ser apenas informativos, utilize C5\_MENNOTA.

**Saiba mais**:

**[Despesas acessórias no faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=239024024)**
