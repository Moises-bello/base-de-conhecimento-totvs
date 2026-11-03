---
article_id: 20672529158935
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 714b3951b29d5c38a84174c5595c8c1c1aefbc88c101ee97fae24599bca18886
fetched_at: '2026-06-28T22:38:39.577153+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Despesas acessórias
  concentradas em um único item, não rateando por peso dentre todos
type: support-article
updated_at: '2024-01-19T16:59:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20672529158935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Despesas-acess%C3%B3rias-concentradas-em-um-%C3%BAnico-item-n%C3%A3o-rateando-por-peso-dentre-todos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20672529116183) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Despesas acessórias não estão rateando por peso, como resolver?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**Ao configurar as despesas acessórias por peso (FR=2;SEG=2;DESP=2) e não por valor (FR=1;SEG=1;DESP=1) o peso do produto (B1\_PESO) de todos os itens deve estar preenchido no cadastro do produto.

Caso o peso do produto não esteja preenchido, a despesa acessória é toda concentrada no último item.

**OBS:** "Frete (C5\_FRETE)" = 10, "Despesa (C5\_DESPESA)" = 5 e "Seguro (C5\_SEGURO)" = 20

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exemplo  1 | Produto | Quant | V.Unit. | Total | Peso | **Despesa** | **Frete** | **Seguro** |
| Item 1 | 1 | 1 | 30 | 30 | 30 | 1,66 | 3,33 | 6,66 |
| Item 2 | 2 | 1 | 10 | 10 | 10 | 2,50 | 5,00 | 10 |
| Item 3 | 3 | 1 | 10 | 10 | 10 | 0,84 | 1,67 | 3,34 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exemplo  2 | Produto | Quant | V.Unit. | Total | Peso | **Despesa** | **Frete** | **Seguro** |
| Item 1 | 1 | 1 | 30 | 30 | 0 | 0 | 0 | 0 |
| Item 2 | 2 | 1 | 10 | 10 | 0 | 0 | 0 | 0 |
| Item 3 | 3 | 1 | 10 | 10 | 0 | 5 | 10 | 20 |

**Saiba mais:**

**[FAT0087\_Não\_abater\_do\_título\_a\_receber\_o\_valor\_do\_frete\_proporcional\_ao\_Item\_que\_não\_gera\_duplicata](https://tdn.totvs.com/x/1ZNSDg)**
