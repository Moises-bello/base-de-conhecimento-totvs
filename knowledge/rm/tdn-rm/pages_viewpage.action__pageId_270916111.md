---
content_hash: 7b95f7f5b9a1c2175967bf07377d7f60d045992d7e75264c62b25e73ee0983a3
fetched_at: '2026-06-29T00:08:25.497568+00:00'
page_id: '270916111'
product: rm
source: tdn-rm
title: DT Alteração do Campo Atividade da Agenda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270916111
version: 118
---

# Alteração do Campo Atividade da Agenda quando Estiver em Período de Retorno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Atendimento / Agendamento / Agenda de Atendimentos  Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros / Parâmetros Gerais / Registro e Controle II | | Cadastros / Faturamento / Condições Contratuais com Convênios / Dias de Retorno | |
| **Parâmetro(s):** | Utiliza Atividade Retorno Automático.  Atividade da Agenda.  Atividade do Registro de Atendimento. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® / Oracle® |
| **Tabelas Utilizadas:** | SZAGENDAMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

 Implementação do status automático de Retorno no processo de Atendimento Ambulatorial. O status automático se dá com base na parametrização da Atividades da Agenda e do período parametrizado nas Condições Contratuais dos Convênios.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu "**Opções / Parâmetros / Parâmetros Gerais**".
2. Acesse a aba "Registro e Controle II" e marque o Parâmetro “Utiliza Status de Retorno Automático”.
3. Selecione as atividades que serão utilizadas na atualização automática na Agenda de Atendimentos e no Registro de Atendimentos, respectivamente.

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Utiliza Atividade Retorno Automático (Ativ. Agenda) |
| **Tipo:** | Booleano |
| **Cont. Por.:** | Falso (Desmarcado) |
| **Descrição:** | Indica se Agenda de Atendimento deve atualizar automaticamente a atividade do agendamento quando encontra-se em período de retorno |

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Atividade Agenda com Status de Retorno (Ativ. Agenda) |
| **Tipo:** | Numérico |
| **Cont. Por.:** | *-1* |
| **Descrição:** | Apresenta as atividades da Agenda para seleção da atividade que utilizará retorno automático. |

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Atividade do Registro de Atendimento com Status de Retorno (Ativ. Reg. Atend.) |
| **Tipo:** | Numérico |
| **Cont. Por.:** | *-1* |
| **Descrição:** | Apresenta as atividades de Registro de Atendimento para seleção da atividade que utilizará retorno automático. |

## Procedimento para Utilização

**Cadastro do Período de Retorno**

1. Acesse o menu "**Cadastros / Faturamento / Condições Contratuais com Convênios**".
2. Selecione o convênio que será utilizado.
3. Anexos / Retorno de Consulta.
4. O tempo de retorno para cada especialidade estará na coluna "Retorno em dias".

   1. Caso não haja registros neste anexo é necessário cadastrar.

**Agendamento com Atividade Automática**

Observação

Para realizar este processo, é necessário realizar o registro de um atendimento previamente, para que o novo Agendamento esteja dentro do período de retorno

1. Acesse o menu "**Atendimento / Agendamento / Agenda de Atendimentos**".
2. Selecione a "**Unidade de Atendimento / Localização por Nomes / Selecione a Agenda desejada / Selecione o horário de Agendamento**".
3. Cadastre o agendamento com os campos necessários para a validação de retorno.

   1. Paciente/Compromisso: Nome do Paciente do Agendamento;
   2. Convênio: Convênio do Paciente (utilizar o convênio configurado anteriormente);
   3. Plano: Plano do Paciente (utilizar o convênio configurado anteriormente);
   4. Atividade: Atividade do Agendamento (utilizar uma atividade diferente da atividade de retorno);
   5. Status: Status do Agendamento;
   6. Especialidade do Agendamento: Especialidade do Agendamento/Prestador do Atendimento;
   7. Motivo: Motivo do Agendamento;
   8. Sala: Sala do Atendimento do Agendamento.
4. Ao salvar o Registro, se a data estiver dentro do período de retorno, o sistema solicitará a confirmação, e a atividade do agendamento será alterada automaticamente

**Registro de Atendimento com Atividade Automática**

Observação

Para realizar este processo, é necessário realizar o registro de um atendimento previamente, para que o novo atendimento esteja dentro do período de retorno.

1. Acesse o menu "**Atendimento / Agendamento / Agenda de Atendimentos**".
2. Selecione a "**Unidade de Atendimento / Localização por Nomes / Selecione a Agenda desejada / Selecione um registro de Agendamento / Botão Atend. Externo**".
3. Os campos da agenda serão transferidos para o registro de atendimento. Clique em "Registra".
4. Atividade do Atendimento será preenchida automaticamente.

divs
