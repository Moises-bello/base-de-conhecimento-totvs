---
article_id: 4418747275287
category: Materiais - Compras (SIGACOM)
content_hash: 5fd8500a361fd0add4807e7bc7f6018e6cd03ea0b333e9b04c90d77e6ca8f6e8
fetched_at: '2026-06-28T22:41:12.902445+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Ao realizar a Cópia
  do Pedido de Compras e alterar o Produto não atualiza os campos Centro de Custo
  e Conta Contábil com as entidades do Cadastro de Produto (B1_CC) e (B1_CONTA) do
  novo produto
type: support-article
updated_at: '2022-01-11T20:04:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418747275287-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-realizar-a-C%C3%B3pia-do-Pedido-de-Compras-e-alterar-o-Produto-n%C3%A3o-atualiza-os-campos-Centro-de-Custo-e-Conta-Cont%C3%A1bil-com-as-entidades-do-Cadastro-de-Produto-B1-CC-e-B1-CONTA-do-novo-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

Ao realizar a Cópia do Pedido de Compras e alterar o Código do produto (C7\_PRODUTO) não estão sendo trazidos o Centro de Custo (C7\_CC) e Conta Contábil (C7\_CONTA) das entidades contábeis  do cadastro do Novo Produto (B1\_CC) e (B1\_CONTA) incluso nesta cópia do Pedido, mantendo as entidades do produto anterior.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
  
**Solução**Altere o parâmetro MV\_PRODCTB para .T. para que o sistema relacione as Entidades Contábeis nos itens do Pedido de Compras (MATA120), conforme cadastradas na tabela SB1 (Cadastro de Produtos), maiores informações sobre o parâmetro consulte a documentação do link [MP - SIGACOM - Qual a Funcionalidade do MV\_PRODCTB no Pedido de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011920891-MP-SIGACOM-Qual-a-Funcionalidade-do-MV-PRODCTB-no-Pedido-de-Compras-?source=search)

***Saiba Mais :***

[MP - SIGACOM - Qual a Funcionalidade do MV\_PRODCTB no Pedido de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011920891-MP-SIGACOM-Qual-a-Funcionalidade-do-MV-PRODCTB-no-Pedido-de-Compras-?source=search)

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

#
