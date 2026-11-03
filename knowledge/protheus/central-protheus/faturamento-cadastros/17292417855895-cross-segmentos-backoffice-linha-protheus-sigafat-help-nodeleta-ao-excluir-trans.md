---
article_id: 17292417855895
category: Faturamento - Cadastros
content_hash: d5ba56fcabf5e7a50b12ab600b0fc7eb70566826c40fc150b32a74c1d982fb70
fetched_at: '2026-06-28T22:38:36.675495+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help NODELETA ao
  excluir transportadora (MATA050)
type: support-article
updated_at: '2023-09-05T17:40:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17292417855895-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-NODELETA-ao-excluir-transportadora-MATA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17292444080279) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao excluir transportadora o Help "NODELETA" aparece, como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Por questões de integridade de banco de dados, não é possível excluir um registro que está inserido em outra tabela (chave primária em outra tabela como chave estrangeira).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17292090783767)

Ao excluir e esse Help aparecer, significa que a transportadora a ser excluída está em outra tabela.

Verifique se a transportadora não está nos campos:

* C5\_TRANSP (Tabela SC5 - Cabeçalho do Pedido de venda)
* C5\_REDESP (Tabela SC5 - Cabeçalho do Pedido de venda)
* A1\_TRANSP (Tabela SA1 - Cliente)
* TB2\_CODTRA (Tabela TB2 - Destino)

Nas demais filiais, só será possível excluir a transportadora, caso ela não esteja em nenhum registro das tabelas nos campos acima. Para excluir, basta excluir os registros que a possuem pelo Protheus.

**Exemplo:**

Em um pedido de venda faturado, deve-se excluir a NF saída (MATA521A) que foi gerada pelo pedido de venda e posteriormente excluir o pedido de venda (MATA410), assim excluindo a tabela SC5 (C5\_TRANSP) com o código da transportadora mencionada.
