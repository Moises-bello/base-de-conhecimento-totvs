---
content_hash: 2c64a265fd702b3893e074afd571fee2f53880f51a801958f524be8f4811d89d
fetched_at: '2026-06-29T00:09:10.472978+00:00'
page_id: '397387931'
product: rm
source: tdn-rm
title: DT Mensagem de Associação de Membro a Equipe de Mobilidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397387931
version: 1
---

# MENSAGEM DE ASSOCIAÇÃO DE MEMBRO A EQUIPE DE MOBILIDADE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Membros de equipes de mobilidade | Membros de equipes de mobilidade | |
| **Cadastros Iniciais:** | Insumos, Pessoas, Funcionários, Funções |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-298](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-298) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Mensagem de validação de existência de membro ativo no momento de cadastrar um novo membro.

## Procedimento para Utilização

No anexo de membros de equipe de mobilidade, ao cadastrar um novo membro, uma série de validações são realizadas, dentre elas a consistência da existência do membro selecionado, o funcionário ou terceiro, estar ativo em uma outra equipe de qualquer projeto existente. Ao salvar o registro, uma mensagem é emitida, na qual informa a equipe e o projeto correspondentes ao funcionário/terceiro selecionado.
