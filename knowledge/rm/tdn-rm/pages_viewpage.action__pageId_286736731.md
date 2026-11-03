---
content_hash: 517e7e3793f3487327df2bf3a8847603bfbd35729bf3ad7827a16203b709e233
fetched_at: '2026-06-29T00:08:41.610975+00:00'
page_id: '286736731'
product: rm
source: tdn-rm
title: DT Preenchimento Automático de Informações ANS TISS do Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286736731
version: 107
---

# Preenchimento Automático de Informações ANS TISS do Atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento Externo | |
| **Cadastros Iniciais:** | Cadastros/Uso Geral/Valores Padrão para Atendimento |
| **Ponto de Entrada:** | Registro de Atendimento Externo |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Ao realizar o Registro de Atendimento Externo com as informações cadastradas na tela de Valores Padrão para Atendimento, o irá carregar os dados automaticamente e não exibirá a tela de informações TISS, ao registrar o atendimento por conta das informações já estarem registradas.

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Sáude), acesse o Registro de Atendimento Externo.

Preencha um atendimento conforme os valores definidos na rela de Valores Padrão para Atendimento

       2.            A tela de informações tiss não será exibida ao registrar o atendimento se os dados de Tipo de Consulta e Tipo de Atendimento ANS ja foram definidos na tela de Valores Padrão de Atendimento

divs
