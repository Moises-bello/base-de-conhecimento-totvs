---
article_id: 15793556359703
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 1c4925f75ab670a2eacb46820cfbe18e9ab0ce4aad0096b70119a6b4a2eadaf5
fetched_at: '2026-06-28T22:38:23.820469+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração
  do TES para utilização do Portal Gestão de Vendas (PGV)
type: support-article
updated_at: '2024-01-02T13:12:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15793556359703-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-TES-para-utiliza%C3%A7%C3%A3o-do-Portal-Gest%C3%A3o-de-Vendas-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15793565920663) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como selecionar o Tipo de Saída (TES) de um item do Pedido de Venda no Portal gestão de Vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33;  
  
**Solução**Diferente da rotina **Pedidos de Venda**(**MATA410**) do **Protheus**onde o usuário pode selecionar o **Tipo de Saída** (C6\_TES) em cada item do Pedido de Venda, o Portal Gestão de Vendas utiliza o campo **Tipo de Operação** na aba **Dados Gerais** para definir o tipo de saída utilizado na gravação do Pedido de Venda, utilizando a rotina [TES Inteligente](https://tdn.totvs.com/x/H5QcJ) (**MATA089**) para definir o tipo de saída.

Caso nenhuma condição cadastrada na rotina [TES inteligente](https://tdn.totvs.com/x/H5QcJ) seja atendida, será utilizada a TES informada no cadastro do [Produto](https://tdn.totvs.com/x/6JpWF) (**MATA010**).

TES Inteligente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15792586789527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15792919760279)

Tipos de Entrada e Saída - TES

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15793046006807)

**Observação:** O Portal Gestão de Vendas não valida o Parâmetro "MV\_ARQPROD = SBZ" ele precisa estar Configurado como "SB1", para o funcionamento correto do PGV.
