---
content_hash: 1e4c8cbb53fbe9375e0dde6b9e1daf66858abb4a8d823a7bd7ddc24bd78efc5f
fetched_at: '2026-06-29T00:05:48.118130+00:00'
page_id: '1023284358'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023284358
version: 2
---

## Visão Geral

O **Agendador de Processos** permite configurar a execução automática de rotinas do sistema em datas e horários definidos, com diferentes tipos de periodicidade. Essas rotinas são utilizadas, por exemplo, para criação automática de usuários e envio de notificações para o App Meu Imóvel.

Esta documentação descreve o fluxo de uso das telas, os campos disponíveis e as regras de funcionamento do agendamento.

## Lista de Processos Disponíveis

Na etapa **Processos**, o sistema apresenta os seguintes processos (podendo variar conforme a configuração do ambiente):

* **Criação de Usuários**  
  Processo responsável pela criação automática de usuários no Portal do Cliente e App Meu Imóvel.
* **Notificações de Boleto para App Meu Imóvel**  
  Responsável pelo envio de notificações push relacionadas a boletos.
* **Notificações de Comunicados via App Meu Imóvel**  
  Envio automático de comunicados para os clientes.
* **Notificações de Atendimentos via App Meu Imóvel**  
  Envio de notificações relacionadas a atendimentos.

Cada processo possui um botão **Agendar**, que abre a tela de configuração do agendamento.

## Tela de Agendamento

Ao clicar em **Agendar**, é exibida a tela **Agendar: [Nome do Processo]**, pode ser composta por três etapas:

1. **Parâmetros** (quando aplicável)
2. **Agendamento**
3. **Conclusão**

Esta documentação foca na etapa **Agendamento**.

## Etapa: Agendamento

### 1. Primeira Execução

Define quando o processo será executado pela primeira vez.

* **Dia**  
  Data da primeira execução do processo.
* **Horário**  
  Horário da primeira execução do processo.

⚠️ A primeira execução será respeitada independentemente da periodicidade selecionada.

### 2. Periodicidade

Define com que frequência o processo será executado após a primeira execução.

As opções disponíveis são:

* **Única**  
  O processo será executado apenas uma vez, na data e horário definidos.
* **Diária**  
  O processo será executado todos os dias no horário configurado.
* **Semanal**  
  O processo será executado semanalmente, nos dias da semana selecionados.
* **Mensal**  
  O processo será executado mensalmente (configurações adicionais podem ser aplicadas conforme regra do sistema).

### 3. Dados da Periodicidade

Esta seção é exibida conforme o tipo de periodicidade selecionado.

#### Horário

* Define o horário padrão das execuções recorrentes.
* Exemplo: `00:00`.

#### Dias da Semana (Periodicidade Semanal)

Disponível quando a opção **Semanal** estiver selecionada.

O usuário pode selecionar um ou mais dias:

* Domingo
* Segunda-feira
* Terça-feira
* Quarta-feira
* Quinta-feira
* Sexta-feira
* Sábado

⚠️ Pelo menos um dia da semana deve ser selecionado para permitir o agendamento.

## Etapa: Conclusão (Resumo do Agendamento)

A etapa **Conclusão** apresenta um **resumo completo do agendamento** antes da execução ou confirmação final do processo. Esta tela permite validar todas as informações configuradas nas etapas anteriores.

### Observações Importantes

* Esta tela não permite edição direta de campos.
* Qualquer divergência identificada deve ser corrigida utilizando o botão **Voltar**.
* Após a confirmação, o agendamento passa a valer imediatamente.
