---
content_hash: 66b781c90dc51a294f86652a7e491139ff0e4c09559ca31c514f4cae1c022624
fetched_at: '2026-06-29T00:06:12.945676+00:00'
page_id: '205922135'
product: rm
source: tdn-rm
title: TTFRQ1_DT_Layout_De_Movimento_NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFRQ1_DT_Layout_De_Movimento_NFC-e
version: 1
---

# LAYOUT DE MOVIMENTO NFC-E

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | ***Construção e Projetos*** |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **MOV.039** | **IMPORTACAO DE MOVIMENTO** | | **MOV.001** | **INCLUSAO DE MOVIMENTO** | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas utilizadas:** | **TMov** |
| **Sistema(s) operacional(is):** | **N/A** |
| **Versões/Release:** | **11.82.41 ou superior** |

## Descrição

Melhoria no sistema com disponibilização de campos no movimento para dados integrados ao Cupom Fiscal Eletrônico (NFC-e).

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch específico **11.82.41.100** ou **11.82.42**deste chamado.

## Procedimento para Utilização

1. Através do "TOTVS Gestão de Estoque, Compras e Faturamento" acesse a aba correspondente ao Tipo de Movimento;
2. Ao incluir ou editar um movimento disponível na visão de registros, os campos correspondentes à NFC-e encontram-se na aba "NFC-e / Cupom Fiscal".
