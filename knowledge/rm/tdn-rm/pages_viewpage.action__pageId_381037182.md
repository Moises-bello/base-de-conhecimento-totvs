---
content_hash: 64cbfc6dfc24768a7bc007370190850e4b552492699c9010c7f1bf783e612da0
fetched_at: '2026-06-29T00:09:03.005739+00:00'
page_id: '381037182'
product: rm
source: tdn-rm
title: 472743 MATESTCNTFTOF01-934 DT Usuário Padrão de Cancelamento do Workflow Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381037182
version: 3
---

# Workflow Fluig - Usuário Padrão para Cancelamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | DEFINIÇÕES GERAIS. | PARÂMETROS GERAIS DO MOVIMENTO. | |
| **Cadastros Iniciais:** | Não se aplica. |
| **Parâmetro(s):** | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Definições Gerais | Etapa Definições Gerais 3/3. |
| **Ponto de Entrada:** | Não se aplica. |
| **Tickets relacionados** | 472743. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-934. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL e Oracle. |
| **Tabelas Utilizadas:** | Não se aplica. |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

Melhoria ao cancelar Workflow no Fluig. Com a criação desta funcionalidade, será possível informar um usuário específico para ser utilizado no cancelamento de Workflows no Fluig. Só é permitido cancelar um Workflow quando é utilizado o mesmo usuário que criou o processo ou um usuário gestor. Devido a isso, aconselha-se colocar um usuário gestor padrão no parametrizador.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.22deste chamado.

## Procedimento para Utilização

* Entrar nos parâmetros do Gestão de Estoque, Compras e Faturamento em: Parâmetros Gerais | Definições Gerais 3/3.
