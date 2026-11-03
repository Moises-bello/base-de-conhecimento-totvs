---
content_hash: c5747536d472a0254e385320d76cdc8323f69384ae160a96541050069c2a3422
fetched_at: '2026-06-29T00:08:55.906526+00:00'
page_id: '351028181'
product: rm
source: tdn-rm
title: 1530913 RMSAU-2729 DT Campo Custo Médio com opção de valor fixo por produtos
  e tabela de convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351028181
version: 2
---

# Campo Custo Médio com opção de valor fixo por produtos e tabela de convênios

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Tabelas de Preço de MATMED |  |  | | --- | | **Rotina(s) envolvida(s)** | | Elaboração de Contas, Movimentação de estoque | |  | |
| **Cadastros Iniciais:** | Produto, Tabelas de MATMED |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-2729 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQl Server, Oracle |
| **Tabelas Utilizadas:** | SZITEMESTQPRECO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Disponibilizar campo de Custo Médio com opção de valor fixo por produtos e tabela de convênios. A ideia é utilizar este novo campo para produtos que são reutilizáveis para obter o custo médio. Caso este campo esteja informado, o sistema utilizará este valor como sendo o custo médio, caso contrário, utilizará o valor definido por produto (ou se tiver parametrizado por produto e filial)

## Procedimento para Utilização

1. Acesse o menu Cadastros / Estoques / Produto
2. Selecione o produto desejado
3. Clique em Anexos / Informações - TOTVS Saúde
4. Clique em Anexos / Tabela de Preço
5. Após informar este campo, o sistema passará a utilizá-lo para gravar o custo médio na tabela SZATENDMATMED, campo VALORCUSTOUNITARIO
6. Nas rotinas de Elaboração de Contas e Movimentação de Estoque, ou seja, os pontos em que há o lançamento do MATMED na conta hospitalar considerarão o novo campo caso esteja informado.
