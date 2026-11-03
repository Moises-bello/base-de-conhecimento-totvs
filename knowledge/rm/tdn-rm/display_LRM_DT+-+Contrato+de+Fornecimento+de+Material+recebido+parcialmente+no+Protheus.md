---
content_hash: 10c6e6662c769a31bb32d6d2a7d6d58371fd0af1498ec744642e3e00a4f73758
fetched_at: '2026-06-29T00:10:30.193182+00:00'
page_id: '519208137'
product: rm
source: tdn-rm
title: DT - Contrato de Fornecimento de Material recebido parcialmente no Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Contrato+de+Fornecimento+de+Material+recebido+parcialmente+no+Protheus
version: 1
---

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | Gestão de Obras e Projetos |
| Função: | Eliminação de Residuos |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPEXECONTROL01-5450](https://jiraproducao.totvs.com.br/browse/TOPEXECONTROL01-8057) |

## **SITUAÇÃO/REQUISITO**

Sistema permitir receber parcialmente em um pedido de material extra utilizando contrato de fornecimento de material .

## SOLUÇÃO

Criação de um processo que verifica quantidade parcial nao utilizada , trazendo para o pedido de material extra o estorno.

Processo disponibilizado na visão da funcionalidade de Pedidos de Materiais do TOTVS Obras e Projetos, e que tem como objetivo verificar a existência de resíduos eliminados no Protheus e atualizar a quantidade estornada do respectivo item no pedido, o que possibilitará que essa quantidade estornada possa ser pedida novamente. Esta rotina pode ser executada através da visão de pedidos de materiais ou ser agendada em ambiente configurado em três camadas.

Para pedidos de Materiais Extras com Contrato, ao executar o processo de Eliminação de Resíduo, é criado um período de estorno no contrato, fazendo com que o saldo daquele item seja estornado no contrato.

Visão dos Pedidos Extras com Contratos Estornados:

Visão do período de estorno no Contrato:

[Eliminação de Residuos](https://tdn.totvs.com/pages/viewpage.action?pageId=387286947)
