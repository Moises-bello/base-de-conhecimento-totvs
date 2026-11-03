---
content_hash: f92d41400cfd95fa38647bb6985a728adc71050ef8540d6a350835d7495cb6cc
fetched_at: '2026-06-29T00:08:28.884464+00:00'
page_id: '271863942'
product: rm
source: tdn-rm
title: 208553 MCP-1878 DT Cadastro Redução Z
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271863942
version: 4
---

# Cadastro Redução Z

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MovReducaoZAction | *Redução Z* | |
| **Tickets relacionados** | *208553.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MCP-1878* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *TREDUCAOZ* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação para alterar a nomenclatura dos campos 'Cupom Inicial' e 'Cupom Final' da Redução Z para 'COO Inicial' e 'COO Final'.

Esse procedimento não afeta o processo do cliente já que a alteração foi apenas na nomenclatura dos campos, visto que o conteúdo dos mesmos já era automaticamente preenchido (e posteriormente escriturado para o TOTVS Gestão Fiscal) com os dados do COO inicial e final da Redução.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.16*deste chamado.

## Procedimento para utilização

Em ***"Cadastros | Fiscais | Mais | Redução Z | Valores Financeiros"***, ao criar uma nova Redução Z ou ao editar uma já existente, o usuário poderá verificar a modificação no nome dos campos.

Veja abaixo:
