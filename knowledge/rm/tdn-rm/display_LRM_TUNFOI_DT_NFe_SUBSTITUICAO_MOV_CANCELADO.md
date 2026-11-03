---
content_hash: 41f8cb3e6e69e032b688e357c188580c0d0cb12dc388bffd9eb3db321a5d9a33
fetched_at: '2026-06-29T00:08:05.565425+00:00'
page_id: '235598124'
product: rm
source: tdn-rm
title: TUNFOI_DT_NFe_SUBSTITUICAO_MOV_CANCELADO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNFOI_DT_NFe_SUBSTITUICAO_MOV_CANCELADO
version: 117
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV.014             .* | COPIA POR REFERENCIA | |
| **Cadastros Iniciais:** | *-.* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | *TUNFOI., TUTII6* |
| **Requisito (ISSUE):** | MOV000103 - Cópia de movimento |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *TMOV* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria para permitir que NF de substituição sejam geradas a partir de movimentos cancelados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.43.100 ou superior d*este chamado

## Procedimento para Utilização

       1.            Gere um Movimento de NFSe

       2.            Gere um Movimento de substituição dessa NFSe (via cópia por referência, Motivo referênbcia Substituicao NFe) - nesse momento o movimento original será cancelado.

       3.            Cancele o movimento de substituição gerado.

       4.            Gere uma nova cópia por referência do movimento original.

divs
