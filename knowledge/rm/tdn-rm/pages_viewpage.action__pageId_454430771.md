---
content_hash: d4c20b15a7f9fcc314907ade25ddc35d93cb40877bdf6034c121260af94f6e33
fetched_at: '2026-06-29T00:10:12.285385+00:00'
page_id: '454430771'
product: rm
source: tdn-rm
title: Utilizando Atividade "Avançar Etapa"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454430771
version: 12
---

# Índice:

---

* Objetivo:
* Configuração:

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Avançar Etapa"**.

# Criando a Fórmula Visual:

ComoFazer

**Passo a Passo:** 

1º Passo - Incluir Atividade

Primeiramente é necessário arrastar a atividade **"Avançar Etapa"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

2º Passo - Preencher Propriedades Obrigatórias

Nas **Propriedades** da atividade, preencha as Propriedades da atividade.

**Contexto:**

**Código da Coligada:** Código da Coligada corrente.

**Usuário:** Código do usuário logado.

**Atendimento:** Dados da chave do atendimento que ira ser utilizado no processo de avanço de etapa)

**Código do atendimento, Coligada do atendimento, Localidade do atendimento.**

Neste exemplo foram informados os valores fixos referentes ao atendimento demonstrado abaixo.

3º Passo - Propriedades Opcionais

Nas Propriedades da atividade, temos as propriedades abaixo opcionais:

**Fluxo:**

**Motivo de Repasse:** Código do motivo de repasse a ser utilizado em um repasse, avanço de etapas, etc.

          **Próxima Etapa:**  Código da etapa para onde o atendimento será direcionado (similar a próxima etapa). Caso informado -1 então significa entrada no fluxo (primeira etapa segundo configuração).
