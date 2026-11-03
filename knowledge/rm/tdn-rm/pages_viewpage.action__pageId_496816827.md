---
content_hash: bdb4ab9a9c76faca96fed6fb68fbd450a29205471987dc8b9c760fe41901dcef
fetched_at: '2026-06-29T00:10:22.511546+00:00'
page_id: '496816827'
product: rm
source: tdn-rm
title: DT Parâmetro não permitir acordo de lançamentos gerados por acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496816827
version: 1
---

# PARÂMETRO NÃO PERMITIR ACORDO DE LANÇAMENTOS GERADOS POR ACORDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Acordo | Parâmetro não permitir acordo de lançamentos gerados por acordo | |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue(informe o requisito relacionado):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-4445 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.25 |

## Descrição

Parâmetro para ser informado no template do acordo para definir se é permitido gerar acordo para lançamentos provenientes de acordo.

Ao realizar o processo para um lançamento proveniente de outro acordo e o parâmetro estiver desmarcado será feita uma consistência que irá impedir a continuidade desse acordo.

## Procedimento para Utilização

Acesse o menu *Contas a Pagar / Receber | Acordo | Template de Acordo | Regras:*

Durante a geração de acordo com o parâmetro desmarcado em lançamentos originados via acordo exibe mensagem de erro e impede a execução.
