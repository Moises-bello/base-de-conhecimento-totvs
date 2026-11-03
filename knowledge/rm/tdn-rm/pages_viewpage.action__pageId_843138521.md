---
content_hash: 9d0dd35398b5791b2a2608e2009ba8ea7bc648230ee809ced2bcaacb0d3d4209
fetched_at: '2026-06-29T00:11:50.572990+00:00'
page_id: '843138521'
product: rm
source: tdn-rm
title: Relacionamento de movimentos que utilizam cópia por referência.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=843138521
version: 5
---

Quando é utilizado o processo de **Cópia por Referência** alguns dos **Motivos de Referência** irão criar um **Relacionamento** entre o movimento original que será copiado e o movimento destino, o que implica na funcionalidade de **Rastreabilidade,** no momento em que for acionada tanto no movimento de origem quanto no movimento de destino será possível a visualização de ambas movimentações.

O conceito de **Relacionamento** diz respeito a tabela do Banco de Dados chamada de TMOVRELAC, esta tabela guarda os dados de movimentações que passaram pelos processos de Faturamento, Devolução e Cópia por Referência. Nela são encontrados as numerações de Identificador do movimento de origem e destino e o Tipo de Relacionamento que foi criado.

**Separados abaixo estão os Motivos de Referência que geram Relacionamento separados pelo Tipo de Relacionamento Gerado (TIPORELAC) e por suas respectivas numerações e nomenclaturas no sistema:**

**Tipo de Relacionamento classificado como TIPORELAC = V para Notas Fiscais de Devolução**

* 3 -NF Acompanhamento de Cupom Fiscal
* 4 -Devolução de Compra de Mercadorias
* 5 - Devolução de Venda de Mercadorias
* 8 - Devolução material receb. conta e ordem
* 30 - Devolução por Recusa
* 31 - Devolução de Empréstimo

**Tipo de Relacionamento classificado como TIPORELAC = M para Documento Eletrônico Complementar**

* 6 -Nota Fiscal Complementar Retificadora

**Tipo de Relacionamento classificado como TIPORELAC = T para movimentações de Estoque Terceiros**

* 10 -Retorno de Remessa - Estoque Terceiros
* 11 -Retorno Mercadoria Não Aplicada Industrialização
* 12 -Retorno de Remessa para Industrialização - Estoque Terceiros
* 14 - Venda Mercadoria Consignada - Estoque Terceiros
* 36 -Retorno de Remessa para Industrialização por Conta e Ordem

**Tipo de Relacionamento classificado como TIPORELAC = G para Notas Fiscais de Devolução de Consignado**

* 13 - Devolução Simbólica de Mercadoria em Consignação - Estoque Terceiros
* 15 - Devolução Mercadoria Consignada não Comercializada - Estoque Terceiros

**Tipo de Relacionamento classificado como TIPORELAC = C para Documento Eletrônico CTE**

* 16 -Conhecimento Transporte Eletrônico (CT-e) – Anulação
* 17 -Conhecimento Transporte Eletrônico (CT-e) - Substituição

**Tipo de Relacionamento classificado como TIPORELAC = S para Notas Fiscais de Substituição**

* 19 - Substituição NFe - Serviço

**Tipo de Relacionamento classificado como TIPORELAC = R para movimentações c****om relacionamento (TIPORELAC = R)**

* 20 -Copia Com Relacionamento
* 25 -Cópia Simples com relacionamento somente de Movimento
* 26 -Transformação de Itens - Movimentações Internas entre Produtos
* 29 -Desmontagem de Mercadorias
* 32 -Reporta Insumo MNT

**Tipo de Relacionamento classificado como TIPORELAC = A para Notas Fiscais de Ajuste (TIPORELAC = A)**

* 21 -Cópia NF-e de Ajuste - Cancelamento Indevido

**Tipo de Relacionamento classificado como TIPORELAC = O  para Notas Fiscais de Ajuste Estorno (TIPORELAC = "O")**

* 22 -Cópia NF-e de Ajuste - Estorno de Venda
* 23 - Cópia NF-e de Ajuste - Estorno de Compra

**Tipo de Relacionamento classificado como TIPORELAC = L para Notas Fiscais de Produtor Rural (TIPORELAC = L)**

* 24 - NF-e Produtor Rural - Contra Nota

**Tipo de Relacionamento classificado como TIPORELAC = X para Notas Fiscais de Remessa Parcelada Exportação**

34 - Remessa Parcelada de Exportação

**Tipo de Relacionamento classificado como TIPORELAC = J para Notas Fiscais de Débito referente a Juros e Multa**

38 - Nota de Débito referente a Juros e Multa
