---
content_hash: 9fa5568218398693427847ec9c554dbaab86b5a89012eb699a0b06188588d72b
fetched_at: '2026-06-29T00:08:48.625525+00:00'
page_id: '327326364'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Recuperar Campos do Formulário do Processo"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327326364
version: 28
---

## **CONTEÚDO**

1. **Objetivo**
2. **Configuração**

## **01. OBJETIVO**

Este documento tem como finalidade, demonstrar o uso da atividade **"Recuperar Campos do Formulário do Processo"**.

## **02. CONFIGURAÇÃO**

**Informações Gerais - Atividade Recuperar Campos do Formulário do Processo**

**Objetivo:** A finalidade da atividade "Recuperar Campos do Formulário do Processo" é permitir que um Colaborador crie (ou recupere) Campos de um Formulário de um **Processo**.  
**Passo a Passo:** Primeiramente é necessário arrastar a atividade **"Recuperar Campos do Formulário do Processo"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Ao Preencher os parâmetros da atividade, uma nova sessão será adicionada, **"Dados do registro de formulário"**. Estarão listadas nessa sessão os campos do formulário do processo. Preencha esses campos.

Essas mesmas propriedades podem ser adicionadas manualmente, quando a Propriedade ProcessId for preenchida através de uma associação:

Clique no botão **[...]** da Propriedade **CardDataKeys** e adiciona quantos itens for necessário:

Após preencher a Propriedade **CardDataKeys**, preencha as propriedades criadas com os seus respectivos valores.

Após preencher as propriedades, salve e execute a **Fórmula Visual**. Verifique o resultado do processo. A **Fórmula Visual** deverá executar com sucesso.

Importante!

**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao **Processo**.  
**Obs:** Caso não seja informado o valor receberá o código da empresa configurado na integração.

A Atividade **"Recuperar Campos do Formulário do Processo"** deverá ser utilizada em conjunto com a Atividade **"Iniciar Solicitação Simples"**

**Dados dos registros do formulário**

* **CardDataKeys (Opcional)**

**Descrição:**Itens de um Formulário de um Processo  
**Tipo:** Array de uma Cadeia de Caracteres (String[])  
**Como Usar:** Esse parâmetro é do tipo Array de uma Cadeia de Caracteres, ou seja, deve-se utilizar um conjunto de valores alfanuméricos que represente os campos do Formulário do Processo.  
**Valor Utilizado na Requisição:**{"Item1", "Item2", "Item3", "Item4", "Item5"}

**Parâmetros do Método GetProcessFormFields**

* **CompanyId****(Obrigatório)**

**Descrição:**Código da Empresa.  
**Tipo:**Inteiro  
**Como Usar:** Esse parâmetro é do tipo Inteiro, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao Processo.  
**obs:**Caso não seja informado o valor receberá o código da empresa configurado na integração.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:** (Qualquer valor numérico que represente o Código da Empresa)

* **ProcessId (Obrigatório)**

**Descrição:** Código do Processo  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o Código do **Processo**.  
**Valor Utilizado na Requisição:** FLUIGADHOC

**Retorno do Método GetProcessFormFields**

**Descrição:** Retorno do método GetProcessFormFields.  
**Tipo:**Array de um Array de uma Cardeia Caracteres (String[][])

**Estrutura de retorno com sucesso:**Essa atividade tem como retorno o próprio CardData criado.
