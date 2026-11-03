---
content_hash: 534b1ebed98ec3af3db186924a056ae06b3b33311a28cd68a35c1bdddd8b111e
fetched_at: '2026-06-29T00:08:23.345481+00:00'
page_id: '270080690'
product: rm
source: tdn-rm
title: ER_SAUHRM02-329_Bloqueio_de_agendamento_por_convenio
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-329_Bloqueio_de_agendamento_por_convenio
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Agendamento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM1** | SAUHRM02-346 |
| **Requisito1** | SAUHRM02-329 | **Subtarefa1** | SAUHRM02-383 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

O objeto desta implementação consiste em disponibilizar um cadastro para configurar os percentuais de horários disponíveis para cada convênio e dia da semana.

O sistema deve alertar quando o percentual configurado for atingido.

### (Obrigatório)

## Definição da Regra de Negócio

**RN01:** Criar uma nova página nas Propriedades da Agenda, denominada  "Percentual de agendamentos por convênio".

Neste cadastro devem existir os seguintes campos:

* percentual de horários permitidos. Validar se a soma dos percentuais por dia não ultrapassa 100%
* dia da semana. Disponibilizar através de checkbox todos os dias da semana
* convênio, sendo este obrigatório.

**RN02:** Criar uma rotina para validação do percentual permitido*.* Esta rotina deve realizar o seguinte cálculo:

* Dados de entrada:
  + Convênio
  + Dia da semana
  + Proprietário da Agenda
* Cálculo
  + Deve calcular a quantidade total de horários do dia
  + Calcular a quantidade de horários agendados para o convênio
  + Calcular a quantidade de horários livres
  + Verificar o percentual parametrizado para o dia e convênio
* Saída:
  + Permitir o registro caso não tenha atingido a quantidade configurada
  + Caso o percentual ultrapasse a quantidade configurada, o sistema deve informar que o limite foi ultrapassado e exibir a quantidade já agendada e a quantidade de horários livres. Deve solicitar a confirmação ao usuário para a gravação do agendamento

**RN03:** Chamar a rotina de validação na gravação do agendamento, na funcionalidade de cópia de agendamentos, na funcionalidade de agendamento seriado e agendamento de exames

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Propriedades da Agenda | [Alteração] | Atendimento -> Agendamento -> Agenda de Atendimentos | RN01 |
| Agendamento | [Alteração] | Atendimento -> Agendamento -> Agenda de Atendimentos | RN02 |
| Agendamento de Exames,  Agendamento seriado,  Cópia de agendamentos | [Alteração] | Atendimento -> Agendamento -> Agenda de Atendimentos | RN03 |

**Tabelas Utilizadas**

* SZAGENDAMENTO – Agendamentos
* SZAGENDACONV – Cadastro de percentuais por convênio

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
