---
content_hash: 6486f600459df575592b63a49a4b6a884ed02cd22ffad7a9a3c398bb7c0e2143
fetched_at: '2026-06-29T00:08:05.260464+00:00'
page_id: '235591789'
product: rm
source: tdn-rm
title: TUKJ91_DT_Atualizar_Diferimento_ICMS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKJ91_DT_Atualizar_Diferimento_ICMS
version: 118
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV.007 .* | FATURAMENTO/RECEBIMENTO | |
| *-* |  |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-.* |
| **Chamados Relacionados** | TUKJ91 |
| **Requisito (ISSUE):** | MOV000155 - Tributos do Movimento e do Item de Movimento |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *.* |
| **Tabelas Utilizadas:** | *TTRBMOV* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria para atualizar diferimento de ICMS ao se alterar a natureza do Movimento

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.83.55.225 ou superior*

## Procedimento para Utilização

**Exemplo:**

       Alterar a natureza do movimento que utiliza o tipo de tributação como (Diferido) para uma natureza que utiliza a regra de ICMS como normal e verifique que no Item do movimento na etapa de Tributos e Valores (Tributos)o campo \*Percentual Diferimento\* será alterado quando a natureza é alterada no movimento.

divs
