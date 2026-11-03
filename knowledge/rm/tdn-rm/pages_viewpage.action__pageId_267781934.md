---
content_hash: ac39f8c88a44f2d6908327aecc59f95d14971b8157d20ca7f1aa1e8005bd5f95
fetched_at: '2026-06-29T00:08:19.349391+00:00'
page_id: '267781934'
product: rm
source: tdn-rm
title: TVXCHN_DT_Permissão_Auditar_Contas_Em_Elaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267781934
version: 110
---

# Permissão para auditar contas em elaboração

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento | Auditoria Pré-Glosa | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para permitir auditar contas com status **Em Elaboração**.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.12.010 do RM Saúde

## Procedimento para Utilização

1. Marque o parâmetro “Permitir auditar contas em elaboração”.
2. Cadastre um atendimento para qualquer paciente e lançar itens na conta do paciente.
3. Ao acessar a tela de auditoria pré-glosa o sistema exibirá o paciente que está com a conta em elaboração.

divs
