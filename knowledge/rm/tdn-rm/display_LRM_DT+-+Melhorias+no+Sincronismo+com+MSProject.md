---
content_hash: 64022afcd405cd434e4089e48305fc0ab6f26410282d19456a3ed43fb59cc4d5
fetched_at: '2026-06-29T00:09:09.734550+00:00'
page_id: '393365896'
product: rm
source: tdn-rm
title: DT - Melhorias no Sincronismo com MSProject
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Melhorias+no+Sincronismo+com+MSProject
version: 5
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Sincronismo com MS Project | Sincronismo com MS Project |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Pert | Pert | |  |  | |
| **Cadastros Iniciais:** | Projeto, Períodos de Cronograma, Tarefas. |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPORCAPLAN001-4446 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Foram feitas algumas alterações no Sincronismo com o MS Project, sendo elas:

* O tipo das atividades sempre será Unidades Fixas;
* As atividades que tem predecessão serão marcadas como agendamento automático.
* As atividades que não tem predecessão serão marcadas como agendamento manual.
* O percentual concluído também será enviado para o campo % físico concluído do MS Project.
* As datas programadas do Pert serão enviadas para a Linha de Base1 do MS Project.
* A Data Fim realizado de uma etapa e obra será preenchida no Project apenas quando todas as suas atividades filhas forem concluídas. Desta forma esta data poderá ser diferente do PERT.

Na tela do Sincronismo foram feitas as alterações:

* Retirada a opção do Plano Fixado (campos em desuso no TOP).
* Quando for a criação de um novo arquivo, será obrigatório o Plano Programado.
* Criada a opção de sincronismo apenas da duração do Plano Programado.
* Colocado um ícone para oferecer maiores explicações sobre o campo: Prioritário no Sincronismo com MS-Project.
