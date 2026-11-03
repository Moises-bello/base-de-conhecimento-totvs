---
content_hash: 3165d6df46877ff873ccd937043edf9a81f30305569a53933893f8646b3da7f6
fetched_at: '2026-06-29T00:12:15.126696+00:00'
page_id: '971106661'
product: rm
source: tdn-rm
title: Visualização de Pacientes por Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971106661
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. ### Descrição da Funcionalidade
3. ### Interface Esperada

sumarioVisão Geral

## **01. VISÃO GERAL**

### **Objetivo**

Permitir que profissionais de odontologia filtrem e visualizem os pacientes vinculados a uma unidade específica, facilitando o acesso e o gerenciamento dos atendimentos odontológicos, independentemente do status (aberto ou finalizado).

Descrição da Funcionalidade

## **02. DESCRIÇÃO DA FUNCIONALIDADE**

Ao acessar o **módulo de Odontologia**, o sistema disponibiliza uma **ferramenta de filtro por unidade**. Após selecionar a unidade desejada, será exibida uma **tabela contendo todos os pacientes associados** àquela unidade, com informações relevantes para identificação e continuidade do atendimento.

### **Critérios de Aceitação**

**Seleção de Unidade:** O sistema deve apresentar um filtro para seleção da unidade ao entrar no módulo de Odontologia.

**Listagem de Pacientes:** Após a seleção da unidade, deve ser exibida uma tabela com todos os pacientes vinculados à unidade, com atendimentos abertos e finalizados.

**Colunas da Tabela:**Código, Nome do paciente, Data de nascimento, Idade, Prontuário do paciente, Número do atendimento, Sexo, Unidade, Link para seleção do paciente.

**Busca Avançada:** Deve ser possível buscar pacientes por nome, número do atendimento ou outros critérios relevantes.

**Redirecionamento:** Ao clicar no link “Selecionar Paciente” na tabela, o sistema deve redirecionar o usuário para a tela de identificação do paciente, apresentando todas as informações do paciente selecionado.

**Menus Disponíveis:** A tela de identificação do paciente deve apresentar o menu lateral com as seções disponíveis, como Página Inicial, Identificação, Odontograma e Orçamentos.

Interface Esperada

## **03. INTERFACE ESPERADA**

* **Filtro de Unidade**: Seleção disponível no topo da tela ou em destaque no módulo.
* **Tabela de Resultados**: Exibição clara e ordenada das informações dos pacientes.
* **Funcionalidade de Busca**: Campo de busca com autocomplete ou pesquisa direta por nome/atendimento.
* **Filtro de Listagem de Pacientes:**

* + **Gerenciar Colunas**:
    - É possível personalizar quais colunas são exibidas na tabela, incluindo: Código, Nome do paciente, Data de nascimento, Idade, Prontuário, Nº de atendimento, Sexo e Unidade.
    - O usuário pode ativar/desativar colunas, alterar a ordem de exibição e fixar colunas para melhor visualização.
    - Há a opção **Restaurar padrão**, que retorna a visualização às configurações originais.

### **Módulos Envolvidos**

* [Odontologia](https://tdn.totvs.com/display/LRM/Odontologia)
* Lista de Pacientes
* PEP Odontológia (Prontuário Eletrônico do Paciente)

### **Benefícios**

* Melhora a **organização e agilidade no atendimento odontológico**.
* Facilita o controle de pacientes atendidos por **unidade de origem**.
* Centraliza informações clínicas em uma visão única e acessível.
* Permite acesso rápido aos prontuários para continuidade do tratamento.
