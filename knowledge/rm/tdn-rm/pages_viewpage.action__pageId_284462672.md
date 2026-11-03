---
content_hash: fc4c186fe81d041f223b3a1dadd3b0872a5d67f8274d10f32aaf226ec43543e1
fetched_at: '2026-06-29T00:08:36.145957+00:00'
page_id: '284462672'
product: rm
source: tdn-rm
title: DT Melhoria na utilização do Painel de eletivos do Posto de Enfermagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284462672
version: 107
---

# Melhoria na utilização do Painel de eletivos do Posto de Enfermagem

Características do Requisito

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Saúde |
| Módulo: | TOTVS Gestão Hospitalar |
| Rotina: | |  | | --- | | Rotina | | Painel de Eletivos |  |  | | --- | | Rotina(s) envolvida(s) | | Agenda de Atendimento | | Registro de Atendimento | | Toten do Painel de Eletivos | |
| Cadastros Iniciais: | Agendar um Atendimento, Solicitar uma senha no Toten, Associar senha ao Agendamento, Associar Agendamento ao Registro de Atendimento |
| Tickets relacionados | Ticket #820955 |
| Requisito/Story/Issue (informe o requisito relacionado): | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1117 |
| País(es): | Brasil |
| Banco(s) de Dados: | SQL Server ® e Oracle ® |
| Sistema(s) Operacional(is): | Windows ® |

## Descrição

A partir dessa implementação, ao utilizar o Posto de Enfermagem do Painel de Eletivos,  é possível iniciar o atendimento, sem que seja necessário abrir o Prontuário do Paciente.

## Procedimento para Utilização

**AGENDAR EXAME**

* Acesse Atendimento / Agendamento / Agenda de Atendimentos
* Agende um atendimento, com pelo menos uma solicitação de exames,  que posteriormente será vinculado a senha do painel de eletivos

**SOLICITAR SENHA**

* Acesse Atendimento / Pronto Atendimento / Toten do Pronto Atendimento
* Solicite um senha para unidade de atendimento com a mesma especialidade do atendimento registrado.

**REALIZAR TRIAGEM**

* Acesse Atendimento / Pronto Atendimento / Painel de Atendimentos Eletivos
* Na aba Registro de Atendimento / Chame a senha na aba Registro de Atendimento (duplo clique na senha)
* Associe o agendamento a um Registro de Atendimento
* Na aba Registro de Triagem / Realize a triagem (duplo clique no registro)

**INICIAR ATENDIMENTO**

* Na aba Posto de Enfermagem / Duplo clique no registro de Posto de Enfermagem
* Os botões serão apresentados
  + Confirmar: Apenas inicia o atendimento.
  + Confirmar e Abrir Prontuário: Inicia o atendimento e posteriormente abre automaticamente o prontuário eletrônico parametrizado.
  + Somente abrir prontuário: Abre o prontuário eletrônico sem iniciar o atendimento.
  + Cancelar: Cancela o processo de iniciar o atendimento do paciente.

divs
