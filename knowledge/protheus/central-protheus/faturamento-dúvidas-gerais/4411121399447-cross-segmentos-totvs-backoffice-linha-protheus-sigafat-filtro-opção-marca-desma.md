---
article_id: 4411121399447
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: bef63f18f3babe21ac1053a2ea0bfb89cac9082cf596ab254a223f1134be5de3
fetched_at: '2026-06-28T22:38:29.977115+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Filtro / Opção
  "Marca-Desmarca todos" MATA460A
type: support-article
updated_at: '2024-05-29T21:26:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411121399447-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Filtro-Op%C3%A7%C3%A3o-Marca-Desmarca-todos-MATA460A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Filtro aplicado na rotina MATA460A não esta sendo respeitado ao marcar a opção todos os registros.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Ao aplicar o filtro pela caixa de pesquisa da rotina de Documento de Saída( **MATA460A**) de um pedido e selecionar o botão marcar/desmarcar todas, o sistema marcará todos os itens independente de estarem ocultos ou não, dessa forma ao invés de faturar somente o Pedido de Venda do filtro, é faturado todos os Pedidos de Venda liberados.

Exemplo abaixo:

![Gravar-_408.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411120842647/Gravar-_408.gif)  
  
Para que seja marcado apenas o pedido de venda da caixa pesquisa é necessário selecionar manualmente:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411121379735/mceclip0.png)

Abaixo os Pontos de Entrada da rotina MATA460A que podem ser utilizados, conforme a necessidade:

* **M460MKB - Retorno de condição**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6784190>

* **M460MARK - Validação de pedidos marcados**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6784189>
