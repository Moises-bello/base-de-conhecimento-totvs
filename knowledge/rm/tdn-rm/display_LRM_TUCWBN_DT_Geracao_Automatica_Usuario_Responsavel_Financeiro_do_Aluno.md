---
content_hash: 348b014f4ba447998a578b7c0afa3962fb669e09b654232bf7ac2a1b00b0e88a
fetched_at: '2026-06-29T00:08:03.795749+00:00'
page_id: '235325348'
product: rm
source: tdn-rm
title: TUCWBN_DT_Geracao_Automatica_Usuario_Responsavel_Financeiro_do_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TUCWBN_DT_Geracao_Automatica_Usuario_Responsavel_Financeiro_do_Aluno
version: 121
---

# Geração automática de usuário para Responsável Financeiro do Aluno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração automática de usuário* | *Geração automática de usuário* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Geração de usuário*.* | *Geração de usuários para Responsável Financeiro do aluno* | |  |  | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | Parâmetros > Geração de Usuários > Aluno > Gerar usuários para responsável financeiro |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foi realizado a inclusão do parâmetro para geração de usuários automáticos de responsável financeiro do aluno, nos parâmetros do sistema.

Desta forma, também será possível criar um usuário para um responsável financeiro no momento em que o aluno é criado no sistema, juntamente com os usuários que já eram criados anteriores durante o cadastro de um novo aluno (usuário do próprio aluno, usuário para pai e mãe, e também usuário para responsável acadêmico).

## Procedimento para Utilização

       1.            Deve ser marcado o parâmetro para geração de usuários para alunos no seguinte caminho: Educacional > Parâmetros > Geração de Usuários > Aluno > Gerar usuário automaticamente ao criar aluno

       2.            Será habilitado uma nova opção em seguida: Gerar usuário para responsável financeiro

       3.            Seguir até etapa "Geração Usuários Alunos 5/5", para definir as parametrizações dos usuários que serão gerados para o responsável financeiro.

       4.            Ao cadastrar um novo aluno, será verificado a existência de um responsável financeiro atribuído ao aluno, e neste caso, será gerado o usuário seguindo as regras parametrizadas acima.

divs
