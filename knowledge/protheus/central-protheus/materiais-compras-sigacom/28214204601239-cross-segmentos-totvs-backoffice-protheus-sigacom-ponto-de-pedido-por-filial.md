---
article_id: 28214204601239
category: Materiais - Compras (SIGACOM)
content_hash: 7048bfa1997e0fe74e3fdd4cfcdd2b5499686d4f6c59419d9d3f91eb8873ac3d
fetched_at: '2026-06-28T22:41:22.129967+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ponto de Pedido por
  Filial
type: support-article
updated_at: '2024-12-02T20:45:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28214204601239-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Ponto-de-Pedido-por-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28214204576919) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Como criar Ponto de Pedido por Filial?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Quando a tabela SB1 for compartilhada, será necessário utilizar a tabela SBZ, por meio da rotina de Indicadores de Produtos.

Será preciso configurar o parâmetro **MV\_ARQPROD = SBZ**.

Dessa forma, será possível informar uma quantidade de ponto de pedido específica por filial. Caso não exista registro na SBZ para determinado produto/filial, a rotina irá considerar as informações do cadastro do produto (SB1)

Saiba mais em :

[Como gerar Solicitação de Compras/Pedido de Compras por ponto de pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011967491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-Solicita%C3%A7%C3%A3o-de-Compras-Pedido-de-Compras-por-ponto-de-pedido)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é realizado o cálculo de necessidade na rotina Ponto de Pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27256450694935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-necessidade-na-rotina-Ponto-de-Pedido)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não está considerando Solicitação de Compras bloqueadas para o cálculo da necessidade na Rotina de solicitação de Compras por Ponto de Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27310881678615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-est%C3%A1-considerando-Solicita%C3%A7%C3%A3o-de-Compras-bloqueadas-para-o-c%C3%A1lculo-da-necessidade-na-Rotina-de-solicita%C3%A7%C3%A3o-de-Compras-por-Ponto-de-Pedido)

[SIGACOM - Pontos de Entrada Solicitação por Ponto de Pedido - MATA170](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408775373207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-Solicita%C3%A7%C3%A3o-por-Ponto-de-Pedido-MATA170)

[Qual a finalidade do parâmetro MV\_ARQPROD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235697807-Qual-a-finalidade-do-par%C3%A2metro-MV-ARQPROD)
