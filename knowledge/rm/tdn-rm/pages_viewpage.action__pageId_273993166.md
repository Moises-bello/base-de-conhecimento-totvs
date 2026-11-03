---
content_hash: ba8eeec353af717d26bed8dac37588a4843bb1bd01b7dde4f0162e3a03781b43
fetched_at: '2026-06-29T00:08:32.606704+00:00'
page_id: '273993166'
product: rm
source: tdn-rm
title: 574120 MSAU-8174 DT Permissão para Movimentações de Estoque em Contas Faturadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273993166
version: 107
---

# Permissão para movimentações de estoque em contas faturadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Estoque | Movimentação de estoque | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Criado parâmetro para permitir cadastro de movimentação de estoque para atendimentos já faturados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.004 do RM Saúde.

## Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar, acesse Opções > Parâmetros > Parâmetros Gerais > Estoque, marque o parâmetro "Inclui movimentos de estoque para contas faturadas";

       2.            Em seguida, crie uma movimentação de estoque para um paciente que já tenha a conta faturada, o sistema vai apresentar uma mensagem informando que a conta já está faturada e caso o usuário clique em sim, o sistema vai cadastrar a movimentação de estoque.

divs
