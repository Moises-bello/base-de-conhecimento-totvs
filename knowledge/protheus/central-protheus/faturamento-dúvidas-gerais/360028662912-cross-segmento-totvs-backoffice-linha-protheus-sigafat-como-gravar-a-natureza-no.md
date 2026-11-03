---
article_id: 360028662912
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 65ffc4d166bd7d24d55cbffdbc335cd2c9c372b673b603c2e49664c47e129139
fetched_at: '2026-06-28T22:38:32.722163+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como gravar
  a Natureza no título gerado pela Devolução de Compras?
type: support-article
updated_at: '2022-02-14T14:17:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028662912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-gravar-a-Natureza-no-t%C3%ADtulo-gerado-pela-Devolu%C3%A7%C3%A3o-de-Compras
---

**Dúvida**  
Como gravar a **Natureza** no campo **E2\_NATUREZ** do título do contas a pagar **gerado** pela **Devolução de Compras** usando a rotina **Pedido de Vendas** (**MATA410**)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Acesse o módulo **Configurador** e configure o parâmetro **MV\_2DUPNAT** para buscar a **Natureza**;

**2.** Configuração **Padrão** do conteúdo do parâmetro **MV\_2DUPNAT** é **SA2->A2\_NATUREZ** ;

**3.** Com essas configurações, o sistema **irá** buscar a **natureza** que esta configurada no campo **A2\_NATUREZ** do cadastro de **fornecedor** para **gravar** no campo **E2\_NATUREZ** do título do **Contas a Pagar**!

**Observação:**

Essa configuração só irá funcionar com o parâmetro **MV\_1DUPNAT = SA1->A1\_NATUREZ**, caso o parâmetro **MV\_1DUPNAT** esteja como **SC5->C5\_NATUREZ** terá que informar a natureza **manualmente** no cabeçalho do pedido no campo **C5\_NATUREZ**.

O motivo do sistema não carregar a informação é porque é possível devolver várias notas de Entrada em uma única nota de saída, e cada uma dessas notas devolvidas poderão ter naturezas diferentes, o sistema tem uma limitação para tratar essa multiplicidade de naturezas na geração da nota de saída.

**Saiba Mais: [Geração de NDF (Nota de Débito Fornecedor) pelo módulo de Faturamento](https://tdn.totvs.com/x/u44jDw)**
