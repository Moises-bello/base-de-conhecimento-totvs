---
content_hash: fa76e098a02565853585f8676880f53d992b39826e91d7033ec4e341febc0dd6
fetched_at: '2026-06-29T00:08:32.558637+00:00'
page_id: '273990934'
product: rm
source: tdn-rm
title: 198737 MSAU-8176 DT Transferência de Produtos Consignados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273990934
version: 109
---

# Transferência de produtos consignados

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | Rotina | Nome Técnico | | Estoque | Movimentação de estoque | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQl Server |

## Descrição

Criado parâmetro para identificar o tipo de movimentação para itens consignados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.105 da biblioteca do RM.

## Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar, acesse o menu Opções > Parâmetros > Integração RM Nucleus;

       2.            Configure um movimento no parâmetro "Mov. Transferência de itens consignados" ;

       3.            Em seguida, acesse a tela de movimentação de estoque e crie uma movimentação de transferência entre centro de custos;

       4.            Na movimentação, lance um produto e configure como item consignado.

       5.           Ao Processar a requisição, o sistema deve realizar a transferência do produto para outro local de estoque, conforme configurado na movimentação.

divs
