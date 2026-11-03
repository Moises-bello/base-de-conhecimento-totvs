---
content_hash: d5674839160bae0ccb88f6075ef33ed7d52652fe157b0afc7abe9c22df5809eb
fetched_at: '2026-06-29T00:08:48.653542+00:00'
page_id: '327329457'
product: rm
source: tdn-rm
title: Utilizando Atividade "Recuperar Campos do Formulário da Solicitação"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327329457
version: 28
---

## **CONTEÚDO**

1. **Objetivo**
2. **Configuração**

## **01. OBJETIVO**

Este documento tem como finalidade, demonstrar o uso da atividade **"**Recuperar Campos do Formulário da Solicitação**"**.

## **02. CONFIGURAÇÃO**

**Informações Gerais - Atividade Recuperar Campos do Formulário da Solicitação**

**Objetivo:** A finalidade da atividade "Recuperar Campos do Formulário da Solicitação" é permitir que um Colaborador crie (ou recupere) Campos de um Formulário de uma **Solicitação**.  
**Passo a Passo:** Primeiramente é necessário arrastar a atividade **"Recuperar Campos do Formulário da Solicitação"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Ao Preencher os parâmetros da atividade, uma nova sessão será adicionada, **"Dados dos registros do formulário"**. Estarão listadas nessa sessão os campos do formulário da solicitação. Esses campos serão preenchidos, pela primeira vez, com o dados do **Fluig**.

Essas mesmas propriedades podem ser adicionadas manualmente, quando a Propriedade ProcessInstanceId for preenchida através de uma associação:

Clique no botão **[...]** da Propriedade **CardDataKeys** e adiciona quantos itens for necessário:

Após preencher a Propriedade **CardDataKeys**, preencha as propriedades criadas com os seus respectivos valores.

Após preencher as propriedades, salve e execute a **Fórmula Visual**. Verifique o resultado do processo. A **Fórmula Visual** deverá executar com sucesso.

Atenção

A Atividade **"Recuperar Campos do Formulário da Solicitação"** deverá ser utilizada em conjunto com a Atividade **"Movimentar Tarefa"**.

**Dados dos registros do formulário**

* **CardDataKeys **(Opcional)****

**Descrição:**Itens de um Formulário de um Processo  
**Tipo:**Array de uma Cadeia de Caracteres (String[])  
**Como Usar:**Esse parâmetro é do tipo**Array de uma Cadeia de Caracteres**, ou seja, deve-se utilizar um conjunto de valores alfanuméricos que represente os campos do Formulário do**Processo**.  
**Valor Utilizado na Requisição:** {"Item1", "Item2", "Item3", "Item4", "Item5"}

**Parâmetros do Método GetInstanceCardData**

* **CompanyId (Opcional)**

**Descrição:**Código da Empresa.  
**Tipo:**Inteiro  
**Como Usar:**Esse parâmetro é do tipo**Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer valor numérico que represente o Código da Empresa)

* **ProcessInstanceId (Obrigatório)**

**Descrição:** Número da Solicitação.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Número da Solicitação do **Processo**.  
**Valor Utilizado na Requisição:** 40

* **UserId (Opcional)**

**Descrição:**Matrícula do usuário que vai executar a tarefa.  
**Tipo:**Cadeia de Caracteres (String)  
**Como Usar:**Esse parâmetro é do tipo**Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente a Matrícula do Usuário que vai executar a tarefa vinculada ao**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer usuário ativo cadastrado no FLUIG)

**Retorno do Método GetInstanceCardData**

**Descrição:** Retorno do método GetProcessFormFields.  
**Tipo:** Array de um Array de uma Cardeia Caracteres (String[][])

**Estrutura de retorno com sucesso:**Essa atividade tem como retorno o próprio CardData criado.

**RM.Net**

* **UpdateCardDataFromFluig**

**Descrição:**Atualiza informações do CardData da solicitação corrente.  
**Tipo:**Lógico (Booleano)  
**Como Usar:**Esse parâmetro é do tipo**Lógico**, ou seja, deve-se utilizar um valor lógico (Sim ou Não / Falso ou Verdadeiro) que indique a vontade de atualizar o CardData com dados do **Fluig**ou não.

Atenção

Ao clicar na propriedade UpdateCardDataFromFluig e escolher o valor "true", uma mensagem de confirmação é apresentada, pedindo confirmação para atualizar os dados. Lembre-se que ao atualizar o CardData com os dados do Fluig, os dados locais serão substituidos, tenha certeza de conferir os dados antes de salvar sua Fórmula Visual.
