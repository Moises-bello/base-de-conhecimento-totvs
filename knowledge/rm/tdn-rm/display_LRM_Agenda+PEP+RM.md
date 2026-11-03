---
content_hash: 13020f76a8669d6cfb02f438e26726bc35a4660ef29754df2c8c2c964a491c20
fetched_at: '2026-06-29T00:10:44.373372+00:00'
page_id: '552571561'
product: rm
source: tdn-rm
title: Agenda PEP RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Agenda+PEP+RM
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Importante**
   1. **Outras Ações / Ações relacionadas**
4. **Passo a passo das telas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Possibilita ao médico verificar os pacientes agendados para o dia. É possível, também, ter acesso aos pacientes que atendeu no dia anterior e aos pacientes que estão agendados posteriormente ao dia em que está.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

PEP RM > Minha Agenda

## **03. IMPORTANTESAUPEPCONV-22993**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Calendário | Necessário para que consiga visualizar e ter acesso aos pacientes da agenda do dia. |

## **04. PASSO A PASSO DAS TELAS UTILIZADAS**

### I - Tela principal **MINHA AGENDA**

A tela abrirá com todos os campos bloqueados aguardando a seleção de unidade.

### II - Selecionar a unidade

Após a seleção da unidade, escolha o dia a ser verificado (por padrão é sempre o dia atual).

### 

### III - Visualização dos pacientes

São exibidos os pacientes atendidos em dias anteriores, dia atual e futuros. No entanto, os agendamentos futuros não podem receber nenhuma alteração ou ação pelo PEP RM.

Através do campo "Buscar paciente"  é possível realizar a busca pela leitura da pulseira de identificação do paciente (código de barras), nome ou nome social do paciente e a palavra buscada poderá estar no início, meio ou final do nome.

### 

### IV - Ações paciente

No lado direito da tela, vemos três pontinhos, os quais tem a finalidade de permitir ao médico iniciar um atendimento, retornar ao prontuário do paciente, indicar paciente ausente, finalizar o atendimento e retornar o paciente para a fila de espera. As opções são disponíveis de acordo com o status do paciente na agenda.

**IMPORTANTE**

---

No PEP RM, apenas os médicos poderão visualizar as agenda, onde cada médico deverá ter acesso apenas à sua agenda.

A tela de minha agenda foi implementada para unidades que não utilizam o painel de eletivos. Os status do menu minha agenda, que foram implementados para poder orientar o usuário no atendimento, não possuem relação com os status do painel de eletivos, mesmo sendo alguns deles similares. 

Para o funcionamento correto a unidade não deve utilizar painel de eletivos, RM>Saúde>Cadastros>Uso Geral>Unidade de Atendimento> Aba identificação.

Os campos de Hora de Chegada e Espera são exibidos na agenda apenas após o registro do atendimento no RM e a entrada do paciente na fila do médico. Portanto, estas informações não ficam visíveis antes do inicio do atendimento.

Caso o status esteja como finalizado, o tempo de espera não será exibido, pois o agendamento já foi encerrado.
