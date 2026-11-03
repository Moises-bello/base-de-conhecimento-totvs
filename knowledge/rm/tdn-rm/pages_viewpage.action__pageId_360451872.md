---
content_hash: f0c9755288b87ff4a92b941c8f35edf0d197371cd2e47f78437b4cb097dbf690
fetched_at: '2026-06-29T00:08:58.627272+00:00'
page_id: '360451872'
product: rm
source: tdn-rm
title: 1723166 RMSAU-3007 DT Inserir quantidade no item de débito (Serviços e Taxas)
  da atividade da agenda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360451872
version: 2
---

# Inserir item quantidade de débito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastros/ Uso Geral/ Agendamento/ Atividades | Atividades da Agenda |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Atendimento/Agendamento/Agenda de Atendimentos | Agenda de Atendimentos | |
| **Tickets relacionados** | [Ticket #1723166](https://totvssuporte.zendesk.com/agent/tickets/1723166 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [RMSAU-3007](http://jiraproducao.totvs.com.br/browse/RMSAU-3007) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZTAXAATIVIDADES |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Adicionado o campo Quantidade na tela de Atividades da Agenda para cobrar automaticamente de acordo com a quantidade configurada, quando estiver registrando o atendimento, na rotina de agenda de atendimento.

1. Passo um para acessar as Atividades da Agenda - Acessar o RM Saúde, menu Cadastros/ Uso Geral/ Agendamento/ Atividades
2. Selecionar uma Atividade, selecionar um serviço na aba Serviços e taxas
3. Passo dois para acessar a Agenda - Acessar o RM Saúde, menu Atendimento/Agendamento/Agenda de Atendimentos
4. Na Agenda de Atendimento selecione um horário para marcar o atendimento e configure o Agendamento de acordo com a atividade configurada
5. Após Configurar a agenda selecione o atendimento e clique em atendimento externo
6. Em atendimento externo clique na aba Guia/Autorização e verifique que a quantidade ficou configurada
