---
article_id: 22398548690839
category: SIGAEST - LEGAIS
content_hash: 3b41e9644f79edd70019bddfdcd7d152aa5788a6b16d2246f25ed08bfaecd476
fetched_at: '2026-06-28T22:38:51.600271+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Bloco K200
  não mostra saldo em estoque próprio
type: support-article
updated_at: '2024-03-28T14:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22398548690839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Bloco-K200-n%C3%A3o-mostra-saldo-em-estoque-pr%C3%B3prio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548656279) Tempo aproximado para leitura: **00:03:00min****Ocorrência**Nesta documentação iremos abordar um cenário de movimentação, que no registro K200 não mostra o saldo de estoque próprio.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para ilustrar essa ocorrência, iremos primeiro demonstrar o cenário de um produto sem saldo em estoque:

**1-** Cadastro de produto;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548660247)

**2-** Receber uma remessa via MATA103 com uma TES que atualiza estoque e controle poder de terceiros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398565719191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548667287)

**3-** Após a remessa, vamos confirmar o saldo do produto através da consulta F4:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548669463)

**4-** Geração do MATR241, para visualização da montagem do Bloco K:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548671511)

**Observação:** Neste cenário é correto não trazer saldo em estoque próprio no K200, pois o produto não tinha saldo e os 20 que recebeu de fato são de terceiros. Caso o sistema listasse 20 em estoque próprio, seria um erro, pois a interpretação deste resultado seria que haveria 40 unidades no total deste produto em estoque.

**5-** Vamos imaginar que fisicamente foi localizado 10 unidades "perdidas" deste mesmo produto, em estoque, que não existem no sistema. Diante deste cenário, é realizado um inventário para ajuste da quantidade no sistema. Para isto, será realizada a digitação de inventário e o acerto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398565730967)

**6-** Após a digitação do inventário, vamos gerar novamente o MATR241 para conferência do Bloco K200:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398548677143)

**Observação:** Mesmo após a digitação do inventário de 10 unidades, o sistema continua listando apenas os 20 que foram recebidos de terceiros, porém este comportamento não se trata de um erro, na verdade o erro está no processo de inventário, pois as 10 unidades que estavam "perdidas" deveriam ser somadas com as 20 unidades que foram recebidos de terceiros atualizando estoque. Desta maneira a digitação deveria ter sido de 30 unidades, (sendo 20 de terceiros e 10 próprio) e com isso no MATR241 iria listar as duas quantidades (10 em estoque próprio e 20 de terceiros).

**Importante:** O conceito da digitação do inventário, é realizar a contagem física de determinado produto, informando a quantidade para acerto do estoque, independente de ser de terceiro ou próprio, visando apenas a quantidade física total.

Saiba mais:

[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
