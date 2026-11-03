---
article_id: 360012397312
category: Materiais - Compras (SIGACOM)
content_hash: 3de961daa38bac914a89218f06c07e39a9e45b8f0a93de994c1f8cf91df5c24c
fetched_at: '2026-06-28T22:41:10.446806+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Solicitação de Compras
  com Aprovação Rejeitada continua com quantidade prevista no Produto
type: support-article
updated_at: '2021-12-24T12:37:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012397312-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Solicita%C3%A7%C3%A3o-de-Compras-com-Aprova%C3%A7%C3%A3o-Rejeitada-continua-com-quantidade-prevista-no-Produto
---

**Dúvida**

Ao Rejeitar a Aprovação uma Solicitação de Compras o sistema não está atualizando a quantidade Prevista de Entrada para o Produto

**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
  
**Solução**

Quando uma SC tem sua aprovação rejeitada, sua quantidade prevista de entrada por padrão não é eliminada.

Para que o campo seja atualizado, é necessário realizar a eliminação do resíduo.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008713732/1.png)

Na rotina Eliminação Por Resíduo (MATA235), atentar- se para os perguntes:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008713712/2.png)

Após o processo o campo B2\_SALPEDI será atualizado.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008713752/3.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
