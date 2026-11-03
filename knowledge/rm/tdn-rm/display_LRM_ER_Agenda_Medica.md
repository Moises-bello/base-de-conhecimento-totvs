---
content_hash: 89c1dc1ff8390418ffbe1cfd320fe90b7352e11013e4b281d0f1f194199b6595
fetched_at: '2026-06-29T00:08:11.993657+00:00'
page_id: '243633369'
product: rm
source: tdn-rm
title: ER_Agenda_Medica
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Agenda_Medica
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Segurança e Saúde Ocupacional | **Módulo** | PCMSO |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## 1.     Objetivo

## 2.      Definição da Regra de Negócio

# 1.   Profissional de Saúde

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** CRUD.

**Acesso:** Cadastro > Profissional de Saúde.

**Descrição:**Será acrescentado um campo, denominado **Visualiza somente sua própria agenda**, Checkbox, no cadastro de Profissional de Saúde.

Essa informação irá ser utilizada para determinar se o usuário correspondente ao profissional de saúde cadastrado pode visualizar, além de sua própria, a agenda de outros profissionais de saúde. A **Agenda Médica** está descrita no item 2.21 desta especificação.

Também será acrescentado um campo, somente leitura, indicando qual é o usuário, caso exista, do profissional de saúde para acesso ao sistema.

# 2.   Agenda Médica

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Visão.

**Acesso:** PCMSO > Agenda Médica.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Agenda Médica.

**Descrição:**Será implementado uma visão que irá exibir registros de **Consultas Agendadas**.

Se o usuário logado corresponder a um profissional de saúde que esteja parametrizado para visualizar somente consultas nas quais ele será o médico responsável, somente os registros em que ele é o médico responsável serão exibidas. Caso contrário, todas as consultas agendadas serão exibidas nesta tela.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data da Consulta | Data | Não se aplica | Somente leitura. |
| Hora da Consulta | Hora | Não se aplica | Somente leitura. |
| Tipo da Consulta | Texto | Não se aplica | Somente leitura. |
| Médico Responsável | Texto | Não se aplica | Somente leitura. |
| Nome do Paciente | Texto | Não se aplica | Somente leitura. |
| Exames | Texto | Não se aplica | Somente leitura. |

# 3.   Assistente de Agendamento Automático

Na etapa "Seleção de "Médicos", se o usuário decidir por agendar consultas para análise clínica dos exames selecionados, será exibida uma outra etapa denominada **Consultas Agendadas**, onde o aplicativo por meio de um processamento, com base nas informações abaixo, irá exibir uma lista sugestiva de atendimentos:

•  Disponibilidade de atendimento dos médicos selecionados na etapa **Seleção de Médicos** (vide item 2.14 desta especificação).

•  Data prevista para entrega dos exames selecionados (vide item 2.18 desta especificação).

Ainda antes de executar o processo, poderá o usuário ajustar as informações sugeridas, modificando o médico responsável, bem como a data e horário dos atendimentos.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
