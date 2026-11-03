---
article_id: 360048825354
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 04f0b84dd8a6935233ca67bfea9e600ca86cc7b52f972a669157562c75a84704
fetched_at: '2026-06-28T22:38:32.872130+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Atualização de
  preço de venda no pedido
type: support-article
updated_at: '2023-08-15T15:01:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048825354-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-de-pre%C3%A7o-de-venda-no-pedido
---

**Dúvida**

 O sistema atualiza automaticamente os preços dos pedidos de venda (**MATA410**) , quando a tabela de preços (**OMSA010**) é atualizada?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O pedido somente será atualizado automaticamente por uma tabela existente no pedido, quando for efetuado o **reajuste** da tabela de preço , através de outras ações, reajuste e na pergunta ***Pedidos em carteira estiver como Atualizar***, conforme a imagem abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/gXm3tJeUbTKuVc4EB1SQ3xr1O/?name=inline1247467781.png)​

Se apenas atualizar a tabela de preço, sem usar a rotina de reajuste, o sistema não atualizará o preço de lista do pedido, a atualização só ocorrerá quando for dado foco na quantidade vendida, dando um enter sobre ela ou incluindo uma nova quantidade.

Saiba mais em: **[FAT0053\_Reajuste\_de\_valores\_na\_tabela\_de\_preço](https://tdn.totvs.com/pages/viewpage.action?pageId=235598896)**
