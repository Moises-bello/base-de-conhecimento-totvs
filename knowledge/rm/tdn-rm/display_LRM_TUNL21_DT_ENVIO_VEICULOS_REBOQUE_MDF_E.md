---
content_hash: 697139e84e7cf50d8112eafda046a73854c6ca3dfad3b88d3ea683d2816919ec
fetched_at: '2026-06-29T00:08:03.950094+00:00'
page_id: '235330800'
product: rm
source: tdn-rm
title: TUNL21_DT_ENVIO_VEICULOS_REBOQUE_MDF_E
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNL21_DT_ENVIO_VEICULOS_REBOQUE_MDF_E
version: 112
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MDF.002 .* | MDF-E - INCONSISTENCIA | |
| **Cadastros Iniciais:** | *Cadastro de Veículos* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | TUNL21, TUPTBN |
| **Requisito (ISSUE):** | MOV000174 - Manifesto Eletrônico de Documentos Fiscais (MDF-e) |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | *N/A.* |
| **Tabelas Utilizadas:** | *TVEICULOS, TCOMPONENTECARGA, TMOV, TMDFE* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Melhoria para envio de veículos de Reboque no XML do MDF-e.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 11.82.42.146, 11.82.43 ou 12.1.11

## Procedimento para Utilização

       1.            Crie um Movimento de MDF-e. Nesse Movimento vincule, além do veículo de tração, outros veículos - cadastrados na tabela TVEICULOS com o campo "Tipo do veículo" como "Reboque".

       2.            Envie o MDF-e e verifique que as tags veicReboque serão preenchidas.

divs
