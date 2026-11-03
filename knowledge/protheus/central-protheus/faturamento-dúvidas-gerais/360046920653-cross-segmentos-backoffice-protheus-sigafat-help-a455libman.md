---
article_id: 360046920653
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 06e3df664cf3e6f7de096bcadb9b686b7ef44ff4a9e9ee83dd2ea03075f219c8
fetched_at: '2026-06-28T22:38:29.823241+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - HELP A455LIBMAN
type: support-article
updated_at: '2026-01-20T18:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046920653-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-HELP-A455LIBMAN
---

**Dúvida**

Ao tentar liberar estoque para os pedidos  de venda apresenta a mensagem **Help: A455LIBMAN**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067139913)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.

**Solução**

O Help **A455libman** só ocorre se a liberação do produto possuir rastro e/ou localização, para este caso, o sistema não permite a liberação do estoque (**MATA455**).

Produtos com Controle de Lote (campo “Rastro” (B1\_RASTRO)) ou de Endereço (campo “Contr.Endere” (B1\_LOCALIZ)) **não podem ser liberados de forma Manual**, pois este tipo de liberação gera saldo negativo e isso comprometeria a integridade de rastreamento configurada no Produto.

Esse produtos  possuem relação entre as  tabela de  saldos fisico (**SB2**),  controle de lote (**SB8**),  controle de localização (**SBF**) entre outras, podendo acarretar falha de integridade de saldos.

É necessário possuir **Saldo Disponível** para que a liberação seja feita somente  no modo **Automático** (utilizando o conceito de FEFO - First expire, First (Primeiro a vencer, primeiro a sair)).

Também é possível indicar manualmente o Lote/Sub-Lote desejado no Pedido de Vendas (MATA410) através dos campos “Lote” (C6\_LOTECTL) e “Sub-Lote” (C6\_NUMLOTE), antes da Análise Automática de Estoque.

Para seleção de Lote e Endereço será necessário avaliar o[Funcionamento da função "Nova Liberação" na rotina Liberação de Estoque (MATA455)](https://tdn.totvs.com/x/TqxZE)

**Saiba mais:** [Liberação / Bloqueio “indevido” de Estoque](https://tdn.totvs.com/x/zGk-Dg)
