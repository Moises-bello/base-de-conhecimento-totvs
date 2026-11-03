---
article_id: 4411239446423
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0f1cbb86d093e780f630769ea03b5939836fcccaaee1c496c96699ecd4b3821c
fetched_at: '2026-06-28T22:38:38.592954+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Nota sobre quantidade
  liberada negativa
type: support-article
updated_at: '2021-10-21T21:11:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411239446423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Nota-sobre-quantidade-liberada-negativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao incluir pedido, deixando o menu F12 com a pergunta "Sugere Qtde Liber?" igual a Sim, está gerando quantidade liberada negativa no campo c6\_qtdlib.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

O fato de deixar a pergunta do **menu F12** do pedido de venda (**mata410**) - "**Sugere Qtde Liber**?" igual a Sim, não pode deixar o campo **c6\_qtdlib** negativo.  
  
Caso essa inconsistência ocorra, procure atualizar o módulo com o pacote de expedição contínua: [**SIGAFAT**](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)
