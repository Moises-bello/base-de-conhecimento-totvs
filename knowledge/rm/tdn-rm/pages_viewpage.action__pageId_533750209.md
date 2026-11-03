---
content_hash: ca7fcd86c9533f55ba4c657d6e6d2d00538d618890faf1fbc5ceac675ee598b8
fetched_at: '2026-06-29T00:10:37.019569+00:00'
page_id: '533750209'
product: rm
source: tdn-rm
title: DT - Cópia do Aditivo de um Item de Contrato para Todos os demais itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533750209
version: 63
---

# Cópia do Aditivo de um Item de Contrato para todos os demais itens

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | CtrItmAditivoCntAction | Aditivos Contratuais | |
| **Tickets relacionados** | -- Central Colaborativa |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** | TITMCNT, TITMCNTADITIVO |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Ao adicionar um aditivo no item de Contrato, é possível fazer uma cópia desse para todos os demais itens.

Será apresentada uma mensagem validando a operação.

Caso o processo seja novamente efetuado, selecionando o mesmo item de aditivo, uma segunda cópia será realizada.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de 12.1.28.

## Procedimento para Utilização

-- Acessar o item de um Contrato e na pasta "Informações Adicionais | Aditivos", incluir um novo item.

-- Salvar o Contrato.

-- Selecionar os aditivos que deseja replicar para os demais itens e clicar no botão "Aplicar aditivo a todos os itens".

divs
