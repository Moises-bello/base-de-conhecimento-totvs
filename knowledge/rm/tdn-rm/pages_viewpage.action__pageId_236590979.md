---
content_hash: 1f3fb16f1e84f3dbf8be2444c97c87d15cd6da8c06c408c2fcebf397a123bfa8
fetched_at: '2026-06-29T00:08:06.297621+00:00'
page_id: '236590979'
product: rm
source: tdn-rm
title: TTQRO8_DT_Copia_Itens_Copia_Referência_NF_e_Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236590979
version: 114
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=219695506) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV.014 .* | COPIA POR REFERENCIA | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TTQRO8 |
| **Requisito (ISSUE):** | MOV000103 - Cópia de movimento |
| **País(es):** | *Bra* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | TMOTIVOREFMOV |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria para permitir copia de itens na cópia de referência para NF-e Complementar.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado 11.82.43 ou superior.

## Procedimento para Utilização

       1. Foi criado um motivo de referência novo (27 - NF Complementar com Cópia de Itens) para essa situação.

       2. Selecione esse Motivo de referência para um  tipo de Movimento, realize a cópia por referência e verifique que os itens serão copiados.

divs
