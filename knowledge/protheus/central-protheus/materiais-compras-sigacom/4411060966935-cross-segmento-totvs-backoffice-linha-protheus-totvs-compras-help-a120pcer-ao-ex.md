---
article_id: 4411060966935
category: Materiais - Compras (SIGACOM)
content_hash: 1ceb8230a7461cc4197bf301af0d663075a029d5a9e2d8bdbed6c4d29b5c1143
fetched_at: '2026-06-28T22:41:11.758184+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras -  Help
  A120PCER Ao Excluir Pedido de Compras
type: support-article
updated_at: '2022-10-26T13:50:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411060966935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Help-A120PCER-Ao-Excluir-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao excluir **Pedido de Compras** é gerado o **Help:  A120PCER**

**![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411060587159/Screenshot_2.png)**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as Versões

**Solução**

O alerta A120PCER é exibido quando na tentativa de exclusão de um pedido de compras, o sistema localiza que a Solicitação de Compras vinculada ao Pedido, teve algum item ou saldo eliminado por resíduo, ou seja, quando o campo C1\_RESIDUO estiver diferente de vazio o help será apresentado;

**![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411065867159/Screenshot_3.png)**

Nesse caso o PC não poderá ser excluído, mas sim eliminado o resíduo, que a SC vinculada também teve esse processo realizado.

![Alert.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411060939031/Alert.gif)
