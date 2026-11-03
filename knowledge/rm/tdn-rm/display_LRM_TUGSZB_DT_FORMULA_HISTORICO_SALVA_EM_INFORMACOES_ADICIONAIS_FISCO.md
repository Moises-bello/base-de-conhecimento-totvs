---
content_hash: 8579930a0df0e422607cd717dc925a47e07abf18f4f9eb5e0227d5d7093d1b10
fetched_at: '2026-06-29T00:08:08.367239+00:00'
page_id: '238031385'
product: rm
source: tdn-rm
title: TUGSZB_DT_FORMULA_HISTORICO_SALVA_EM_INFORMACOES_ADICIONAIS_FISCO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGSZB_DT_FORMULA_HISTORICO_SALVA_EM_INFORMACOES_ADICIONAIS_FISCO
version: 113
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | LI.01.0037 | OBRIGAÇÕES PRINCIPAIS - APURAÇÃO ICMS | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TUGSZB |
| **Requisito (ISSUE):** | MOV000062 - Parâmetros do tipo de movimento |
| **País(es):** | *Bra* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *TITMTMV* |
| **Sistema(s) Operacional(is):** | *-.* |

## Descrição

Melhoria para permitir que a fórmula do histórico afete os campos de Informações Adicionais do Fisco e Informações do Contribuinte.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 11.82.44 deste chamado

## Procedimento para Utilização

       1.            Criado novo parâmetro no Movimento e no item de Movimento para permitir que a fórmula do histórico  seja enviada para o campo Informações Adicionais do Fisco e do Contribuinte.

       2.            Após parametrizar, salvar o movimento e verificar que o resultado foi salvo no campo certo.

divs
