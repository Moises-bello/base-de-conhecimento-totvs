---
content_hash: 7d1412c6fd9714d8459a06bf059bebe9e808ccbeeff27f79d60568d4ebf7a355
fetched_at: '2026-06-29T00:08:39.836451+00:00'
page_id: '286022419'
product: rm
source: tdn-rm
title: DT Prontuário Eletrônico do Paciente x TOTVS Gestão Hospitalar - Aleta de Receitas,
  Atestados e Orientações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286022419
version: 103
---

# Prontuário Eletrônico do Paciente x TOTVS Gestão Hospitalar - Aleta de Receitas, Atestados e Orientações

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Integração Prontuário Eletrônico do Paciente x TOTVS Gestão Hospitalar | Institution | |
| **Cadastros Iniciais:** | Unidade de Atendimento, Unidade de Faturamento, Prestador Principal |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [SAUHRM02-1261](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1261 "PEP x RM 12.1.16 - Aleta de Receitas, Atestados e Orientações") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZUNIDATEND e SZCADGERAL |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada parte da integração entre TOTVS Gestão Hospitalar e  Prontuário Eletrônico do Paciente responsável por carregar os dados da instituição do RM Saúde (prestador principal da unidade de faturamento) para serem mostrados em relatórios do Prontuário Eletrônico do Paciente da aleta Receitas, Atestados e Orientações .

## Procedimento para Utilização

**Exemplo:**

       1.            Acesse Cadastros/Uso Geral/Unidades de Atendimento.

       2.            Edite as informações de algum registro. Ao verificar as informações, uma unidade de faturamento deverá ser definida para a unidade de atendimento, a menos que ela própria seja a unidade de faturamento.

       3.            Acesse o cadastro da unidade de faturamento selecionada acima clicando no nome dela (em azul) ou retornando ao cadastro e buscando pela mesma.

       4.            Ao acessar o cadastro, um prestador principal deverá ser definido para esta unidade de faturamento.

       5.            Os dados do prestador cadastrado acima serão carregados pela integração com o PEP 2 e mostrados nos relatórios de Receitas, Atestados e Orientações. Estes dados são referentes a CNPJ/CPF, endereço e contato da instituição (prestador principal).

divs
