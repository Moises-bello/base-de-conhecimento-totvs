---
article_id: 18724802868375
category: PMS - Projetos
content_hash: 884419124511cc6909d9302e45cda3df0b62df09b078f30dabbd46d020f0f3e0
fetched_at: '2026-06-28T22:37:15.977275+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Quantia do projeto vinculada
  nas rotinas de entrada e o parâmetro MV_DIFAFN
type: support-article
updated_at: '2024-02-26T18:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18724802868375-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Quantia-do-projeto-vinculada-nas-rotinas-de-entrada-e-o-par%C3%A2metro-MV-DIFAFN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18724789756055) Tempo aproximado para leitura: **02:30:00 min** **Dúvida**Ao referenciar o pedido de compra no documento de entrada, o projeto herda a quantia da solicitação de compras e não do pedido de compras, como configurar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

O processo de geração de documento de entrada não tem autonomia para alterar a quantidade de amarração com o projeto, isso porque não há obrigatoriedade de a quantidade do item ser igual ao rateado no projeto, assim como os itens podem ser rateados em n projetos.

A quantidade do item nem sempre o quanto está informado no vínculo com o projeto, um exemplo é que pode ser feita a entrada de 10 unidades de um produto e direcionar apenas 5 para os projetos, o restante fica como estoque.

Atualmente a única obrigatoriedade é que a quantidade total rateada nos projetos para um item não pode ser maior que a quantidade do item, já que seria inviável a entrada de 10 unidades direcionar 15 para os projetos, sendo esta a origem da mensagem apresentada, indicando que a informação de rateio em projetos deve ser ajustada.

Sendo assim o indicativo das quantidades direcionadas aos projetos devem ser realizadas sempre pelo operador.

Adicionalmente existe o parâmetro **MV\_DIFAFN**, que quando ativo, este obriga que as quantidades nos vínculos com projetos sejam iguais a quantidade do item, ou seja, nem maior nem menor, entretanto não elimina a necessidade da alteração por parte do operador, é apenas uma configuração de segurança que barra a movimentação.

**Saiba mais:**

[PMS0015\_Mensagem PMSQTNF no Documento de Entrada](https://tdn.totvs.com/x/7dhZE)
