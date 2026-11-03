---
content_hash: b57402f7dc94cc6ba2f95dfcd6ca8329f622758f0cb024b60a9d5ef06a507723
fetched_at: '2026-06-29T00:08:49.437327+00:00'
page_id: '330831020'
product: rm
source: tdn-rm
title: 1372071 RMSAU-204 DT Personalização do GRID - Agenda de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330831020
version: 6
---

# Personalização do GRID - Agenda de Atendimentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Saúde* |
| **Módulo:** | *Gestão Hospitalar* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Atendimento / Agendamento / Agenda de Atendimento* | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastros / Campos Complementares / Agenda de Atendimentos.* | *Campos Complementares* | | *Cadastros / Segurança / perfis* | *Perfis* | |
| **Cadastros Iniciais:** | *Campos Complementares* |
| **Tickets relacionados** | *1372071* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-204 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **SQL SERVER® e ORACLE®** |
| **Sistema(s) Operacional(is):** | **Windows®** |

## Descrição

Grid da agenda de atendimentos personalizada para o cliente Master Medical Group com o objetivo de melhorar a usabilidade, com os campos Hora, Atividade, Chegada,Status, Prontuario, CodPaciente,Paciente, Tel. Resid, Celular, Obs, Motivo, Prestador e Valor Consulta (Campo complementar).

## Procedimento para Utilização

* Acessar o RM Saúde – **Cadastros / Campos Complementares / Agenda de Atendimentos.**

* Cadastrar o campo **VALORCONSULTA** com a descrição Valor Consulta e Tio **Real**.

* Acessar o RM Saúde, **Atendimento / Agendamento / Agenda de Atendimento.**

* O grid personalizada para o cliente **MASTER MEDICAL GROUP** será apresentada.

* Para retirar os campos **Tel. Residencial e Celular** por perfil acessar: **Cadastros / Segurança / perfis**.

* Selecione o perfil que deseja restringir. Na aba Acesso a Campos Selecione a tabela **SZAGENDAMENTO** e retire as permissões para os campos **TELEFONERES** e **TELEFONECEL**.

* Selecione a coligada novamente e após acesse novamente a agenda de atendimentos, note que os campos **Tel. Residencial e Celular** não estão mais no Grid.
