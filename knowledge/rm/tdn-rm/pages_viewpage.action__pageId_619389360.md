---
content_hash: e386f59568cb73bb3fcde54f48cf3fa3c9a86ef3be4ea7723aff0cad23244b1c
fetched_at: '2026-06-29T00:11:02.809586+00:00'
page_id: '619389360'
product: rm
source: tdn-rm
title: Permitir o choque de horário entre as turmas/disciplinas e o Termo de compromisso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619389360
version: 8
---

##### **Essa funcionalidade está disponível a partir da versão 12.1.29.255.**

Este parâmetro tem como objetivo, permitir o choque de horário entre as turmas/disciplinas nas quais o Aluno esteja matriculado e Termo de compromisso do estágio.

Esse parâmetro será validado em dois momentos:

**1 -** Na aprovação da Solicitação de Estágio.

**2 -**Na Assinatura do Termo de Compromisso.

#### **1 - APROVAR SOLICITAÇÃO DE ESTÁGIO.**

**Parâmetro marcado:**

Quando o aluno inclui uma Solicitação de Estágio pelo Portal,  a Instituição de ensino deve realizar a validação do mesmo e alterar o status para: Aprovado ou Reprovado.  
Caso a Solicitação de Estágio seja "Aprovada", e tenha choque de horário entre o estágio e alguma turma/disciplina em que o aluno esteja matriculado; o sistema irá apresentar uma mensagem informado a relação de turmas/disciplinas com choque de horário. Caso seja do interesse da Instituição de Ensino permitir a aprovação mesmo com choque de horário basta o usuário clicar em 'SIM'.

**Parâmetro desmarcado:**

Ocorrendo choque de horário, o sistema emitirá a mensagem de erro e não efetivará a aprovação da solicitação de estágio

#### **2- ASSINATURA DO TERMO DE COMPROMISSO**

**Parâmetro marcado:**

Quando o aluno é selecionado para uma vaga de estágio a Instituição de Ensino deve criar um termo de compromisso para o estágio. Quando existir choque de horário entre alguma turma/disciplina na qual o aluno esteja matriculado e o horário do estágio na mudança do status para "Assinado"; o sistema irá apresentar a mensagem de choque de horário informado a relação de turmas/disciplinas. Sendo de interesse da Instituição de Ensino permitir a assinatura do termo de compromisso mesmo com choque de horário, basta o usuário clicar em 'SIM'.

**Parâmetro desmarcado:**

Ocorrendo choque de horário, o sistema emitirá a mensagem de erro e não permitirá a mudança do status do termo de compromisso para "Assinado"
