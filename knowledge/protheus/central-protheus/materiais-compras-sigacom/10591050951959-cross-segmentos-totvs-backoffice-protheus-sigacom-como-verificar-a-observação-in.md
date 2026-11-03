---
article_id: 10591050951959
category: Materiais - Compras (SIGACOM)
content_hash: 34d41c0ba8232c70518c6b144b707a490bfe6845528de34bbfb38bdb73cc171a
fetched_at: '2026-06-28T22:41:16.107285+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como verificar a Observação
  inserida ao fazer a Liberação de um Pedido de Compras ?
type: support-article
updated_at: '2022-12-06T19:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10591050951959-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-verificar-a-Observa%C3%A7%C3%A3o-inserida-ao-fazer-a-Libera%C3%A7%C3%A3o-de-um-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como verificar a Observação inserida ao fazer a Liberação de um Pedido de Compras ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**Na Liberação de um Pedido de Compras, ao ser inserida uma informação no campo "Observação" da tela de liberação:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10591059182615)

A possibilidade existente no padrão do sistema de verificação da observação inserida, é na através da Visualização do pedido, na opção "Outras ações -> Aprovac":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10591061030423)

Na tela das aprovações realizadas que é aberta, na linha do aprovador que fez a aprovação e inseriu a observação, pode-se verificar clicando em "Memo" no campo/coluna "Observações" as informações que foram colocadas no momento da aprovação:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10591047446679)

A informação que é inserida no campo "Observações" na tela de liberação do Pedido (MATA094) fica gravada no campo ***CR\_OBS*** da tabela SCR, e caso se desejar, pode-se desenvolver um relatório personalizado para extração da informação conforme a necessidade.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
