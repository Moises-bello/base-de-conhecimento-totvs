---
content_hash: 72b6e31e10c3e74171a5e89c03e7d5d22e9e3a66cdd63928c18a58994d3a589e
fetched_at: '2026-06-29T00:12:14.152491+00:00'
page_id: '966201815'
product: rm
source: tdn-rm
title: Menu Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=966201815
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ### Critérios de Aceitação
4. **Exemplo de Campos na Tela**

SumárioVisão Geral

## **01. VISÃO GERAL**

Permitir ao dentista selecionar e registrar procedimentos odontológicos vinculados ao convênio do paciente, com valores consistentes com a tabela de preços contratual, a fim de gerar orçamentos claros, precisos e automatizados.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

**Descrição da Funcionalidade**

Durante o atendimento ou elaboração de orçamento, o sistema deve exibir os campos para **seleção de convênio, procedimentos, quantidade e valores**, com integração automática à tabela de preços do convênio vinculado ao paciente.

A funcionalidade garante que os valores utilizados para orçamento estejam alinhados com as condições comerciais de cada convênio e que as informações possam ser ajustadas conforme necessidade do atendimento.

Critérios de Aceitação

## **03. CRITÉRIOS DE ACEITAÇÃO**

|  |  |
| --- | --- |
| **Critério** | **Descrição** |
| **Informações do Convênio** | O campo **Convênio** deve ser preenchido automaticamente com base no cadastro do paciente. Deve ser possível **editar o convênio manualmente**, caso necessário para geração de orçamento com outro plano. |
| **Procedimentos Disponíveis** | A lista de procedimentos exibida deve ser **filtrada conforme a tabela do convênio selecionado**. A seleção deve permitir **um procedimento por vez**. |
| **Quantidade e Valores** | O campo **Quantidade** deve aceitar valores inteiros, representando o número de vezes que o procedimento será realizado. O **Valor Unitário** deve ser preenchido automaticamente com base na tabela do convênio. O **Valor Total** deve ser calculado automaticamente (*Quantidade x Valor Unitário*). |
| **Validação e Usabilidade** | A interface deve validar o preenchimento obrigatório dos campos antes de permitir salvar. Ao alterar o convênio, o sistema deve **atualizar automaticamente** os procedimentos e valores correspondentes. |

### **Comportamento Esperado**

* O campo **Convênio** será preenchido automaticamente, mas permanecerá editável.

* Ao selecionar um procedimento, o sistema:

* Exibe apenas os procedimentos disponíveis para o convênio.

* Preenche o valor unitário automaticamente.

* Permite definir a quantidade.

* Calcula e exibe o valor total.
Campos na Tela

## **04. EXEMPLO DE CAMPOS NA TELA**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| **Convênio** | [Auto preenchido com o convênio do paciente, editável] |
| **Procedimento** | [Caixa de seleção com lista filtrada] |
| **Quantidade** | [Campo numérico editável] |
| **Valor Unitário** | [Preenchido automaticamente] |
| **Valor Total** | [Calculado automaticamente] |

  
  

### **Módulos Envolvidos**

* PEP Odontológico

* Cadastro de Convênios

* Tabela de Preços de Procedimentos

### **Benefícios**

* Garante **precisão no orçamento odontológico** com base no convênio.

* Automatiza o cálculo de valores, reduzindo erros manuais.

* Permite flexibilidade ao dentista ao trocar convênios conforme demanda.
* Facilita a geração e validação de propostas de tratamento para o paciente.
