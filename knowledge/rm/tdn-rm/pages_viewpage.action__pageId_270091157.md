---
content_hash: 7459097e8aeb91657a9e5bc8ec35188730e3dba5ca6790dd26d2b7243b62e9be
fetched_at: '2026-06-29T00:08:23.781649+00:00'
page_id: '270091157'
product: rm
source: tdn-rm
title: DT Bloqueio de Agendamentos Simultâneos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270091157
version: 114
---

# Bloqueio de agendamentos simultâneos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Atendimento / Agendamento / Agenda de Atendimentos | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® / Oracle® |
| **Tabelas Utilizadas:** | SZAGENDAMENTO, SZAGENDAMENTOSIMULT |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A melhoria possibilita que o  TOTVS Gestão Hospitalar realize o bloqueio de horários de agendamento de atendimentos, com o objetivo de evitar agendamentos simultâneos e agregando uma melhoria operacional ao produto.

## Procedimento para Utilização

### Acessar a Agenda de Atendimentos

1. Acesse o menu **Atendimento** / **Agendamento** / **Agenda de Atendimentos.**
2. O sistema apresentará a **Agenda de Atendimentos¹.**

   Observação

   ¹ É necessário acessar a Agenda com um usuário com permissões de registrar atendimentos através da Agenda de Atendimentos.
3. Selecione a Unidade de Atendimento.
4. Localize o prestador através dos filtros apresentados (Ex.: Grupo Nomes¹) e selecione a agenda do profissional desejado.Observação

   ² A localização das agendas pode ser realizada através de todos os filtros apresentados (ex.: Por Nome, Por Especialidade, etc.), a escolha do filtro é realizada pelo usuário.

### Agendamento Singular

1. Acesse a Agenda de Atendimento.
2. Selecione um horário livre na Agenda de Atendimentos.  
     
   1. Caso o horário selecionado esteja sendo utilizado para registrar o atendimento por outro usuário no momento do registro, o sistema apresenta a seguinte mensagem:

### Cópia de Agendamento Singular

1. Acesse a **Agenda de Atendimento**.
2. Selecione o registro que deseja copiar, clique no botão **Cópia de Agendamento** (CTRL + C).
3. Selecione o horário que deseja colar o registro copiado no passo anterior e clique no botão **Colar Agendamento** (CTRL + V).  
     
   1. Caso o horário selecionado esteja sendo utilizado para registrar o atendimento por outro usuário no momento da colagem do registro, o sistema apresenta a seguinte mensagem:

 

### Cópia de Agendamento Múltiplo

1. Acesse a **Agenda de Atendimento**.
2. Clique no botão **Copiar todos Agendamentos.**
3. Selecione o dia em que deseja colar os registros copiados.
4. Clique no botão **Colar Agendamentos** (CTRL + V).
5. Caso algum horário dos registros copiados esteja em processo de agendamento no dia selecionado para a colagem o sistema apresentará as seguintes mensagens:

### Agendamento Seriado

1. Acesse a **Agenda de Atendimento**.
2. Selecione o Registro que deseja serializar, clique em **Agendamentos Seriados.**
3. Preencha os dados da serialização de acordo com o desejado.
4. Os horários que estão em processo de agendamento não são apresentados na lista de horários seriados.

divs
