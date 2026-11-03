---
article_id: 360028357991
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 40f343eb4f3ac07630620a99d34b215140aaa1f3af968d4861095cb714d32b6d
fetched_at: '2026-06-28T22:38:41.102670+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como cadastrar
  abas no pedido de venda
type: support-article
updated_at: '2022-08-29T17:43:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028357991-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-cadastrar-abas-no-pedido-de-venda
---

**Dúvida**

Como cadastrar abas no pedido de venda?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões

**Solução**

Por padrão, o pedido de vendas não utiliza abas para agrupar os campos. Porém e aberto para que seja agrupado.  
O cadastro de pastas é o arquivo de dicionário **SXA**, porém, o vinculo entre o campo e a pasta é feita pelo campo **X3\_FOLDER**.

Para cadastrar abas no pedido de venda, realize os seguintes passos:  
1. Acesse o Configurador;  
2. Acesse Base de Dados > Dicionario > Arquivos;  
3. Pesquise pela tabela SC5 > Editar;  
4. Selecione a aba Agrupamentos > Clique em Incluir.

![Agrupadores.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360028408072/Agrupadores.gif)
