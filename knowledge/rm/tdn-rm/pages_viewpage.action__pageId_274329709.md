---
content_hash: afbb9e7e8382519b8a7455b9b95a7db891ced70173b001886d93e6c363b378be
fetched_at: '2026-06-29T00:08:33.853683+00:00'
page_id: '274329709'
product: rm
source: tdn-rm
title: DT Imprimir Relatório de Alta ao Finalizar Atendimento Médico na Classificação
  de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274329709
version: 112
---

# Imprimir Relatório de Alta ao Finalizar Atendimento Médico na Classificação de Risco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Risco | |
| **Parâmetro(s):** | Relatório de Alta do Paciente na Classificação de Risco |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada funcionalidade ao realizar a finalização do atendimento na classificação de risco, automaticamente imprimir o relatório de alta parametrizado no "Relatório de Alta do Paciente na Classificação de Risco" nos Parâmetros Gerais aba de Relatórios via Gerador

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM Saúde**, acesse **Opções/Parâmetros/Parâmetros Gerais/**. Na aba Relatórios via Geradorconfigure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Relatório de Alta do Paciente na Classificação de Risco |
| **Tipo:** | Número Inteiro |
| **Cont. Por.:** | -1 |
| **Descrição:** | Relatório de Alta do Paciente na Classificação de Risco, informar os parâmetros CODCOLIGADA, CODPACIENTE, CODATENDIMENTO |

## Procedimento para Utilização

**Exemplo:**

       1.            Acesse o TOTVS Gestão Hospitalar (RM Saúde), com perfil médico.

       2.            No Painel de Classificação de Risco na aba de atendimento médico finalize um atendimento.

       3.            Com o parâmetro Relatório de Alta do Paciente na Classificação de Risco marcado, ao finalizar o atendimento, será impresso o relatório parametrizado.

divs
