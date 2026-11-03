---
content_hash: ddc0e32b3055b40bf7311e3602d3d30cdf237a5c9fe36cb6265ee06bf2008fb4
fetched_at: '2026-06-29T00:08:18.670966+00:00'
page_id: '266964323'
product: rm
source: tdn-rm
title: TVNHBJ_DT_NAO_CONSISTIR_CFO_AO_SALVAR_MOVIMENTO_DE DEVOLUCAO_DE_SAT
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNHBJ_DT_NAO_CONSISTIR_CFO_AO_SALVAR_MOVIMENTO_DE+DEVOLUCAO_DE_SAT
version: 115
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | VEN.004 | DEVOLUCAO DE VENDAS | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TVNHBJ |
| **Requisito (ISSUE):** | *MOV000103 - Cópia de movimento* |
| **País(es):** | *-* |
| **Banco(s) de Dados:** | *.* |
| **Tabelas Utilizadas:** | - |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria para não consistir a troca de cliente/fornecedor no Movimento de Destino  de devolução quando o Movimento de Origem possuir o Tipo de Documento 59

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.45.106*

## Procedimento para Utilização

1. Criar um movimento de saída com Tipo de Documento igual a 59

2. Criar um movimento de devolução de venda(Cópia por referência - Motivo 5) e troque o Cliente fornecedor.

3. Salve e verifique que não haverá consistência nessa troca.

divs
