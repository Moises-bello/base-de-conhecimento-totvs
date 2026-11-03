---
content_hash: 00cdccaa4bde3b537e3ee2d1bce02160f21700a47c2d4c75267c843fdafffbc0
fetched_at: '2026-06-29T00:12:08.509280+00:00'
page_id: '937248851'
product: rm
source: tdn-rm
title: Incluir Procedimentos na tela de "Odontograma"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937248851
version: 11
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Funcioanalidade**
3. **Critérios de Aceitção**
4. **Comportamento esperado**
5. **Módulos envolvidos**
6. **Benefícios**

Inclusão de Procedimentos na Tela "Odontograma"Visão Geral

## **01. VISÃO GERAL**

### **Objetivo:**

Facilitar a inclusão de procedimentos odontológicos diretamente na tela integrada "Odontograma",

otimizando o fluxo de trabalho clínico e a geração de orçamentos personalizados para o paciente.

Descrição da Funcionalidade

## **02. FUNCIONALIDADE**

### **Descrição da Funcionalidade:**

Na tela **"Odontograma"**, o sistema disponibiliza o botão **“Incluir procedimentos”**, permitindo ao

dentista adicionar procedimentos odontológicos de forma rápida e prática, sem a necessidade de

associar diretamente a um dente.

O sistema exibe os valores conforme o convênio vigente no atendimento e permite ajustes, garantindo

consistência com a tabela contratual.

Critérios de Aceitação

## **03. CRITÉRIOS DE ACEITAÇÃO**

**Exibição do Botão:** A tela "Odontograma" deve conter o botão “Incluir procedimentos” de forma visível e acessível.

**Formulário de Inclusão:** O botão deve abrir um formulário modal para inclusão de um único procedimento por vez.

**Seleção de Dentes:** Não é necessário selecionar dentes para registrar o procedimento.

**Convênio do Paciente:** O campo Convênio deve ser automaticamente preenchido com o convênio do atendimento atual.

**Edição de Convênio:** O usuário pode alterar o convênio para fins de orçamento, se necessário.

**Informações de Valores:**Devem ser exibidos:

* **Valor unitário**, conforme tabela do convênio selecionado
* V**alor total**, calculado com base na quantidade informada

**Campo de Observações:** O formulário deve conter um campo livre para observações adicionais relacionadas ao procedimento.

Comportamento Esperado

## **04. COMPORTAMENTO ESPERADO**

O botão **“Incluir procedimentos”** será exibido dentro da tela combinada de "**Odontograma"**

* Ao clicar no botão:
  + Abre-se um **formulário de inclusão** com os seguintes campos:
    - Convênio (auto preenchido e editável)
    - Plano (lista filtrada conforme o convenio)
    - Procedimento (lista filtrada conforme o convênio)
    - Quantidade (editavél)
    - Valor unitário (auto preenchido)
    - Valor total (calculado)
    - Observações

* O usuário poderá salvar o procedimento e repeti-lo para adicionar novos registros. Conforme demonstrado no print abaixo,

após salvar um orçamento, ele é exibido na lista de orçamentos. Para incluir outro, é necessário clicar novamente em *Incluir*

*Procedimento*, pois o modal é fechado automaticamente após o salvamento.

Módulos envolvidos e Benefícios

## **05. MÓDULOS ENVOLVIDOS**

* Odontograma
* Orçamento Odontológico
* Tabela de Preços
* Convênios e Planos de Saúde

## **06. BENEFÍCIOS**

* Agilidade na geração de orçamentos durante o atendimento.
* Flexibilidade para lidar com diferentes convênios em um único fluxo.
* Evita erros de associação indevida a dentes, quando não necessário.
* Aumenta a clareza no planejamento clínico e financeiro do paciente.
