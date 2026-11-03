---
article_id: 35334349407511
category: Materiais - Compras (SIGACOM)
content_hash: d85172edb23e83e5a5f0fb2e93ea4a7cea74917d6f0a6e8777b03fc61bde7deb
fetched_at: '2026-06-28T22:41:13.028594+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Na alteração do Pedido
  de compras apresenta a mensagem " Este pedido não poderá ser alterado pois foi gerado
  pelo modulo SIGAPLS "
type: support-article
updated_at: '2025-10-01T17:24:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35334349407511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-altera%C3%A7%C3%A3o-do-Pedido-de-compras-apresenta-a-mensagem-Este-pedido-n%C3%A3o-poder%C3%A1-ser-alterado-pois-foi-gerado-pelo-modulo-SIGAPLS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35334317045783) Tempo aproximado para leitura: **00:02:SS min**  
  
**Dúvida**  
Ao alterar uma pedido de compras, o sistema exibe a mensagem " Este pedido não poderá ser alterado pois foi gerado pelo modulo SIGAPLS .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35334317046295)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigacom - Todas as versões]  
  
**Solução**  
Caso o pedido tenha sido incluído manualmente pela rotina pedido de compras no módulo de compras, é necessário avaliar se o campo C7\_LOTPLS  está preenchido, pois esse campo só deverá estar preenchido, quando o pedido for gerado pelo módulo do Sigapls. ( Plano de Saúde ). Para pedidos incluídos diretamente pelo compras, esse campo deverá ficar em branco, para que o sistema não identifique vínculo com o PLS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35334317046423)

Caso o Pedido de compras tenha sido gerado pelo módulo do PLS, a alteração deverá ocorrer pelo módulo. No compras a alteração não será passível de ser executada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
