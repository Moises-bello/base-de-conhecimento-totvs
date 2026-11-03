---
content_hash: 987141adc58352f66111ca682e09f27bec07c80e40d812166e7e9b17b5774577
fetched_at: '2026-06-29T00:05:51.246137+00:00'
page_id: '1050299606'
product: rm
source: tdn-rm
title: Obrigatoriedades clínicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050299606
version: 2
---

painelvisao-geralVisão geral

## **01. VISÃO GERAL**

A funcionalidade de obrigatoriedades clínicas é o motor de conformidade e segurança assistencial do Prontuário Eletrônico do Paciente (PEP). Ela permite que a gestão hospitalar parametrize condições específicas que devem ser atendidas antes que determinadas ações clínicas sejam executadas, garantindo que o prontuário reflita fielmente o cuidado prestado e atenda aos padrões regulatórios.

O objetivo central deste módulo é mitigar o risco de prontuários incompletos. Através da configuração de gatilhos de validação, o sistema assegura que informações cruciais tenham sido registradas dentro de um intervalo de tempo adequado antes que o profissional realize alguma ação.

Cadastro

## **02. CADASTRO**

Disponível em **Cadastros** / **Cuidados com o Paciente** / **Outros Cadastros** / **Obrigatoriedades clínicas**.

O cadastro de regras é realizado através de uma interface centralizada que divide a configuração em três blocos principais: Identificação/Status, Contexto (Para quem se aplica) e Definição da Regra.

#### **Bloco 1: Validação e Identificação**

* **Situação (Ativo/Inativo):** Chave seletora que define se a regra está em vigor no sistema. Regras inativas não serão processadas pelo motor de validação.
* **Descrição (Obrigatório):** Campo de texto livre para identificar a finalidade da regra.

  + *Exemplo: "Obrigatoriedade de Anotação Clínica ao Finalizar Atendimento".*

#### **Bloco 2: Contexto (Para quem se aplica)**

Neste bloco, define-se o escopo de aplicação. A regra só será disparada se o atendimento em questão atender a **todos** os critérios selecionados:

| **Campo** | **Descrição** |
| --- | --- |
| **Classes de Profissional** | Define quais categorias profissionais (Ex: Médico, Enfermeiro) serão impactadas. |
| **Unidades de Atendimento** | Unidades onde a regra deve ser validada (Ex: UTI, Pronto Atendimento). |
| **Classificação do Atendimento** | Define o regime do atendimento: Interno ou Externo. |
| **Tipo de Atendimento** | Contexto específico do atendimento (Ex: Consulta, Urgência). |

#### **Bloco 3: Regra e Comportamento**

Define o gatilho, a funcionalidade exigida e o que o sistema deve fazer caso a regra não seja cumprida:

* **Momento da Ação:** Define em qual momento a validação será executada.
* **Funcionalidade:** Seleção única da funcionalidade clínica que será validada (Ex: Anamnese).
* **Tipo da Ação:** Seleção múltipla das ações que disparam a verificação (Ex: "Finalizar atendimento", "Sair do prontuário").
* **Validade (h):** Prazo em horas. O sistema buscará o último registro da funcionalidade escolhida. Se o registro for mais antigo que o valor definido, a regra é considerada "não atendida".
* **Ação (Obrigatório):** Comportamento do sistema perante a irregularidade:

  1. **Impedir:** Bloqueia a continuidade da ação até que o registro seja feito.
  2. **Solicitar Justificativa:** Abre campo para o usuário justificar a ausência do registro e permite prosseguir.
  3. **Alertar:** Exibe aviso informativo, mas permite que o usuário prossiga sem impedimentos.
validacaoValidação da regra

## **03. VALIDAÇÃO DA REGRA**

Esta seção da documentação foca na experiência do usuário assistencial (médicos, enfermeiros, etc.) dentro do Prontuário Eletrônico, detalhando como o sistema se comporta quando uma regra de obrigatoriedade é disparada.

A validação ocorre de forma automática e transparente para o profissional de saúde, garantindo que o fluxo assistencial siga os protocolos institucionais de preenchimento.

### **Gatilhos**

* **Ao Sair do Prontuário:** Quando o usuário tenta sair do prontuário voltando aos painéis sem ter cumprido as obrigatoriedades configuradas.
* **Ao Finalizar o Atendimento:** No momento em que o profissional clica em "Finalizar atendimento", o sistema verifica se todos os registros clínicos exigidos (ex: Anamnese) foram realizados dentro do prazo de validade (h) definido.

### **Comportamento do Sistema (Tipos de Ação)**

Conforme a parametrização da regra, o sistema apresentará uma das três interfaces abaixo quando identificar uma pendência:

#### **A. Ação: Impedir**

* **Comportamento:** O sistema exibe uma mensagem de erro impeditiva. O usuário **não consegue** prosseguir com a ação (sair ou finalizar) até que o registro clínico obrigatório seja realizado.
* **Objetivo:** Garantir 100% de conformidade em itens de altíssimo risco ou obrigatoriedade legal imediata.
* + *Exemplo de alerta impeditivo informando que a Anamnese é obrigatória para sair do prontuário.*

#### **B. Ação: Solicitar Justificativa**

* **Comportamento:** O sistema identifica a ausência do registro e exibe uma tela com um campo de texto obrigatório. O usuário só poderá finalizar a ação após digitar o motivo pelo qual o registro não foi realizado.

  + *Interface solicitando que o profissional justifique a ausência de anamnese antes de sair do prontuário.*

#### **C. Ação: Alertar (Caráter Informativo)**

* **Comportamento:** O sistema exibe uma mensagem de aviso (Warning) listando as pendências encontradas.
* **Objetivo:** Apoio à decisão e lembrete de boas práticas, sem interromper o fluxo de trabalho em casos de menor criticidade.

  + *Aviso informativo lembrando o usuário sobre a validade da Anamnese.*
