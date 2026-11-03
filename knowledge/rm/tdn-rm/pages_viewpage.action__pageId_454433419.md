---
content_hash: e8298753ea84e888e40b9cd3d43dac5cb57fb368f01c385ab65c99e135bc3a75
fetched_at: '2026-06-29T00:10:12.305609+00:00'
page_id: '454433419'
product: rm
source: tdn-rm
title: Utilizando Atividade "Criar Atendimento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454433419
version: 8
---

# Índice:

---

* Objetivo:
* Configuração:

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Criar Atendimento"**.

# Criando a Fórmula Visual:

ComoFazer

**Passo a Passo:** 

1º Passo - Incluir Atividade

Primeiramente é necessário arrastar a atividade **"Criar Atendimento"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

2º Passo - Preencher Propriedades Obrigatórias

Nas **Propriedades** da atividade, preencha as Propriedades da atividade. (Propriedades Obrigatórias)

**Contexto:**

**Código da Coligada:** Código da Coligada corrente.

**Usuário:** Código do usuário logado.

**Atendimento:**

**Assunto:** Assunto do atendimento que sera criado.

**Atendente criador do atendimento:** Código do atendente criador do atendimento, caso não preenchido será utilizado o atendente associado ao usuário.

**Atendente de destino/responsável do atendimento:** Código do atendente que será o responsável pelo atendimento tão logo seja criado.

**Nomes campos complementares:** Nome dos campos complementares separados por ;

**Solicitação:** Texto de Solicitação do atendimento criado.

**Valores dos campos complementares:** Valor dos campos complementares separados por ;

**Fluxo:**

**Grupo de atendimento:** Código do grupo de atendimento cujo fluxo de tarefas (tipo de atendimento) está associado.

**Tipo de Atendimento:** Código do fluxo de tarefas (tipo de atendimento)

**Utilizar modelo do tipo de atendimento:** Indicativo de é para utilizar o modelo de atendimento associado ao fluxo de atendimento (tipo de atendimento)

Neste exemplo foram informados os valores fixos referentes ao atendimento demonstrado abaixo.

2º Passo - Propriedades Opcionais

Nas Propriedades da atividade, temos as propriedades abaixo opcionais:

**Cliente:**

**Cliente do atendimento:** Código do cliente do atendimento

          **Coligada do cliente do atendimento:** Código de coligada do cliente do atendimento

**Contato do Cliente: Contato do cliente:** Código do contato do cliente que estará associado ao atendimento.

**Tipo do Cliente:** Tipo do Cliente

**Possíveis valores:** A , C, P, R, T que se referem a ( Aluno, Cliente, Pessoa, Professor, Prospect )

# Exemplo:
