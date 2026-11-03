---
content_hash: cf4170611fa7d799130e117e6753861e53d8973e027e24b4f974ee4a6e4b3574
fetched_at: '2026-06-29T00:10:15.061555+00:00'
page_id: '463802887'
product: rm
source: tdn-rm
title: DT Histórico de Equipes de Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463802887
version: 2
---

# HISTÓRICO DE EQUIPES DE PROJETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Obras e Projetos** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Histórico de Equipe | Histórico de Equipe |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Equipe de Mobilidade | Equipe de Mobilidade | | Equipe de Timesheet | Equipe de Timesheet | | Equipe de Gestão de Risco | Equipe de Gestão de Risco | |
| **Cadastros Iniciais:** | Projeto, Insumo, Função, Equipes e Membros de Equipes |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-6677](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6677) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | *Não se aplica.* |

TOPORCAPLAN001-6677

## Descrição

Histórico de Alterações nas Equipes de Mobilidade, Timesheet e Gestão de Risco.

## Procedimento para Utilização

No cadastro de Equipes de Mobilidade, Timesheet e Gestão de Risco, existe o anexo **"Histórico de Equipe"**, que apresenta as ocorrências relacionadas à equipe e aos seus respectivos membros.

Os Tipos de Histórico que esse anexo apresenta são os seguintes:

* CRIAR EQUIPE: Ao salvar a inclusão de uma nova equipe;
* ATIVAR EQUIPE: Ao ativar uma determinada equipe;
* DESATIVAR EQUIPE: Ao desativar uma determinada equipe;
* ATIVAR MEMBRO: Ao ativar um determinado membro;
* DESATIVAR MEMBRO: Ao desativar um determinado membro;
* INCLUIR MEMBRO: Ao salvar a inclusão de um novo membro;
* EXCLUIR MEMBRO: Ao excluir um membro de uma determinada equipe.

No anexo de cada tipo de equipe é possível visualizar as alterações realizadas:

Outros processo que envolvem essa funcionalidade são:

* Backup e Restore de projetos;
* Revisões de projeto;
* Cópia de Itens, que ao copiar a equipe (somente de timesheet), incluir um novo histórico de CRIAR EQUIPE, com a Observação "Inclusão via Cópia de Itens".
