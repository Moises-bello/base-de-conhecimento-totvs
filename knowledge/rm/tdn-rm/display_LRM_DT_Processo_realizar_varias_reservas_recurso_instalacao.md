---
content_hash: 5577a2a8a93e41a34c1dfe5f30795ad79f9d0246ea46accf80c5adad787cf416
fetched_at: '2026-06-29T00:08:27.361347+00:00'
page_id: '271408014'
product: rm
source: tdn-rm
title: DT_Processo_realizar_varias_reservas_recurso_instalacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Processo_realizar_varias_reservas_recurso_instalacao
version: 2
---

# Processo de reserva de recurso e instalação realizar várias reservas

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Reserva de recurso e instalação*.* | Reserva de recurso e instalação | | | |
| **Requisito (ISSUE):** | EDUEDU001-706 | | |
| **País:** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

 Permitir que o processo de reserva de recurso e de instalação possa realizar várias reservas para um mesmo recurso ou uma mesma instalação.

## 

## Definição da Regra de Negócio

 

# Realizar reserva de recurso ou instalação em vários horários

Acessar:****Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Reserva de recurso e instalação****

Selecionar uma atividade agendada, executar o Processo de reserva de recurso ou o Processo de reserva de instalação:

Na primeira etapa é informado solicitante e na etapa de definir os horários é possível informar uma data de início e fim, hora de incio e fim, dias da semana e avançar o processo.

Para  incluir várias datas e horários informe uma data de início e fim, hora de incio e fim, dias da semana e clicar no botão "Adicionar horário" para cada reserva de dia e horário que desejar. Caso deseje  remover algum dos horários incluídos na lista, basta selecionar o horário  e clicar em "Remover horário" adicionado na lista.

Para concluir a execução do processo informe um recurso ou uma instalação de acordo com processo de executado.

Assim ao realizar uma reserva de instalação ou recurso  será possível definir diferentes horários:

 

Informar apenas um dia e hora específica

**Exemplo:**

Entre 08/06/2017 e 08/06/2017 de 08:00 às 09:00

 Vários dias diferentes com o mesmo horário ou o mesmo dia com horários diferentes

**Exemplo:**

Entre 09/06/2017 e 09/06/2017 de 08:00 às 09:00

Entre 10/06/2017 e 10/06/2017 de 08:00 às 09:00

Entre 11/06/2017 e 11/06/2017 de 08:00 às 09:00

Entre 11/06/2017 e 11/06/2017 de 11:00 às 12:00

 Fazer a reserva para os dias da semana em um intervalo de datas

**Exemplo**:

Entre 01/07/2017 e 30/072017 de 08:00 às 09:00

Para os dias da semana: segunda, quarta e sexta

Realizar reserva para um período contínuo. Habilitando o parâmetro "Reservar período contínuo", a instalação será reservada por todo período que for informado no processo.

**Exemplo**:

Entre 01/08/2017 08:00 e 10/08/2017 18:00

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Reserva de recurso | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Processo reserva de recurso | - |
| Reserva de instalação | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação -> Processo reserva de instalação | - |
