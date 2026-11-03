---
content_hash: b09ab909390350527b61eb366916c00804bbbcb03f204bfe7d0fab269dbb1624
fetched_at: '2026-06-29T00:08:46.985868+00:00'
page_id: '317318148'
product: rm
source: tdn-rm
title: 1201607 RMSAU-1393 DT Vincular somente um Atendimento por Agendamento
type: documentation
url: https://tdn.totvs.com/display/LRM/1201607+RMSAU-1393+DT+Vincular+somente+um+Atendimento+por+Agendamento
version: 4
---

# Vincular somente um Atendimento por Agendamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Atendimento | | Agenda de Atendimentos | |
| **Cadastros Iniciais:** | Agenda para o dia em qualquer médico |
| **Parâmetro(s):** | Vincula somente um Atendimento por Agendamento |
| **Ponto de Entrada:** | Agenda de Atendimentos |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Ao realizar mais de um agendamento para o mesmo paciente no mesmo dia para o mesmo médico o sistema apresenta a mensagem abaixo:

Foi alterado o sistema para que quando o parâmetro "Vincula somente um Atendimento por Agendamento" esteja marcado não apresente essa mensagem e sempre registre um novo atendimento para o paciente, independente se ele já teve registro no mesmo dia.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Vincula somente um Atendimento por Agendamento |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado (F) |
| **Descrição:** | Vincula somente um Atendimento por Agendamento |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Sáude), acesse Atendimento / Agendamento / Agenda de Atendimentos.

O sistema apresenta a janela de agendamentos, selecione um médico com agendamento para a data de hoje.

       2.            Após registrar o agendamento, clique no botão Atend. Externo

       3.            Registrar o atendimento do paciente e criar um novo registro no agendamento, para o mesmo paciente e médico e repita o procedimento de clicar no Atend. Externo.

       4.            Com o parâmetro marcado o sistema não vai apresentar a mensagem abaixo e vai partir direto para o registro de atendimento, não permitindo vincular mais de um agendamento a um atendimento.
