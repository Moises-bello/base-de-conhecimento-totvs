---
article_id: 22761068053655
category: Materiais - Compras (SIGACOM)
content_hash: ec6a2b7790557f1d5b1fe56af4db4ccff269b5345db34e69cfacfb79d3058a18
fetched_at: '2026-06-28T22:41:20.228815+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Na exclusão do pedido
  de compras, apresentação do help informando que o pedido foi gerado pelo Sigapls
type: support-article
updated_at: '2024-04-12T14:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22761068053655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-exclus%C3%A3o-do-pedido-de-compras-apresenta%C3%A7%C3%A3o-do-help-informando-que-o-pedido-foi-gerado-pelo-Sigapls
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22761073299223) Tempo aproximado para leitura:  **Dúvida**Ao excluir um pedido de compras, o sistema exibe help, informando que o pedido foi gerado pelo módulo do SIGAPLS e não permite a exclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22761073302679)

**Ambiente**Protheus – Gestão de Compras – A partir da versão 12  
  
**Solução**O sistema exibe esse help e não permite a exclusão, em virtude do **campo C7\_LOTEPLS estar com conteúdo diferente de branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22761068040343)

Esse campo só é preenchido por padrão, quando o pedido de compas é gerado através do módulo do Sigapls. Quando a inclusão do pedido de compras for efetuada diretamente pelo módulo do compras, ele deve ficar em branco. Assim a exclusão do mesmo, ocorrerá normalmente.

***Saiba Mais:***

**[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Demais Artigos Materiais - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)**
