---
article_id: 4411683662231
category: SIGAEST - RELATORIOS
content_hash: 48658fa81b373de0bd967741c5c5c79143680e97a678472a05486f87c712b62d
fetched_at: '2026-06-28T22:39:06.219822+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Por que a coluna "Custo
  Médio do Movimento" ficou em branco no meu relatório MATR900?
type: support-article
updated_at: '2021-11-08T11:41:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411683662231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Por-que-a-coluna-Custo-M%C3%A9dio-do-Movimento-ficou-em-branco-no-meu-relat%C3%B3rio-MATR900
---

**Dúvida**Por que a coluna "Custo Médio do Movimento" ficou em branco no meu relatório MATR900?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Nesse cenário que iremos apresentar é normal que o custo médio não apareça quando a quantidade é 0, ou seja não movimentou saldo em quantidade, principalmente em nota complementar ou movimentação apenas de custo do produto.

O custo médio do movimento é formado da seguinte forma, por exemplo, vamos pegar a nota fiscal de entrada, é somente um exemplo e pode ser feito com outras tabelas de movimentação de estoque como a SD2 e SD3:  
  
D1\_CUSTO / D1\_QUANT = Custo Médio do Movimento.

Temos uma nota complementar que movimentou apenas custo do produto, logo , ele está dividindo por 0, sendo assim não tem com o que dividir, então na coluna "Custo Médio do Movimento" fica em branco:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411683404823/mceclip0.png)

Isso não é uma regra do sistema Protheus e sim matematicamente falando, ou seja não é possível dividir um valor por 0.

Repare no relatório acima que somente o movimento que possui quantidade, tem a coluna**"custo médio do movimento"** preenchido.

Não se preocupem, o custo de 30 reais entrou no custo atual do produto, sendo assim, ele vai ser somado ao custo médio do produto.

**Saiba mais:**

*[MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)*

*[MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)*

*[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)*

*[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
