---
content_hash: 7c4954a21ae719dc80eba2836c7bd165ff70c10ca0d962e1f64f30acdc6cba02
fetched_at: '2026-06-29T00:08:45.767790+00:00'
page_id: '315890037'
product: rm
source: tdn-rm
title: RMSAU-1580 DT Campo Sequêncial na aba Mat/Med da Elaboração de Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315890037
version: 95
---

# Campo Sequêncial na aba Mat/Med da Elaboração de Contas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Elaboração de Contas | |
| **Parâmetro(s):** | Exibe campo Sequencial da grid de MatMed da Elaboração de Contas |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZATENDMATMED |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Foi adicionado a grid de MatMed da Elaboração de Contas o campo Sequêncial (Seq.) para mostrar a ordem do mat med e permitir uma melhor ordenação dos itens na tela, foi adicionado também um campo na tela chamado Seq. o usuário assim pode informar para qual Sequêncial deseja que o item seja movido e clicar em Gravar para ordenar corretamente.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais/ Aba Faturamento ||**. Configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Exibe campo Sequencial da grid de MatMed da Elaboração de Contas |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado |
| **Descrição:** | Exibe campo Sequencial da grid de MatMed da Elaboração de Contas |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse a Elaboração de Contas de qualquer paciente.

Com o parâmetro "Exibe campo Sequencial da grid de MatMed da Elaboração de Contas" marcado o campo Sequêncial será exibido na grid de MatMed

       2.            O usuário pode também alterar o campo Seq. na tela de MatMed para ordenar o item para a posição que deseja ordenar.

divs
