---
content_hash: 55e2e13886f86300424f4c55cb4460c9c29ad7147168c179ec18e4673c32ffc3
fetched_at: '2026-06-29T00:06:15.004796+00:00'
page_id: '210051130'
product: rm
source: tdn-rm
title: DT_Copiar_Parametros_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Copiar_Parametros_Funcionario
version: 4
---

# COPIAR PARÂMETROS DO FUNCIONÁRIO

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Configurações* | *Funcionário* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

O processo **“Copiar Parâmetros do Funcionário”** tem como objetivo copiar os parâmetros de um funcionário origem para o funcionário destino que não foi configurado, e para os funcionários que já foram configurados o processo substitui os parâmetros.

## Procedimento para Utilização

Para acessar o processo **“Copiar Parâmetros do Funcionário”** acesse **Automação de Ponto / Configurações / Parametrizador**

O sistema irá exibir a tela **“Assistente de Implantação de Processos”** e nela selecione o processo **“Funcionário”** e avance

Logo após, selecione o funcionário que deseja copiar a parametrização e acesse **Processos / Copiar Parâmetros do Funcionário**

A tela do processo contém o campo **“Funcionário Origem”** que estará preenchido com o funcionário selecionado anteriormente, e o campo **“Funcionário Destino”** onde deve ser informado o funcionário que irá receber os parâmetros.  
Clique no lookup  do campo **“Funcionário Destino”** e selecione o funcionário que irá receber os parâmetros do funcionário origem

Clique em executar, e será exibida a tela perguntando se deseja que os parâmetros sejam sobrescritos. Responda e execute o processo

Para certificar-se de que todos os parâmetros realmente foram copiados para o funcionário destino, selecione o funcionário de destino e clique no ícone “Parametrizar”  da tela de **“Seleção de Funcionários”.**

O sistema irá exibir uma tela com as etapas da parametrização, e em cada uma delas será possível verificar se foi copiado os parâmetros para o funcionário destino
