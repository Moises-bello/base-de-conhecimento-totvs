---
article_id: 115004964687
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 61c05374d7257f0162e17eb8242644eed3e221ed815fb87a5ae2435dd2830af6
fetched_at: '2026-06-28T22:38:38.563526+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagens de
  Help:  A410NATVZO - A410NATUSO - A410NATCLI - A410NATPED - A410NATBLK no Pedido
  de Vendas (MATA410)'
type: support-article
updated_at: '2021-12-20T20:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004964687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagens-de-Help-A410NATVZO-A410NATUSO-A410NATCLI-A410NATPED-A410NATBLK-no-Pedido-de-Vendas-MATA410
---

**Dúvida**

Mensagens de Help: A410NATVZO - A410NATUSO - A410NATCLI - A410NATPED - A410NATBLK no Pedido de Vendas (MATA410)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para as mensagens:

* **A410NATVZO -** refere-se ao conteúdo do parâmetro **MV\_1DUPNAT** que está vazio, sendo necessário informar a natureza;
* **A410NATUSO -** refere-se aos campos que tratam natureza (**A1\_NATUREZ ou C5\_NATUREZ**) não estarem em uso, neste caso precisando habilitar o campo via configurador;
* **A410NATCLI -** refere-se ao campo **A1\_NATUREZ** que está vazio, quando o parâmetro MV\_1DUPNAT foi configurado para natureza do cliente (**SA1->A1\_NATUREZ**);
* **A410NATPED -** refere-se ao campo **C5\_NATUREZ** que está vazio, quando o parâmetro MV\_1DUPNAT foi configurado para natureza do pedido de vendas (**SC5->C5\_NATUREZ**);
* **A410NATBLK**- refere-se a bloqueio de registro de de cadastro da natureza, utilizado no **A1\_NATUREZ** ou **C5\_NATUREZ**, chamado pelo **MV\_1DUPNAT** ou a natureza do cadastro Fornecedor , conforme configuração do **MV\_2DUPNAT** . Sendo necessário utilizar uma natureza desbloqueada.

Saiba mais: **[FAT0038\_A410NATVZO\_A410NATUSO\_A410NATCLI\_A410NATPED\_ A410NATBLK \_ no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/h_ruDQ)**
