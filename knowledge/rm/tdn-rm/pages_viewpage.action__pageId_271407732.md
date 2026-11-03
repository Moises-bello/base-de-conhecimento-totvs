---
content_hash: 9a2639fb8353c5e16751747eec43f547c11e49ab5cb5aaf03c9db23810ce6693
fetched_at: '2026-06-29T00:08:27.347132+00:00'
page_id: '271407732'
product: rm
source: tdn-rm
title: DT_Exibir_Informacoes_Adicionais_reserva_recurso_instalação_agenda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271407732
version: 2
---

# Informações adicionais da reserva de recurso e instalação no compromisso da agenda

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Reserva de recurso e instalação | Reserva de recurso e instalação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Reserva de recurso e instalação | Reserva de recurso e instalação | | Agenda | Agenda | | | |
| **Requisito (ISSUE):** | EDUEDU001-708 | | |
| **País:** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Visualizar as informações adicionais da reserva de  recurso e instalação no compromisso da agenda.

## 

## Definição da Regra de Negócio

# Parametrização

 

Acessar:****Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Reserva de recurso e instalação****

Editar uma atividade agendada e habilitar os parâmetros "Permite  exportação para agenda global" e "Permite seleção de usuários". Com estes parâmetros habilitados a reserva de recurso e instalação é exibida na agenda  dos usuários que foram definidos na atividade agendada ou durante a execução do processo.

# Realizar reserva de recurso e instalação

No sistema, acessar: **Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Reserva de recurso e instalação**

Realizar reserva de Recurso

* Selecionar a atividade agendada que permite reserva de recurso
* Ir em Processo "Processo de reserva de recurso":
* Informe o solicitante da reserva
* Defina os horários
* Selecione o tipo de recurso e recurso
* **Informações adicionais**: Informe o responsável pela reserva, descrição e a observação
* Conclua a execução do processo

Realizar reserva de Instalação

 

* Selecionar a atividade agendada que permite reserva de instalação
* Ir em Processo "Processo de reserva de instalação":
* Informe o solicitante da reserva
* Defina os horários
* Selecione o tipo de sala e sala
* **Informações adicionais**: Informe o responsável pela reserva, descrição e a observação
* Conclua a execução do processo

# Visualizar as reservas de recurso e instalação na agenda

.Acessar:****Módulo Educacional | Gestão | Utilitários | Agenda****, visualizar na agenda as informações adicionais da reserva.

**Importante:**

* Caso não exista informações adicionais preenchidas, será exibido somente a informação sobre a atividade agendada.
* Lembrando que para visualizar corretamente a informação na agenda, deve-se habilitar para visualizar intervalos de 15 minutos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Reserva de recurso | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Processo reserva de recurso | - |
| Reserva de instalação | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação -> Processo reserva de instalação | - |
| Agenda | [Envolvida] | Módulo Educacional | Gestão | Utilitários | Agenda | - |
