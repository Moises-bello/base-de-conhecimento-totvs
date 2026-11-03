---
content_hash: bf9aa17ad26cd4e9349e4d6210c6372e094b7959b5cfa45cd732c236652842c1
fetched_at: '2026-06-29T00:10:15.796660+00:00'
page_id: '465179453'
product: rm
source: tdn-rm
title: DT Utilização dos relatórios referentes ao gerador antigo e ao novo no Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465179453
version: 6
---

# TRATAMENTO DOS RELATÓRIOS ANTIGOS NO EDUCACIONAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Geração de relatórios |
| **Rotina:** | TOTVS Educacional   |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Alunos | Cadastro de alunos | | Ocorrências | Cadastro de ocorrências | | Boletos | Boletos de alunos | | Contratos | Contratos de alunos | | Histórico | Histórico do aluno | | Disciplinas do histórico | Disciplinas do histórico do aluno | | Aproveitamento de estudo | Aproveitamento de estudo | | Disciplinas de origem | Disciplinas de origem do aproveitamento de estudo | | Cursos/Habilitações | Cursos/Habilitações do aluno | | Matrícula no período letivo | Matrícula no período letivo | | Parâmetros do portal | Parâmetros do portal | | Professores | Cadastro de professores | | Turma | Cadastro de turma | | Turma/Disciplina | Cadastro de turma/disciplina | | Horários da turma | Cadastro de horários da turma | | Professores da turma | Cadastro de professores da turma | | Subturma | Cadastro de subturma | | Horários da subturma | Cadastro de horários da subturma | | Parâmetros da secretaria | Parâmetros da secretaria |     TOTVS Processo Seletivo   |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro do processo seletivo | Definições de comprovante de inscrição e boleto para pagamento |     TOTVS Gestão Bibliotecária   |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetros do sistema / Emissão de recibos | Recibos de movimentações | | Parâmetros do sistema / Integração financeira | Boleto para pagamento no portal | |
| **Parâmetro(s):** | Tipo de relatório |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | EDUCACIONAL01-8429 / EDUCACIONAL01-8428 |
| **País(es):** | Todos os países |
| **Banco(s) de Dados:** | SQL Server/Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Inclusão de tratamento no sistema para que os recursos que utilizem relatórios criados pelo gerador antigo, do Delphi, serão descontinuados e não serão disponibilizados para novos contratos de clientes.

Os parâmetros do sistema, atualmente, permitem a parametrização para a utilização do novo e do antigo gerador de relatório. Essa parametrização era realizada nos parâmetros da secretaria e do portal.

Para novos contatos, essa parametrização não será mais disponibilizada. Dessa forma, o sistema trabalhará apenas com relatórios criados pelo novo gerador.
