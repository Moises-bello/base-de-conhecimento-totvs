---
content_hash: bb2ecfcdf2e639d95ab2bd0653ba1651429fda2cb8a9f20daece5fc8e1135524
fetched_at: '2026-06-29T00:06:04.938226+00:00'
page_id: '200912780'
product: rm
source: tdn-rm
title: TTARPA_DT_Alteracao_Global_Salario_Tabela_Vitae_Reducao_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TTARPA_DT_Alteracao_Global_Salario_Tabela_Vitae_Reducao_Salarial
version: 1
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | **Folha de Pagamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Alteração Global de Salários.* | *FopRotinasAlteracaoGlobalSalariosProcess* | |
| **Cadastros Iniciais:** | 1. *Configurar integração com o TOTVS Gestão de Pessoas (RM Vitae)* 2. *Cadastrar no RM Vitae um Nível Salarial, Faixa Salarial e Tabela Salarial* 3. *Vincular um funcionário a uma tabela salarial em seu registro.* 4. *Alterar o salário do funcionário para que o mesmo fique com um salário maior do que o previsto na tabela salarial.* |
| **Parâmetro(s):** | *Tipo de mudança do salário: Alteração Tipo de alteração: Tabelas Salariais do TOTVS Gestão de Pessoas Parâmetro Permitir redução do salário: Marcado* |
| **Chamados relacionados** | *TTARPA* |
| **Banco(s) de Dados:** | *SQL Server, Oracle.* |
| **Tabelas utilizadas:** | *PFUNC, PFHSTSAL* |
| **Sistema(s) operacional(is):** | *Windows* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Devido ao PPE - Programa de Proteção ao Emprego, que permite às empresas reduzirem a jornada e salário dos funcionários, foi realizada esta implementação que visa possibilitar a redução do valor do salário para alterações que consultem as Tabelas Salariais do TOTVS Gestão de Pessoas e também a alteração de jornada por fórmula, que antes era dispobilizada apenas para alterações de salário por percentual ou fórmula.

## Procedimento para Utilização

* 1. *Configurar integração com o TOTVS Gestão de Pessoas (RM Vitae)*
  2. *Cadastrar no RM Vitae um Nível Salarial, Faixa Salarial e Tabela Salarial*
  3. *Vincular um funcionário a uma tabela salarial em seu registro.*
  4. *Alterar o salário do funcionário para que o mesmo fique com um salário maior do que o previsto na tabela salarial.*
  5. *Executar a rotina de Alteração Global de Salários utilizando Tabelas Salarias e selecionando o funcionário utilizado no item 3.*
